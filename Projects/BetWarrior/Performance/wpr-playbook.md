# WPR Playbook — BetWarrior Brasil

> Guia operacional para construção do Weekly Performance Report.
> Consolidado em 28/05/2026 — incorpora aprendizados das entregas Mai 01-21 e Mai 01-27.
> Modelo de referência: arquivos em `Performance/WEEKLY/` prefixo `wpr-mai-01-27-*`.

---

## 1. Periodicidade e Entrega

- Entrega: toda **quarta-feira** (reunião WPR)
- Período: **definido por Darwin na solicitação** — sempre comparar períodos com os mesmos dias da semana (normalização por dia, não por contagem fixa de dias)
- Arquivos individuais em `WEEKLY/`: `wpr-[mes]-[dd]-[dd]-slide.html` (P1–P4)
- Arquivo unificado: `WPR_Brasil_[Mês][DD-DD]_[YYYY].html` — capa + P1 + P2 + P3 + P4 empilhados, escalagem automática via JS
- Fonte de mídia paga (P3): solicitar PACING-PERFO ao Diego com antecedência

---

## 2. Normalização de Períodos

**Regra**: âncora na 1ª sexta-feira do mês. Janela de dias definida por Darwin na solicitação.

**Princípio de comparação**: sempre comparar meses usando janelas com os mesmos dias da semana — não compara Jan 01-31 vs Fev 01-28. Compara Jan 02-28 (sex a dom) vs Fev 06-04/mar (sex a dom), mantendo a distribuição de dias úteis equivalente.

| Mês | Âncora (1ª Sex) |
|-----|-----------------|
| JAN | 02/01 |
| FEV | 06/02 |
| MAR | 06/03 |
| ABR | 03/04 |
| MAI | 01/05 |
| JUN | 05/06 |
| JUL | 03/07 |
| AGO | 07/08 |
| SET | 04/09 |
| OUT | 02/10 |
| NOV | 06/11 |
| DEZ | 04/12 |

**Referência de pacing**: dias transcorridos / dias totais do mês (ex: 27/31 = 87,1%).

---

## 3. Fontes de Dados

| Dado | Fonte | Campo / Observação |
|------|-------|--------------------|
| Sessões | GA4 | Filtro: país=BR |
| FullReg | PowerBI — FactFullRegistration | Ver regra locked_status abaixo |
| FTDs | PowerBI — FactFirstDeposit | Ver regra locked_status abaixo |
| GGR / NGR / GB | PowerBI — FactAGGAccountTransaction | Fórmulas na seção 10 |
| Funil No Lock | PowerBI — DimPlayer[locked_status]="NOT_LOCKED" | Não expor o filtro nas legendas |
| Funil Pronto p/Dep | PowerBI — DimPlayer[locked_status]="READY_FOR_DEPOSIT" | |
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

### 5.1 Funil de Ativação (SVG trapézio)

**4 steps obrigatórios:**
```
Sessões → No Lock → Pronto p/ Dep → FTD
```

| Step | Fonte | Legenda |
|------|-------|---------|
| Sessões | GA4 | "GA4" |
| No Lock | PowerBI DimPlayer[locked_status]="NOT_LOCKED" | "PowerBI" |
| Pronto p/ Dep | PowerBI DimPlayer[locked_status]="READY_FOR_DEPOSIT" | "KYC PASS" |
| FTD | PowerBI FactFirstDeposit | "PowerBI" |

**Taxas de conversão em cada interseção** — formato `±X,Xpp vs [Mês anterior]`.

**SVG — especificações obrigatórias**:
- viewBox: `0 0 432 120`
- Números: `y=60`, `dominant-baseline="middle"`, `font-size="13"`, `text-anchor="middle"`
- Centros X: 54 (Sessões), 162 (No Lock), 270 (Pronto p/Dep), 378 (FTD)
- Cores trapézios: `#FF7A50` → `#FF3900` → `#CC2E00` → `#8B1500`

### 5.2 Tabela Métricas de Negócio

