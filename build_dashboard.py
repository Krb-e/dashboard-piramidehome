#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build del dashboard de Piramide Home (Krab-e).
index.html self-contained que lee EN VIVO de Supabase (tablas piramidehome_*) con la anon key publishable.
Branding Krab-e (skill krab-e-branding) + estandar UI Krab-e (Satoshi en numeros, selector Looker default mes en curso).
"""
import os

SKILL = "/sessions/vibrant-focused-wozniak/mnt/.claude/skills/krab-e-branding/assets"

def load(name):
    with open(f"{SKILL}/{name}.b64") as f:
        return f.read().strip()

LOGO = load("logo")
CRAB = load("pixel_crab")
FONT = load("font_bitroad")

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
:root{
  --ke-bg:#191919; --ke-card:#1f1f1f; --ke-header:#2a2a2a;
  --ke-text:#e6e6e6; --ke-muted:rgba(230,230,230,0.38); --ke-border:rgba(230,230,230,0.07);
  --ke-orange:#ff700a; --ke-ok:#9dffbf; --ke-warn:#ffd88a; --ke-bad:#ffb0a0;
  --ke-green:#4dcc80; --ke-purple:#c084fc; --ke-blue:#4fa3ff; --ke-pink:#ff6eb4;
}
*{box-sizing:border-box; margin:0; padding:0;}
body{ background:var(--ke-bg); color:var(--ke-text); font-family:'General Sans',sans-serif; -webkit-font-smoothing:antialiased; }
body::after{ content:''; position:fixed; inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity:.028; pointer-events:none; z-index:9999; }
.num{ font-family:'Satoshi','General Sans',sans-serif; font-weight:600; font-variant-numeric:tabular-nums; letter-spacing:-.01em; }

.ke-nav{ position:sticky; top:0; z-index:100; background:rgba(25,25,25,.96); backdrop-filter:blur(12px);
  border-bottom:1px solid var(--ke-border); padding:0 32px; display:flex; align-items:center; gap:14px; flex-wrap:wrap; }
.ke-nav-logo{ padding-right:20px; border-right:1px solid var(--ke-border); margin-right:4px; flex-shrink:0; display:flex; align-items:center; gap:12px; }
.ke-nav-logo img{ width:30px; height:30px; object-fit:contain; }
.ke-nav-logo b{ font-family:'Bitroad',sans-serif; font-size:15px; letter-spacing:.02em; }
.ke-nav-logo b span{ color:var(--ke-orange); }
.ke-nav-right{ margin-left:auto; display:flex; align-items:center; gap:8px; flex-wrap:wrap; padding:10px 0; }
.ke-preset{ font-size:10px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; padding:7px 12px;
  cursor:pointer; color:var(--ke-muted); background:var(--ke-card); border:1px solid var(--ke-border);
  border-radius:7px; transition:all .15s; font-family:'General Sans',sans-serif; }
.ke-preset:hover{ color:var(--ke-text); border-color:rgba(255,112,10,.4); }
.ke-preset.active{ color:var(--ke-orange); border-color:var(--ke-orange); background:rgba(255,112,10,.08); }
.ke-date{ display:flex; align-items:center; gap:6px; font-size:10px; color:var(--ke-muted); text-transform:uppercase; letter-spacing:.1em; }
.ke-date input{ background:var(--ke-card); border:1px solid var(--ke-border); color:var(--ke-text);
  border-radius:7px; padding:6px 8px; font-family:'Satoshi',sans-serif; font-size:12px; color-scheme:dark; }

.wrap{ max-width:1320px; margin:0 auto; padding:32px; }

.ke-pg-header{ display:grid; grid-template-columns:1fr auto; align-items:end; gap:20px;
  padding-bottom:24px; margin-bottom:28px; border-bottom:2px solid rgba(255,112,10,.25); position:relative; }
.ke-pg-header::after{ content:''; position:absolute; bottom:-2px; left:0; width:80px; height:2px; background:var(--ke-orange); }
.ke-eyebrow{ font-size:10px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--ke-orange);
  margin-bottom:12px; display:flex; align-items:center; gap:8px; }
.ke-eyebrow::before{ content:''; width:18px; height:2px; background:var(--ke-orange); border-radius:999px; display:inline-block; }
.ke-pg-title{ font-family:'Bitroad',sans-serif; font-size:clamp(30px,4vw,50px); line-height:1; color:var(--ke-text); margin-bottom:10px; }
.ke-pg-title span{ color:var(--ke-orange); }
.ke-pg-sub{ font-size:12px; color:var(--ke-muted); letter-spacing:.04em; }
.ke-pg-stat{ text-align:right; }
.ke-pg-stat-val{ font-family:'Satoshi',sans-serif; font-weight:900; font-size:34px; color:var(--ke-orange); line-height:1; font-variant-numeric:tabular-nums; }
.ke-pg-stat-lbl{ font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--ke-muted); margin-top:4px; }

.ke-grid-4{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:12px; }
.ke-grid-3{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:12px; }
@media(max-width:900px){ .ke-grid-4{ grid-template-columns:repeat(2,1fr);} .ke-grid-3{ grid-template-columns:1fr;} }
.ke-kc{ background:var(--ke-card); border:1px solid var(--ke-border); border-radius:12px; padding:18px 20px; position:relative; overflow:hidden; }
.ke-kc::before{ content:''; position:absolute; top:0; left:0; right:0; height:2px; background:var(--ke-orange); }
.ke-kc.g::before{ background:var(--ke-green);} .ke-kc.b::before{ background:var(--ke-blue);}
.ke-kc.p::before{ background:var(--ke-purple);} .ke-kc.o::before{ background:var(--ke-warn);} .ke-kc.r::before{ background:var(--ke-bad);}
.ke-kl{ font-size:9px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--ke-muted); margin-bottom:8px; }
.ke-kv{ font-family:'Satoshi',sans-serif; font-weight:700; font-size:32px; line-height:1; color:var(--ke-orange); font-variant-numeric:tabular-nums; letter-spacing:-.01em; }
.ke-kv.g{ color:var(--ke-green);} .ke-kv.b{ color:var(--ke-blue);} .ke-kv.p{ color:var(--ke-purple);}
.ke-kv.o{ color:var(--ke-warn);} .ke-kv.r{ color:var(--ke-bad);} .ke-kv.w{ color:var(--ke-text);}
.ke-ks{ font-size:10px; color:var(--ke-muted); margin-top:6px; }

.ke-sec-head{ display:flex; align-items:center; gap:10px; margin:38px 0 16px; padding-bottom:10px; border-bottom:1px solid var(--ke-border); }
.ke-sec-line{ width:20px; height:2px; background:var(--ke-orange); border-radius:999px; }
.ke-sec-line.b{ background:var(--ke-blue);} .ke-sec-line.g{ background:var(--ke-green);} .ke-sec-line.p{ background:var(--ke-purple);}
.ke-sec-label{ font-size:10px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--ke-muted); flex:1; }
.ke-sec-pill{ padding:3px 10px; border-radius:999px; font-size:10px; font-weight:600; letter-spacing:.05em; background:rgba(255,112,10,.12); color:var(--ke-orange); }

.ke-block{ background:var(--ke-card); border:1px solid var(--ke-border); border-radius:12px; overflow:hidden; margin-bottom:16px; }
.ke-block-top{ height:2px; background:linear-gradient(90deg,var(--ke-orange),rgba(255,112,10,.06)); }
.ke-bh{ display:flex; justify-content:space-between; align-items:center; padding:11px 18px; border-bottom:1px solid var(--ke-border); background:var(--ke-header); }
.ke-bt{ font-size:10px; font-weight:700; letter-spacing:.16em; text-transform:uppercase; color:var(--ke-muted); }
.tbl-scroll{ overflow-x:auto; }
table.ke-t{ width:100%; border-collapse:collapse; }
table.ke-t thead th{ font-size:9px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--ke-muted);
  padding:9px 14px; text-align:right; border-bottom:1px solid var(--ke-border); background:var(--ke-header); white-space:nowrap; }
table.ke-t thead th:first-child{ text-align:left; }
table.ke-t thead th.acc{ color:var(--ke-orange); }
table.ke-t tbody td{ padding:9px 14px; border-bottom:1px solid rgba(255,255,255,.035); font-size:12.5px; text-align:right; white-space:nowrap;
  font-family:'Satoshi','General Sans',sans-serif; font-weight:600; font-variant-numeric:tabular-nums; letter-spacing:-.01em; }
table.ke-t tbody td:first-child{ text-align:left; font-family:'General Sans',sans-serif; font-weight:500; color:var(--ke-text); white-space:normal; max-width:340px; }
table.ke-t tbody tr:last-child td{ border-bottom:none; }
table.ke-t tbody tr:hover td{ background:rgba(255,255,255,.012); }
table.ke-t tfoot td{ padding:11px 14px; font-family:'Satoshi',sans-serif; font-weight:700; font-size:13px; text-align:right;
  background:rgba(255,112,10,.03); border-top:1px solid rgba(255,112,10,.15); font-variant-numeric:tabular-nums; }
table.ke-t tfoot td:first-child{ text-align:left; }

.chart-wrap{ padding:18px; height:320px; }
.muted{ color:var(--ke-muted); }
.o{ color:var(--ke-orange);} .g{ color:var(--ke-green);} .b{ color:var(--ke-blue);} .r{ color:var(--ke-bad);}

.ke-footer{ padding:28px 32px; border-top:1px solid var(--ke-border); display:flex; justify-content:space-between; align-items:center;
  font-size:10px; color:var(--ke-muted); letter-spacing:.12em; text-transform:uppercase; }

#loading{ position:fixed; inset:0; background:var(--ke-bg); z-index:10000; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; }
#loading img{ width:56px; height:56px; object-fit:contain; animation:pulse 1.3s ease-in-out infinite; }
#loading div{ font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--ke-muted); }
@keyframes pulse{ 0%,100%{opacity:.35;} 50%{opacity:1;} }
#err{ display:none; margin:24px 0; }
</style>
</head>
<body>

<div id="loading"><img src="data:image/png;base64,__LOGO__"><div>Cargando datos…</div></div>

<nav class="ke-nav">
  <div class="ke-nav-logo"><img src="data:image/png;base64,__LOGO__"><b>PIRAMIDE<span>HOME</span></b></div>
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
      <div class="ke-eyebrow">Performance · Detrics + Meta + Facturacion</div>
      <div class="ke-pg-title">PERFORMANCE<br><span id="rangeLbl">—</span></div>
      <div class="ke-pg-sub">Meta Ads · Google Ads · GA4 · Facturacion — datos en vivo desde Supabase</div>
    </div>
    <div class="ke-pg-stat">
      <div class="ke-pg-stat-val num" id="kAcos">—</div>
      <div class="ke-pg-stat-lbl">ACOS del periodo</div>
    </div>
  </div>

  <div class="ke-alert" id="err" style="background:var(--ke-card);border:1px solid rgba(255,176,160,.18);border-left:3px solid var(--ke-bad);border-radius:0 10px 10px 0;padding:16px 20px;">
    <p style="font-size:13px;color:rgba(230,230,230,.7);line-height:1.6;">No se pudieron cargar los datos. Reintenta recargando la pagina.</p>
  </div>

  <div class="ke-grid-4">
    <div class="ke-kc"><div class="ke-kl">Inversion total</div><div class="ke-kv num" id="kInv">—</div><div class="ke-ks" id="kInvSub">Meta + Google</div></div>
    <div class="ke-kc g"><div class="ke-kl">Facturacion</div><div class="ke-kv g num" id="kVentas">—</div><div class="ke-ks" id="kVentasSub">Ordenes pagas</div></div>
    <div class="ke-kc o"><div class="ke-kl">ACOS</div><div class="ke-kv o num" id="kAcos2">—</div><div class="ke-ks">Inversion / Facturacion</div></div>
    <div class="ke-kc b"><div class="ke-kl">ROAS</div><div class="ke-kv b num" id="kRoas">—</div><div class="ke-ks">Facturacion / Inversion</div></div>
  </div>

  <div class="ke-block">
    <div class="ke-block-top"></div>
    <div class="ke-bh"><span class="ke-bt">Evolucion diaria · Inversion vs Facturacion</span><span class="ke-bt o" id="chartRange">—</span></div>
    <div class="chart-wrap"><canvas id="trend"></canvas></div>
  </div>

  <div class="ke-sec-head"><div class="ke-sec-line"></div><span class="ke-sec-label">Meta Ads</span><span class="ke-sec-pill" id="metaSpendPill">—</span></div>
  <div class="ke-grid-4">
    <div class="ke-kc"><div class="ke-kl">Inversion Meta</div><div class="ke-kv num" id="mSpend">—</div></div>
    <div class="ke-kc g"><div class="ke-kl">Valor compras</div><div class="ke-kv g num" id="mVal">—</div><div class="ke-ks" id="mPurch">—</div></div>
    <div class="ke-kc b"><div class="ke-kl">ROAS Meta</div><div class="ke-kv b num" id="mRoas">—</div></div>
    <div class="ke-kc o"><div class="ke-kl">CTR · CPM</div><div class="ke-kv o num" id="mCtr">—</div><div class="ke-ks" id="mCpm">—</div></div>
  </div>
  <div class="ke-block">
    <div class="ke-block-top"></div>
    <div class="ke-bh"><span class="ke-bt">Meta · por campana</span><span class="ke-bt muted" id="mCampCount">—</span></div>
    <div class="tbl-scroll"><table class="ke-t" id="tMeta">
      <thead><tr><th>Campana</th><th>Inversion</th><th>Impr.</th><th>Clicks</th><th>CTR</th><th>CPC</th><th class="acc">Compras</th><th class="acc">Valor</th><th class="acc">ROAS</th></tr></thead>
      <tbody></tbody><tfoot></tfoot>
    </table></div>
  </div>

  <div class="ke-sec-head"><div class="ke-sec-line b"></div><span class="ke-sec-label">Google Ads</span><span class="ke-sec-pill" id="gSpendPill">—</span></div>
  <div class="ke-grid-4">
    <div class="ke-kc"><div class="ke-kl">Inversion Google</div><div class="ke-kv num" id="gSpend">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Impresiones</div><div class="ke-kv w num" id="gImpr">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Clicks</div><div class="ke-kv w num" id="gClicks">—</div></div>
    <div class="ke-kc o"><div class="ke-kl">CTR · CPC</div><div class="ke-kv o num" id="gCtr">—</div><div class="ke-ks" id="gCpc">—</div></div>
  </div>
  <div class="ke-block">
    <div class="ke-block-top"></div>
    <div class="ke-bh"><span class="ke-bt">Google · por campana</span><span class="ke-bt muted" id="gCampCount">—</span></div>
    <div class="tbl-scroll"><table class="ke-t" id="tGoogle">
      <thead><tr><th>Campana</th><th>Inversion</th><th>Impr.</th><th>Clicks</th><th>CTR</th><th>CPC</th></tr></thead>
      <tbody></tbody><tfoot></tfoot>
    </table></div>
  </div>

  <div class="ke-sec-head"><div class="ke-sec-line g"></div><span class="ke-sec-label">Analytics GA4</span><span class="ke-sec-pill" id="gaSessPill">—</span></div>
  <div class="ke-grid-4">
    <div class="ke-kc"><div class="ke-kl">Sesiones</div><div class="ke-kv w num" id="gaSess">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Usuarios</div><div class="ke-kv w num" id="gaUsers">—</div></div>
    <div class="ke-kc g"><div class="ke-kl">Transacciones</div><div class="ke-kv g num" id="gaTx">—</div><div class="ke-ks" id="gaCvr">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Add to cart</div><div class="ke-kv w num" id="gaAtc">—</div></div>
  </div>
  <div class="ke-block">
    <div class="ke-block-top"></div>
    <div class="ke-bh"><span class="ke-bt">GA4 · por fuente / medio (top 12 por sesiones)</span></div>
    <div class="tbl-scroll"><table class="ke-t" id="tGa">
      <thead><tr><th>Fuente / Medio</th><th>Sesiones</th><th>Usuarios</th><th>Transac.</th><th class="acc">Ingresos</th></tr></thead>
      <tbody></tbody><tfoot></tfoot>
    </table></div>
  </div>

  <div class="ke-sec-head"><div class="ke-sec-line p"></div><span class="ke-sec-label">Facturacion</span><span class="ke-sec-pill" id="vPill">—</span></div>
  <div class="ke-grid-4">
    <div class="ke-kc g"><div class="ke-kl">Facturacion (pagas)</div><div class="ke-kv g num" id="vPaid">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Ordenes pagas</div><div class="ke-kv w num" id="vOrders">—</div></div>
    <div class="ke-kc o"><div class="ke-kl">Ticket promedio</div><div class="ke-kv o num" id="vAvg">—</div></div>
    <div class="ke-kc"><div class="ke-kl">Productos vendidos</div><div class="ke-kv w num" id="vProd">—</div></div>
  </div>
</div>

<div class="ke-footer">
  <img src="data:image/png;base64,__LOGO__" style="width:26px;height:26px;object-fit:contain;opacity:.7">
  <div id="footLbl">Piramide Home · Performance · Krab-e</div>
  <img src="data:image/png;base64,__CRAB__" style="width:30px;height:30px;object-fit:contain;opacity:.2">
</div>

<script>
const SUPA="__URL__", ANON="__ANON__";
const TABLES={
  meta:"piramidehome_meta_ads?select=date,campaign_name,amount_spent,impressions,clicks,reach,website_purchases,purchases_conv_value",
  google:"piramidehome_google_ads?select=date,campaign_name,cost,impressions,clicks",
  ga4:"piramidehome_ga4_sessions?select=date,source_medium,sessions,total_users,transactions,add_to_carts,total_revenue",
  ventas:"piramidehome_tiendanube_orders?select=date,order_payment_status,order_total_paid,order_total_products"
};
let DATA={meta:[],google:[],ga4:[],ventas:[]};
let RANGE={from:null,to:null};
let chart=null;

async function fetchTable(q){
  let out=[], from=0, step=1000;
  while(true){
    const res=await fetch(SUPA+"/"+q, {headers:{apikey:ANON, Authorization:"Bearer "+ANON, Range:from+"-"+(from+step-1), "Range-Unit":"items"}});
    if(!res.ok) throw new Error("fetch "+q+" "+res.status);
    const rows=await res.json();
    out=out.concat(rows);
    if(rows.length<step) break;
    from+=step;
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

function render(){
  document.getElementById("rangeLbl").textContent = RANGE.label||"";
  document.getElementById("chartRange").textContent = RANGE.from+" → "+RANGE.to;
  document.getElementById("footLbl").textContent = "Piramide Home · Performance · "+RANGE.from+" a "+RANGE.to+" · Krab-e";

  const meta=DATA.meta.filter(r=>inRange(r.date));
  const goog=DATA.google.filter(r=>inRange(r.date));
  const ga=DATA.ga4.filter(r=>inRange(r.date));
  const ven=DATA.ventas.filter(r=>inRange(r.date));

  const mSpend=sum(meta,r=>r.amount_spent), gSpend=sum(goog,r=>r.cost);
  const inv=mSpend+gSpend;
  const isPaid=r=>{ const s=(r.order_payment_status||"").toLowerCase(); return s==="paid"||s==="pagado"||s==="pagada"; };
  const venPaid=ven.filter(isPaid);
  const ventas=sum(venPaid,r=>r.order_total_paid);
  const orders=venPaid.length;
  const prod=sum(venPaid,r=>r.order_total_products);
  const acos = ventas>0 ? inv/ventas*100 : null;
  const roas = inv>0 ? ventas/inv : null;

  document.getElementById("kAcos").textContent=pct(acos);
  document.getElementById("kAcos2").textContent=pct(acos);
  document.getElementById("kInv").textContent=money(inv);
  document.getElementById("kInvSub").textContent="Meta "+money(mSpend)+" · Google "+money(gSpend);
  document.getElementById("kVentas").textContent=money(ventas);
  document.getElementById("kVentasSub").textContent=num(orders)+" ordenes pagas";
  document.getElementById("kRoas").textContent=xd(roas);

  const mImpr=sum(meta,r=>r.impressions), mClicks=sum(meta,r=>r.clicks);
  const mVal=sum(meta,r=>r.purchases_conv_value), mPurch=sum(meta,r=>r.website_purchases);
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

  const sess=sum(ga,r=>r.sessions), users=sum(ga,r=>r.total_users), tx=sum(ga,r=>r.transactions), atc=sum(ga,r=>r.add_to_carts);
  document.getElementById("gaSess").textContent=num(sess);
  document.getElementById("gaUsers").textContent=num(users);
  document.getElementById("gaTx").textContent=num(tx);
  document.getElementById("gaCvr").textContent="CVR "+pct(sess>0?tx/sess*100:null);
  document.getElementById("gaAtc").textContent=num(atc);
  document.getElementById("gaSessPill").textContent=num(sess)+" sesiones";
  buildGa(ga);

  document.getElementById("vPaid").textContent=money(ventas);
  document.getElementById("vOrders").textContent=num(orders);
  document.getElementById("vAvg").textContent=money(orders>0?ventas/orders:0);
  document.getElementById("vProd").textContent=num(prod);
  document.getElementById("vPill").textContent=money(ventas);

  buildChart(meta,goog,venPaid);
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
    const ctr=r.impressions>0?r.clicks/r.impressions*100:null;
    const cpc=r.clicks>0?r.amount_spent/r.clicks:null;
    const roas=r.amount_spent>0?r.purchases_conv_value/r.amount_spent:null;
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
  let d=aggBy(rows,"source_medium",["sessions","total_users","transactions","total_revenue"]);
  d.sort((a,b)=>b.sessions-a.sessions);
  const top=d.slice(0,12);
  const tb=document.querySelector("#tGa tbody"); tb.innerHTML="";
  for(const r of top){
    tb.insertAdjacentHTML("beforeend","<tr><td>"+esc(r.name)+"</td><td>"+num(r.sessions)+"</td><td>"+num(r.total_users)+"</td><td>"+num(r.transactions)+"</td><td class='o'>"+money(r.total_revenue)+"</td></tr>");
  }
  const tS=sum(d,r=>r.sessions),tU=sum(d,r=>r.total_users),tT=sum(d,r=>r.transactions),tR=sum(d,r=>r.total_revenue);
  document.querySelector("#tGa tfoot").innerHTML="<tr><td>Total ("+d.length+")</td><td>"+num(tS)+"</td><td>"+num(tU)+"</td><td>"+num(tT)+"</td><td>"+money(tR)+"</td></tr>";
}

function buildChart(meta,goog,venPaid){
  const days={};
  const add=(d,k,v)=>{ const day=iso(parseISO(d)); if(!days[day]) days[day]={inv:0,ven:0}; days[day][k]+=(+v||0); };
  meta.forEach(r=>add(r.date,"inv",r.amount_spent));
  goog.forEach(r=>add(r.date,"inv",r.cost));
  venPaid.forEach(r=>add(r.date,"ven",r.order_total_paid));
  const labels=Object.keys(days).sort();
  const inv=labels.map(d=>Math.round(days[d].inv));
  const ven=labels.map(d=>Math.round(days[d].ven));
  const lab=labels.map(fmtShort);
  if(chart) chart.destroy();
  const ctx=document.getElementById("trend");
  chart=new Chart(ctx,{ type:"bar",
    data:{ labels:lab, datasets:[
      {label:"Facturacion", data:ven, backgroundColor:"rgba(77,204,128,.55)", borderColor:"#4dcc80", borderWidth:1, borderRadius:3, order:2},
      {label:"Inversion", type:"line", data:inv, borderColor:"#ff700a", backgroundColor:"rgba(255,112,10,.12)", borderWidth:2, tension:.3, pointRadius:0, fill:true, order:1}
    ]},
    options:{ responsive:true, maintainAspectRatio:false,
      plugins:{ legend:{ labels:{ color:"#e6e6e6", font:{family:"General Sans",size:11}, usePointStyle:true, boxWidth:8 } },
        tooltip:{ callbacks:{ label:c=>c.dataset.label+": $"+nf0.format(c.parsed.y) } } },
      scales:{ x:{ ticks:{ color:"rgba(230,230,230,.38)", font:{family:"Satoshi",size:10}, maxRotation:0, autoSkip:true, maxTicksLimit:14 }, grid:{ color:"rgba(255,255,255,.04)" } },
        y:{ ticks:{ color:"rgba(230,230,230,.38)", font:{family:"Satoshi",size:10}, callback:v=>"$"+nf0.format(v) }, grid:{ color:"rgba(255,255,255,.04)" } } } }
  });
}

function esc(s){ return String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }

function setPreset(p){
  const today=new Date(); today.setHours(0,0,0,0);
  let from,to=new Date(today), label;
  if(p==="mtd"){ from=new Date(today.getFullYear(),today.getMonth(),1); label=from.toLocaleDateString("es-AR",{month:"long",year:"numeric"}).toUpperCase(); }
  else if(p==="all"){ from=new Date(2000,0,1); label="HISTORICO"; }
  else { const n=+p; from=new Date(today); from.setDate(from.getDate()-(n-1)); label="ULTIMOS "+n+"D"; }
  RANGE={from:iso(from),to:iso(to),label:label};
  document.getElementById("from").value=RANGE.from;
  document.getElementById("to").value=RANGE.to;
  document.querySelectorAll(".ke-preset").forEach(e=>e.classList.toggle("active",e.dataset.p===p));
  render();
}
document.querySelectorAll(".ke-preset").forEach(e=>e.addEventListener("click",()=>setPreset(e.dataset.p)));
function onInput(){
  RANGE.from=document.getElementById("from").value;
  RANGE.to=document.getElementById("to").value;
  RANGE.label="PERSONALIZADO";
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
  }catch(e){
    document.getElementById("loading").style.display="none";
    document.getElementById("err").style.display="block";
    console.error(e);
  }
}
init();
</script>
</body>
</html>
"""

out = (HTML
       .replace("__FONT__", FONT)
       .replace("__LOGO__", LOGO)
       .replace("__CRAB__", CRAB)
       .replace("__URL__", SUPA_URL)
       .replace("__ANON__", ANON))

path = "/sessions/vibrant-focused-wozniak/mnt/outputs/index.html"
with open(path, "w", encoding="utf-8") as f:
    f.write(out)
print("WROTE", path, len(out), "bytes")
