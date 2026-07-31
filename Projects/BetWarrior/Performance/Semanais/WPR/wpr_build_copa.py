#!/usr/bin/env python3
# Slide "Copa: Demanda vs Captura". 3 atos: a onda chegou / a midia respondeu (search e o buraco) / gargalo no onboarding.
PERIODO="Copa 11–17 vs Pré-Copa 02–10 / Jun 2026"; GERADO="19/06"
HEADLINE=("A Copa trouxe a maior onda de intenção do ano e o Paid Social respondeu (3x, com criativos novos de Copa). "
          "O que nos custa a onda: o Paid Search sem trazer uma sessão de Copa no pico de busca, e um onboarding com fricção pesada onde só 17% "
          "de quem inicia o cadastro chega ao depósito.")
# funil onboarding (Copa 11-17)
FNL=[("Pending Confirmation",3943,None,"início do cadastro"),
     ("No Lock",2071,"−47%","onboarding / compliance"),
     ("Ready for Deposit",1073,"−48%","dados bancários"),
     ("FTD",683,"−36%","primeiro depósito")]
def br(n): return format(int(round(n)),",.0f").replace(",",".")
CSS=open("wpr-jun-01-10-slide.html").read().split("<style>")[1].split("</style>")[0]
EXTRA='''
.band{display:flex;flex-direction:column;gap:7px;min-height:0;}
.b1{flex:0.95;} .b2{flex:1.05;} .b3{flex:1.25;}
.band-hd{display:flex;align-items:center;gap:10px;flex-shrink:0;}
.band-tag{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:2px;text-transform:uppercase;padding:3px 11px;border-radius:3px;color:#fff;}
.band-sub{font-size:11.5px;color:#999;}
.cards{display:flex;gap:10px;flex:1;min-height:0;}
.card{flex:1;background:#FFF;border:1px solid #E0E0E0;border-radius:4px;padding:14px 16px;display:flex;flex-direction:column;justify-content:center;gap:5px;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.card .l{font-size:11px;color:#AAA;text-transform:uppercase;letter-spacing:1px;}
.card .v{font-family:'Archivo Black',sans-serif;font-size:42px;line-height:1;}
.card .d{font-size:13px;font-weight:700;}
.card .n{font-size:12px;color:#888;line-height:1.4;}
.kw{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px;}
.kw span{font-size:10.5px;padding:2px 8px;border-radius:10px;background:#F2F2F2;color:#777;}
.kw .copa{background:#FDECEC;color:#EF4444;font-weight:700;border:1px dashed #EF4444;}
/* funil onboarding */
.fnl{flex:1;display:flex;flex-direction:column;justify-content:center;gap:3px;padding:4px 0;}
.fnl-row{display:flex;align-items:center;gap:14px;}
.fnl-name{width:200px;text-align:right;flex-shrink:0;}
.fnl-name b{font-size:13.5px;color:#222;} .fnl-name span{display:block;font-size:10.5px;color:#AAA;}
.fnl-track{flex:1;height:38px;background:#F4F4F4;border-radius:3px;overflow:hidden;}
.fnl-fill{height:100%;background:#FF3900;border-radius:3px;display:flex;align-items:center;justify-content:flex-end;padding-right:12px;color:#fff;font-family:'Archivo Black',sans-serif;font-size:16px;}
.fnl-gap{margin-left:214px;font-size:12px;font-weight:700;color:#EF4444;padding:1px 0;}
.fnl-side{width:230px;flex-shrink:0;display:flex;flex-direction:column;justify-content:center;align-items:center;border-left:1px solid #EEE;padding-left:18px;}
.fnl-side .big{font-family:'Archivo Black',sans-serif;font-size:60px;color:#EF4444;line-height:1;}
.fnl-side .lbl{font-size:12px;color:#555;text-align:center;margin-top:6px;line-height:1.4;}
'''
def card(label,val,vcolor,delta,dcolor,note):
    return (f'<div class="card"><div class="l">{label}</div>'
            f'<div class="v" style="color:{vcolor};">{val}</div>'
            f'<div class="d" style="color:{dcolor};">{delta}</div>'
            f'<div class="n">{note}</div></div>')
