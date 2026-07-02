// PTA適正運営スターターキット v1.0
// Googleフォーム・スプレッドシート実装用スタブ
// 非加入届、二択フォーム、学校名簿照合、非会員児童一覧は作成しない。

const PTA_FORMS = [
  '入会申込フォーム',
  '退会通知フォーム',
  '会員情報更新フォーム',
  '役員立候補・承諾フォーム'
];

const PTA_SHEETS = [
  '会員台帳',
  '会費管理',
  '退会管理',
  '役員承諾',
  '権限管理',
  '削除予定',
  'ログ'
];

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('PTA適正運営')
    .addItem('初期シートを作成', 'setupSheets')
    .addItem('禁止機能を確認', 'showForbiddenPolicy')
    .addToUi();
}

function setupSheets() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  PTA_SHEETS.forEach(name => {
    if (!ss.getSheetByName(name)) ss.insertSheet(name);
  });
  SpreadsheetApp.getActive().toast('必要シートを確認しました');
}

function showForbiddenPolicy() {
  SpreadsheetApp.getUi().alert([
    '作成しない機能:',
    '非加入届フォーム',
    '加入・非加入二択フォーム',
    '未提出者督促',
    '学校名簿インポート',
    '学校名簿照合',
    '非会員児童一覧',
    '役員免除申請',
    '家庭事情申告'
  ].join('\n'));
}
