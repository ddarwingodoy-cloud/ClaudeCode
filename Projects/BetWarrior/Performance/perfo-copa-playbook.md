# Playbook — Monitoramento da Campanha de Copa (Perfo / Pipol)

> Objetivo: monitorar diariamente a campanha de Search da Copa (`br_search_aon_conv_mundial`) e julgar se a Pipol está otimizando, focado no que a BR vem cobrando.
> **Trigger: `PERFO COPA`**

## Acesso (a realidade)
- **Claude puxa:** GA4 (captura de Copa no paid search) + Power BI (aquisição).
- **Não há ferramenta de Google Ads no toolset.** IS, lost-to-rank/budget, IS por keyword, spend nativo e Change History só pelo **login do Darwin** (UI / export / print). O acesso de leitura é do navegador dele, não dá pra Claude conectar via API.
- Logo: rotina **híbrida** — Claude roda GA4/PBI, Darwin traz os números do Google Ads, Claude cruza no scorecard.

## 1. O que Claude puxa (diário)
**GA4 — a tese central (captura de Copa no paid search):**
- `run_report` dims `['sessionGoogleAdsKeyword']`, metrics `['sessions','newUsers']`, últimos 1-2 dias.
- Escanear a lista por termos de Copa: `copa`, `mundial`, `brasil x`, `palpite`, `apost*`, nomes de jogos/seleções.
- Pergunta-chave: **termos de Copa estão gerando sessão paga?** Se ~0, a campanha não está capturando.
- + dims `['sessionDefaultChannelGrouping']` para Paid Search sessions/newUsers DoD.

**Power BI — aquisição do dia (suporte):** registros / FTD / depósitos BR External + variação DoD.

## 2. O que o Darwin puxa do Google Ads (com guia)
Foco na campanha **`br_search_aon_conv_mundial`** (ontem + tendência 7d):
- Spend, impressões, cliques, conversões.
- **Search Impr. share** + **IS lost to rank** + **IS lost to budget** (em Columns/Metrics).
- Top keywords + **IS de cada** (especialmente "apostar no brasil").
- Budget diário da campanha (o aumento da Copa entrou de fato?).
- **Change History** (o que a Pipol mexeu desde ontem).
- → manda print/export, Claude interpreta.

## 3. Scorecard — "a Pipol está otimizando a Copa?"
| Critério | 🟢 Verde | 🔴 Vermelho |
|---|---|---|
| Impression Share | subindo (>30%) | parado em ~10% |
| IS lost to rank | caindo (QS/lance melhorando) | preso em ~65% |
| Budget da Copa | aumentou (vs prometido) | igual / sem mudança |
| Termos de Copa no GA4 | aparecendo no paid search | ~0 sessão |
| Cobertura de keyword | IS subindo nos que convertem | top converter capado (apostar no brasil ~16%) |
| Responsividade | agem em ≤24-48h quando apontamos | precisa cobrar toda vez |

## Pacing diário (Sheet)
Toda leitura vai pro Sheet **PERFO COPA — Pacing diário**: `1D4PXQ-hIDBKPMlQLzTn_dHLkijivx2YzmGTV39nKTrs` (aba `Pacing diário`). Uma linha por dia. Claude preenche as colunas GA4 (PS sessões/new, Copa sessões paid, P.Social) e PBI (Registros/FTD); Darwin preenche as do Google Ads (Spend, Impr., Cliques, Conv., IS%, IS lost rank/budget, Budget/dia, IS "apostar no brasil"). Coluna Copa sessões = soma dos termos de Copa/jogos/palpite no `sessionGoogleAdsKeyword` do dia.

## Como rodar
Darwin aciona **`PERFO COPA`** → Claude roda GA4 + PBI, **grava a linha do dia no Sheet de pacing** e pede os números do Google Ads → cruza no scorecard → entrega **snapshot do dia + alertas (verde/vermelho) + o que cobrar**.

## Histórico / âncoras (pra não perder o fio)
- Campanha de Copa **criada em 17/jun 11h45 (Lucas Villalba / Pipol)** — 6 dias após o início do Mundial (11/jun). Change History + impressões zeradas até 17 = prova na fonte.
- Diagnóstico do Juanca (23/06): IS **10,5%**, **rank-limited** (65% rank vs 24% budget) → fix = QS/relevância/lance, não verba. Plano dele: melhorar Ad Rank + aumentar budget da Copa.
- Pontos em cobrança (JP/Darwin): plano de rank com meta+data, confirmação do budget da Copa live, acesso (já liberado 24/06), priorizar termos que convertem.
- Memória: [[project_perfo_search_escalation]] · [[project_btag_landing_tracking]].
