#!/usr/bin/env python3
# Gerador do P3 (Performance de Midia). REFEITO 26/06: CPA = GA x 1.33 (FTDs do GA corrigidos pelo fator do Juanca),
#   alinhado a Perfo. % verba do PACING (Diego). FTDs e CPA da aba CPL (1Rc_ckov). Cambio USD->BRL=5,0.
#   (O CPA BI/PowerBI daria mais baixo ~US$105 por atribuir mais FTD ao paid (first-click), mas ficaria rosado; usamos GA x1.33.)
FX=5.0; GERADO="02/07"; PERIODO="Jun 2026 · fechado 01–30"
REF=100  # pace ideal (mês fechado)
HEADLINE=("No fechamento da Copa o paid gastou quase toda a verba (99%) mas entregou só 51% da meta de FTD. Google foi o mais "
          "eficiente (77% da meta, menor CPA R$558) e ainda subexecutou (91%); Meta (52%) e TikTok (25%) estouraram a verba (114%/122%) sem entregar. X sem retorno. CPA na base GA×1,33.")
# nome, %budget, %FTD, CPA_BRL, invest_USD_k, atribuicao_ok
PLAT=[("Google",91,77,558,149,True),
      ("Meta",114,52,818,136,True),
      ("TikTok",122,25,1090,30,True),
      ("X",49,0,0,11,False)]
TOTAL=("TOTAL",99,51,735,340)
CSS=open("wpr-jun-01-10-slide.html").read().split("<style>")[1].split("</style>")[0]
EXTRA='''
.p3wrap{display:flex;flex-direction:column;flex:1;min-height:0;gap:0;}
.p3head{display:flex;font-size:11px;color:#AAA;text-transform:uppercase;letter-spacing:1px;padding:0 0 8px;border-bottom:2px solid #FF3900;}
.p3head .c1{width:120px;} .p3head .c2{flex:1;} .p3head .c3{flex:1;} .p3head .c4{width:130px;text-align:right;} .p3head .c5{width:150px;text-align:right;}
.p3row{display:flex;align-items:center;padding:14px 0;border-bottom:1px solid #F2F2F2;}
.p3row.tot{border-top:2px solid #E0E0E0;border-bottom:none;background:#FFF7F4;}
.p3-name{width:120px;font-family:'Archivo Black',sans-serif;font-size:16px;color:#111;}
.p3-name span{display:block;font-size:10px;font-family:'Archivo',sans-serif;color:#AAA;font-weight:400;}
.p3-barcol{flex:1;padding-right:24px;}
.p3-track{position:relative;height:26px;background:#F2F2F2;border-radius:3px;overflow:visible;}
.p3-fill{height:100%;border-radius:3px;display:flex;align-items:center;justify-content:flex-end;padding-right:8px;color:#fff;font-family:'Archivo Black',sans-serif;font-size:12px;}
.p3-ref{position:absolute;top:-3px;bottom:-3px;width:2px;background:#111;}
.p3-reflbl{position:absolute;top:-15px;font-size:9px;color:#111;transform:translateX(-50%);white-space:nowrap;}
.p3-cpa{width:130px;text-align:right;font-family:'Archivo Black',sans-serif;font-size:18px;color:#111;}
.p3-inv{width:150px;text-align:right;font-size:14px;color:#888;}
.dash{background:repeating-linear-gradient(45deg,#C8C8C8,#C8C8C8 5px,#E5E5E5 5px,#E5E5E5 10px)!important;color:#777!important;}
'''
def row(name,bud,ftd,cpa,inv,ok,tot=False):
    budw=min(bud,100); ftdsc=130.0
    ftdw=min(ftd/ftdsc*100,100); refb=REF; reff=100/ftdsc*100
    ftdcls="p3-fill dash" if not ok else "p3-fill"
    dag="†" if not ok else ""
    cls="p3row tot" if tot else "p3row"
    nm=f'{name}<span>{("sem atribuição" if not ok else "")}</span>' if not tot else f'{name}'
    cpahtml=("s/ FTD" if cpa==0 else "R$"+format(cpa,",d").replace(",","."))
    return (f'<div class="{cls}"><div class="p3-name">{nm}</div>'
            f'<div class="p3-barcol"><div class="p3-track"><div class="p3-fill" style="width:{budw}%;background:#C8C8C8;">{bud}%</div>'
            f'<div class="p3-ref" style="left:{refb}%;"></div></div></div>'
            f'<div class="p3-barcol"><div class="p3-track"><div class="{ftdcls}" style="width:{ftdw:.0f}%;background:#FF3900;">{ftd}%{dag}</div>'
            f'<div class="p3-ref" style="left:{reff:.0f}%;"></div></div></div>'
            f'<div class="p3-cpa">{cpahtml}</div>'
            +f'<div class="p3-inv">US${inv}k</div></div>')
rows=''.join(row(*p) for p in PLAT)+row(*TOTAL,True,tot=True)
HTML=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>WPR Brasil · P3 Performance de Mídia · Jun 2026</title>
<style>{CSS}{EXTRA}</style></head><body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">PERFORMANCE DE MÍDIA</div>
    <div class="hdr-sub"><strong>{HEADLINE}</strong></div></div>
  <div class="hdr-meta">{PERIODO}<br>PACING-PERFO · câmbio R${str(FX).replace('.',',')}<br>Gerado {GERADO}</div>
</div>
<div class="body">
  <div class="panel" style="flex:1;">
    <div class="ph"><svg width="13" height="13" viewBox="0 0 13 13"><rect x="0" y="6" width="3" height="7" rx="1" fill="#C8C8C8"/><rect x="5" y="2" width="3" height="11" rx="1" fill="#FF3900"/><rect x="10" y="8" width="3" height="5" rx="1" fill="#111"/></svg>
      <span class="ph-title">Budget vs FTDs · CPA por Plataforma</span>
      <span class="ph-note">PACING-PERFO (Diego) + CPA GA×1,33 (Perfo/GA) · fechado 01–30 · pace ideal {REF}% (linha preta) · X sem atribuição (†)</span></div>
    <div class="p-body">
      <div class="p3wrap">
        <div class="p3head"><div class="c1">Plataforma</div><div class="c2">Budget executado · vs pace {REF}%</div>
          <div class="c3">FTDs realizados · vs meta 100%</div><div class="c4">CPA (R$)</div><div class="c5">Investido (US$)</div></div>
        {rows}
        <div style="margin-top:auto;padding-top:14px;font-size:12px;color:#888;line-height:1.6;border-top:1px solid #F0F0F0;">
          Google é o <b>mais eficiente</b> (77% da meta de FTD, <b>menor CPA R$558</b>) mas subexecutou (<b>91%</b> da verba). Meta e TikTok <b>estouraram a verba (114% / 122%)</b> e ainda ficaram longe da meta (52% / 25%), com CPA alto (R$818 / R$1.090). X praticamente <b>sem retorno</b> (sem atribuição). No total, o paid gastou 99% da verba e entregou só <b>51%</b> da meta de FTD. CPA na base <b>GA×1,33</b> (FTDs do GA corrigidos pelo fator, alinhado à Perfo). Câmbio R${str(FX).replace('.',',')}.
        </div>
      </div>
    </div>
  </div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>WPR · PÁG. 3 · PERFORMANCE DE MÍDIA · JUN 2026</span><span>{GERADO}/2026</span></div>
</body></html>'''
open("wpr-jun-01-30-slide-p3.html","w").write(HTML)
print("OK -> wpr-jun-01-30-slide-p3.html (%d bytes)"%len(HTML))
