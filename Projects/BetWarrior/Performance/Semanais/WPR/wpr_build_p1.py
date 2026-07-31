#!/usr/bin/env python3
# Gerador do slide P1 do WPR. Mantem o layout do deck aprovado (wpr-jun-01-10-slide.html),
# so troca os dados. SVGs calculados (nunca desenhar a mao). Uso: python3 wpr_build_p1.py
import io

# ===================== DADOS (Jun 01-30, fechamento do mês, base Registros=1o step) =====================
PERIODO="01–30 / Jun 2026"; GERADO="02/07"
HEADLINE=("Copa entregou aquisição, não receita. FTD +6% e apostadores ativos +23% vs Mai, mas o mês fechou em 46% da meta de FTD (curva Copa agressiva) e com a receita no chão: GGR −78% e NGR no zero (−R$4k). "
          "O driver é estrutural, não o evento: hold de Sports negativo (Tennis ITF + eFootball + high-rollers), com ticket e valor por apostador em queda.")
# tabela: 3 meses de calendário cheio
ROWS=[  # mes, janela, registros(1o step), ftd, cr%, ggr_k, ngr_k, marg%, sb%, cs%, depmed, star
 ("Abr","01–30",22366,4369,19.5,247,217,3.4,3.4,3.4,145,True),
 ("Mai","01–31",20165,3200,15.9,246,211,3.3,2.7,3.8,139,False),
 ("Jun","01–30",23045,3385,14.7,54,-4,0.9,-2.2,1.8,108,False),
]
DELTA=dict(reg="+14,3%",ftd="+5,8%",cr="−1,2pp",ggr="−78,0%",ngr="−101,9%",marg="−2,4pp",sb="−4,9pp",cs="−2,0pp")
META=dict(reg=51458,ftd=7343,cr=14.3,ggr=438,ngr=386,marg=4.8,sb=6.0,cs=4.0)
VSMETA=dict(reg="45%",ftd="46%",cr="+0,4pp",ggr="12%",ngr="−1%",marg="−3,9pp",sb="−8,2pp",cs="−2,2pp")
# FTD vs Meta (real, meta_janela=mês cheio, ating%, meta_mes_cheia)
FTDMETA=[("Abr",4369,4369,100,4369,False),("Mai",3200,3216,100,3216,False),("Jun",3385,7343,46,7343,True)]
DEPMED=[("Abr",145,False),("Mai",139,False),("Jun",108,True)]
# funil
FUNIL=[("SESSÕES","GA4","417.146"),("REGISTROS","onboarding","23.045"),("PRONTO P/ DEP","KYC PASS","5.880"),("FTD","PowerBI","3.385")]
CONV=[("5,53%","+1,8pp vs Mai","#22C55E"),("25,5%","−2,3pp vs Mai","#EF4444"),("57,6%","+0,6pp vs Mai","#22C55E")]
CARDS=[("GB Total","R$6,00M","−18,7% vs R$7,38M Mai","#EF4444"),
       ("Apostadores Ativos","6.090","+23,3% vs 4.939 Mai","#22C55E"),
       ("Gross Bets / Apostador","R$985","−34,0% vs R$1.493 Mai","#EF4444"),
       ("GB · Novos FTDs","R$3,39M","−7,1% vs R$3,65M Mai","#EF4444"),
       ("GB · Base Existente","R$2,60M","−30,1% vs R$3,72M Mai","#EF4444")]
INCIDENTE="Mês inclui o incidente de CRM de 01/06 (~2.578 registros sem tag, ~0 FTD): infla registros e deprime o CR do topo. Sem ele, o CR fica ~17%."

def br(n):  # 1234 -> 1.234
    return format(int(round(n)),",.0f").replace(",",".")

