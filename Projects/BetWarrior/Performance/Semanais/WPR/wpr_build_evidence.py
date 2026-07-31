#!/usr/bin/env python3
# Evidence one-pager (EN) for the Search/Perfo discussion. Media only, no onboarding. Safe frame.
PERIODO="World Cup window 11-17 vs pre-Cup 02-10 / Jun 2026"; GERADO="19/06"
HEADLINE=("World Cup search demand surged ~10x, but from our only view (GA4) Paid Search brought zero Cup-term sessions "
          "and Google ran at 50% of budget. We can't tell from our side if that's coverage, bid or auction loss, that view lives in Google Ads.")
CSS=open("wpr-jun-01-10-slide.html").read().split("<style>")[1].split("</style>")[0]
EXTRA='''
.band{display:flex;flex-direction:column;gap:7px;min-height:0;}
.b1{flex:1;} .b2{flex:1.15;} .b3{flex:0.8;}
.band-hd{display:flex;align-items:center;gap:10px;flex-shrink:0;}
.band-tag{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:2px;text-transform:uppercase;padding:3px 11px;border-radius:3px;color:#fff;}
.band-sub{font-size:11.5px;color:#999;}
.cards{display:flex;gap:10px;flex:1;min-height:0;}
.card{flex:1;background:#FFF;border:1px solid #E0E0E0;border-radius:4px;padding:14px 16px;display:flex;flex-direction:column;justify-content:center;gap:5px;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.card .l{font-size:11px;color:#AAA;text-transform:uppercase;letter-spacing:1px;}
.card .v{font-family:'Archivo Black',sans-serif;font-size:40px;line-height:1;}
.card .d{font-size:13px;font-weight:700;}
.card .n{font-size:12px;color:#888;line-height:1.4;}
.kw{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px;}
.kw span{font-size:10.5px;padding:2px 8px;border-radius:10px;background:#F2F2F2;color:#777;}
.kw .copa{background:#FDECEC;color:#EF4444;font-weight:700;border:1px dashed #EF4444;}
.ask{flex:1;display:flex;align-items:center;gap:14px;background:#FFF7F4;border:1px solid #FFD9CC;border-radius:4px;padding:14px 20px;}
.ask .big{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:1px;text-transform:uppercase;color:#FF3900;width:150px;flex-shrink:0;}
.ask ol{margin:0 0 0 18px;font-size:13px;color:#444;line-height:1.7;columns:2;column-gap:32px;}
'''
def card(label,val,vcolor,delta,dcolor,note):
    return (f'<div class="card"><div class="l">{label}</div>'
            f'<div class="v" style="color:{vcolor};">{val}</div>'
            f'<div class="d" style="color:{dcolor};">{delta}</div>'
            f'<div class="n">{note}</div></div>')
demand=(card("Cup search · Google Trends","+10x","#FF3900","“odd” peaked 100 · “aposta copa” +8x","#FF3900","Brazil, spiked Jun 11-13 (Cup start + Brazil match)")
    +card("Site traffic","+29%","#FF3900","13,252 → 17,136 sessions/day","#FF3900","The wave reached the site on match days")
    +card("Sports engagement (base)","+13%","#22C55E","sports bettors · handle +6%","#22C55E","The existing base leaned into the Cup"))
HTML=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>BetWarrior BR · Paid Media · World Cup Search Evidence</title>
<style>{CSS}{EXTRA}
@page {{ size: 1920px 1080px; margin: 0; }}
</style></head><body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">PAID MEDIA · WORLD CUP SEARCH</div>
    <div class="hdr-sub"><strong>{HEADLINE}</strong></div></div>
  <div class="hdr-meta">{PERIODO}<br>GA4 · Google Trends<br>Generated {GERADO}</div>
</div>
<div class="body">
  <div class="band b1">
    <div class="band-hd"><span class="band-tag" style="background:#FF3900;">1 · The demand surged</span>
      <span class="band-sub">World Cup search and engagement spiked, on and off site</span></div>
    <div class="cards">{demand}</div>
  </div>
  <div class="band b2">
    <div class="band-hd"><span class="band-tag" style="background:#22C55E;">2 · Where we captured it</span>
      <span class="band-sub">Paid Social responded; Paid Search did not move</span></div>
    <div class="cards">
      <div class="card"><div class="l">Paid Social · responded to the Cup</div>
        <div class="v" style="color:#FF3900;">3x</div>
        <div class="d" style="color:#22C55E;">2,006 → 6,387 sessions/day (+218% vs May)</div>
        <div class="n">New Cup creatives drove ~72% of the traffic lift. The channel did its job.</div></div>
      <div class="card"><div class="l">Paid Search · flat at the search peak</div>
        <div class="v" style="color:#EF4444;">+6%</div>
        <div class="d" style="color:#EF4444;">942 → 1,000 sessions/day · Google at 50% of budget</div>
        <div class="n">At the Cup search peak (“odd” at 100), paid search brought <b>zero sessions from Cup terms</b>. The keywords that did drive traffic point to casino and competitors:</div>
        <div class="kw"><span>betwarrior</span><span>site de apostas</span><span>plataforma de cassino</span><span>betano</span><span>betsson</span><span>palpites futebol</span><span class="copa">Cup terms: 0 sessions</span></div></div>
    </div>
  </div>
  <div class="band b3">
    <div class="band-hd"><span class="band-tag" style="background:#111;">3 · The blind spot · what we need</span>
      <span class="band-sub">GA4 shows outcomes, not bids. The cause lives in Google Ads</span></div>
    <div class="ask">
      <div class="big">To close the gap together:</div>
      <ol>
        <li>Read access to Google Ads &amp; Business Manager (or a recurring report)</li>
        <li>Impression Share lost: budget vs rank (bid / quality)</li>
        <li>The current keyword basket for the Cup (brand, match, long-tail)</li>
        <li>Budget pacing: Google at ~50% vs ~57% of the month</li>
      </ol>
    </div>
  </div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>PAID MEDIA · WORLD CUP SEARCH EVIDENCE · JUN 2026</span><span>GA4 + Google Trends · {GERADO}</span></div>
</body></html>'''
open("evidence-search-copa.html","w").write(HTML)
print("OK -> evidence-search-copa.html (%d bytes)"%len(HTML))
