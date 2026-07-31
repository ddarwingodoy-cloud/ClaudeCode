# WPR Playbook — BetWarrior Brasil

> Guia operacional para construção do Weekly Performance Report.
> Consolidado em 28/05/2026 — incorpora aprendizados das entregas Mai 01-21 e Mai 01-27.
> Modelo de referência: arquivos em `Performance/Semanais/WPR/` prefixo `wpr-mai-01-27-*`.

---

## 1. Periodicidade e Entrega

- Entrega: toda **quarta-feira** (reunião WPR)
- Período: **definido por Darwin na solicitação** — sempre comparar períodos com os mesmos dias da semana (normalização por dia, não por contagem fixa de dias)
- Arquivos individuais em `Semanais/WPR/`: `wpr-[mes]-[dd]-[dd]-slide.html` (P1–P4)
- Arquivo unificado: `WPR_Brasil_[Mês][DD-DD]_[YYYY].html` — capa + P1 + P2 + P3 + P4 empilhados, escalagem automática via JS
- Fonte de mídia paga (P3): **PACING - PERFO** (Google Sheet vivo do Diego, ID `1LnnVk3mtjmx6ibXXtyA7_JqIxu0gf8DyeCK9MGve53w`). **Checar `modifiedTime` antes de usar** — o xlsx local em `Semanais/WPR/PACING - PERFO (1).xlsx` fica desatualizado (era de maio em 18/06). Não perguntar ao Darwin: verificar a versão do Drive direto.

---

## 2. Normalização de Períodos

> **NÃO perguntar período/normalização ao Darwin. Calcular pela regra abaixo.** (gerou atrito 18/06)

**Janela (MTD):** do dia 1 até o último dia de referência fechado, a quarta-feira anterior à quarta de entrega. Ex.: entrega 24/06 → janela Jun **01–17**; entrega 12/06 → Jun **01–10**.

**Normalização por dia da semana:** a âncora é o **dia da semana do dia 1 do mês atual** (varia por mês, NÃO é fixa em sexta). Cada mês comparado começa na 1ª ocorrência desse mesmo dia da semana e usa o **mesmo número de dias**. Jun/2026: dia 1 = **segunda**, janela 01–17 (seg→qua, 17 dias) → Mai equivalente = **04–20** (seg→qua, 1ª segunda de maio + 16 dias); Abr = 1ª segunda + 16 dias; etc. Comparar por dia de calendário (Jun 01-17 vs Mai 01-17) está ERRADO.

**A tabela do P1 carrega a série inteira de 2026, Jan → mês atual** (não é MoM de 2 meses). Ex. `wpr-jun-01-10`: linhas Jan, Fev, Mar, Abr★, Mai, Jun▶. A quantidade de meses **cresce a cada ciclo**. Marcações: ▶ mês atual, ★ pico histórico. Linhas de análise: Δ vs mês anterior, Meta, vs Meta (ver §13.3).

**Referência de pacing**: dias transcorridos / dias totais do mês (ex: 17/30 = 56,7% em jun).

---

## 3. Fontes de Dados

| Dado | Fonte | Campo / Observação |
|------|-------|--------------------|
| Sessões | GA4 | Filtro: país=BR |
| FullReg | PowerBI — FactFullRegistration | Ver regra locked_status abaixo |
| FTDs | PowerBI — FactFirstDeposit | Ver regra locked_status abaixo |
| GGR / NGR / GB | PowerBI — FactAGGAccountTransaction | Fórmulas na seção 10 |
| Funil Registros (1º step) | PowerBI — DISTINCTCOUNT(kyc_onboardings_logs[username]) @ status_onboarding="PENDING_CONFIRMATION" | Bate com The Dashboard (Betinho). NÃO usar COUNTROWS (reenvio VERIFICATION_CODE_RESENT infla); party_id nulo no 1º step |
| Funil Pronto p/Dep | PowerBI — kyc_onboardings_logs status_onboarding="READY_FOR_DEPOSIT" | KYC PASS |
| Meta FTD | Forecast Dada `1UtdEyu8...` aba "Simulator - New" linha **8+9** (FTD + Afiliados), col B=Abr/C=Mai/D=Jun | distribuir pela curva Copa |
| Meta GGR/NGR/Margens | Forecast Dada linhas **44/47/42/43** + Mix Sports linha **41** | GGR/NGR pela curva; margens flat |
| Canais | PowerBI — DimPlayer[utm_medium_signup] | Campo correto — não usar utm_medium |
| Apostadores / R$/ap | PowerBI — FactAGGAccountTransaction por utm_medium_signup | |
| GB new vs base | PowerBI — FactAGGAccountTransaction[customer_new_or_returning] | New Customer = FTDs do período |
| Invest / Budget / CPA | PACING-PERFO (Diego) | **Valores em USD** → converter para BRL |
| Câmbio | Verificar no dia da entrega | Usar câmbio do dia; registrar no ph-note |

