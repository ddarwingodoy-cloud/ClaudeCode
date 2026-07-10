# TODO — Darwin Godoy

> Atualizado diariamente. Trigger de fim de dia: **"fecha o dia"**.

---

## ☀️ Começar TODO dia por aqui
- **`PERFO COPA`** — monitorar a campanha de Copa (captura no paid search + IS/rank/budget). Claude puxa GA4/PBI, Darwin traz os números do Google Ads, cruzam no scorecard. Playbook: `Performance/perfo-copa-playbook.md` · [[project_perfo_search_escalation]]
- **`PIX TRACKING`** — puxar o funil do dia fechado anterior (Registros/Onb Finished/Ready for Deposit/RFD-rate/FTD/conv) e anexar no Sheet **PIX Onboarding pós-fix** (`17mQYC6nvje0cWGi_-DTrT52p-nQoHD1DaL9Bt8Gs_Vk`). Sinal limpo = **RFD-rate** (gargalo eliminado); conv same-day é ruidosa. Regra de parada: até ~14/07 (5-7 dias fechados) → dimensionar lift real via coorte. Fix ativado 07/07 · *08/07*

---

## Recorrentes semanais

| Dia | Report | Trigger |
|---|---|---|
| Segunda | Santi | `SANTI` |
| Terça | Perfo Juanca | a criar |
| Quinta | WPR | `WPR DD-DD/mês/AAAA` |
| Segunda (até 10h) | Semanal Pedro | aba 📈 Marketing do KPI Tracker do mês (`1TduQ6Il...`) |

---

## Em aberto

### ✉️ Drafts prontos pra enviar (Gmail) — *estado 01/07*
- **July budget $10k** → Juanca, cc JP + Santi/Joaco (working number, foco Google, confirmar quinta)
- **Contratos bares** → Gala (dados dos 2 bares + thread do Barba, encadeado no último e-mail dela)
- **BET-824 PIX** → Pedro Burna (anexar os prints manualmente + enviar)
- **Federico (InfoSec)** → resumo em espanhol das 2 ativações
- **Raphael (afiliado grupodupla)** → resposta rápida ("chegou o convite?")
- **Juanca / World Cup** → decidir: segurar p/ quinta (recomendado) ou mandar a resposta (b)

### 🔥 Budget H2 (foco da semana)
- [ ] **Targets Q3 / novo padrão KPI Tracker (Pedro)** — Pedro topou ajustar os targets. **Reunião 08/07 (qua) 10h-12h** (Pedro + Darwin) pra rever todas as assumptions + expectativa de resolução de cada → visão do impacto nos números → propor os **targets Q3 atualizados**. Encaminhamentos já alinhados no Slack: adotar padrão **MTD acumulado + % Achieved**; direção por KPI (FullReg/FTD/GGR/GGR-FTD ↑, **CPA ↓**); **alinhar definição de "registro"** (OKR mostra 21.877 jun vs ~23k 1º step que reportávamos); guardrails de retenção (2nd Deposit D30 / Retention / ARPU D30) → **aba CRM**, não Marketing. GGR/GGR-FTD ficam na aba mas não são KRs. Pedro pediu reservar a sala · *07/07*
- [ ] **Reunião budget Jul-Dez** — quinta **02/07 10:30** (Juanca + JP). Corte agressivo; **Perfo = $10k em julho** (já comunicado ao Juanca; e-mail oficial em draft). Prep: (1) **Verve**: rescisão enviada 30/06, junho+julho pagáveis, **saving = só agosto** (não os ~$31k); (2) Copa Search pacing (estrangulamento Pipol, levar como realocação não denúncia); (3) cenários. Postura: bisturi, não machado · *30/06*
- [ ] **Verve/Match2One (Display)** — **Juanca enviou o aviso formal de rescisão hoje (30/06)**, "Notice of Contract Termination". Cláusula 3.2: 30 dias → encerra **~30/07**. Junho consumido + **julho roda e é pagável** (services rendered); **agosto+ cortado**. Pendências: (a) confirmar com finance/Luiz o valor de junho (nenhuma fatura emitida ainda); (b) pedido de **pausar/capar a entrega de julho** (clawback) está com o Juanca. Saving real = agosto, não os ~$31k · *30/06*
- [ ] **Copa Search — budget** — Pipol estrangulou ($500→$26 em 25/06; só $150 no jogo do Japão, ainda 77% capado). Peça executiva pronta (IS por jogo + Change History). **HOLD**: levar pra quinta como alocação, não enviar agora (conflita com o corte) · [[project_perfo_search_escalation]] · *30/06*

