#!/usr/bin/env python3
# -*- coding: utf-8 -*-
SKILL = "/sessions/vibrant-focused-wozniak/mnt/.claude/skills/krab-e-branding/assets"
def load(name):
    with open(f"{SKILL}/{name}.b64") as f:
        return f.read().strip()
LOGO = load("logo"); CRAB = load("pixel_crab"); FONT = load("font_bitroad")
SUPA_URL = "https://yixbnmwdzexjygmtszii.supabase.co/rest/v1"
ANON = "sb_publishable_Scfh5GvD_1yBmNJWRQePEg_2AVeeV-q"
HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Piramide Home · Performance | Krab-e</title>
<link rel="preconnect" href="https://api.fontshare.com">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=general-sans@300,400,500,600,700&f[]=satoshi@400,500,700,900&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
@font-face { font-family:'Bitroad'; src:url('data:font/otf;base64,__FONT__') format('opentype'); }
:root{ --ke-bg:#191919; --ke-card:#1f1f1f; --ke-header:#2a2a2a; --ke-text:#e6e6e6; --ke-muted:rgba(230,230,230,0.38); --ke-border:rgba(230,230,230,0.07); --ke-orange:#ff700a; --ke-green:#4dcc80; --ke-purple:#c084fc; --ke-blue:#4fa3ff; --ke-warn:#ffd88a; --ke-bad:#ffb0a0; }
*{box-sizing:border-box; margin:0; padding:0;}
body{ background:var(--ke-bg); color:var(--ke-text); font-family:'General Sans',sans-serif; -webkit-font-smoothing:antialiased; }
body::after{ content:''; position:fixed; inset:0; background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); opacity:.028; pointer-events:none; z-index:9999; }
.num{ font-family:'Satoshi','General Sans',sans-serif; font-weight:600; font-variant-numeric:tabular-nums; letter-spacing:-.01em; }
.ke-nav{ position:sticky; top:0; z-index:100; background:rgba(25,25,25,.96); backdrop-filter:blur(12px); border-bottom:1px solid var(--ke-border); padding:0 32px; display:flex; align-items:center; gap:14px; flex-wrap:wrap; }
.ke-nav-logo{ padding-right:20px; border-right:1px solid var(--ke-border); margin-right:4px; flex-shrink:0; display:flex; align-items:center; gap:12px; }
.ke-nav-logo img{ width:30px; height:30px; object-fit:contain; }
.ke-nav-logo b{ font-family:'Bitroad',sans-serif; font-size:15px; letter-spacing:.02em; }
.ke-nav-logo b span{ color:var(--ke-orange); }
.ke-nav-tabs{ display:flex; gap:2px; }
.ke-nav-tab{ font-size:10px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; padding:14px 12px; cursor:pointer; color:var(--ke-muted); border-bottom:3px solid transparent; font-family:'General Sans',sans-serif; white-space:nowrap; transition:color .15s; }
.ke-nav-tab:hover{ color:var(--ke-text); }
.ke-nav-tab.active{ color:var(--ke-orange); border-bottom-color:var(--ke-orange); }
.ke-nav-right{ margin-left:auto; display:flex; align-items:center; gap:8px; flex-wrap:wrap; padding:10px 0; }
.ke-preset{ font-size:10px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; padding:7px 12px; cursor:pointer; color:var(--ke-muted); background:var(--ke-card); border:1px solid var(--ke-border); border-radius:7px; transition:all .15s; font-family:'General Sans',sans-serif; }
.ke-preset:hover{ color:var(--ke-text); border-color:rgba(255,112,10,.4); }
.ke-preset.active{ color:var(--ke-orange); border-color:var(--ke-orange); background:rgba(255,112,10,.08); }
.ke-date{ display:flex; align-items:center; gap:6px; font-size:10px; color:var(--ke-muted); text-transform:uppercase; letter-spacing:.1em; }
.ke-date input{ background:var(--ke-card); border:1px solid var(--ke-border); color:var(--ke-text); border-radius:7px; padding:6px 8px; font-family:'Satoshi',sans-serif; font-size:12px; color-scheme:dark; }
.wrap{ max-width:1320px; margin:0 auto; padding:32px; }
.ke-page{ display:none; } .ke-page.active{ display:block; }
.ke-pg-header{ display:grid; grid-template-columns:1fr auto; align-items:end; gap:20px; padding-bottom:24px; margin-bottom:28px; border-bottom:2px solid rgba(255,112,10,.25); position:relative; }
.ke-pg-header::after{ content:''; position:absolute; bottom:-2px; left:0; width:80px; height:2px; background:var(--ke-orange); }
.ke-eyebrow{ font-size:10px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--ke-orange); margin-bottom:12px; display:flex; align-items:center; gap:8px; }
.ke-eyebrow::before{ content:''; width:18px; height:2px; background:var(--ke-orange); border-radius:999px; display:inline-block; }
.ke-pg-title{ font-family:'Bitroad',sans-serif; font-size:clamp(28px,3.6vw,46px); line-height:1; color:var(--ke-text); margin-bottom:10px; }
.ke-pg-title span{ color:var(--ke-orange); }
.ke-pg-sub{ font-size:12px; color:var(--ke-muted); letter-spacing:.04em; }
.ke-pg-stat{ text-align:right; }
.ke-pg-stat-val{ font-family:'Satoshi',sans-serif; font-weight:900; font-size:34px; color:var(--ke-orange); line-height:1; font-variant-numeric:tabular-nums; }
.ke-pg-stat-lbl{ font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--ke-muted); margin-top:4px; }
.ke-grid-5{ display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin-bottom:12px; }
.ke-grid-4{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:12px; }
.ke-grid-2{ display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px; }
@media(max-width:1000px){ .ke-grid-5{ grid-template-columns:repeat(3,1fr);} .ke-grid-4{ grid-template-columns:repeat(2,1fr);} .ke-grid-2{ grid-template-columns:1fr;} }
.ke-kc{ background:var(--ke-card); border:1px solid var(--ke-border); border-radius:12px; padding:18px 20px; position:relative; overflow:hidden; }
.ke-kc::before{ content:''; position:absolute; top:0; left:0; right:0; height:2px; background:var(--ke-orange); }
.ke-kc.g::before{ background:var(--ke-green);} .ke-kc.b::before{ background:var(--ke-blue);} .ke-kc.p::before{ background:var(--ke-purple);} .ke-kc.o::before{ background:var(--ke-warn);}
.ke-kl{ font-size:9px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--ke-muted); margin-bottom:8px; }
.ke-kv{ font-family:'Satoshi',sans-serif; font-weight:700; font-size:30px; line-height:1; color:var(--ke-orange); font-variant-numeric:tabular-nums; letter-spacing:-.01em; }
.ke-kv.g{ color:var(--ke-green);} .ke-kv.b{ color:var(--ke-blue);} .ke-kv.p{ color:var(--ke-purple);} .ke-kv.o{ color:var(--ke-warn);} .ke-kv.w{ color:var(--ke-text);}
.ke-ks{ font-size:10px; color:var(--ke-muted); margin-top:6px; }
.ke-sec-head{ display:flex; align-items:center; gap:10px; margin:0 0 16px; padding-bottom:10px; border-bottom:1px solid var(--ke-border); }
.ke-sec-line{ width:20px; height:2px; background:var(--ke-orange); border-radius:999px; }
.ke-sec-line.b{ background:var(--ke-blue);} .ke-sec-line.g{ background:var(--ke-green);}
.ke-sec-label{ font-size:10px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--ke-muted); flex:1; }
.ke-sec-pill{ padding:3px 10px; border-radius:999px; font-size:10px; font-weight:600; letter-spacing:.05em; background:rgba(255,112,10,.12); color:var(--ke-orange); }
.ke-block{ background:var(--ke-card); border:1px solid var(--ke-border); border-radius:12px; overflow:hidden; margin-bottom:16px; }
.ke-block-top{ height:2px; background:linear-gradient(90deg,var(--ke-orange),rgba(255,112,10,.06)); }
.ke-bh{ display:flex; justify-content:space-between; align-items:center; padding:11px 18px; border-bottom:1px solid var(--ke-border); background:var(--ke-header); }
.ke-bt{ font-size:10px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--ke-muted); }
.tbl-scroll{ overflow-x:auto; }
table.ke-t{ width:100%; border-collapse:collapse; }
table.ke-t thead th{ font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--ke-muted); padding:9px 14px; text-align:right; border-bottom:1px solid var(--ke-border); background:var(--ke-header); white-space:nowrap; }
table.ke-t thead th:first-child{ text-align:left; }
table.ke-t thead th.acc{ color:var(--ke-orange); }
table.ke-t tbody td{ padding:9px 14px; border-bottom:1px solid rgba(255,255,255,.035); font-size:12.5px; text-align:right; white-space:nowrap; font-family:'Satoshi','General Sans',sans-serif; font-weight:600; font-variant-numeric:tabular-nums; letter-spacing:-.01em; }
table.ke-t tbody td:first-child{ text-align:left; font-family:'General Sans',sans-serif; font-weight:500; color:var(--ke-text); white-space:normal; max-width:340px; }
table.ke-t tbody tr:last-child td{ border-bottom:none; }
table.ke-t tbody tr:hover td{ background:rgba(255,255,255,.012); }
table.ke-t tfoot td{ padding:11px 14px; font-family:'Satoshi',sans-serif; font-weight:700; font-size:13px; text-align:right; background:rgba(255,112,10,.03); border-top:1px solid rgba(255,112,10,.15); font-variant-numeric:tabular-nums; }
table.ke-t tfoot td:first-child{ text-align:left; }
.chart-wrap{ padding:18px; height:300px; }
.chart-wrap.pie{ height:300px; }
.muted{ color:var(--ke-muted); } .o{ color:var(--ke-orange);} .b{ color:var(--ke-blue);}
.funnel{ padding:20px; display:flex; flex-direction:column; gap:14px; }
.fn-row{ display:flex; justify-content:space-between; align-items:baseline; margin-bottom:5px; }
.fn-lbl{ font-size:10px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--ke-muted); }
.fn-val{ font-family:'Satoshi',sans-serif; font-weight:700; font-size:18px; font-variant-numeric:tabular-nums; }
.fn-bar{ height:12px; border-radius:6px; background:rgba(255,255,255,.05); overflow:hidden; }
.fn-fill{ height:100%; border-radius:6px; }
.fn-conv{ font-size:10px; color:var(--ke-muted); margin-top:4px; letter-spacing:.04em; }
.ke-footer{ padding:28px 32px; border-top:1px solid var(--ke-border); display:flex; justify-content:space-between; align-items:center; font-size:10px; color:var(--ke-muted); letter-spacing:.12em; text-transform:uppercase; }
#loading{ position:fixed; inset:0; background:var(--ke-bg); z-index:10000; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; }
#loading img{ width:56px; height:56px; object-fit:contain; animation:pulse 1.3s ease-in-out infinite; }
#loading div{ font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--ke-muted); }
@keyframes pulse{ 0%,100%{opacity:.35;} 50%{opacity:1;} }
#err{ display:none; margin:24px 0; background:var(--ke-card); border-left:3px solid var(--ke-bad); border-radius:0 10px 10px 0; padding:16px 20px; }
</style>
</head>
<body>
<div id="loading"><img src="data:image/png;base64,__LOGO__"><div>Cargando datos…</div></div>
<nav class="ke-nav">
  <div class="ke-nav-logo"><img src="data:image/png;base64,__LOGO__"><b>PIRAMIDE<span>HOME</span></b></div>
  <div class="ke-nav-tabs">
    <div class="ke-nav-tab active" data-pg="overview">Overview</div>
    <div class="ke-nav-tab" data-pg="meta">Meta</div>
    <div class="ke-nav-tab" data-pg="google">Google</div>
    <div class="ke-nav-tab" data-pg="ga4">GA4</div>
  </div>
  <div class="ke-nav-right">
    <span class="ke-preset" data-p="mtd">Mes actual</span>
    <span class="ke-preset" data-p="7">7d</span>
    <span class="ke-preset" data-p="30">30d</span>
    <span class="ke-preset" data-p="90">90d</span>
    <span class="ke-preset" data-p="all">Todo</span>
    <span class="ke-date">Desde <input type="date" id="from"></span>
    <span class="ke-date">Hasta <input type="date" id="to"></span>
  </div>