### Filtros obrigatórios em todas as queries PowerBI

```
DimPlayer[internal_external_player] = "External"
```

### Regra locked_status

Usar `DimPlayer[locked_status] = "NOT_LOCKED"` **somente no funil** (No Lock e Pronto p/Dep) e em P2 (FullReg por canal). **Nunca expor** o filtro nas legendas, títulos ou tooltips — exibir apenas "FullReg" ou "Full Registration". Não usar NOT_LOCKED para FTDs ou para a tabela principal de P1.

---

## 4. Arquitetura de Arquivos (HTML)

```
WPR_Brasil_[Mês][DD-DD]_[YYYY].html   ← master (capa dark + iframes escalados)
wpr-[mes]-[dd]-[dd]-slide.html        ← P1 Métricas de Negócio
wpr-[mes]-[dd]-[dd]-slide-p2.html     ← P2 Aquisição por Canal
wpr-[mes]-[dd]-[dd]-slide-p3.html     ← P3 Performance de Mídia
wpr-[mes]-[dd]-[dd]-slide-p4.html     ← P4 Próximos Passos
```

**Regra de escala (master HTML)**:
```js
function scaleSlides() {
  document.querySelectorAll('.slide-wrap').forEach(wrap => {
    const scale = wrap.clientWidth / 1920;
    wrap.style.height = Math.round(1080 * scale) + 'px';
    const iframe = wrap.querySelector('iframe');
    if (iframe) iframe.style.transform = 'scale(' + scale + ')';
  });
}
scaleSlides();
window.addEventListener('resize', scaleSlides);
```

Cada iframe: `width: 1920px; height: 1080px; transform-origin: top left`.  
**Cache busting obrigatório**: incrementar `?v=N` nos srcs dos iframes a cada atualização.

**Capa**: fundo `#111`, painel direito `#FF3900` com ghost text "WPR". Header sem labels de texto adicionais (`.cv-hdr-label` e `.cv-hdr-meta` removidos em 28/05/2026 — não restaurar).

---

## 5. P1 — Métricas de Negócio

### 5.1 Funil de Ativação (evolução, linhas=meses)

**3 steps (a partir de Jul 01-22 — Pronto p/Dep APOSENTADO):**
```
Sessões → Registros → FTD
```

| Step | Fonte | Legenda |
|------|-------|---------|
| Sessões | GA4 BR | "GA4" |
| Registros (New Registrations) | PowerBI SUM(FactRegistration[registration_count]) + escopo BR+BWBRA | "PowerBI" |
| FTD | PowerBI FactFirstDeposit | "PowerBI" |

> **Registros = New Registrations (`FactRegistration[registration_count]`), CORRIGIDO 24/07.** Bate EXATO com o report Weekly KPIs by Brand / The Dashboard do Betinho (Jul 01-22 = 3.499, CR 25,0% ≈ Betinho 25,1%). **Substituiu o antigo "1º step do kyc"** (`DISTINCTCOUNT(kyc_onboardings_logs[username])` @ PENDING_CONFIRMATION), que era **all-brand** (misturava brand_id 1002, ~+322 registros em jul) e **não batia o Dashboard** (dava 4.020 e inflava, derrubando o CR pra 21,8% em vez de 25,0%). Não voltar pro kyc.

