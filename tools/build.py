# -*- coding: utf-8 -*-
"""Legacy rebuild helper. Prefer editing index.html directly for day-to-day updates."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT.parent
src = (ROOT / "site.dc.html").read_text(encoding="utf-8")

old_head = """<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="./support.js"></script>
</head>"""

new_head = """<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>専修大学射撃部 | SENSHUU SHOOTING CLUB</title>
<meta name="description" content="専修大学射撃部の公式サイト。未経験から始まる部活です。見学・入部案内、活動実績、免許取得の流れ、射撃記録アプリ shoot!! をご紹介します。">
<meta property="og:title" content="専修大学射撃部 | SENSHUU SHOOTING CLUB">
<meta property="og:description" content="経験者ほぼゼロから始まる部活。週1回の練習と合宿、大会に向けて活動しています。">
<meta property="og:image" content="assets/logo.png">
<meta name="theme-color" content="#1f8f52">
<link rel="icon" href="assets/logo.png">
<link rel="apple-touch-icon" href="assets/logo.png">
<script src="./support.js"></script>
<style id="site-overrides">
  html, body { overflow-x: hidden; }
  img { max-width: 100%; height: auto; }
  iframe { max-width: 100%; }
  @media (max-width: 900px) {
    [style*="font-size:128px"] { font-size: 52px !important; line-height: 1 !important; }
    [style*="font-size:88px"] { font-size: 38px !important; line-height: 1.1 !important; }
    [style*="height:115px"] { height: auto !important; flex-wrap: wrap; }
    [style*="font:900 52px"], [style*="font:900 50px"] { font-size: 34px !important; }
    [style*="grid-template-columns:repeat(3,1fr)"] { grid-template-columns: 1fr !important; }
    [style*="grid-template-columns:repeat(4,1fr)"] { grid-template-columns: 1fr 1fr !important; }
    [style*="grid-template-columns:1.6fr 1fr"],
    [style*="grid-template-columns:1.3fr 1fr"] { grid-template-columns: 1fr !important; }
    [style*="grid-template-columns:1fr 30px 1fr 30px 1fr"] { grid-template-columns: 1fr !important; }
    [style*="grid-template-columns:120px 132px 1fr 30px"] { grid-template-columns: 88px 1fr 24px !important; }
    [style*="grid-template-columns:80px 1fr 30px"] { grid-template-columns: 48px 1fr 24px !important; }
    [style*="grid-template-columns:1.4fr 1fr 1fr"] { grid-template-columns: 1fr !important; }
    [style*="margin:14px 0 0 272px"] { margin-left: 0 !important; }
    [style*="grid-auto-rows:230px"] { grid-template-columns: 1fr 1fr !important; grid-auto-rows: 160px !important; }
    [style*="width:400px;height:400px"] { width: 220px !important; height: 220px !important; }
  }
  @media (max-width: 520px) {
    [style*="grid-template-columns:repeat(4,1fr)"],
    [style*="grid-auto-rows:230px"] { grid-template-columns: 1fr !important; }
  }
  form.contact-form input, form.contact-form textarea, form.contact-form select {
    width: 100%; box-sizing: border-box; font: 14px/1.6 "Noto Sans JP", sans-serif;
    color: #16201a; background: #faf9f5; border: 1px solid #e2ded0; border-radius: 8px;
    padding: 12px 14px; margin-bottom: 20px;
  }
  form.contact-form textarea { min-height: 120px; resize: vertical; }
  form.contact-form .kind { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 20px; font-size: 14px; }
  form.contact-form button {
    appearance: none; border: 0; cursor: pointer;
    display: inline-block; padding: 15px 34px; border-radius: 999px;
    background: #1f8f52; color: #fff; font: 700 15px/1 "Noto Sans JP", sans-serif;
  }
