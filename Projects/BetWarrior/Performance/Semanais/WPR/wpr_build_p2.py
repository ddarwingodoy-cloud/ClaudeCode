#!/usr/bin/env python3
# Gerador do slide P2 (Aquisicao por Bloco). 5 blocos single-assignment (utm_source+medium):
# Paid, Influs/Streamers, Afiliados, Org/Direct, Sem UTM. utm_source prioriza influs/streamers. Uso: python3 wpr_build_p2.py
PERIODO="01–30 / Jun 2026"; GERADO="02/07"
HEADLINE=("Atribuição fragmentada, não cega: 23% sem UTM (inclui o incidente de 01/06), não 50%. Paid Media carrega volume e valor (1.822 FTD, R$162k). "
          "Influs/Streamers lidera a conversão (CR 60%) mas com ticket de só R$20 (volume, não valor); Org/Direct traz o maior ticket (R$203, qualidade).")
TOT_REG=12340; TOT_FTD=3407; TOT_VAL=366598
# bloco, FullReg, FTD, CR%, Valor1oDep(R$), cor
BLK=[("Paid Media",6647,1822,27.4,161662,"#FF3900"),
     ("Influs/Streamers",922,550,59.7,10740,"#FF6B3D"),
     ("Afiliados",1521,295,19.4,46541,"#FF8C5A"),
     ("Org/Direct",377,147,39.0,29777,"#FFA07A"),
     ("Sem UTM",2873,593,20.6,117878,"#C8C8C8")]

def br(n): return format(int(round(n)),",.0f").replace(",",".")
CSS=open("wpr-jun-01-10-slide.html").read().split("<style>")[1].split("</style>")[0]
P2CSS='''
.blk-wrap{display:flex;flex-direction:column;gap:18px;flex:1;justify-content:center;padding:8px 6px;min-height:0;}
.blk{display:flex;align-items:center;gap:12px;}
.blk-name{width:120px;font-size:13px;color:#333;font-weight:600;flex-shrink:0;text-align:right;}
.blk-track{flex:1;height:34px;background:#F2F2F2;border-radius:3px;overflow:hidden;}
.blk-fill{height:100%;border-radius:3px;}
.blk-val{width:115px;text-align:left;flex-shrink:0;}
.blk-val b{font-family:'Archivo Black',sans-serif;font-size:17px;color:#111;}
.blk-val span{font-size:11px;color:#AAA;margin-left:5px;}
.att-big{font-family:'Archivo Black',sans-serif;font-size:64px;color:#F59E0B;line-height:1;}
.att-sub{font-size:14px;color:#555;margin-top:6px;}
.att-row{display:flex;gap:8px;margin-top:14px;}
.att-chip{flex:1;background:#F8F8F8;border:1px solid #EFEFEF;border-radius:3px;padding:8px;text-align:center;}
.att-chip .l{font-size:9px;color:#AAA;text-transform:uppercase;letter-spacing:1px;}
.att-chip .v{font-family:'Archivo Black',sans-serif;font-size:18px;color:#111;margin-top:2px;}
.att-note{font-size:11px;color:#888;line-height:1.55;margin-top:14px;padding-top:10px;border-top:1px solid #F0F0F0;}
'''