# ===================== SVG: FTD vs META =====================
def svg_ftdmeta():
    BASE=314.0; MAXH=250.0
    mx=max(max(r,m) for _,r,m,_,_,_ in FTDMETA)
    sc=MAXH/mx
    centers={"Abr":176.7,"Mai":450.0,"Jun":723.3}
    s=[f'<line x1="20" y1="{BASE}" x2="880" y2="{BASE}" stroke="#E0E0E0" stroke-width="1"/>']
    for mes,real,meta,ating,mescheia,cur in FTDMETA:
        c=centers[mes]; rx=c-54; mx2=c+4
        rh=real*sc; mh=meta*sc; ry=BASE-rh; my=BASE-mh
        col= "#22C55E" if ating>=100 else ("#F59E0B" if ating>=90 else "#EF4444")
        s.append(f'<rect x="{rx:.1f}" y="{ry:.1f}" width="50" height="{rh:.1f}" fill="#FF3900" rx="2"/>')
        s.append(f'<rect x="{mx2:.1f}" y="{my:.1f}" width="50" height="{mh:.1f}" fill="#C8C8C8" rx="2"/>')
        s.append(f'<text x="{rx+25:.1f}" y="{ry-7:.1f}" text-anchor="middle" font-family="Archivo Black,sans-serif" font-size="13" fill="#FF3900">{br(real)}</text>')
        s.append(f'<text x="{mx2+25:.1f}" y="{my-7:.1f}" text-anchor="middle" font-family="Archivo,sans-serif" font-size="13" fill="#999999" font-weight="700">{br(meta)}</text>')
        s.append(f'<text x="{c:.1f}" y="34" text-anchor="middle" font-family="Archivo Black,sans-serif" font-size="23" fill="{col}">{ating}%</text>')
        lab=f'{mes} ▶' if cur else mes
        lc="#FF3900" if cur else "#888888"
        s.append(f'<text x="{c:.1f}" y="343" text-anchor="middle" font-family="Archivo,sans-serif" font-size="15" fill="{lc}" font-weight="700">{lab}</text>')
        s.append(f'<text x="{c:.1f}" y="358" text-anchor="middle" font-family="Archivo,sans-serif" font-size="11" fill="#AAAAAA">{br(mescheia)}</text>')
    return '<svg viewBox="0 0 900 360" preserveAspectRatio="xMidYMid meet">'+''.join(s)+'</svg>'

# ===================== SVG: DEP MEDIO =====================
def svg_depmed():
    BASE=318.0; MAXH=272.0
    mx=max(v for _,v,_ in DEPMED); sc=MAXH/mx
    centers={"Abr":176.7,"Mai":450.0,"Jun":723.3}
    s=[f'<line x1="20" y1="{BASE}" x2="880" y2="{BASE}" stroke="#E0E0E0" stroke-width="1"/>']
    for mes,v,cur in DEPMED:
        c=centers[mes]; x=c-42; h=v*sc; y=BASE-h
        col="#FF3900" if cur else "#C8C8C8"; tc="#FF3900" if cur else "#999999"
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="84" height="{h:.1f}" fill="{col}" rx="2"/>')
        s.append(f'<text x="{c:.1f}" y="{y-9:.1f}" text-anchor="middle" font-family="Archivo Black,sans-serif" font-size="17" fill="{tc}">R${v}</text>')
        lab=f'{mes} ▶' if cur else mes; lc="#FF3900" if cur else "#888888"
        s.append(f'<text x="{c:.1f}" y="346" text-anchor="middle" font-family="Archivo,sans-serif" font-size="15" fill="{lc}" font-weight="700">{lab}</text>')
    return '<svg viewBox="0 0 900 360" preserveAspectRatio="xMidYMid meet">'+''.join(s)+'</svg>'

# ===================== FUNIL (poligonos fixos) =====================
def svg_funil():
    nums=[f[2] for f in FUNIL]; xs=[54,162,270,378]
    poly=('<polygon points="0,0   108,25  108,95  0,120"  fill="#FF7A50"/>'
          '<polygon points="108,25 216,42  216,78  108,95" fill="#FF3900"/>'
          '<polygon points="216,42 324,50  324,70  216,78" fill="#CC2E00"/>'
          '<polygon points="324,50 432,55  432,65  324,70" fill="#8B1500"/>'
          '<line x1="108" y1="25" x2="108" y2="95" stroke="white" stroke-width="1.5" opacity="0.35"/>'
          '<line x1="216" y1="42" x2="216" y2="78" stroke="white" stroke-width="1.5" opacity="0.35"/>'
          '<line x1="324" y1="50" x2="324" y2="70" stroke="white" stroke-width="1.5" opacity="0.35"/>')
    t=''.join(f'<text x="{xs[i]}" y="60" dominant-baseline="middle" text-anchor="middle" fill="white" font-family="\'Archivo Black\',sans-serif" font-size="13">{nums[i]}</text>' for i in range(4))
    return '<svg viewBox="0 0 432 120" preserveAspectRatio="none">'+poly+t+'</svg>'

