from pathlib import Path

p = Path('PTA運営適正化ガイドブック_第4版_改訂本文.html')
s = p.read_text(encoding='utf-8')

replacements = {
    '<div class="toc-item"><span class="toc-num">第３章</span><span class="toc-text">個人情報保護法第69条──学校からPTAへの情報提供という根本問題</span></div>': '<div class="toc-item"><span class="toc-num">第３章</span><span class="toc-text">学校保有情報のPTA目的利用・提供──第61条と第69条</span></div>',
    '<div class="toc-sub"><span class="toc-kana">3-1</span><span class="toc-text">第69条の構造──原則禁止と例外</span></div>': '<div class="toc-sub"><span class="toc-kana">3-1</span><span class="toc-text">第61条・第69条の構造──所掌事務、利用目的、例外</span></div>',
    '<div class="toc-sub"><span class="toc-kana">3-2</span><span class="toc-text">「本人の同意」という例外は、現場では機能しない</span></div>': '<div class="toc-sub"><span class="toc-kana">3-2</span><span class="toc-text">本人同意を根拠とする場合の条件</span></div>',
    '<div class="toc-sub"><span class="toc-kana">3-4</span><span class="toc-text">学校連絡ツールの使用も認められない</span></div>': '<div class="toc-sub"><span class="toc-kana">3-4</span><span class="toc-text">学校連絡ツールを使う場合の確認</span></div>',
    '<div class="toc-item"><span class="toc-num">第４章</span><span class="toc-text">学校教育法第137条──学校施設利用の根拠と要件、そしてその逆説</span></div>': '<div class="toc-item"><span class="toc-num">第４章</span><span class="toc-text">学校教育法第137条──学校施設利用の許可条件と見直し</span></div>',
}

for old, new in replacements.items():
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'expected one marker, found {count}: {old[:80]}')
    s = s.replace(old, new)

p.write_text(s, encoding='utf-8')