> **Pronto p/Dep (READY_FOR_DEPOSIT) foi retirado do funil em Jul 01-22.** O fix do PIX (BET-824) eliminou o passo bancário do caminho crítico: ninguém mais para no RFD, então FTD > RFD e a conversão "Pronto→FTD" dava >100% (sem sentido). Some o problema técnico extra: o RFD vem do kyc_onboardings_logs **sem filtro de marca** (all-brand), enquanto o FTD é BR+BWBRA — não são a mesma base. Funil virou 3 steps, com a CR (Registros→FTD) batendo EXATO com a CR% da tabela. Se o RFD voltar a fazer sentido (mudança de fluxo), reavaliar.
> **Registros = 1º step do onboarding** (decidido 18/06, alinha com a visão do Betinho/The Dashboard). A **tabela** segue com FullReg = FactFullRegistration (isonomia histórica, não muda).

**Taxas de conversão em cada interseção** — formato `±X,Xpp vs [Mês anterior]`.

**SVG — especificações obrigatórias**:
- viewBox: `0 0 432 120`
- Números: `y=60`, `dominant-baseline="middle"`, `font-size="13"`, `text-anchor="middle"`
- Centros X: 54 (Sessões), 162 (No Lock), 270 (Pronto p/Dep), 378 (FTD)
- Cores trapézios: `#FF7A50` → `#FF3900` → `#CC2E00` → `#8B1500`

### 5.2 Tabela Métricas de Negócio

**Colunas fixas**: Mês | Registros | FTDs | CR% | GGR (R$) | NGR (R$) | Marg. | SB | CS