# ===================== HTML =====================
CSS=open("wpr-jun-01-10-slide.html").read().split("<style>")[1].split("</style>")[0]

def tcls(s):
    s=str(s).strip()
    if s.startswith("+"): return "hi-g"
    if s.startswith("−") or s.startswith("-"): return "n"
    try:
        n=float(s.replace("%","").replace("pp","").replace(".","").replace(",","."))
        if "pp" in s and abs(n)<0.05: return ""
        return "hi-g" if n>=100 else "n"
    except: return ""

def table_rows():
    K=["reg","ftd","cr","ggr","ngr","marg","sb","cs"]
    out=[]
    for mes,jan,reg,ftd,cr,ggr,ngr,marg,sb,cs,dep,star in ROWS:
        nm=f'{mes} ★' if star else (f'{mes} ▶' if mes=="Jun" else mes)
        rcls=' class="cw"' if mes=="Jun" else ''
        out.append(f'<tr{rcls}><td>{nm}</td><td>{br(reg)}</td><td>{br(ftd)}</td><td>{cr:.1f}%</td>'
                   f'<td>{ggr}k</td><td>{ngr}k</td><td>{marg:.1f}%</td><td>{sb:.1f}%</td><td>{cs:.1f}%</td></tr>')
    d=DELTA
    out.append('<tr class="dr"><td class="mu">Δ vs Mai</td>'+''.join(f'<td class="{tcls(d[k])}">{d[k]}</td>' for k in K)+'</tr>')
    M=META
    out.append(f'<tr class="mt"><td>Meta</td><td>{br(M["reg"])}</td><td>{br(M["ftd"])}</td><td>{M["cr"]:.1f}%</td>'
               f'<td>{M["ggr"]}k</td><td>{M["ngr"]}k</td><td>{M["marg"]:.1f}%</td><td>{M["sb"]:.1f}%</td><td>{M["cs"]:.1f}%</td></tr>')
    v=VSMETA
    out.append('<tr class="dr"><td class="mu">vs Meta</td>'+''.join(f'<td class="{tcls(v[k])}">{v[k]}</td>' for k in K)+'</tr>')
    return ''.join(out)

def cards():
    out=[]
    for lbl,num,delta,col in CARDS:
        out.append(f'<div style="flex:1;background:#F8F8F8;border:1px solid #EFEFEF;border-radius:3px;padding:8px 10px;text-align:center;">'
          f'<div style="font-size:10px;color:#AAAAAA;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:3px;">{lbl}</div>'
          f'<div style="font-family:\'Archivo Black\',sans-serif;font-size:26px;color:{col};">{num}</div>'
          f'<div style="font-size:12px;font-weight:600;color:{col};margin-top:2px;">{delta}</div></div>')
    return ''.join(out)

fn_names=''.join(f'<div class="fn-name"><span class="fn-stage">{n}</span><span class="fn-src">{s}</span></div>' for n,s,_ in FUNIL)
convs=''.join(f'<div class="fn-conv" style="left:{p}%"><div class="fn-c-pct">{pct}</div><div class="fn-c-wow" style="color:{col};">{wow}</div></div>'
              for p,(pct,wow,col) in zip([25,50,75],CONV))

HTML=f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WPR Brasil · P1 Métricas de Negócio · Jun 01–30/2026</title>
<style>{CSS}</style>
</head>
<body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">WEEKLY PERFORMANCE REPORT</div>
    <div class="hdr-sub"><strong>{HEADLINE}</strong></div></div>
  <div class="hdr-meta">{PERIODO}<br>SB + Casino · BRL<br>Gerado {GERADO}</div>