### Ativação RS / Produto
- [ ] **Contratos dos bares (Canto/Espartano)** — Legal (Clara) mandou os 2 contratos; **revisados 07/07**. Resposta à Clara **enviada**: pagamento 26/06 confirmado; achados devolvidos → (1) **bônus FTD (R$65/FTD acima de 400 combinado, via links) precisa entrar na Ordem de Ativação** e a OA está como template (evento/local/endereço/datas a preencher); (2) **conta do Espartano é PF (Lorenzo)** → pedir PJ; (3) **indenização 5.4 ainda em USD** → padronizar BRL; (4) cross-refs 2.4 e 5.4 a confirmar. ✅ 1.3 (QR/registro voluntário), prazo indeterminado + OA, fee R$40k, dados societários OK. **Msg pro Barba enviada** pedindo a conta **PJ da SPTN Ltda** (trava a assinatura do Espartano). Próximo: Legal completa a OA + USD→BRL, chega a conta PJ → circular pra assinatura. Canto já redondo · *07/07*
- [ ] **BET-824 / PIX (fricção de depósito)** — draft de resposta pro **Pedro Burna (Product)** pronto; falta **anexar prints + enviar** (manual, sandbox não anexa). Msg pro **Federico (InfoSec)** pronta · *27/06*
- [ ] **BMA-8912 (TI) — falhas de PIX/depósito Espartano** — chamado aberto 07/07 com base no log do Barba (03-05/07): cluster de erros "conta/instituição de destino" (lado receptor BW, pico sáb 04/07, ~55% travados) + redefinição de senha travando retorno. **Pablo Fernandez já escalou** (status Escalated), cc Maria Paula Burtin. Reforço opcional: BI puxar transações reais pela tag `1211-espartano-bar` (03-05/07) pra anexar número duro · *07/07*
- [ ] **Pilot tracking Copa (btag páginas de Produto)** — rodou no jogo 29/06 (Canto/Espartano → especiais); acompanhar resultado com Matias/Haonan · *29/06*
- [ ] **MyAffiliates — Mkt_Brasil (hierarquia)** — proposta (árvore + texto) enviada ao JP; aguardando decisão dos 3 agrupamentos (3º grupo Ativações, Streamers sub-grupo, Casa Mundialista) · *27/06*

### Afiliados / Parcerias
- [ ] **Arena Afiliados (Mike Martins / Raphael Guedes)** — proposta declinada por ora (abaixo do mercado deles). **Benchmarks Arena:** RevShare ~35%, baseline (min dep **e** wager, rollover ~1x) de **15/30/50**, CPA abaixo das melhores casas. Nossa qFTD (150/100) é 3-10x o baseline deles → **o nó é o baseline** (= trava de exposição do JP); RevShare a gente ganha (40>35), CPA sobe até 200. **Sequência definida:** (1) aguardar o **painel da operação** (Raphael/Mike mandam no grupo); (2) painel na mão → escrever pro **JP** com o cenário + benchmarks; (3) resposta do JP → definir o que responder pro Mike. Mike parkou pro **pós-Copa**, sem risco de esfriar · *03/07*
- [ ] **Beto (streamer/influ) — proposta híbrida** — 2 cenários pra Gi (giovannanucci) mandar pra ele: **A (Híbrida)** R$6k/mês conteúdo (piloto 3m, revisão no meio; entra ago ou via realocação, linha influ de jul comprometida) + afiliado **RevShare 25%** NGR c/ carryover, qFTD dep≥R$50 **e** Gross Bets≥R$50; **B (Só Afiliado)** **CPA R$100/qFTD + RevShare 20%** c/ carryover, mesmo qFTD. **Sem dado validado do Beto** (o estudo −$499 NGR / ticket R$28 era de OUTRO afiliado, Gi confundiu) → o **qFTD do piloto gera o 1º número limpo** dele; acompanhar na revisão do meio pra calibrar renovação. Darwin envia o e-mail · *06/07*
- [ ] **Super Afiliados** — deal fechado; aguardar a minuta de contrato deles · *18/06*
- [ ] **Ampfy** — mandato de mídia; **pago 26/06 (Luiz)**. Acompanhar a frente com a Gala · *16/06*
- [ ] **RDC / Fernando Leomil** — proposta (Pacote M R$50K); analisar e devolver · *27/05*
- [ ] **Streamers** — falar com o Ulisses (pedido do JP) · *22/06*
- [ ] **NFA — encerramento** — acordo fechado: Distrato v2 com **quitação plena de R$230.000** (NFA pedia ~R$290k, Gala ofereceu R$150k). Indo pra **assinatura**; **pagamento dia 10/07**. Conduzido por Gala/Legal + JP; Darwin só CC, sem ação · *30/06*