def hbars(metric):  # metric: 'reg','ftd','val','cr' (sempre ordem decrescente)
    if metric=='reg': vals=[(n,r,c) for n,r,f,cr,vl,c in BLK]; tot=TOT_REG; fmt=lambda v,sh:f"<b>{br(v)}</b><span>{sh:.0f}%</span>"
    elif metric=='ftd': vals=[(n,f,c) for n,r,f,cr,vl,c in BLK]; tot=TOT_FTD; fmt=lambda v,sh:f"<b>{br(v)}</b><span>{sh:.0f}%</span>"
    elif metric=='ticket': vals=[(n,round(vl/f) if f else 0,c) for n,r,f,cr,vl,c in BLK]; tot=None; fmt=lambda v,sh:f"<b>R$ {br(v)}</b>"
    else: vals=[(n,cr,c) for n,r,f,cr,vl,c in BLK]; tot=None; fmt=lambda v,sh:f"<b>{v:.1f}%</b>"
    vals=sorted(vals,key=lambda t:-t[1]); mx=max(v for n,v,c in vals)
    rows=[]
    for n,v,c in vals:
        w=v/mx*100; sh=(v/tot*100) if tot else 0
        rows.append(f'<div class="blk"><div class="blk-name">{n}</div>'
                    f'<div class="blk-track"><div class="blk-fill" style="width:{w:.1f}%;background:{c};"></div></div>'
                    f'<div class="blk-val">{fmt(v,sh)}</div></div>')
    return '<div class="blk-wrap">'+''.join(rows)+'</div>'

def panel(title,note,body,cls="p-half"):
    return (f'<div class="panel {cls}"><div class="ph">'
            f'<svg width="13" height="13" viewBox="0 0 13 13"><rect x="0" y="2" width="13" height="3" rx="1" fill="#FF3900"/><rect x="0" y="7" width="9" height="3" rx="1" fill="#FF3900" opacity=".5"/></svg>'
            f'<span class="ph-title">{title}</span><span class="ph-note">{note}</span></div>'
            f'<div class="p-body">{body}</div></div>')

ATT=('<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">'
     '<div class="att-big">19%</div>'
     '<div class="att-sub"><b>sem nenhuma UTM</b> (era 50% olhando só o medium, a diferença vivia no utm_source)</div>'
     '<div class="att-row">'
     '<div class="att-chip"><div class="l">Sem UTM (gap real)</div><div class="v">1.914</div></div>'
     '<div class="att-chip"><div class="l">Influs/Streamers</div><div class="v">551 FTD</div></div>'
     '<div class="att-chip"><div class="l">CR Influs/Streamers</div><div class="v">58%</div></div>'
     '</div>'
     '<div class="att-note">Metade parecia cega porque olhávamos só o <b>utm_medium</b>. Cruzando com o <b>utm_source</b>, '
     'o recuperado é quase todo <b>Influs/Streamers</b> (streamers + influs_br), o canal de maior CR. Afiliados, streamers e influs '
     'são geridos no <b>MyAffiliates</b> (Jocelyne: 564 FTD em jun), fora do PowerBI. O 19% restante é o gap real: '
     'ativações e influs cujo <b>btag quebra na landing de conteúdo</b> (fix da Perfo em teste).</div>'
     '</div>')

HTML=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>WPR Brasil · P2 Aquisição por Bloco · Jun 01–30/2026</title>
<style>{CSS}{P2CSS}</style></head><body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">AQUISIÇÃO POR BLOCO</div>
    <div class="hdr-sub"><strong>{HEADLINE}</strong></div></div>
  <div class="hdr-meta">{PERIODO}<br>Registros · FTD · CR%<br>Gerado {GERADO}</div>
</div>
<div class="body">
  <div class="row row-top">
    {panel("Registros por Bloco","Full Registration · External · cinza = % do total",hbars("reg"))}
    {panel("FTD por Bloco","FactFirstDeposit · cinza = % do total",hbars("ftd"))}
  </div>
  <div class="row row-bot">
    {panel("Taxa de Conversão (CR%) por Bloco","FTD ÷ Registros · ordem decrescente",hbars("cr"))}
    {panel("Ticket Médio do 1º Depósito","Valor 1º dep ÷ FTD · qualidade por fonte · média R$108",hbars("ticket"))}
  </div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>WPR · PÁG. 2 · AQUISIÇÃO POR BLOCO · JUN 01–30/2026</span><span>02/07/2026</span></div>
</body></html>'''
open("wpr-jun-01-30-slide-p2.html","w").write(HTML)
print("OK -> wpr-jun-01-30-slide-p2.html (%d bytes)"%len(HTML))