**Colunas fixas**: Mês | FullReg | FTDs | CR% | GGR (R$) | NGR (R$) | Marg. | SB | CS

- **CR%** = FTDs / FullReg (sem NOT_LOCKED — isonomia com tabela geral)
- **Marg.** = NGR / Gross Bets
- **GGR/NGR**: em R$k
- Linha mês atual: `class="cw"` (fundo #FFF5F2, borda-left laranja)
- Linha delta Δ vs mês anterior: `class="dr"` (fundo #F5F5F5)
- Mês de pico histórico = `★`; mês atual = `▶`

**CSS fontes (não alterar)**:
- `thead th`: 12px | `tbody td`: 13px | `tbody td:first-child`: 12px | `.hi`/`.hi-g`: 14px | `.tnote`: 11px

### 5.3 Cards Base Ativa (4 cards)

| Card | Métrica | Cor delta |
|------|---------|-----------|
| Apostadores Ativos | Únicos com ≥1 GAME_BET no período | vermelho se ↓ |
| Gross Bets / Apostador | GB total / apostadores | verde se ↑ |
| GB — Novos FTDs | GB de players com FTD no período (`customer_new_or_returning = "New Customer"`) | contexto |
| GB — Base Existente | GB de players com FTD antes do período (`customer_new_or_returning = "Returning Customer"`) | verde se ↑ |

**Fonte cards 3 e 4**: `KEEPFILTERS(FILTER(FactAGGAccountTransaction, [account_transaction_type] = "GAME_BET"))` + `KEEPFILTERS(FILTER(DimPlayer, [internal_external_player] = "External"))` agrupado por `[customer_new_or_returning]`.

**CSS cards**: label 10px #AAAAAA; número 26px Archivo Black; delta 12px bold.

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
GGR = ABS(GAME_BET) − (GAME_WIN + CASH_OUT + CORRECTION)        [todas as sub-contas]
NGR = RealGGR − Released Bonus                                  [METODO CORRETO — bate com o dashboard do Bira]
   RealGGR       = ABS(GAME_BET) − (GAME_WIN+CASH_OUT+CORRECTION)  filtrado por dim_sub_account_key = "AMOUNT_REAL"
   Released Bonus = SUM(BONUS_REL) filtrado por dim_sub_account_key = "AMOUNT_RELEASED_BONUS"
Gross Bets = ABS(SUM(FactAGGAccountTransaction[account_transaction_amount]))
             WHERE account_transaction_type = "GAME_BET"
Gross Wins = SUM WHERE type IN {"GAME_WIN", "CASH_OUT", "CORRECTION"}
Margem = GGR / Gross Bets    (SB/CS = GGR do produto / GB do produto, via DimGame[game_platform_name])
```

> **NGR — NUNCA usar a fórmula simplificada `GGR − (CRE_BONUS+PRODUC_BON+MAN_BONUS)`.** Ela diverge do dashboard do Bira (deu 29k vs 35k em Jun/2026). O método correto é por `dim_sub_account_key` acima. O script `WEEKLY/wpr_pull.py` já faz isso.

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
- **Modelo HTML aprovado (atual)**: `WEEKLY/wpr-jun-01-10-slide*.html` + `WPR_Brasil_Jun01-10_2026.html`

---

## 13. Kit de produção travado (a partir de Jun/2026)

> Reescrito após uma entrega desgastante (Darwin perdeu ~3h ajustando layout). **Regra de ouro: copiar o deck aprovado, trocar só o dado, nunca redesenhar.** Alinhar a estrutura ANTES de construir. Dado faltando = levantar a mão, não improvisar. (memória `feedback_wpr_process`)

### 13.1 Estrutura travada do P1 (4 painéis, não inventar)
1. **FTD vs Meta** (topo esq.) — barras Realizado (laranja) vs Meta (cinza) por mês a partir de Abr, % de atingimento em cima, meta cheia do mês (número só) abaixo do nome. Janela 01–10, meta proporcional.
2. **Depósito Médio por FTD** (topo dir.) — valor do 1º depósito (`AVERAGE(FactFirstDeposit[payment_amount])`), Abr em diante.
3. **Funil de Ativação** — Sessões(GA4) → No Lock(FRNL NOT_LOCKED) → Pronto p/Dep(KYC READY_FOR_DEPOSIT) → FTD, com Δ vs mês anterior em ≥12px.
4. **Tabela Métricas de Negócio + Base Ativa** — meses (Jan→atual) + 3 linhas de análise: **Δ vs Mai** (MoM), **Meta** (valores, fonte normal), **vs Meta** (atingimento). Base Ativa colada no rodapé (`margin-top:auto`).

Gráficos de topo = **SVGs gêmeos** (mesmo viewBox `0 0 900 360`, fonte 17px) para fonte/escala consistentes.

### 13.2 Regra de cor (única)
Cor **só nas linhas comparativas** (Δ vs Mai, vs Meta): verde = acima, vermelho = abaixo. Meses = dado neutro; o mês atual se distingue só pelo fundo (`.cw`). Nunca negrito/cor "decorativo" nos meses.

### 13.3 Linhas de análise
- **Δ vs Mai** = variação % MoM (taxas em p.p.).
- **vs Meta** = atingimento: **absolutos em % (realizado/meta)**, **taxas em p.p. (realizado − meta)**.
- Atingimento = realizado ÷ (meta_mês × dias_decorridos / dias_do_mês). FullReg meta = FTD meta ÷ CR alvo. Fecha o funil: ating.FTD = ating.FullReg × ating.CR.

### 13.4 Fontes de META
| Métrica | Fonte | Onde |
|---|---|---|
| FTD (total, c/ contingência) | planilha Distribuição por Canal | `1Rc_ckovbxUUj3M0XBXFx6JHXqGF1q06VQYG0Dur7PHg` aba `Distribuição`, **linha 14 TOTAL** (col Abr=F, Mai=I, Jun=L...) |
| GGR / NGR / Margens | forecast de receita interno | `1UtdEyu8MhpfADMF7TOUDj2SeSaJcf6gR_yXxThTUnno`, linhas **44 (GGR R$)**, **47 (NGR R$)**, **42 (Margem Sports)**, **43 (Margem Casino)**; col B=Abr, C=Mai, D=Jun |
| Registros (FullReg) | derivada | FTD meta ÷ **CR alvo** |
| CR alvo | benchmark iGaming BR 20–30% | **25%** (default) |

> O forecast de receita separa `FTDs` (sem afiliados) de `FTDs Afiliados` — somar as duas para o total (≈ linha 14 da distribuição). **Nunca citar a fonte do forecast no report entregue.**

### 13.5 Passo a passo (semana que vem)
1. `python3 WEEKLY/wpr_pull.py <mes> 1 10` → todos os números do P1 (tabela, funil, cards, depósito médio) com NGR já correto.
2. GA4 sessões (No Lock do funil): MCP `google-analytics run_report` metric=`sessions` dim=`country`, filtrar Brazil, mês atual e anterior.
3. Meta: ler as duas planilhas (13.4) e calcular atingimento.
4. Copiar `wpr-jun-01-10-slide*.html`, renomear para o período, **trocar só os números** (SVGs: regenerar com o mesmo gerador; tabela: trocar células).
5. Master: trocar período da capa + `?v=N` dos iframes.
6. PDF: Chrome headless `--screenshot` por slide + PIL.
7. **Travessão**: `grep -c "—"` em cada arquivo = 0 (memória `feedback_sem_travessao`).
8. Token PowerBI expira ~1h: o script renova sozinho; se o refresh falhar, refazer Device Code Flow (memória `feedback_powerbi_token_renewal`).

### 13.6 Chrome de apresentação (master)
Scroll-snap tela cheia, dots à direita (chip escuro), lock de 800ms anti double-scroll, teclado (setas/PageUp-Down/espaço), iframes 1920×1080 escalados por `min(vw/1920, vh/1080)`. Páginas claras dentro (não escurecer o conteúdo, prejudica leitura).