</div>
<div class="body">
  <div class="row row-top">
    <div class="panel p-half">
      <div class="ph"><svg width="13" height="13" viewBox="0 0 13 13"><rect x="0" y="3" width="3" height="10" rx="1" fill="#FF3900"/><rect x="5" y="3" width="3" height="10" rx="1" fill="#C8C8C8"/><rect x="10" y="3" width="3" height="10" rx="1" fill="#FF3900"/></svg>
        <span class="ph-title">FTD vs Meta · Jun 01–30</span>
        <span class="ph-note">Realizado vs meta (curva Copa, não linear) · fonte: Forecast</span></div>
      <div class="p-body"><div class="trend-svg">{svg_ftdmeta()}</div>
        <div class="chart-legend">
          <div class="cl"><div class="cl-dot" style="background:#FF3900;"></div>Realizado</div>
          <div class="cl"><div class="cl-dot" style="background:#C8C8C8;"></div>Meta janela</div>
          <div class="cl" style="margin-left:auto;color:#AAA;">Jun: 46% da meta de FTD · meta do mês 7.343 (curva Copa)</div></div></div>
    </div>
    <div class="panel p-half">
      <div class="ph"><svg width="13" height="13" viewBox="0 0 13 13"><circle cx="6.5" cy="6.5" r="5.5" stroke="#FF3900" stroke-width="1.5" fill="none"/><line x1="6.5" y1="3.5" x2="6.5" y2="6.5" stroke="#FF3900" stroke-width="1.5" stroke-linecap="round"/><circle cx="6.5" cy="9" r="1" fill="#FF3900"/></svg>
        <span class="ph-title">Depósito Médio por FTD · Jun 01–30</span>
        <span class="ph-note">Valor do 1º depósito · FactFirstDeposit · External</span></div>
      <div class="p-body"><div class="trend-svg">{svg_depmed()}</div>
        <div class="chart-legend">
          <div class="cl"><div class="cl-dot" style="background:#FF3900;"></div>Período atual (Jun)</div>
          <div class="cl"><div class="cl-dot" style="background:#C8C8C8;"></div>Meses anteriores</div>
          <div class="cl" style="margin-left:auto;color:#AAA;">Ticket do 1º depósito em queda: R$145 → R$108</div></div></div>
    </div>
  </div>
  <div class="row row-bot">
    <div class="panel p-hi">
      <div class="ph"><svg width="13" height="13" viewBox="0 0 13 13"><polygon points="1,1 12,1 9,5.5 9,12 4,12 4,5.5" fill="#FF3900"/></svg>
        <span class="ph-title">Funil de Ativação</span>
        <span class="ph-note">GA4 + PowerBI · Jun 01–30 · Δ vs Mai 01–31</span></div>
      <div class="p-body" style="padding-top:10px;padding-bottom:8px;">
        <div class="fn-wrap">
          <div class="fn-names">{fn_names}</div>
          <div class="fn-svg-wrap">{svg_funil()}</div>
          <div class="fn-convs">{convs}</div>
          <div class="fn-note">Sessões: GA4 BR · Registros: 1º step onboarding (PENDING_CONFIRMATION) · Pronto p/Dep: KYC READY_FOR_DEPOSIT · FTD: PowerBI</div>
        </div></div>
    </div>
    <div class="panel p-wide">
      <div class="ph"><svg width="13" height="13" viewBox="0 0 13 13"><rect x="0" y="0" width="13" height="3" rx="1" fill="#FF3900"/><rect x="0" y="5" width="13" height="3" rx="1" fill="#FF3900" opacity=".5"/><rect x="0" y="10" width="13" height="3" rx="1" fill="#FF3900" opacity=".25"/></svg>
        <span class="ph-title">Métricas de Negócio · Jun 01–30</span>
        <span class="ph-note">SB + Casino · BRL · meses de calendário cheios</span></div>
      <div class="p-body">
        <table><thead><tr><th>Mês</th><th>Registros</th><th>FTDs</th><th>CR%</th>
          <th class="th-hi">GGR (R$)</th><th class="th-hi">NGR (R$)</th><th class="th-hi">Marg.</th><th>SB</th><th>CS</th></tr></thead>
          <tbody>{table_rows()}</tbody></table>
        <div class="tnote">★ Pico Abr (NFA) · ▶ Período atual · Registros = 1º step do onboarding · Δ vs Mai = variação MoM · vs Meta = atingimento (absolutos em %, taxas em p.p.) · meta pela curva da Copa · CR alvo 14,3% (YTD 2026) · GGR/NGR em R$k<br>{INCIDENTE}</div>
        <div style="margin-top:20px;padding-top:12px;border-top:1px solid #F0F0F0;flex-shrink:0;">
          <div style="font-family:'Archivo Black',sans-serif;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#AAAAAA;margin-bottom:8px;">Base Ativa · mais apostadores, menos por apostador</div>
          <div style="display:flex;gap:10px;">{cards()}</div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>WPR · PÁG. 1 · MÉTRICAS DE NEGÓCIO · JUN 01–30/2026</span><span>02/07/2026</span></div>
</body></html>'''

open("wpr-jun-01-30-slide.html","w").write(HTML)
print("OK -> wpr-jun-01-30-slide.html  (%d bytes)"%len(HTML))
