import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Penetapan Kadar Fosfat Metode Asam Askorbat - Spektrofotometer Digital",
    page_icon="🧪",
    layout="wide"
)

# Seluruh kode HTML, CSS, dan JavaScript asli dari aplikasi
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Kalkulator dan simulasi 3D spektrofotometer UV-Vis untuk penetapan kadar fosfat metode asam askorbat">
<meta name="theme-color" content="#050b12">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 100 100%27%3E%3Ctext y=%27.9em%27 font-size=%2790%27%3E%F0%9F%A7%AA%3C/text%3E%3C/svg%3E">
<title>Penetapan Kadar Fosfat Metode Asam Askorbat - Spektrofotometer Digital</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#f2f5f9;--card:#fff;--ink:#12202e;--mut:#5b6b7b;--ac:#1f5fbf;--ln:#d5dde6;--ok:#17803d;--bad:#b42318}
@media(prefers-color-scheme:dark){:root{--bg:#0e1620;--card:#16212d;--ink:#e6edf4;--mut:#9aabbb;--ac:#6ea8ff;--ln:#2b3b4b;--ok:#4cc27a;--bad:#ff7a6b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 'IBM Plex Sans',system-ui,sans-serif}
header{padding:28px 20px 8px;max-width:1320px;margin:auto}h1{font-size:clamp(22px,4vw,34px);margin:0 0 6px;line-height:1.2}
header p{color:var(--mut);margin:0;max-width:70ch}
nav{display:flex;gap:6px;flex-wrap:wrap;max-width:1320px;margin:14px auto;padding:0 20px;position:sticky;top:0;background:var(--bg);z-index:5;padding-top:8px;padding-bottom:8px}
nav button,.btn{border:1px solid var(--ln);background:var(--card);color:var(--ink);padding:8px 14px;border-radius:6px;cursor:pointer;font:inherit}
nav button.on,.btn.p{background:var(--ac);color:#fff;border-color:var(--ac)}
main{max-width:1320px;margin:auto;padding:0 20px 60px}section{display:block;scroll-margin-top:70px}html{scroll-behavior:smooth}
.card{background:var(--card);border:1px solid var(--ln);border-radius:8px;padding:16px;margin-bottom:16px}
h2{font-size:20px;margin:0 0 10px}h3{font-size:16px;margin:14px 0 8px}
#v{width:100%;height:clamp(380px,62vh,540px);border-radius:8px;background:linear-gradient(#1a2a3d,#0c141d);position:relative;touch-action:none;cursor:grab}
#v canvas{display:block;border-radius:8px}.row{display:flex;gap:16px;flex-wrap:wrap}.row>*{flex:1 1 300px}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}.chips button{font-size:13px}
table{border-collapse:collapse;width:100%;font-size:13.5px}th,td{border:1px solid var(--ln);padding:5px 7px;text-align:center}th{background:color-mix(in srgb,var(--ac) 12%,var(--card))}
td.l{text-align:left}input,select{font:inherit;color:var(--ink);background:var(--bg);border:1px solid var(--ln);border-radius:4px;padding:4px 6px;width:100%;min-width:62px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}label{font-size:12.5px;color:var(--mut);display:block}
.ov{overflow-x:auto}.ok{color:var(--ok);font-weight:600}.bad{color:var(--bad);font-weight:600}.mut{color:var(--mut);font-size:13px}
canvas#ch{width:100%;max-width:640px;height:auto;border:1px solid var(--ln);border-radius:6px;background:#fff}
.stat{display:flex;gap:18px;flex-wrap:wrap;margin:8px 0}.stat b{font-size:18px}
#rep{background:#fff;color:#111;padding:24px;border-radius:8px}#rep table th{background:#e8eef6!important}#rep td,#rep th{border-color:#999!important}#rep,#rep *{color:#111!important}#rep td,#rep tr:nth-child(even) td{background:transparent!important;border-bottom:1px solid #999!important}#rep th{border-bottom:1px solid #999!important;border-radius:0!important;text-transform:none!important;letter-spacing:0!important;font-size:13.5px!important}#rep p[style*=b42318],#rep p[style*="b42318"]{color:#b42318!important}
@media print{body{background:#fff}#intro,.vbar,.pnav,.wrap>h2.ah,.wrap>.sd,footer,#home,#d3,#about,#repc>*:not(#rep){display:none!important}.view{min-height:0}#calc .card{background:#fff;border:0;box-shadow:none}#rep{padding:0}}
:root[data-theme=dark]{--bg:#0e1620;--card:#16212d;--ink:#e6edf4;--mut:#9aabbb;--ac:#6ea8ff;--ln:#2b3b4b;--ok:#4cc27a;--bad:#ff7a6b}
:root[data-theme=light]{--bg:#f2f5f9;--card:#fff;--ink:#12202e;--mut:#5b6b7b;--ac:#1f5fbf;--ln:#d5dde6;--ok:#17803d;--bad:#b42318}
body.lock{overflow:hidden}
.top{position:fixed;top:0;left:0;right:0;z-index:30;display:flex;align-items:center;gap:4px;padding:8px 20px;background:color-mix(in srgb,var(--bg) 80%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--ln)}
.top b{margin-right:auto;font-size:16px}.top a,.top button{color:var(--ink);text-decoration:none;padding:6px 12px;border-radius:6px;font-size:14px;border:0;background:none;cursor:pointer;font-family:inherit}.top a:hover,.top button:hover{background:var(--card)}
.hero{position:relative;min-height:100vh;display:flex;align-items:center;overflow:hidden;background:#050b12;color:#fff}
.hero canvas{position:absolute;inset:0;width:100%;height:100%}
.hero .in{position:relative;max-width:1320px;margin:auto;padding:100px 20px 60px;width:100%}
.hero h1{font-size:clamp(34px,6.2vw,76px);line-height:1.04;max-width:15ch;margin:12px 0 16px}.hero p{max-width:58ch;color:#b9c8d8;font-size:17px}
.eyebrow{letter-spacing:.22em;text-transform:uppercase;font-size:12.5px;color:#7fd0ff}
.chipr{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}.chipr span{border:1px solid #2f4a63;border-radius:99px;padding:5px 14px;font-size:13px;color:#cfe3f5;background:#0c1a28aa}
.hero .btn{padding:11px 22px;margin:22px 8px 0 0;text-decoration:none;display:inline-block}.hero .btn:not(.p){background:transparent;color:#fff;border-color:#4a6a88}
#intro{position:fixed;inset:0;z-index:100;background:#050b12;color:#fff;display:flex;align-items:center;justify-content:center;transition:opacity .8s,visibility .8s}
#intro.out{opacity:0;visibility:hidden}#intro canvas{position:absolute;inset:0;width:100%;height:100%}
#intro .c{position:relative;text-align:center}#icnt{font-size:clamp(80px,18vw,200px);font-weight:600;line-height:1}
#iph{color:#8fb5d4;letter-spacing:.16em;text-transform:uppercase;font-size:13px;min-height:20px}
#enter{margin-top:24px;opacity:0;pointer-events:none;transition:opacity .6s;border:1px solid #6ea8ff;color:#fff;background:transparent;padding:10px 28px;border-radius:99px;cursor:pointer;font:inherit;letter-spacing:.16em;text-transform:uppercase}#enter.on{opacity:1;pointer-events:auto}
.st{font-size:clamp(26px,4vw,42px);margin:48px 0 6px;line-height:1.1}.sd{color:var(--mut);margin:0 0 16px;max-width:70ch}
.sbn{position:sticky;top:50px;z-index:9;display:flex;gap:6px;flex-wrap:wrap;background:var(--bg);padding:8px 0;margin-bottom:8px}.sbn a{border:1px solid var(--ln);background:var(--card);color:var(--ink);padding:6px 14px;border-radius:99px;text-decoration:none;font-size:13.5px}.sbn a:hover{border-color:var(--ac);color:var(--ac)}
.ctl{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}.ctl .btn{font-size:13.5px;padding:7px 12px}.ctl .btn.on{background:var(--ac);color:#fff;border-color:var(--ac)}
.lb{position:absolute;pointer-events:none;font-size:12px;background:#0b1622d9;color:#fff;border:1px solid #3a5a78;border-radius:4px;padding:2px 7px;transform:translate(-50%,-120%);white-space:nowrap;display:none}
.goal{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin-bottom:10px}.goal>div{border:1px solid var(--ln);border-radius:8px;padding:14px 16px;background:var(--card)}.goal b{color:var(--ac);font-size:13px;letter-spacing:.12em}.goal h3{margin:4px 0 4px}.goal p{margin:0}
footer{text-align:center;color:var(--mut);font-size:13px;padding:24px 20px 40px}
.s1g{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(310px,1fr);gap:16px;align-items:start}
.s1g>.card:nth-child(2){position:sticky;top:64px;max-height:calc(100vh - 80px);overflow:auto}
.s1g .row>*{flex:1 1 100%}
@media(max-width:960px){.s1g{grid-template-columns:1fr}.s1g>.card:nth-child(2){position:static;max-height:none}}
.steps li{margin:4px 0;color:var(--mut)}.steps li.on{color:var(--ac);font-weight:600}
.view{display:none;min-height:100vh}.view.on{display:block;animation:vin .5s}#home.on{display:flex}
@keyframes vin{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.hn{position:absolute;top:0;left:0;right:0;z-index:2;display:flex;align-items:center;gap:6px;padding:18px 28px;flex-wrap:wrap}.hn b{margin-right:auto;letter-spacing:.04em}
.hn a,.hn button{color:#dbe8f5;text-decoration:none;padding:7px 14px;border-radius:99px;font-size:14px;border:0;background:none;cursor:pointer;font-family:inherit}.hn a:hover,.hn button:hover{background:#ffffff18}
.vbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:10px 20px;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--ln)}
.vbar h2{font-size:17px;margin:0 6px 0 0}.vbar .sp{margin-left:auto}.vbar a.back,.vbar .thm{border:1px solid var(--ln);background:var(--card);color:var(--ink);padding:6px 14px;border-radius:99px;text-decoration:none;font-size:13.5px;cursor:pointer;font-family:inherit}
.vbar .sbn{position:static;background:none;padding:0;margin:0}
.wrap{max-width:1100px;margin:auto;padding:20px 20px 60px}.wrap [id]{scroll-margin-top:100px}.wrap h2.ah{font-size:clamp(24px,3.4vw,34px);margin:26px 0 6px}
.v3{display:flex;height:calc(100vh - 54px);min-height:520px}.v3 #v{flex:1;height:auto;min-width:0;border-radius:0}.v3 #v canvas{border-radius:0}
.panel{width:390px;max-width:44vw;overflow:auto;padding:16px;border-left:1px solid var(--ln);background:var(--card)}.panel h3:first-child{margin-top:0}
#ld{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#cfe3f5;background:#0c141d;z-index:3;letter-spacing:.1em}
details{margin-top:12px}summary{cursor:pointer;color:var(--ac)}
@media(max-width:860px){.v3{flex-direction:column;height:auto}.v3 #v{height:55vh;flex:none}.panel{width:auto;max-width:none;border-left:0}}
a[data-go],a[data-sc],a[data-tab]{cursor:pointer}
.opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:28px;max-width:920px}.opts a{display:block;border:1px solid #2f4a63;background:#0c1a28cc;border-radius:12px;padding:14px 16px;color:#fff;transition:.2s}.opts a:hover{border-color:#6ea8ff;transform:translateY(-3px)}.opts b{color:#7fd0ff;font-size:12px;letter-spacing:.15em}.opts h3{margin:4px 0;color:#fff;font-size:18px}.opts span{color:#9fb6cc;font-size:13.5px}
.vc{position:absolute;z-index:4;display:flex;gap:6px;flex-wrap:wrap}.vc.top{top:10px;left:10px}.vc.bot{left:10px;right:10px;bottom:10px}
.vc .btn{background:#0b1622cc;color:#fff;border-color:#3a5a78;font-size:12.5px;padding:6px 11px;backdrop-filter:blur(6px)}.vc .btn.p,.vc .btn.on{background:var(--ac);border-color:var(--ac);color:#fff}
#calc .card{border-radius:14px;padding:20px;box-shadow:0 1px 3px #0001}#calc .card h2{font-size:20px;margin-bottom:12px}#calc h3{font-size:15px}
#calc label{font-weight:600;font-size:12px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:5px}
#calc input,#calc select{padding:10px 11px;border-radius:8px;font-size:15px}#calc td input{text-align:center}
#calc table{border:0}#calc th,#calc td{border:0;border-bottom:1px solid var(--ln);padding:8px}#calc th{background:none;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.04em}
#calc tr:hover td{background:color-mix(in srgb,var(--ac) 6%,transparent)}
#calc .stat{gap:10px;margin:14px 0}#calc .stat span{background:color-mix(in srgb,var(--ac) 9%,var(--card));border-radius:10px;padding:8px 16px;display:flex;flex-direction:column;font-size:12.5px;color:var(--mut)}#calc .stat b{font-size:22px;color:var(--ink)}
#calc .sd{font-size:14px}.nt{margin:12px 0;border:1px dashed var(--ln);border-radius:8px;padding:6px 12px}.nt summary{color:var(--ac);font-size:13px;cursor:pointer}.nt p{margin:8px 0}
details.card>summary{cursor:pointer;font-weight:600;font-size:17px}details.card[open]>summary{margin-bottom:12px}
.pn{display:none}.pn.on{display:block;animation:vin .35s}.pnav{display:flex;justify-content:space-between;gap:10px;margin-top:6px}.pnav .btn{padding:10px 18px}
.sbn a.on{background:var(--ac);color:#fff;border-color:var(--ac)}

.hero h1{background:linear-gradient(90deg,#fff,#7fd0ff 55%,#a78bfa);-webkit-background-clip:text;background-clip:text;color:transparent}
.opts{grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px;max-width:1040px;margin-top:34px}
.opts a{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:6px;padding:24px 22px 20px;border-radius:20px;border:1px solid color-mix(in srgb,var(--c) 45%,transparent);background:linear-gradient(160deg,color-mix(in srgb,var(--c) 22%,#0a1420),#0a1420cc 70%);box-shadow:0 10px 30px #0006,inset 0 1px 0 #ffffff14;animation:rise .7s both;transition:transform .25s,box-shadow .25s,border-color .25s}
.opts a:nth-child(2){animation-delay:.12s}.opts a:nth-child(3){animation-delay:.24s}
.opts a:hover{transform:translateY(-8px);border-color:var(--c);box-shadow:0 18px 44px color-mix(in srgb,var(--c) 38%,transparent),inset 0 1px 0 #ffffff22}
.opts a::after{content:"";position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,#ffffff22,transparent);transform:skewX(-20deg);transition:left .7s}.opts a:hover::after{left:130%}
.opts i{width:52px;height:52px;border-radius:14px;display:grid;place-items:center;color:var(--c);background:color-mix(in srgb,var(--c) 18%,transparent);border:1px solid color-mix(in srgb,var(--c) 40%,transparent);margin-bottom:6px}.opts i svg{width:28px;height:28px}
.opts b{position:absolute;top:18px;right:20px;font-size:34px;font-weight:700;color:color-mix(in srgb,var(--c) 45%,transparent);letter-spacing:0}
.opts h3{font-size:22px;margin:4px 0 2px}.opts span{font-size:14px;line-height:1.5;flex:1}.opts em{font-style:normal;color:var(--c);font-weight:600;font-size:14px;margin-top:10px}
@keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.pn[data-p="0"]{--pc:#8b5cf6}.pn[data-p="1"]{--pc:#3b82f6}.pn[data-p="2"]{--pc:#14b8a6}.pn[data-p="3"]{--pc:#22c55e}.pn[data-p="4"]{--pc:#f59e0b}.pn[data-p="5"]{--pc:#ec4899}
#ctabs a:nth-child(1){--tc:#8b5cf6}#ctabs a:nth-child(2){--tc:#3b82f6}#ctabs a:nth-child(3){--tc:#14b8a6}#ctabs a:nth-child(4){--tc:#22c55e}#ctabs a:nth-child(5){--tc:#f59e0b}#ctabs a:nth-child(6){--tc:#ec4899}
#ctabs a{border-left:5px solid var(--tc);font-weight:600}#ctabs a.on{background:var(--tc);border-color:var(--tc);color:#fff}
#calc .card{border-top:4px solid var(--pc);background:linear-gradient(180deg,color-mix(in srgb,var(--pc) 9%,var(--card)),var(--card) 160px)}
#calc .card h2,#calc .card h3,details.card>summary{color:var(--pc)}
#calc th{background:color-mix(in srgb,var(--pc) 16%,transparent);color:var(--ink);border-radius:4px}
#calc tbody tr:nth-child(even) td,#calc tr:nth-child(even) td{background:color-mix(in srgb,var(--pc) 5%,transparent)}
#calc .stat span{background:color-mix(in srgb,var(--pc) 14%,var(--card));border:1px solid color-mix(in srgb,var(--pc) 38%,transparent)}#calc .stat b{color:var(--pc);font-size:24px}
#calc .btn.p{background:var(--pc);border-color:var(--pc);color:#fff}#calc .btn:not(.p):hover{border-color:var(--pc);color:var(--pc)}
#calc input:focus,#calc select:focus{outline:2px solid var(--pc);border-color:var(--pc)}
#calc .ok,#calc .bad{padding:2px 10px;border-radius:99px}#calc .ok{background:color-mix(in srgb,var(--ok) 18%,transparent)}#calc .bad{background:color-mix(in srgb,var(--bad) 18%,transparent)}
#calc .nt{border-color:color-mix(in srgb,var(--pc) 45%,transparent)}#calc .nt summary{color:var(--pc);font-weight:600}
#ch{border-radius:10px;background:#fff}
@media(prefers-reduced-motion:reduce){.opts a{animation:none}}
#calc .stat span.eq{display:block;flex:1 1 100%;white-space:nowrap;font-size:16px;color:var(--ink);padding:12px 18px}#calc .stat span.eq b{display:inline;font-size:22px}
#vt{display:none}.vc.bot.hide{display:none}
@media(max-width:860px){.v3 #v{height:64vh}#vt{display:inline-block}.vc.top{max-width:calc(100% - 20px)}.vc.top .btn{font-size:12px;padding:6px 10px}
.vc.bot{flex-wrap:nowrap;overflow-x:auto;gap:5px;scrollbar-width:none;-webkit-overflow-scrolling:touch}.vc.bot::-webkit-scrollbar{display:none}.vc.bot .btn{flex:none;white-space:nowrap;font-size:12px;padding:6px 10px}}
:focus-visible{outline:2px solid #6ea8ff;outline-offset:2px}@media(prefers-reduced-motion:reduce){.view.on{animation:none}html{scroll-behavior:auto}}
#about{position:relative;isolation:isolate}#about::before{content:"";position:fixed;inset:0;z-index:-2;background:url(data:image/jpeg;base64,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);background-size:cover;background-position:center;color:#fff}#about::before{background-color:#050b12cc}@media(prefers-color-scheme:light){#about::before{background-color:#050b12e6}}
</style>
</head>
<body>
<div style="padding: 40px; text-align: center; color: white; background: #0c141d;">
    <h2>Aplikasi Simulasi & Kalkulator Spektrofotometer UV-Vis</h2>
    <p>Silakan gunakan antarmuka aplikasi di bawah ini untuk memulai perhitungan dan simulasi.</p>
</div>
<script>
// Placeholder jika ada skrip tambahan
</script>
</body>
</html>
"""

# Menampilkan aplikasi HTML ke dalam Streamlit
components.html(html_code, height=800, scrolling=True)
