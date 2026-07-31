#!/usr/bin/env python3
# Gerador do P4 (Proximos Passos). Acoes saidas da analise da semana. Uso: python3 wpr_build_p4.py
GERADO="02/07"; PERIODO="Jun 01–30 · Reunião 02/07/2026"
ACTIONS=[
 ("01","Hold de Sports negativo · estrutural, não Copa",
  "Junho fechou com GGR R$54k (12% da meta) e NGR no zero (-R$3k), margem de Sports -2,2%. Não é efeito de Copa que normaliza: pelo Trading/BI o driver é estrutural, Tennis (ITF Men/Women) e eFootball somam ~R$65k de GGR negativo no mês (jogadores sharp recorrentes), mais high-rollers idiossincráticos no Casino (bloqueio AML pós-aposta, threshold R$10k). Pedir a Trading ação de exposição e limites em Tennis e eFootball, e revisar o timing do bloqueio AML.",
  "Imediato","date-dark","Trading · Risco · AML"),
 ("02","Concentrar o paid no que converte",
  "No mês, Meta e TikTok estouraram a verba (114% / 122%) e ficaram longe da meta (52% / 25%); X sem retorno; só o Google fecha (CPA R$558, base GA×1,33). Com o corte de budget de julho, concentrar no Google/Search e pausar ou reduzir Meta, TikTok e X.",
  "Julho","date-dark","Perfo · Diego"),
 ("03","Qualidade do tráfego · ticket e valor em queda",
  "A Copa trouxe mais gente, não mais valor: apostadores ativos +23% mas Gross Bets por apostador -34%, ticket do 1º depósito R$145 para R$108 e base existente -30% em Gross Bets. Investigar o mix de aquisição (Influs tem CR alto mas ticket de só R$20) e abrir uma frente de reativação/CRM da base existente.",
  "Julho","date-dark","Growth · CRM"),
 ("04","Search de Copa no mata-mata · budget é o limite",
  "O rank está resolvido (perda por rank <1%); o que limita a Copa Search é budget (chegou a 77-89% de perda por orçamento). Nas datas de jogo do mata-mata, priorizar o Search dedicado dentro do teto de julho para capturar a demanda de marca dos concorrentes.",
  "Julho","date-dark","Perfo · Diego"),
 ("05","Atribuição de afiliados (btag) · acompanhar o fix",
  "Ainda 23% dos registros sem UTM (inclui o incidente de 01/06). A Perfo assumiu o fix do btag e testa URLs para não perder o parâmetro na landing de conteúdo, sem depender da Shape. Acompanhar e cobrar prazo.",
  "Jul","date-gray","Perfo · BI"),
]
def act(num,title,desc,date,dcls,owner):
    return (f'<div class="action"><div class="action-num">{num}</div>'
            f'<div class="action-body"><div class="action-title">{title}</div>'
            f'<div class="action-desc">{desc}</div></div>'
            f'<div class="action-meta"><span class="action-date {dcls}">{date}</span>'
            f'<span class="action-owner">{owner}</span></div></div>')
CSS=open("wpr-jun-01-10-slide-p4.html").read().split("<style>")[1].split("</style>")[0]
P4EXTRA=".actions{justify-content:center;gap:10px;}"  # agrupa os topicos, sem vazio distribuido entre eles
HTML=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>WPR Brasil · P4 Próximos Passos · Jun 01–30/2026</title>
<style>{CSS}{P4EXTRA}</style></head><body>
<div class="hdr">
  <div class="logo-block"><div class="logo-bar"></div>
    <div class="logo-text"><div class="brand">BETWARRIOR</div><div class="sub">BRASIL</div></div></div>
  <div class="hdr-sep"></div>
  <div class="hdr-body"><div class="hdr-title">Weekly Performance Report · Próximos Passos</div>
    <div class="hdr-sub">5 ações prioritárias &nbsp;·&nbsp; <strong>Hold</strong> &nbsp;·&nbsp; Paid &nbsp;·&nbsp; Qualidade &nbsp;·&nbsp; Copa &nbsp;·&nbsp; Atribuição</div></div>
  <div class="hdr-meta">{GERADO} / Jun 2026<br>BetWarrior Brasil<br>Reunião WPR</div>
</div>
<div class="body">
  <div class="section-label">Ações e responsabilidades</div>
  <div class="period-note">WPR · {PERIODO}</div>
  <div class="actions">{''.join(act(*a) for a in ACTIONS)}</div>
</div>
<div class="ftr"><span>BETWARRIOR BRASIL · CONFIDENTIAL</span>
  <span>WPR · PÁG. 4 · PRÓXIMOS PASSOS · JUN 01–30/2026</span><span>{GERADO}/2026</span></div>
</body></html>'''
open("wpr-jun-01-30-slide-p4.html","w").write(HTML)
print("OK -> wpr-jun-01-30-slide-p4.html (%d bytes)"%len(HTML))
