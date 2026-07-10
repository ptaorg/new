from pathlib import Path

path = Path(__file__).resolve().parents[1] / "support.html"
text = path.read_text(encoding="utf-8")
old = "https://qr.paypay.ne.jp/p2p01_eKhgFmancxej9Wv8"
new = "https://qr.paypay.ne.jp/p2p01_sK4WOlBcTNasfkhU"
count = text.count(old)
if count != 1:
    raise SystemExit(f"Expected exactly one old PayPay URL, found {count}")
text = text.replace(old, new)
if old in text or text.count(new) != 1:
    raise SystemExit("PayPay URL replacement verification failed")
path.write_text(text, encoding="utf-8")