### Casa Mundialista / Tracking
- [ ] **Casa Mundialista / feed de odds** — BC × Kambi; só acompanhar · *16/06*
- [ ] **Tracking ações Casa Mundialista** — cobrar o Diego · *22/06*
- [ ] **Clever × Kambi (odds dinâmicas)** — abrir frente com o Jose de Miguel · *22/06*

### Outros
- [ ] **Power BI — licença** — conta caiu pra **Free** (perdeu Pro/PPU); ticket **BMA-8843** aberto no IT (status "aguardando suporte"). API/token segue OK, só a UI web travada · *30/06*
- [ ] **PERFO COPA — status 30/06** — pacing preenchido até 30/06. Copa Search **rank-ok (0,07%) mas 80,6% lost-to-budget** com $150/dia (gasta 100%); só budget limita. **Confirmar se a campanha está "Paused" hoje** (rodou dia 30, gastou $148; se pausada na virada = contradiz manter Google). "All ads limited by policy" a cobrar da Pipol · *01/07*
- [ ] **Agendar consulta urologista** — mensagem enviada ao **Flavio Hering**; aguardando retorno. Comparativo em `Projects/Pessoal/urologistas-rede-comparativo.md` · *30/06*
- [ ] **WPR — pacing por canal** — modelo indefinido; pensar formato · *03/06*
- [ ] **NFL no Rio (No Huddle)** — jogo Maracanã 29/09; frente do Joaquin (AR), Darwin em cópia; retomar pós-Copa (ativação BR de carona) · *25/06*

---

## Concluído (últimos 7 dias)

- [x] **SANTI semana 21-27** — draft entregue (ativação RS, revisão de budget/pausa estratégica, tracking afiliados; highlight FTD −23% com aquisição +15%) · *30/06*
- [x] **PERFO COPA — análise do budget Copa Search** — Change History (estrangulamento 25/06 $500→$26), pacing 25-29 completo, correlação jogos×budget, peça executiva pra liderança · *30/06*
- [x] **Planilha do Luiz (Financeiro)** — revisada; JP encaminhou ao Grossi (CFO) a versão com os 2 cenários do 2º semestre · *30/06*
- [x] **Affiliate Manager** — fechado com **Ruan** (começa 13/07) · *30/06*
- [x] **Semanal Pedro W26 (22-28)** — número final pós-backfill; FTD/conversão de depósito caindo (BET-824) + hold de Sports negativo; 3 destinos preenchidos · *29/06*
- [x] **Semanal Pedro W25 (15-21)** — número final pós-backfill; GGR/NGR negativos; 3 destinos; correção do GGR via finance (Luiz) · *22/06*
- [x] **SANTI semana 14-20** — draft revisado e enviado · *23/06*
- [x] **WPR Jun 02-17 (ex-incidente 01/06)** — reconstruído; deck 4 telas; incidente CRM 01/06 quantificado · *19/06*
- [x] **Análise "antes x depois" pros acionistas** — funil BR Jan-Mar vs Abr-Jun · *17/06*
- [x] **Ampfy display — modelo + brief Gala** — docs + aditivo enviado à Gala · *16/06*
- [x] **Casa Mundialista — e-mail Kambi/BC** — reforço dos IPs + recap deep-linking · *16/06*
</content>
