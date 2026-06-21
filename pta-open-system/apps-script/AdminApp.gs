// ============================================================================
// 追加: PTA管理アプリ画面（役員用Web UI）
// ============================================================================
// このブロックは、既存の申込管理シートをブラウザ画面で操作するためのUIです。
// 裏側のデータはスプレッドシート、表側はHTMLServiceの管理画面です。

function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('PTA管理アプリ')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

function showAdminApp() {
  const html = HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('PTA管理アプリ')
    .setWidth(1200)
    .setHeight(820);
  SpreadsheetApp.getUi().showModalDialog(html, 'PTA管理アプリ');
}

const ADMIN_APP = {
  SHEETS: {
    SETTINGS: '設定',
    APPLICATIONS: '申込管理',
    MEMBERS: '会員名簿',
    LOG: '操作ログ',
  },
  STATUS: {
    APPLIED: '申込受付（入金前）',
    MEMBER: '会員（入金確認済）',
    WITHDRAWN: '取下げ／無効',
    REVIEW: '確認要',
  }
};

function admin_getInitialData() {
  return {
    dashboard: admin_getDashboard(),
    applications: admin_listApplications('all'),
    members: admin_getMembers(),
    settings: admin_getSettings(),
  };
}

function admin_getDashboard() {
  const applications = admin_listApplications('all');
  const members = admin_getMembers();
  const settings = admin_getSettings();

  const total = applications.length;
  const confirmed = applications.filter(r => r.status === ADMIN_APP.STATUS.MEMBER).length;
  const withdrawn = applications.filter(r => r.status === ADMIN_APP.STATUS.WITHDRAWN).length;
  const pending = applications.filter(r => r.status !== ADMIN_APP.STATUS.MEMBER && r.status !== ADMIN_APP.STATUS.WITHDRAWN).length;

  return {
    totalApplications: total,
    pendingApplications: pending,
    confirmedApplications: confirmed,
    withdrawnApplications: withdrawn,
    memberCount: members.length,
    fiscalYear: settings['年度'] || '',
    feeLabel: settings['会費名目'] || '',
    feeAmount: settings['会費額'] || '',
    formUrl: settings['公開フォームURL'] || '',
    editFormUrl: settings['編集用フォームURL'] || '',
    orgName: settings['団体名'] || 'PTA',
    contactEmail: settings['問い合わせ先メール'] || '',
    updatedAt: admin_formatDateTime_(new Date()),
  };
}

function admin_listApplications(filter) {
  const table = admin_readTable_(ADMIN_APP.SHEETS.APPLICATIONS);
  const rows = table.rows.map(row => ({
    rowNumber: row.__rowNumber,
    id: row['申込ID'] || '',
    timestamp: admin_formatCell_(row['受付日時']),
    guardian: row['保護者氏名'] || '',
    email: row['メールアドレス'] || '',
    child: row['児童・生徒情報（任意）'] || '',
    grade: row['学年・組等（任意）'] || '',
    confirm: row['入会申込'] || '',
    consentVersion: admin_formatCell_(row['同意文版']),
    status: row['状態'] || '',
    paidDate: admin_formatCell_(row['入金確認日']),
    guideCount: row['支払い案内送信回数'] || '',
    lastGuideDate: admin_formatCell_(row['最終案内日']),
    note: row['備考'] || '',
  })).filter(row => row.id || row.guardian || row.email);

  if (filter === 'pending') {
    return rows.filter(r => r.status !== ADMIN_APP.STATUS.MEMBER && r.status !== ADMIN_APP.STATUS.WITHDRAWN);
  }
  if (filter === 'confirmed') {
    return rows.filter(r => r.status === ADMIN_APP.STATUS.MEMBER);
  }
  if (filter === 'withdrawn') {
    return rows.filter(r => r.status === ADMIN_APP.STATUS.WITHDRAWN);
  }
  return rows;
}

function admin_confirmMember(rowNumber) {
  rowNumber = Number(rowNumber);
  if (!rowNumber || rowNumber < 2) throw new Error('行番号が不正です。');

  const sheet = admin_getSheet_(ADMIN_APP.SHEETS.APPLICATIONS);
  const headers = admin_getHeaders_(sheet);
  const row = admin_rowObject_(headers, sheet.getRange(rowNumber, 1, 1, headers.length).getValues()[0], rowNumber);

  const id = row['申込ID'];
  if (!id) throw new Error('申込IDがない行です。');

  admin_setByHeader_(sheet, headers, rowNumber, '状態', ADMIN_APP.STATUS.MEMBER);
  admin_setByHeader_(sheet, headers, rowNumber, '入金確認日', new Date());

  const updatedValues = sheet.getRange(rowNumber, 1, 1, headers.length).getValues()[0];
  const updated = admin_rowObject_(headers, updatedValues, rowNumber);
  admin_upsertMember_(updated);
  admin_log_('会員確定', id + ' / ' + (updated['保護者氏名'] || ''));

  return {
    ok: true,
    message: '会員確定しました。',
    dashboard: admin_getDashboard(),
    applications: admin_listApplications('all'),
    members: admin_getMembers(),
  };
}