</nav>
<div class="wrap">
  <div class="ke-pg-header">
    <div>
      <div class="ke-eyebrow">Performance · Meta · Google · GA4 · Facturacion</div>
      <div class="ke-pg-title">PERFORMANCE<br><span id="rangeLbl">—</span></div>
      
    </div>
    <div class="ke-pg-stat"><div class="ke-pg-stat-val num" id="hAcos">—</div><div class="ke-pg-stat-lbl">ACOS del periodo</div></div>
  </div>
  <div id="err"><p style="font-size:13px;color:rgba(230,230,230,.7);line-height:1.6;">No se pudieron cargar los datos. Reintenta recargando la pagina.</p></div>

  <section class="ke-page active" id="pg-overview">
    <div class="ke-grid-5">
      <div class="ke-kc"><div class="ke-kl">Gasto (inversion)</div><div class="ke-kv num" id="oGasto">—</div><div class="ke-ks" id="oGastoSub">Meta + Google</div></div>
      <div class="ke-kc g"><div class="ke-kl">Facturacion</div><div class="ke-kv g num" id="oVentas">—</div><div class="ke-ks" id="oVentasSub">Ordenes pagas</div></div>
      <div class="ke-kc o"><div class="ke-kl">ACOS</div><div class="ke-kv o num" id="oAcos">—</div><div class="ke-ks">Gasto / Facturacion</div></div>
      <div class="ke-kc b"><div class="ke-kl">ROAS</div><div class="ke-kv b num" id="oRoas">—</div><div class="ke-ks">Facturacion / Gasto</div></div>
      <div class="ke-kc p"><div class="ke-kl">Ticket promedio</div><div class="ke-kv p num" id="oTicket">—</div><div class="ke-ks">Facturacion / ordenes</div></div>
    </div>
    <div class="ke-grid-2">
      <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Evolucion diaria · Gasto vs Facturacion</span><span class="ke-bt o" id="chartRange">—</span></div><div class="chart-wrap"><canvas id="trend"></canvas></div></div>
      <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Trafico por fuente / medio (sesiones GA4)</span></div><div class="chart-wrap pie"><canvas id="pie"></canvas></div></div>
    </div>
  </section>

  <section class="ke-page" id="pg-meta">
    <div class="ke-sec-head"><div class="ke-sec-line"></div><span class="ke-sec-label">Meta Ads</span><span class="ke-sec-pill" id="metaSpendPill">—</span></div>
    <div class="ke-grid-4">
      <div class="ke-kc"><div class="ke-kl">Inversion Meta</div><div class="ke-kv num" id="mSpend">—</div></div>
      <div class="ke-kc g"><div class="ke-kl">Valor compras</div><div class="ke-kv g num" id="mVal">—</div><div class="ke-ks" id="mPurch">—</div></div>
      <div class="ke-kc b"><div class="ke-kl">ROAS Meta</div><div class="ke-kv b num" id="mRoas">—</div></div>
      <div class="ke-kc o"><div class="ke-kl">CTR · CPM</div><div class="ke-kv o num" id="mCtr">—</div><div class="ke-ks" id="mCpm">—</div></div>
    </div>
    <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Meta · por campana</span><span class="ke-bt muted" id="mCampCount">—</span></div>
      <div class="tbl-scroll"><table class="ke-t" id="tMeta"><thead><tr><th>Campana</th><th>Inversion</th><th>Impr.</th><th>Clicks</th><th>CTR</th><th>CPC</th><th class="acc">Compras</th><th class="acc">Valor</th><th class="acc">ROAS</th></tr></thead><tbody></tbody><tfoot></tfoot></table></div>
    </div>
  </section>

  <section class="ke-page" id="pg-google">
    <div class="ke-sec-head"><div class="ke-sec-line b"></div><span class="ke-sec-label">Google Ads</span><span class="ke-sec-pill" id="gSpendPill">—</span></div>
    <div class="ke-grid-4">
      <div class="ke-kc"><div class="ke-kl">Inversion Google</div><div class="ke-kv num" id="gSpend">—</div></div>
      <div class="ke-kc"><div class="ke-kl">Impresiones</div><div class="ke-kv w num" id="gImpr">—</div></div>
      <div class="ke-kc"><div class="ke-kl">Clicks</div><div class="ke-kv w num" id="gClicks">—</div></div>
      <div class="ke-kc o"><div class="ke-kl">CTR · CPC</div><div class="ke-kv o num" id="gCtr">—</div><div class="ke-ks" id="gCpc">—</div></div>
    </div>
    <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Google · por campana</span><span class="ke-bt muted" id="gCampCount">—</span></div>
      <div class="tbl-scroll"><table class="ke-t" id="tGoogle"><thead><tr><th>Campana</th><th>Inversion</th><th>Impr.</th><th>Clicks</th><th>CTR</th><th>CPC</th></tr></thead><tbody></tbody><tfoot></tfoot></table></div>
    </div>
  </section>

  <section class="ke-page" id="pg-ga4">
    <div class="ke-sec-head"><div class="ke-sec-line g"></div><span class="ke-sec-label">Analytics GA4 · Embudo y trafico</span><span class="ke-sec-pill" id="gaSessPill">—</span></div>
    <div class="ke-grid-4">
      <div class="ke-kc"><div class="ke-kl">Sesiones</div><div class="ke-kv w num" id="gaSess">—</div><div class="ke-ks" id="gaUsers">—</div></div>
      <div class="ke-kc g"><div class="ke-kl">Evento clave · Compras</div><div class="ke-kv g num" id="gaTx">—</div><div class="ke-ks" id="gaCvr">—</div></div>
      <div class="ke-kc p"><div class="ke-kl">Facturacion GA4 (purchase)</div><div class="ke-kv p num" id="gaRev">—</div><div class="ke-ks">Evento clave · purchase</div></div>
      <div class="ke-kc o"><div class="ke-kl">Ticket promedio GA4</div><div class="ke-kv o num" id="gaTicket">—</div><div class="ke-ks">Facturacion GA4 / compras</div></div>
    </div>
    <div class="ke-grid-2">
      <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Embudo de conversion</span></div><div class="funnel" id="funnel"></div></div>
      <div class="ke-block"><div class="ke-block-top"></div><div class="ke-bh"><span class="ke-bt">Trafico por fuente / medio (top 12)</span></div>
        <div class="tbl-scroll"><table class="ke-t" id="tGa"><thead><tr><th>Fuente / Medio</th><th>Sesiones</th><th>Usuarios</th><th class="acc">Compras</th></tr></thead><tbody></tbody><tfoot></tfoot></table></div>
      </div>
    </div>
  </section>