onda=(card("Busca de aposta · Google Trends","+10x","#FF3900","“odd” picou 100 · “aposta copa” +8x","#FF3900","Pico no Jun 11-13, início da Copa e jogo do Brasil")
    +card("Tráfego ao site","+29%","#FF3900","13.252 → 17.136 sessões/dia","#FF3900","Onda real de visitas nos dias de Copa")
    +card("Engajamento esportivo da base","+13%","#22C55E","apostadores esportivos · handle +6%","#22C55E","A base existente abraçou a Copa"))
mx=FNL[0][1]
fnl_rows=[]
for name,v,gap,desc in FNL:
    if gap: fnl_rows.append(f'<div class="fnl-gap">↓ {gap} · {desc}</div>')
    w=v/mx*100
    fnl_rows.append(f'<div class="fnl-row"><div class="fnl-name"><b>{name}</b><span>{desc if not gap else ""}</span></div>'
                    f'<div class="fnl-track"><div class="fnl-fill" style="width:{w:.0f}%;">{br(v)}</div></div></div>')
funil=('<div style="display:flex;flex:1;gap:8px;min-height:0;">'
       '<div class="fnl">'+''.join(fnl_rows)+'</div>'
       '<div class="fnl-side"><div class="big">17%</div><div class="lbl">de quem inicia o cadastro chega ao depósito. Dois portões derrubam ~metade cada.</div></div>'
       '</div>')
HTML=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>WPR Brasil · Copa: Demanda vs Captura</title>
<style>{CSS}{EXTRA}</style></head><body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">COPA: DEMANDA vs CAPTURA</div>
    <div class="hdr-sub"><strong>{HEADLINE}</strong></div></div>
  <div class="hdr-meta">{PERIODO}<br>GA4 · PowerBI · Google Trends<br>Gerado {GERADO}</div>
</div>
<div class="body">
  <div class="band b1">
    <div class="band-hd"><span class="band-tag" style="background:#FF3900;">1 · A onda chegou</span>
      <span class="band-sub">a demanda de Copa explodiu, fora e dentro do site</span></div>
    <div class="cards">{onda}</div>
  </div>
  <div class="band b2">
    <div class="band-hd"><span class="band-tag" style="background:#22C55E;">2 · A mídia respondeu, com um buraco</span>
      <span class="band-sub">Paid Social surfou a onda; Paid Search ficou de fora</span></div>
    <div class="cards">
      <div class="card"><div class="l">Paid Social · respondeu à Copa</div>
        <div class="v" style="color:#FF3900;">3x</div>
        <div class="d" style="color:#22C55E;">2.006 → 6.387 sessões/dia (+218% vs Mai)</div>
        <div class="n">Criativos novos de Copa puxaram ~72% do aumento de tráfego. O canal está fazendo o trabalho.</div></div>
      <div class="card"><div class="l">Paid Search · o buraco</div>
        <div class="v" style="color:#EF4444;">+6%</div>
        <div class="d" style="color:#EF4444;">942 → 1.000 sessões/dia · Google a 50% da verba</div>
        <div class="n">No pico de busca de Copa (“odd” a 100), o search pago <b>não trouxe uma única sessão de termo de Copa</b>, e subexecutamos o Google (50% da verba). As keywords que trouxeram tráfego miram casino e concorrente:</div>
        <div class="kw"><span>betwarrior</span><span>site de apostas</span><span>plataforma de cassino</span><span>betano</span><span>palpites futebol</span><span class="copa">Copa: 0 sessão</span></div></div>
    </div>
  </div>
  <div class="band b3">
    <div class="band-hd"><span class="band-tag" style="background:#EF4444;">3 · O gargalo: onboarding com fricção</span>
      <span class="band-sub">a onda chega, mas o funil de cadastro derruba a maioria antes do depósito</span></div>
    {funil}
  </div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>WPR · COPA · DEMANDA vs CAPTURA · JUN 2026</span><span>{GERADO}/2026</span></div>
</body></html>'''
open("wpr-jun-copa-slide.html","w").write(HTML)
print("OK -> wpr-jun-copa-slide.html (%d bytes)"%len(HTML))
