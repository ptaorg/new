const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'index.html');
const requested = process.argv[2];
const date = requested ? new Date(`${requested}T00:00:00+09:00`) : new Date();
if (Number.isNaN(date.getTime())) throw new Error('Date must be YYYY-MM-DD');

const formatted = new Intl.DateTimeFormat('ja-JP', {
  timeZone: 'Asia/Tokyo',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
}).format(date);

const before = fs.readFileSync(file, 'utf8');
if (!/掲載情報更新：\d{4}年\d{1,2}月\d{1,2}日/.test(before)) throw new Error('Home update label not found');
const after = before.replace(/掲載情報更新：\d{4}年\d{1,2}月\d{1,2}日/, `掲載情報更新：${formatted}`);
if (after !== before) fs.writeFileSync(file, after, 'utf8');
console.log(`${after === before ? 'Home label already uses' : 'Updated home label to'} ${formatted}`);