- **Registros** = New Registrations (`SUM(FactRegistration[registration_count])`, escopo BR+BWBRA), mesma fonte do funil. **Corrigido 24/07** (era 1º step do kyc, all-brand, não batia o Dashboard). Bate com o report/Betinho.
- **CR%** = FTDs / Registros (New Registrations). Meta = CR alvo 25% (Jul, ver §13.4). Jul 01-22 fechou 25,0% = na meta.
- **Marg.** = NGR / Gross Bets
- **GGR/NGR**: em R$k
- Linha mês atual: `class="cw"` (fundo #FFF5F2, borda-left laranja)
- Linha delta Δ vs mês anterior: `class="dr"` (fundo #F5F5F5)
- Mês de pico histórico = `★`; mês atual = `▶`

**CSS fontes (padrão ampliado 24/07 — WPR Jul 01-22, para leitura em tela/projeção)**:
- `thead th`: 14px (padding 11px 8px) | `tbody td`: 15px (padding 13px 8px) | `tbody td:first-child`: 14px | `.tnote`: 11,5px
- Tabela agora vive em **painel próprio** (esquerda da linha de baixo), com `.p-tbl .p-body { justify-content:center }` para centralizar e matar o vazio. Substituiu o quadro "efeito PIX", aposentado em Jul 01-22.
- **Nota do NGR** (embaixo da tabela, substitui a tnote de metodologia): explica por que o NGR está negativo (GGR positivo = livro não perde p/ apostador; vermelho = bônus > GGR fino por hold de SB + bônus/Gross Bets subindo). O caveat "Meta = Forecast não flexibilizada" e "Registros = 1º step" migraram para os ph-notes/rodapé do funil (não repetir na tabela).

### 5.3 Cards Base Ativa + Composição do Gross Bets (painel "Saúde da Base Ativa")

| Card | Métrica | Cor delta |
|------|---------|-----------|
| Apostadores Ativos | Únicos com ≥1 GAME_BET no período | vermelho se ↓ |
| Gross Bets / Apostador | GB total / apostadores | verde se ↑ |
| GB — Novos FTDs | GB de players com FTD no período (`customer_new_or_returning = "New Customer"`) | contexto |
| GB — Base Existente | GB de players com FTD antes do período (`customer_new_or_returning = "Returning Customer"`) | verde se ↑ |

**Fonte cards 3 e 4**: `KEEPFILTERS(FILTER(FactAGGAccountTransaction, [account_transaction_type] = "GAME_BET"))` + `KEEPFILTERS(FILTER(DimPlayer, [internal_external_player] = "External"))` agrupado por `[customer_new_or_returning]`.

**CSS cards (ampliado 24/07)**: label 10px #AAAAAA (nowrap); número 27px Archivo Black; delta 14px bold; sub-delta `.dv` 10,5px #BBB (linha "vs [mês ant.]" separada, cabe em card estreito). 5 cards: GB Total · Apostadores · GB/Apostador · GB Novos FTDs · GB Base Existente.

**Composição do Gross Bets · Novos vs Base Existente** (barra empilhada 3 meses, abaixo dos cards): Novos (`New Customer`, cinza #D8D8D8) vs Base Existente (`Returning Customer`, laranja #FF3900). Foco = **a virada de share** (ex. Jul 01-22: base 46%→42%→73% com o corte de mídia), não a foto do mês. Cards seguem vermelhos (absolutos caíram); a composição mostra que dentro do bolo menor a base virou maioria — leitura honesta, sem maquiar. Read enquadra como transição ("enquanto estruturamos Afiliados e VIP..."), não abandono de aquisição.

---

## 6. P2 — Aquisição por Canal

### Mapeamento de Canais (DimPlayer[utm_medium_signup])

| Canal exibido | Valores utm_medium_signup |
|---------------|--------------------------|
| Paid Media | `paid_media` |
| Org. / Direct | `(none)`, `organic`, `(direct)`, vazio |
| Affiliates | `affiliate` |
| Others | `social_paid`, `email`, demais não mapeados |

**`social_paid` = publisher/comparador (ex: betdasorte) — problema de atribuição confirmado. Manter em Others.**

### 6.1 Full Registration por Canal
- Fonte: PowerBI FactFullRegistration + DimPlayer[utm_medium_signup] + NOT_LOCKED
- Exibir como "Full Registration" — não mencionar NOT_LOCKED

### 6.2 FTDs por Canal
- Fonte: PowerBI FactFirstDeposit + DimPlayer[utm_medium_signup]

### 6.3 CR% por Canal
- CR% = FTDs canal / FullReg canal
- Ordenação: decrescente
- Canal líder: barra laranja; abaixo da média: cinza

### 6.4 Gross Bets Evolução (3 meses)
- 3 períodos normalizados: Mar, Abr, Mai
- Mar = cinza claro `#DDDDDD`; Abr = cinza médio `#999999`; Mai = laranja `#FF3900`
- Referência 100%: maior valor individual entre todos os canais/meses
- Others = social_paid + demais somados

**Regra de ordenação universal em P2**: todos os gráficos do maior para o menor — mesma ordem em todos os painéis.

---

## 7. P3 — Performance de Mídia

### 7.1 Câmbio — Regra Crítica

Todo dado do PACING-PERFO (Diego) está em USD. Converter para BRL antes de incluir. Registrar câmbio no `ph-note`: ex. `"câmbio R$5,56"`. Usar câmbio do dia da entrega.

### 7.2 G1 — Budget vs FTDs · CPA por Plataforma

**Fonte**: PACING-PERFO (Diego)  
**Dados por plataforma**: % budget executado (cinza), % FTDs realizados (laranja), CPA R$ (linha preta), investimento US$.  
**Plataformas sem atribuição** (X, Taboola): barra FTD tracejada, FTDs marcados com †.

**Posições SVG** (viewBox 0 0 600 320, chart y=16..225, escala 1%=2,09px):
| Plataforma | Budget x | FTD x | Dot x |
|------------|----------|-------|-------|
| Google | 68 | 96 | 108 |
| Meta | 168 | 196 | 208 |
| TikTok | 268 | 296 | 308 |
| X | 368 | 396 | — |
| Taboola | 468 | 496 | — |

Escala CPA: `y = 225 − (CPA_BRL × 209/1500)`. Máximo do eixo = R$1.500 → y=16.

### 7.3 G2 — Gross Bets · R$/Apostador por Canal

**Fonte**: PowerBI — utm_medium_signup, 27 dias normalizados  
**4 canais distribuídos uniformemente** (centros x = 110, 237, 364, 491):

| Canal | Centro X | Gray rect x | Red rect x | Dot x |
|-------|----------|-------------|------------|-------|
| Paid Media | 110 | 84 | 112 | 124 |
| Org/Direct | 237 | 211 | 239 | 251 |
| Affiliates | 364 | 338 | 366 | 378 |
| Others | 491 | 465 | 493 | 505 |

Polyline conecta os dots. Linha avg R$/apostador tracejada horizontal.

### 7.4 Painel Pacing

**Referência**: dias transcorridos / dias do mês (ex: 27/31 = 87,1%)  
**Por plataforma**: % orçamento, % FTDs, Δ vs referência em pp  
**Coloração dos deltas**:
- Δ > −5pp: `#F59E0B` (âmbar)
- Δ ≤ −5pp: `#EF4444` (vermelho)
- Δ ≥ +5pp: `#22C55E` (verde)

---

## 8. P4 — Próximos Passos

- **Ordenação**: cronológica — mais próximo primeiro
- **Date pill dark** (`date-dark`, fundo #111): prazo definido
- **Date pill gray** (`date-gray`, fundo #F0F0F0): TBD / longo prazo
- Máximo 8 ações; se mais, priorizar

**CSS fontes (ajuste de 28/05, não reverter)**:
- `.action-num`: 25px | `.action-title`: 15px | `.action-desc`: 13.5px | `.action-date`: 13px | `.action-owner`: 12.5px

---

## 9. Design System — Tokens (nunca alterar)

| Elemento | Valor |
|----------|-------|
| Fundo páginas | `#F2F2F2` |
| Fundo painéis | `#FFFFFF` |
| Borda painéis | `#E0E0E0` |
| Accent / Header | `#FF3900` |
| Texto principal | `#111111` |
| Texto muted | `#AAAAAA` |
| Sucesso | `#22C55E` |
| Alerta | `#F59E0B` |
| Erro / negativo | `#EF4444` |
| Fonte título | Archivo Black |
| Fonte corpo | Archivo Regular |
| Header height | 80px |
| Footer height | 28–30px |
| Body padding | 14px 20px |
| Gap painéis | 12px |

---

## 10. Fórmulas PowerBI

```
ESCOPO OBRIGATORIO (corrigido 10/07/2026): Brazil + BWBRA + External
   FILTER(DimPlayer, player_country_name="Brazil" && brand_name="BWBRA" && internal_external_player="External")
   >>> Sem o filtro marca/pais, pega outras operacoes e o NGR inverte o sinal. FTD 01-08/jul = 385 (bate o Dashboard).
GGR = ABS(GAME_BET) − (GAME_WIN + CASH_OUT + CORRECTION)        [TODAS as sub-contas, NAO filtrar AMOUNT_REAL]
NGR = GGR − BonusCost                                          [METODO CORRETO — as colunas do report Power BI]
   BonusCost = SUM WHERE account_transaction_type IN {"CRE_BONUS","PRODUC_BON","CANC_BONUS"}
Gross Bets = ABS(SUM(FactAGGAccountTransaction[account_transaction_amount]))
             WHERE account_transaction_type = "GAME_BET"
Gross Wins = SUM WHERE type IN {"GAME_WIN", "CASH_OUT", "CORRECTION"}
Margem = GGR / Gross Bets    (SB/CS = GGR do produto / GB do produto, via DimGame[game_platform_name])
```

> **NGR (corrigido 10/07/2026) = GGR total − BonusCost.** Reconciliado peça a peça com o report Power BI (01-08/jul): GrossBets 557.389, GrossWins 550.924, GGR 6.464, todos exatos. NGR ≈ -R$4,7K (External) / dashboard -4,5K / report -4,0K.
> **O método ANTIGO `RealGGR(AMOUNT_REAL) − ReleasedBonus` estava ERRADO** — dava +R$8,9k (sinal invertido) sem o escopo BR, e mesmo com escopo dá -5,5k (∼R$1,5k longe do report). NÃO usar. O `wpr_pull.py` já foi corrigido.
> **⚠ Os WPRs anteriores (mai/jun) usaram o método antigo + escopo sem BWBRA** — o NGR deles pode estar com esse viés; re-checar se algum for reapresentado.
> Resíduo ∼R$500 no BonusCost vs report (10.975 meu vs 10.465 dele) = measure fino de bônus do report; pinar com o Betinho se precisar byte-exact.

**Armadilhas críticas**:
- `GAME_BET` é negativo — sempre usar `ABS()`
- Gross Wins = 3 tipos, nunca só GAME_WIN
- Withdrawals: usar `FactPayment` com `payment_type="WITHDRAWAL"` e `payment_status="COMPLETED"` — nunca FactAGGAccountTransaction
- Datas: sempre `FILTER(DimDate, DimDate[Date] = ...)` — não filtrar campos de data nas tabelas de fato

---

## 11. Checklist Pré-Entrega

### P1
- [ ] Funil: 4 steps, taxas em cada interseção, Δ vs mês anterior
- [ ] Números do funil centralizados (y=60, dominant-baseline=middle, font-size=13)
- [ ] Tabela: colunas Mês | FullReg | FTDs | CR% | GGR | NGR | Marg. | SB | CS
- [ ] Cards Base Ativa: 4 cards (Apostadores, GB/apost, GB Novos FTDs, GB Base Existente)

### P2
- [ ] FullReg exibido sem menção a NOT_LOCKED
- [ ] CR% bate com FTD/FullReg da mesma página (conferir canal por canal)
- [ ] Todos os gráficos ordenados do maior para o menor, na mesma ordem
- [ ] Others = social_paid + demais fundidos (não exibir "Paid Social" separado)

### P3
- [ ] Invest/Budget/CPA do Diego convertidos de USD para BRL
- [ ] Câmbio registrado no ph-note
- [ ] G2: 4 canais distribuídos uniformemente no eixo X
- [ ] Others inclui social_paid

### P4
- [ ] Ações em ordem cronológica (mais próximo primeiro)
- [ ] Date pills e owners preenchidos

### Master HTML
- [ ] Capa com período correto (cv-tag + cv-period)
- [ ] Cache busting `?v=N` incrementado nos 4 iframes
- [ ] Testar abertura no browser antes da reunião

### Geral
- [ ] Períodos normalizados com mesmos dias da semana entre meses
- [ ] Câmbio do dia registrado
- [ ] Commit antes da entrega

---

## 12. Referências

- **Queries PowerBI detalhadas**: `Projects/BetWarrior/BI/pbi-overview-bira.md`
- **Conexão PowerBI** (tokens, IDs, fluxo auth): memória `project_powerbi_connection.md`
- **Design System**: tokens no `CLAUDE.md` (raiz do projeto)
- **Agentes**: `Projects/BetWarrior/Agentes/agents-registry.md`
- **Modelo HTML aprovado (atual)**: `Semanais/WPR/wpr-jun-01-10-slide*.html` + `WPR_Brasil_Jun01-10_2026.html`

---

## 13. Kit de produção travado (a partir de Jun/2026)

> Reescrito após uma entrega desgastante (Darwin perdeu ~3h ajustando layout). **Regra de ouro: copiar o deck aprovado, trocar só o dado, nunca redesenhar.** Alinhar a estrutura ANTES de construir. Dado faltando = levantar a mão, não improvisar. (memória `feedback_wpr_process`)

### 13.1 Estrutura travada do P1 (4 painéis, não inventar)
1. **FTD vs Meta** (topo esq.) — barras Realizado (laranja) vs Meta (cinza) por mês a partir de Abr, % de atingimento em cima, meta cheia do mês (número só) abaixo do nome. Janela 01–10, meta proporcional.
2. **Depósito Médio por FTD** (topo dir.) — valor do 1º depósito (`AVERAGE(FactFirstDeposit[payment_amount])`), Abr em diante.
3. **Funil de Ativação** — Sessões(GA4 BR) → Registros(1º step: PENDING_CONFIRMATION, `DISTINCTCOUNT(username)`) → Pronto p/Dep(KYC READY_FOR_DEPOSIT) → FTD, com Δ vs mês anterior em ≥12px.
4. **Tabela Métricas de Negócio + Base Ativa** — meses (Jan→atual) + 3 linhas de análise: **Δ vs Mai** (MoM), **Meta** (valores, fonte normal), **vs Meta** (atingimento). Base Ativa colada no rodapé (`margin-top:auto`).

Gráficos de topo = **SVGs gêmeos** (mesmo viewBox `0 0 900 360`, fonte 17px) para fonte/escala consistentes.

### 13.2 Regra de cor (única)
Cor **só nas linhas comparativas** (Δ vs Mai, vs Meta): verde = acima, vermelho = abaixo. Meses = dado neutro; o mês atual se distingue só pelo fundo (`.cw`). Nunca negrito/cor "decorativo" nos meses.

### 13.3 Linhas de análise
- **Δ vs Mai** = variação % MoM (taxas em p.p.).
- **vs Meta** = atingimento: **absolutos em % (realizado/meta)**, **taxas em p.p. (realizado − meta)**.
- Atingimento = realizado ÷ (meta_mês × dias_decorridos / dias_do_mês). FullReg meta = FTD meta ÷ CR alvo. Fecha o funil: ating.FTD = ating.FullReg × ating.CR.

### 13.4 Fontes de META
> **Fonte única de meta (travado 18/06): Forecast Dada** `1UtdEyu8MhpfADMF7TOUDj2SeSaJcf6gR_yXxThTUnno`, aba **"Simulator - New (Cambio Margenes)"**. Col B=Abr, C=Mai, D=Jun, E=Jul. (A planilha Distribuição por Canal **não** é mais a fonte de meta de FTD.)

| Métrica | Linha (Forecast Dada) | Observação |
|---|---|---|
| FTD (total) | **linha 8 + linha 9** (FTDs + FTDs Afiliados) | Jun = D8+D9 = 6.343+1.000 = 7.343 |
| GGR R$ | linha **44** | distribuir pela curva |
| NGR R$ | linha **47** | distribuir pela curva |
| Margem Sports / Casino | linha **42 / 43** | **flat**, não distribui |
| Mix Sports % | linha **41** | p/ margem blended = mix·SB + (1−mix)·CS |
| Registros (1º step) meta | derivada | FTD meta ÷ **CR alvo** |
| CR alvo | **CR realizado YTD 2026** (registros 1º step → FTD) | **14,27%** (14.447 FTD / 101.226 registros, 01/01–17/06). Recalibrar a cada ciclo com o acumulado do ano. O 23% antigo era de registro completo, morreu. |

> O forecast de receita separa `FTDs` (sem afiliados) de `FTDs Afiliados` — somar as duas para o total (≈ linha 14 da distribuição). **Nunca citar a fonte do forecast no report entregue.**

### 13.5 Passo a passo (semana que vem)
1. `python3 Semanais/WPR/wpr_pull.py <mes> 1 10` → todos os números do P1 (tabela, funil, cards, depósito médio) com NGR já correto.
2. GA4 sessões (No Lock do funil): MCP `google-analytics run_report` metric=`sessions` dim=`country`, filtrar Brazil, mês atual e anterior.
3. Meta: ler as duas planilhas (13.4) e calcular atingimento.
4. Copiar `wpr-jun-01-10-slide*.html`, renomear para o período, **trocar só os números** (SVGs: regenerar com o mesmo gerador; tabela: trocar células).
5. Master: trocar período da capa + `?v=N` dos iframes.
6. PDF: Chrome headless `--screenshot` por slide + PIL.
7. **Travessão**: `grep -c "—"` em cada arquivo = 0 (memória `feedback_sem_travessao`).
8. Token PowerBI expira ~1h: o script renova sozinho; se o refresh falhar, refazer Device Code Flow (memória `feedback_powerbi_token_renewal`).

### 13.6 Chrome de apresentação (master)
Scroll-snap tela cheia, dots à direita (chip escuro), lock de 800ms anti double-scroll, teclado (setas/PageUp-Down/espaço), iframes 1920×1080 escalados por `min(vw/1920, vh/1080)`. Páginas claras dentro (não escurecer o conteúdo, prejudica leitura).

## 14. Aprendizados Jun 01-24

### 14.1 P2 , Atribuição: cruzar utm_source + medium (NUNCA só medium)
Olhar só `utm_medium_signup` joga metade no "sem atribuição" (50%), está errado e é frágil na reunião. Correto: **single-assignment cruzando utm_source + utm_medium** (prioridade: influs/streamers no source, depois affiliate medium, depois paid, depois org, resto = Sem UTM). Real: só **19% Sem UTM**. Influs/Streamers (utm_source `streamers` + `influs_br`) é canal escondido e o de MAIOR CR (58%), invisível no medium. Afiliados/streamers/influs vivem todos no MyAffiliates (agrupados, ~564 FTD jun, bate com a Jocelyne).
Query: `SUMMARIZECOLUMNS(DimPlayer[utm_medium_signup], DimPlayer[utm_source], FR, FTD)` + bucketize em Python por prioridade.

### 14.2 P2 , Quadros: Registros · FTD · CR% · Ticket Médio (todos em ordem decrescente)
CR alto não é boa fonte por si só. Trazer **ticket médio** (`SUM(FactFirstDeposit[payment_amount]) ÷ FTD`) revela qualidade: Influs maior CR (58%) mas menor ticket (R$22, volume não valor); Org/Direct R$279 e Afiliados R$182 são os de qualidade; média R$111. Usar ticket (número menor) em vez de valor total, lê melhor e ancora qualidade. O % cinza nos quadros = participação no total, NÃO MoM, sempre rotular.

### 14.3 P1/P4 , Hold de Sports negativo é ESTRUTURAL, não Copa
Nunca atribuir NGR negativo a "favoritos da Copa, evento que normaliza" (overclaim, `feedback_no_causal_overclaim`). Driver real (Trading/BI): Tennis ITF Men/Women + eFootball, ~R$65k GGR negativo/mês há ~30 dias, mais high-rollers idiossincráticos no Casino (bloqueio AML pós-aposta, threshold R$10k). Copa é secundária. O dataset não quebra Sports por liga (`DimGame` Sports = 1 linha "KAMBI_GAME_ID"); o detalhe por liga vive no Kambi/Omega, citar lastreado no Trading/BI.

## 15. P3 — Pipeline de Afiliados (a partir de Jul 01-30/2026)

Estrutura atual do WPR: **P1 + P2 + P3** (o P3 de mídia e o P4 foram aposentados pós-corte). O P3 é a foto do **board CRM Interno do Ruan** (pipeline de prospecção de afiliados), forward-looking. Markup exato e detalhes na memória `project_wpr_p3_pipeline`; deck ref: `Semanais/WPR/Entregas/Jul01-30/wpr-jul-01-30-slide-p3.html`.

**Layout (copiar, não redesenhar):**
- Topo, **largura cheia (painel precisa de `flex:1`)**: "Distribuição por Etapa" = tirinha de chips (Lead→Campanha Ativa), cor fria→quente, nº grande (42px) + Δ vs snapshot anterior.
- Base-esquerda estreita (`flex:0.62`): "Pipeline por Tipo" = **rosca (donut)** conic-gradient, total no centro, Top 5 tipos + "Outros" (cauda + sem tipo).
- Base-direita larga (`flex:1.55`, fontes maiores): "Deals & Integração em Destaque" (cards com termo comercial + próximo passo; featured com selo).

**Fontes:** board Slack List `F0BJ2BVLXBJ`; Δ vs snapshot em `Afiliados/Reports/forecast-ruan/snapshots/`; status de deals/blocks **confirmado nos e-mails** (não só nos comentários do board).

**Regra de dimensão:** cada painel corta por dimensão distinta (o quê=tipo · onde+movimento=etapa · destaques=deals). Nunca dois painéis pela mesma dimensão (funil macro + tirinha = redundante).

**Tom:** construtivo, **sem holofote no negativo** (memória `feedback_report_sem_holofote_negativo`) — número honesto em cor neutra, texto no progresso/destrava.

**Versionamento (revisado 31/07):** os arquivos leves do WPR (HTML, `.md`, `.py`) são versionados **automaticamente** no working folder; só os dados pesados/sensíveis (`*.xlsx`, `*.pdf`, `*.csv`) ficam ignorados. Não precisa mais copiar pra `Entregas/` (a pasta segue existindo pro histórico) — basta commitar.