</div>
<div class="ke-footer">
  <img src="data:image/png;base64,__LOGO__" style="width:26px;height:26px;object-fit:contain;opacity:.7">
  <div id="footLbl">Piramide Home · Performance · Krab-e</div>
  <img src="data:image/png;base64,__CRAB__" style="width:30px;height:30px;object-fit:contain;opacity:.2">
</div>
<script>
const SUPA="__URL__", ANON="__ANON__";
const TABLES={
  meta:"piramidehome_meta_ads?select=date,campaign_name,amount_spent,impressions,clicks,website_purchases,purchases_conv_value",
  google:"piramidehome_google_ads?select=date,campaign_name,cost,impressions,clicks",
  ga4:"piramidehome_ga4_sessions?select=date,source_medium,sessions,total_users,add_to_carts,transactions,total_revenue",
  ventas:"piramidehome_tiendanube_orders?select=date,order_payment_status,order_total_paid,order_total_products"
};
let DATA={meta:[],google:[],ga4:[],ventas:[]};
let RANGE={from:null,to:null};
let chTrend=null, chPie=null;
async function fetchTable(q){
  let out=[], from=0, step=1000;
  while(true){
    const res=await fetch(SUPA+"/"+q, {headers:{apikey:ANON, Authorization:"Bearer "+ANON, Range:from+"-"+(from+step-1), "Range-Unit":"items"}});
    if(!res.ok) throw new Error("fetch "+q+" "+res.status);
    const rows=await res.json(); out=out.concat(rows);
    if(rows.length<step) break; from+=step;
  }
  return out;
}
function iso(d){ return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0"); }
function parseISO(s){ const p=String(s).slice(0,10).split("-"); return new Date(+p[0],+p[1]-1,+p[2]); }
function fmtShort(s){ const d=parseISO(s); return String(d.getDate()).padStart(2,"0")+"/"+String(d.getMonth()+1).padStart(2,"0"); }
const nf0=new Intl.NumberFormat("es-AR",{maximumFractionDigits:0});
const nf1=new Intl.NumberFormat("es-AR",{minimumFractionDigits:1,maximumFractionDigits:1});
const nf2=new Intl.NumberFormat("es-AR",{minimumFractionDigits:2,maximumFractionDigits:2});
function money(n){ if(n==null||isNaN(n)) return "$0"; return "$"+nf0.format(Math.round(n)); }
function pct(n){ if(n==null||isNaN(n)||!isFinite(n)) return "—"; return nf1.format(n)+"%"; }
function xd(n){ if(n==null||isNaN(n)||!isFinite(n)) return "—"; return nf2.format(n)+"x"; }
function num(n){ return nf0.format(Math.round(n||0)); }
function inRange(s){ const d=iso(parseISO(s)); return d>=RANGE.from && d<=RANGE.to; }
function sum(arr,f){ let t=0; for(const r of arr){ const v=f(r); if(v!=null&&!isNaN(v)) t+=+v; } return t; }
function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }
const PAL=["#ff700a","#4fa3ff","#4dcc80","#c084fc","#ffd88a","#ff6eb4","rgba(230,230,230,.35)"];
function render(){
  document.getElementById("rangeLbl").textContent = RANGE.label||"";
  document.getElementById("chartRange").textContent = RANGE.from+" → "+RANGE.to;
  document.getElementById("footLbl").textContent = "Piramide Home · Performance · "+RANGE.from+" a "+RANGE.to+" · Krab-e";
  const meta=DATA.meta.filter(r=>inRange(r.date)), goog=DATA.google.filter(r=>inRange(r.date)), ga=DATA.ga4.filter(r=>inRange(r.date)), ven=DATA.ventas.filter(r=>inRange(r.date));
  const mSpend=sum(meta,r=>r.amount_spent), gSpend=sum(goog,r=>r.cost), inv=mSpend+gSpend;
  const isPaid=r=>{ const s=(r.order_payment_status||"").toLowerCase(); return s==="paid"||s==="pagado"||s==="pagada"; };
  const venPaid=ven.filter(isPaid);
  const ventas=sum(venPaid,r=>r.order_total_paid), orders=venPaid.length;
  const ticket= orders>0 ? ventas/orders : null, acos = ventas>0 ? inv/ventas*100 : null, roas = inv>0 ? ventas/inv : null;
  document.getElementById("hAcos").textContent=pct(acos);
  document.getElementById("oGasto").textContent=money(inv);
  document.getElementById("oGastoSub").textContent="Meta "+money(mSpend)+" · Google "+money(gSpend);
  document.getElementById("oVentas").textContent=money(ventas);
  document.getElementById("oVentasSub").textContent=num(orders)+" ordenes pagas";
  document.getElementById("oAcos").textContent=pct(acos);
  document.getElementById("oRoas").textContent=xd(roas);
  document.getElementById("oTicket").textContent=money(ticket||0);
  buildTrend(meta,goog,venPaid); buildPie(ga);
  const mImpr=sum(meta,r=>r.impressions), mClicks=sum(meta,r=>r.clicks), mVal=sum(meta,r=>r.purchases_conv_value), mPurch=sum(meta,r=>r.website_purchases);
  document.getElementById("mSpend").textContent=money(mSpend);
  document.getElementById("mVal").textContent=money(mVal);
  document.getElementById("mPurch").textContent=num(mPurch)+" compras";
  document.getElementById("mRoas").textContent=xd(mSpend>0?mVal/mSpend:null);
  document.getElementById("mCtr").textContent=pct(mImpr>0?mClicks/mImpr*100:null);
  document.getElementById("mCpm").textContent="CPM "+money(mImpr>0?mSpend/mImpr*1000:0);
  document.getElementById("metaSpendPill").textContent=money(mSpend);
  buildMeta(meta);
  const gImpr=sum(goog,r=>r.impressions), gClicks=sum(goog,r=>r.clicks);
  document.getElementById("gSpend").textContent=money(gSpend);
  document.getElementById("gImpr").textContent=num(gImpr);
  document.getElementById("gClicks").textContent=num(gClicks);
  document.getElementById("gCtr").textContent=pct(gImpr>0?gClicks/gImpr*100:null);
  document.getElementById("gCpc").textContent="CPC "+money(gClicks>0?gSpend/gClicks:0);
  document.getElementById("gSpendPill").textContent=money(gSpend);
  buildGoogle(goog);
  const sess=sum(ga,r=>r.sessions), users=sum(ga,r=>r.total_users), atc=sum(ga,r=>r.add_to_carts), tx=sum(ga,r=>r.transactions), rev=sum(ga,r=>r.total_revenue);
  document.getElementById("gaSess").textContent=num(sess);
  document.getElementById("gaUsers").textContent=num(users)+" usuarios";
  document.getElementById("gaTx").textContent=num(tx);
  document.getElementById("gaCvr").textContent="CVR "+pct(sess>0?tx/sess*100:null);
  document.getElementById("gaRev").textContent=money(rev);
  document.getElementById("gaTicket").textContent=money(tx>0?rev/tx:0);
  document.getElementById("gaSessPill").textContent=num(sess)+" sesiones";
  buildFunnel(atc,tx); buildGa(ga);
}
function aggBy(arr,key,fields){
  const m={};
  for(const r of arr){ const k=r[key]||"(sin nombre)"; if(!m[k]){ m[k]={}; fields.forEach(f=>m[k][f]=0);} fields.forEach(f=>{ const v=r[f]; if(v!=null&&!isNaN(v)) m[k][f]+=+v; }); }
  return Object.entries(m).map(([k,v])=>({name:k,...v}));
}
function buildMeta(rows){
  let d=aggBy(rows,"campaign_name",["amount_spent","impressions","clicks","purchases_conv_value","website_purchases"]);
  d.sort((a,b)=>b.amount_spent-a.amount_spent);
  const tb=document.querySelector("#tMeta tbody"); tb.innerHTML="";
  let tS=0,tI=0,tC=0,tV=0,tP=0;
  for(const r of d){
    tS+=r.amount_spent; tI+=r.impressions; tC+=r.clicks; tV+=r.purchases_conv_value; tP+=r.website_purchases;
    const ctr=r.impressions>0?r.clicks/r.impressions*100:null, cpc=r.clicks>0?r.amount_spent/r.clicks:null, roas=r.amount_spent>0?r.purchases_conv_value/r.amount_spent:null;
    tb.insertAdjacentHTML("beforeend","<tr><td>"+esc(r.name)+"</td><td>"+money(r.amount_spent)+"</td><td>"+num(r.impressions)+"</td><td>"+num(r.clicks)+"</td><td>"+pct(ctr)+"</td><td>"+money(cpc)+"</td><td class='o'>"+num(r.website_purchases)+"</td><td class='o'>"+money(r.purchases_conv_value)+"</td><td class='b'>"+xd(roas)+"</td></tr>");
  }
  const ctrT=tI>0?tC/tI*100:null, cpcT=tC>0?tS/tC:null, roasT=tS>0?tV/tS:null;
  document.querySelector("#tMeta tfoot").innerHTML="<tr><td>Total ("+d.length+")</td><td>"+money(tS)+"</td><td>"+num(tI)+"</td><td>"+num(tC)+"</td><td>"+pct(ctrT)+"</td><td>"+money(cpcT)+"</td><td>"+num(tP)+"</td><td>"+money(tV)+"</td><td>"+xd(roasT)+"</td></tr>";
  document.getElementById("mCampCount").textContent=d.length+" campanas";
}
function buildGoogle(rows){
  let d=aggBy(rows,"campaign_name",["cost","impressions","clicks"]);
  d.sort((a,b)=>b.cost-a.cost);
  const tb=document.querySelector("#tGoogle tbody"); tb.innerHTML="";
  let tS=0,tI=0,tC=0;
  for(const r of d){
    tS+=r.cost; tI+=r.impressions; tC+=r.clicks;
    const ctr=r.impressions>0?r.clicks/r.impressions*100:null, cpc=r.clicks>0?r.cost/r.clicks:null;
    tb.insertAdjacentHTML("beforeend","<tr><td>"+esc(r.name)+"</td><td>"+money(r.cost)+"</td><td>"+num(r.impressions)+"</td><td>"+num(r.clicks)+"</td><td>"+pct(ctr)+"</td><td>"+money(cpc)+"</td></tr>");
  }
  const ctrT=tI>0?tC/tI*100:null, cpcT=tC>0?tS/tC:null;
  document.querySelector("#tGoogle tfoot").innerHTML="<tr><td>Total ("+d.length+")</td><td>"+money(tS)+"</td><td>"+num(tI)+"</td><td>"+num(tC)+"</td><td>"+pct(ctrT)+"</td><td>"+money(cpcT)+"</td></tr>";
  document.getElementById("gCampCount").textContent=d.length+" campanas";
}
function buildGa(rows){
  let d=aggBy(rows,"source_medium",["sessions","total_users","transactions"]);
  d.sort((a,b)=>b.sessions-a.sessions);
  const top=d.slice(0,12);
  const tb=document.querySelector("#tGa tbody"); tb.innerHTML="";
  for(const r of top){ tb.insertAdjacentHTML("beforeend","<tr><td>"+esc(r.name)+"</td><td>"+num(r.sessions)+"</td><td>"+num(r.total_users)+"</td><td class='o'>"+num(r.transactions)+"</td></tr>"); }
  const tS=sum(d,r=>r.sessions),tU=sum(d,r=>r.total_users),tT=sum(d,r=>r.transactions);
  document.querySelector("#tGa tfoot").innerHTML="<tr><td>Total ("+d.length+")</td><td>"+num(tS)+"</td><td>"+num(tU)+"</td><td>"+num(tT)+"</td></tr>";
}
function buildFunnel(atc,tx){
  const steps=[{l:"Vista de producto",v:null,c:"#4fa3ff"},{l:"Add to cart",v:atc,c:"#ffd88a"},{l:"Payment info",v:null,c:"#c084fc"},{l:"Compra (purchase)",v:tx,c:"#4dcc80"}];
  const vals=steps.map(s=>s.v).filter(v=>v!=null); const max=Math.max.apply(null,vals.concat([1]));
  let html="";
  steps.forEach((s,i)=>{
    if(s.v==null){ html+="<div><div class='fn-row'><span class='fn-lbl'>"+s.l+"</span><span class='fn-val muted'>s/d</span></div><div class='fn-bar'><div class='fn-fill' style='width:3%;background:rgba(230,230,230,.15)'></div></div><div class='fn-conv'>pendiente de dato en GA4</div></div>"; return; }
    const w=Math.max(s.v/max*100, s.v>0?2:0);
    let prev=null; for(let j=i-1;j>=0;j--){ if(steps[j].v!=null){ prev=steps[j]; break; } }
    let conv = prev ? (prev.v>0? nf1.format(s.v/prev.v*100):"0")+"% desde "+prev.l.toLowerCase() : "inicio con dato";
    html+="<div><div class='fn-row'><span class='fn-lbl'>"+s.l+"</span><span class='fn-val' style='color:"+s.c+"'>"+num(s.v)+"</span></div><div class='fn-bar'><div class='fn-fill' style='width:"+w+"%;background:"+s.c+"'></div></div><div class='fn-conv'>"+conv+"</div></div>";
  });
  document.getElementById("funnel").innerHTML=html;
}
function buildTrend(meta,goog,venPaid){
  const days={};
  const add=(d,k,v)=>{ const day=iso(parseISO(d)); if(!days[day]) days[day]={inv:0,ven:0}; days[day][k]+=(+v||0); };
  meta.forEach(r=>add(r.date,"inv",r.amount_spent));
  goog.forEach(r=>add(r.date,"inv",r.cost));
  venPaid.forEach(r=>add(r.date,"ven",r.order_total_paid));
  const labels=Object.keys(days).sort();
  const inv=labels.map(d=>Math.round(days[d].inv)), ven=labels.map(d=>Math.round(days[d].ven)), lab=labels.map(fmtShort);
  if(chTrend) chTrend.destroy();
  chTrend=new Chart(document.getElementById("trend"),{ type:"bar",
    data:{ labels:lab, datasets:[
      {label:"Facturacion", data:ven, backgroundColor:"rgba(77,204,128,.55)", borderColor:"#4dcc80", borderWidth:1, borderRadius:3, order:2},
      {label:"Gasto", type:"line", data:inv, borderColor:"#ff700a", backgroundColor:"rgba(255,112,10,.12)", borderWidth:2, tension:.3, pointRadius:0, fill:true, order:1}
    ]},
    options:{ responsive:true, maintainAspectRatio:false,
      plugins:{ legend:{ labels:{ color:"#e6e6e6", font:{family:"General Sans",size:11}, usePointStyle:true, boxWidth:8 } }, tooltip:{ callbacks:{ label:c=>c.dataset.label+": $"+nf0.format(c.parsed.y) } } },
      scales:{ x:{ ticks:{ color:"rgba(230,230,230,.38)", font:{family:"Satoshi",size:10}, maxRotation:0, autoSkip:true, maxTicksLimit:12 }, grid:{ color:"rgba(255,255,255,.04)" } }, y:{ ticks:{ color:"rgba(230,230,230,.38)", font:{family:"Satoshi",size:10}, callback:v=>"$"+nf0.format(v) }, grid:{ color:"rgba(255,255,255,.04)" } } } }
  });
}
function buildPie(ga){
  let d=aggBy(ga,"source_medium",["sessions"]);
  d.sort((a,b)=>b.sessions-a.sessions);
  const top=d.slice(0,6), otros=d.slice(6).reduce((t,r)=>t+r.sessions,0);
  const labels=top.map(r=>r.name), vals=top.map(r=>r.sessions);
  if(otros>0){ labels.push("Otros"); vals.push(otros); }
  const tot=vals.reduce((a,b)=>a+b,0)||1;
  if(chPie) chPie.destroy();
  chPie=new Chart(document.getElementById("pie"),{ type:"doughnut",
    data:{ labels:labels, datasets:[{ data:vals, backgroundColor:PAL.slice(0,labels.length), borderColor:"#191919", borderWidth:2 }] },
    options:{ responsive:true, maintainAspectRatio:false, cutout:"58%",
      plugins:{ legend:{ position:"right", labels:{ color:"#e6e6e6", font:{family:"General Sans",size:10}, usePointStyle:true, boxWidth:8, padding:8 } }, tooltip:{ callbacks:{ label:c=>c.label+": "+nf0.format(c.parsed)+" ("+nf1.format(c.parsed/tot*100)+"%)" } } } }
  });
}
document.querySelectorAll(".ke-nav-tab").forEach(t=>t.addEventListener("click",()=>{
  document.querySelectorAll(".ke-nav-tab").forEach(x=>x.classList.remove("active"));
  document.querySelectorAll(".ke-page").forEach(x=>x.classList.remove("active"));
  t.classList.add("active");
  document.getElementById("pg-"+t.dataset.pg).classList.add("active");
  window.scrollTo(0,0);
}));
function setPreset(p){
  const today=new Date(); today.setHours(0,0,0,0);
  let from,to=new Date(today), label;
  if(p==="mtd"){ from=new Date(today.getFullYear(),today.getMonth(),1); label=from.toLocaleDateString("es-AR",{month:"long",year:"numeric"}).toUpperCase(); }
  else if(p==="all"){ from=new Date(2000,0,1); label="HISTORICO"; }
  else { const n=+p; from=new Date(today); from.setDate(from.getDate()-(n-1)); label="ULTIMOS "+n+"D"; }
  RANGE={from:iso(from),to:iso(to),label:label};
  document.getElementById("from").value=RANGE.from; document.getElementById("to").value=RANGE.to;
  document.querySelectorAll(".ke-preset").forEach(e=>e.classList.toggle("active",e.dataset.p===p));
  render();
}
document.querySelectorAll(".ke-preset").forEach(e=>e.addEventListener("click",()=>setPreset(e.dataset.p)));
function onInput(){
  RANGE.from=document.getElementById("from").value; RANGE.to=document.getElementById("to").value; RANGE.label="PERSONALIZADO";
  document.getElementById("rangeLbl").textContent="";
  document.querySelectorAll(".ke-preset").forEach(e=>e.classList.remove("active"));
  if(RANGE.from&&RANGE.to&&RANGE.from<=RANGE.to) render();
}
document.getElementById("from").addEventListener("change",onInput);
document.getElementById("to").addEventListener("change",onInput);
async function init(){
  try{
    const [m,g,a,v]=await Promise.all([fetchTable(TABLES.meta),fetchTable(TABLES.google),fetchTable(TABLES.ga4),fetchTable(TABLES.ventas)]);
    DATA={meta:m,google:g,ga4:a,ventas:v};
    document.getElementById("loading").style.display="none";
    setPreset("mtd");
  }catch(e){ document.getElementById("loading").style.display="none"; document.getElementById("err").style.display="block"; console.error(e); }
}
init();
</script>
</body>
</html>
"""
out = HTML.replace("__FONT__", FONT).replace("__LOGO__", LOGO).replace("__CRAB__", CRAB).replace("__URL__", SUPA_URL).replace("__ANON__", ANON)
with open("/sessions/vibrant-focused-wozniak/mnt/outputs/index.html","w",encoding="utf-8") as f:
    f.write(out)
print("WROTE", len(out), "bytes")