function admin_withdrawApplication(rowNumber, reason) {
  rowNumber = Number(rowNumber);
  if (!rowNumber || rowNumber < 2) throw new Error('行番号が不正です。');

  const sheet = admin_getSheet_(ADMIN_APP.SHEETS.APPLICATIONS);
  const headers = admin_getHeaders_(sheet);
  const row = admin_rowObject_(headers, sheet.getRange(rowNumber, 1, 1, headers.length).getValues()[0], rowNumber);

  const id = row['申込ID'];
  if (!id) throw new Error('申込IDがない行です。');

  admin_setByHeader_(sheet, headers, rowNumber, '状態', ADMIN_APP.STATUS.WITHDRAWN);

  const oldNote = row['備考'] || '';
  const addNote = '取下げ／無効: ' + admin_formatDateTime_(new Date()) + (reason ? ' / ' + reason : '');
  admin_setByHeader_(sheet, headers, rowNumber, '備考', oldNote ? oldNote + '\n' + addNote : addNote);

  admin_log_('取下げ／無効', id + (reason ? ' / ' + reason : ''));

  return {
    ok: true,
    message: '取下げ／無効にしました。',
    dashboard: admin_getDashboard(),
    applications: admin_listApplications('all'),
    members: admin_getMembers(),
  };
}

function admin_getMembers() {
  const table = admin_readTable_(ADMIN_APP.SHEETS.MEMBERS);
  return table.rows.map(row => ({
    rowNumber: row.__rowNumber,
    id: row['会員ID'] || '',
    confirmedAt: admin_formatCell_(row['会員確定日']),
    guardian: row['保護者氏名'] || '',
    email: row['メールアドレス'] || '',
    child: row['児童・生徒情報（任意）'] || '',
    grade: row['学年・組等（任意）'] || '',
    consentVersion: admin_formatCell_(row['同意文版']),
    note: row['備考'] || '',
  })).filter(row => row.id || row.guardian || row.email);
}

function admin_getSettings() {
  const sheet = admin_getSheet_(ADMIN_APP.SHEETS.SETTINGS);
  const lastRow = sheet.getLastRow();
  const result = {};
  if (lastRow < 2) return result;
  const values = sheet.getRange(2, 1, lastRow - 1, 2).getValues();
  values.forEach(r => {
    if (r[0]) result[String(r[0])] = admin_formatCell_(r[1]);
  });
  return result;
}

function admin_updateSetting(key, value) {
  if (!key) throw new Error('設定項目が指定されていません。');
  const sheet = admin_getSheet_(ADMIN_APP.SHEETS.SETTINGS);
  const lastRow = sheet.getLastRow();
  const values = lastRow >= 2 ? sheet.getRange(2, 1, lastRow - 1, 1).getValues() : [];
  for (let i = 0; i < values.length; i++) {
    if (String(values[i][0]) === String(key)) {
      sheet.getRange(i + 2, 2).setValue(value);
      admin_log_('設定更新', key + ' = ' + value);
      return { ok: true, settings: admin_getSettings(), dashboard: admin_getDashboard() };
    }
  }
  sheet.appendRow([key, value, '管理アプリから追加']);
  admin_log_('設定追加', key + ' = ' + value);
  return { ok: true, settings: admin_getSettings(), dashboard: admin_getDashboard() };
}

function admin_refreshMemberList() {
  const applications = admin_listApplications('confirmed');
  applications.forEach(app => {
    const sheet = admin_getSheet_(ADMIN_APP.SHEETS.APPLICATIONS);
    const headers = admin_getHeaders_(sheet);
    const values = sheet.getRange(app.rowNumber, 1, 1, headers.length).getValues()[0];
    const row = admin_rowObject_(headers, values, app.rowNumber);
    admin_upsertMember_(row);
  });
  admin_log_('会員名簿再作成', applications.length + '件');
  return {
    ok: true,
    message: '会員名簿を再作成しました。',
    dashboard: admin_getDashboard(),
    applications: admin_listApplications('all'),
    members: admin_getMembers(),
  };
}