</style>
</head>"""

if old_head not in src:
    raise SystemExit("head block not found")
src = src.replace(old_head, new_head, 1)
src = src.replace("<html>", '<html lang="ja">', 1)

old_form = """<div style="position:relative;background:#fff;border:1px solid #e2ded0;border-radius:12px;padding:32px">
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px">お名前</label>
<div style="height:48px;border:1px solid #e2ded0;border-radius:8px;background:#faf9f5;display:flex;align-items:center;padding:0 14px;color:#9aa39b;font-size:14px;margin-bottom:20px">（入力欄）</div>
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px">学年・所属</label>
<div style="height:48px;border:1px solid #e2ded0;border-radius:8px;background:#faf9f5;display:flex;align-items:center;padding:0 14px;color:#9aa39b;font-size:14px;margin-bottom:20px">（入力欄）</div>
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px">メールアドレス</label>
<div style="height:48px;border:1px solid #e2ded0;border-radius:8px;background:#faf9f5;display:flex;align-items:center;padding:0 14px;color:#9aa39b;font-size:14px;margin-bottom:20px">（入力欄）</div>
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:10px">お問い合わせ種別</label>
<div style="display:flex;gap:20px;margin-bottom:20px;font-size:14px">
<span style="display:flex;align-items:center;gap:8px"><span style="width:16px;height:16px;border-radius:50%;border:1.5px solid #b9c0b6;display:inline-block"></span>見学希望</span>
<span style="display:flex;align-items:center;gap:8px"><span style="width:16px;height:16px;border-radius:50%;border:1.5px solid #b9c0b6;display:inline-block"></span>入部について</span>
<span style="display:flex;align-items:center;gap:8px"><span style="width:16px;height:16px;border-radius:50%;border:1.5px solid #b9c0b6;display:inline-block"></span>その他</span>
</div>
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px">お問い合わせ内容</label>
<div style="height:120px;border:1px solid #e2ded0;border-radius:8px;background:#faf9f5;padding:14px;color:#9aa39b;font-size:14px;margin-bottom:24px">（入力欄）</div>
<span style="display:inline-block;padding:15px 34px;border-radius:999px;background:#1f8f52;color:#fff;font:700 15px/1 'Noto Sans JP',sans-serif">送信する</span>
</div>"""

new_form = """<form class="contact-form" action="https://formsubmit.co/senshu_u_air@yahoo.co.jp" method="POST" style="position:relative;background:#fff;border:1px solid #e2ded0;border-radius:12px;padding:32px">
<input type="hidden" name="_subject" value="専修大学射撃部サイトからのお問い合わせ">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_template" value="table">
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px" for="name">お名前</label>
<input id="name" name="name" required placeholder="山田 太郎">
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px" for="grade">学年・所属</label>
<input id="grade" name="grade" placeholder="1年・経済学部 など">
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px" for="email">メールアドレス</label>
<input id="email" type="email" name="email" required placeholder="example@example.com">
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:10px">お問い合わせ種別</label>
<div class="kind">
<label><input type="radio" name="kind" value="見学希望" required> 見学希望</label>
<label><input type="radio" name="kind" value="入部について"> 入部について</label>
<label><input type="radio" name="kind" value="その他"> その他</label>
</div>
<label style="display:block;font-weight:700;font-size:14px;margin-bottom:8px" for="message">お問い合わせ内容</label>
<textarea id="message" name="message" required placeholder="ご用件をご記入ください"></textarea>
<button type="submit">送信する</button>
</form>"""

if old_form not in src:
    raise SystemExit("contact form block not found")
src = src.replace(old_form, new_form, 1)

src = src.replace(
    '<p style="position:relative;margin:0 0 24px;padding:14px 18px;border-radius:8px;background:#fdf6e7;border:1px solid #f0e3c6;font-size:13px;color:#5b6259">これは見た目だけのフォームです。送信先（メール／Googleフォーム連携など）が決まり次第、実際に動くようにします。</p>',
    '<p style="position:relative;margin:0 0 24px;padding:14px 18px;border-radius:8px;background:#eaf5ee;border:1px solid #cfe8d7;font-size:13px;color:#5b6259">送信すると部のメール（senshu_u_air@yahoo.co.jp）に届きます。SNSのDMでも受け付けています。</p>',
    1,
)

src = src.replace(
    '<p style="margin:0;font-size:13px;color:rgba(255,255,255,.6)">SNSリンク（Instagram / X 等）</p>',
    '<div style="display:flex;flex-direction:column;gap:10px"><a href="https://www.instagram.com/senshu_shooting_2026" target="_blank" rel="noreferrer" style="color:rgba(255,255,255,.8)">Instagram @senshu_shooting_2026</a><a href="https://x.com/senshu_shooting" target="_blank" rel="noreferrer" style="color:rgba(255,255,255,.8)">X @senshu_shooting</a></div>',
    1,
)
src = src.replace(
    '<span style="color:rgba(255,255,255,.55);font-size:13px">SNSリンク（Instagram / X 等）</span>',
    '<span style="color:rgba(255,255,255,.55);font-size:13px"><a href="https://www.instagram.com/senshu_shooting_2026" target="_blank" rel="noreferrer" style="color:#fff">Instagram</a> / <a href="https://x.com/senshu_shooting" target="_blank" rel="noreferrer" style="color:#fff">X</a></span>',
    1,
)

old_go = """  go(p) {
    return (e) => {
      if (e && e.preventDefault) e.preventDefault();
      this.setState({ page: p, nav: false });
      if (typeof window !== 'undefined') window.scrollTo(0, 0);
    };
  }"""

new_go = """  go(p) {
    return (e) => {
      if (e && e.preventDefault) e.preventDefault();
      this.setState({ page: p, nav: false });
      if (typeof window !== 'undefined') {
        const hash = '#' + p;
        if (window.location.hash !== hash) history.replaceState(null, '', hash);
        window.scrollTo(0, 0);
      }
    };
  }

  applyHash() {
    const allowed = { top:1, about:1, records:1, join:1, license:1, members:1, access:1, contact:1, app:1 };
    const h = ((typeof window !== 'undefined' && window.location.hash) || '').replace(/^#/, '') || 'top';
    if (allowed[h]) this.setState({ page: h, nav: false });
  }"""

if old_go not in src:
    raise SystemExit("go() not found")
src = src.replace(old_go, new_go, 1)

src = src.replace(
    """  componentDidMount() {
    this.setupFx();
    this._splashT = setTimeout(() => this.setState({ splash: false }), 2400);
  }""",
    """  componentDidMount() {
    this.setupFx();
    this.applyHash();
    this._onHash = () => this.applyHash();
    if (typeof window !== 'undefined') window.addEventListener('hashchange', this._onHash);
    this._splashT = setTimeout(() => this.setState({ splash: false }), 2400);
  }""",
    1,
)

src = src.replace(
    "  componentWillUnmount() { if (this._io) this._io.disconnect(); if (this._rio) this._rio.disconnect(); clearTimeout(this._fx); clearTimeout(this._splashT); }",
    "  componentWillUnmount() { if (this._io) this._io.disconnect(); if (this._rio) this._rio.disconnect(); clearTimeout(this._fx); clearTimeout(this._splashT); if (this._onHash && typeof window !== 'undefined') window.removeEventListener('hashchange', this._onHash); }",
    1,
)

src = src.replace(
    '<span style="display:inline-block;padding:16px 30px;border-radius:999px;background:#3060a0;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">SNSをフォローする</span>',
    '<a href="https://www.instagram.com/senshu_shooting_2026" target="_blank" rel="noreferrer" style="display:inline-block;padding:16px 30px;border-radius:999px;background:#3060a0;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">SNSをフォローする</a>',
)
src = src.replace(
    '<span style="display:inline-block;padding:15px 28px;border-radius:999px;background:#1f8f52;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">新歓イベント日程を見る</span>',
    '<a href="https://www.instagram.com/senshu_shooting_2026" target="_blank" rel="noreferrer" style="display:inline-block;padding:15px 28px;border-radius:999px;background:#1f8f52;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">新歓イベント日程を見る</a>',
)
src = src.replace(
    '<span style="display:inline-block;padding:15px 28px;border-radius:999px;background:#3060a0;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">SNSをフォローする</span>',
    '<a href="https://www.instagram.com/senshu_shooting_2026" target="_blank" rel="noreferrer" style="display:inline-block;padding:15px 28px;border-radius:999px;background:#3060a0;color:#fff;font:700 15px/1 \'Noto Sans JP\',sans-serif">SNSをフォローする</a>',
)

out = SITE / "index.html"
out.write_text(src, encoding="utf-8")
print("wrote", out, out.stat().st_size)