function admin_upsertMember_(appRow) {
  const sheet = admin_getSheet_(ADMIN_APP.SHEETS.MEMBERS);
  admin_ensureMemberHeader_(sheet);
  const headers = admin_getHeaders_(sheet);

  const id = appRow['申込ID'];
  const existingRow = admin_findRowByHeaderValue_(sheet, '会員ID', id);

  const valuesByHeader = {
    '会員ID': id,
    '会員確定日': appRow['入金確認日'] || new Date(),
    '保護者氏名': appRow['保護者氏名'] || '',
    'メールアドレス': appRow['メールアドレス'] || '',
    '児童・生徒情報（任意）': appRow['児童・生徒情報（任意）'] || '',
    '学年・組等（任意）': appRow['学年・組等（任意）'] || '',
    '同意文版': appRow['同意文版'] || '',
    '備考': appRow['備考'] || '',
  };

  const rowValues = headers.map(h => valuesByHeader[h] !== undefined ? valuesByHeader[h] : '');

  if (existingRow) {
    sheet.getRange(existingRow, 1, 1, headers.length).setValues([rowValues]);
  } else {
    sheet.appendRow(rowValues);
  }
}

function admin_ensureMemberHeader_(sheet) {
  const headers = admin_getHeaders_(sheet);
  const required = ['会員ID', '会員確定日', '保護者氏名', 'メールアドレス', '児童・生徒情報（任意）', '学年・組等（任意）', '同意文版', '備考'];
  if (!headers.length || headers[0] !== '会員ID') {
    sheet.clear();
    sheet.getRange(1, 1, 1, required.length).setValues([required]);
  }
}

function admin_readTable_(sheetName) {
  const sheet = admin_getSheet_(sheetName);
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();
  if (lastRow < 1 || lastCol < 1) return { headers: [], rows: [] };

  const values = sheet.getRange(1, 1, lastRow, lastCol).getValues();
  const headers = values[0].map(h => String(h || '').trim());
  const rows = values.slice(1).map((row, i) => admin_rowObject_(headers, row, i + 2));
  return { headers, rows };
}

function admin_rowObject_(headers, row, rowNumber) {
  const obj = { __rowNumber: rowNumber };
  headers.forEach((h, i) => {
    if (h) obj[h] = row[i];
  });
  return obj;
}

function admin_getSheet_(sheetName) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) throw new Error('スプレッドシートが取得できません。コンテナバインドのApps Scriptで実行してください。');
  const sheet = ss.getSheetByName(sheetName);
  if (!sheet) throw new Error('シートが見つかりません: ' + sheetName);
  return sheet;
}

function admin_getHeaders_(sheet) {
  const lastCol = sheet.getLastColumn();
  if (lastCol < 1) return [];
  return sheet.getRange(1, 1, 1, lastCol).getValues()[0].map(h => String(h || '').trim());
}

function admin_headerIndex_(headers, headerName) {
  const idx = headers.indexOf(headerName);
  if (idx === -1) throw new Error('列が見つかりません: ' + headerName);
  return idx + 1;
}

function admin_setByHeader_(sheet, headers, rowNumber, headerName, value) {
  const col = admin_headerIndex_(headers, headerName);
  sheet.getRange(rowNumber, col).setValue(value);
}

function admin_findRowByHeaderValue_(sheet, headerName, value) {
  const headers = admin_getHeaders_(sheet);
  const col = admin_headerIndex_(headers, headerName);
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return null;
  const values = sheet.getRange(2, col, lastRow - 1, 1).getValues();
  for (let i = 0; i < values.length; i++) {
    if (String(values[i][0]) === String(value)) return i + 2;
  }
  return null;
}

function admin_log_(action, detail) {
  try {
    const sheet = admin_getSheet_(ADMIN_APP.SHEETS.LOG);
    const user = Session.getActiveUser().getEmail() || '';
    sheet.appendRow([new Date(), action, user, detail || '']);
  } catch (err) {
    // ログ失敗は操作を止めない
  }
}

function admin_formatCell_(value) {
  if (value instanceof Date) return admin_formatDateTime_(value);
  if (value === null || value === undefined) return '';
  return String(value);
}

function admin_formatDateTime_(date) {
  return Utilities.formatDate(date, Session.getScriptTimeZone() || 'Asia/Tokyo', 'yyyy/MM/dd HH:mm');
}
