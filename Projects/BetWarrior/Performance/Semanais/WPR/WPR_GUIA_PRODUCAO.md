# WPR BetWarrior Brasil — Guia de Produção

> Referência técnica para montagem do próximo WPR. Atualizado em 28/05/2026.
> Modelo de referência: WPR Mai 01–27/2026 (arquivos: WPR_Brasil_Mai01-27_2026.html + slides p1–p4).

---

## Arquitetura de Arquivos

```
WPR_Brasil_[MES]-[DD]-[DD]_[ANO].html   ← master (capa + iframes)
wpr-[mes]-[dd]-[dd]-slide.html          ← P1 Métricas de Negócio
wpr-[mes]-[dd]-[dd]-slide-p2.html       ← P2 Aquisição por Canal
wpr-[mes]-[dd]-[dd]-slide-p3.html       ← P3 Performance de Mídia
wpr-[mes]-[dd]-[dd]-slide-p4.html       ← P4 Próximos Passos
```

**Master HTML**: capa escura (dark) + separadores + iframes escalados via JS.
- Base dos iframes: `width: 1920px; height: 1080px`
- Escala aplicada via `scaleSlides()`: `scale = wrap.clientWidth / 1920`
- Cache busting obrigatório: `?v=N` nos srcs dos iframes a cada atualização
- Aspect ratio da capa: `16/9` (não alterar)

---

## Normalização de Período (regra âncora)

| Mês | Período normalizado 27d | Âncora |
|-----|------------------------|--------|
| Jan | 02–28/01 | 1ª Sex (02/01) |
| Fev | 06/02–04/03 | 1ª Sex (06/02) |
| Mar | 06/03–01/04 | 1ª Sex (06/03) |
| Abr | 03–29/04 | 1ª Sex (03/04) |
| Mai | 01–27/05 | 1ª Sex (01/05) |

**Regra**: sempre 27 dias corridos a partir da 1ª sexta-feira do mês.
**Exceção fechamento**: quando o mês fecha, recalcular com dias totais reais (ex: Abr = 27 dias até 29/04).
**Referência de pacing**: dias transcorridos / dias totais do mês (ex: 27/31 = 87,1%).

---

## CAPA (Master)

**Elementos presentes:**
- Logo BetWarrior + barra laranja #FF3900
- Título "WEEKLY PERFORMANCE REPORT" (centralizado, Archivo Black)
- Período: "[DD]–[DD] / [MES] · [ANO]"
- Detalhe: "SB + Casino · BRL · Gerado [DD/MM]"
- Painel direito vermelho #FF3900 com watermark "WPR" semitransparente
- Footer: "BETWARRIOR BRASIL · CONFIDENTIAL | WPR · CAPA · [PERÍODO] | [DATA]"

**Elementos removidos (não colocar de volta):**
- `.cv-hdr-label` "WEEKLY PERFORMANCE REPORT" no header da capa
- `.cv-hdr-meta` com data/meta/reunião no canto direito do header

---

## P1 — Métricas de Negócio

### Cabeçalho
- Título: "WEEKLY PERFORMANCE REPORT"
- Subtítulo (headline editorial): destaca o achado principal do mês
- Meta: "01–27 / [MES ANO] | SB + Casino · BRL | Gerado [DD/MM]"

### Painel: FTDs MTD 27D Normalizado por Canal (barras verticais)

**Fonte**: `FactFirstDeposit` · PowerBI  
**Query**: SUMMARIZECOLUMNS filtrando por período normalizado, agrupando por utm_medium_signup

**Dados a atualizar**: total por mês (número acima da barra) + alturas das barras proporcional ao maior valor histórico  
**Segmentos dentro da barra** (coloração):
- Vermelho `#FF3900` = Affiliates (utm_medium_signup = 'affiliate')
- Âmbar `#F59E0B` = Paid Social (revisar nomenclatura — ver pendências)
- Cinza `#C8C8C8` = Demais canais

**ATENÇÃO**: os percentuais visuais (%) dentro de cada barra são estimativas manuais baseadas na proporção do total. No próximo WPR, calcular os valores reais por canal e converter em altura (px) proporcionalmente.

**Escala de alturas**: o mês com mais FTDs = 100px de altura de barra. Os demais são proporcionais.

### Painel: Depósito Médio por FTD (barras verticais)

**Fonte**: PowerBI (1º depósito + redepositos no período de entrada do jogador)  
**Âncora**: 1ª sexta-feira do mês

**Dados a atualizar**: R$ médio por mês + alturas proporcionais ao maior valor histórico  
**Nota de rodapé**: breakdown por canal (Org./Direct, Others, Paid Media, Affiliates)

**PENDÊNCIA CRÍTICA**: A nota ainda exibe "Paid Social R$119" — no próximo WPR trocar para "Others" (após merge de social_paid → Others feito na sessão de 28/05).

### Painel: Funil de Ativação (SVG trapézio)

**Fontes por etapa**:
| Etapa | Fonte | Campo |
|-------|-------|-------|
| Sessões | GA4 | sessions, filtro Brasil |
| No Lock | PowerBI | FullReg com locked_status = 'NOT_LOCKED' + internal_external_player = 'External' |
| Pronto p/ Dep | PowerBI | locked_status = 'READY_FOR_DEPOSIT' |
| FTD | PowerBI | FactFirstDeposit |

**SVG — especificações de layout**:
- viewBox: `0 0 432 120`
- Números dentro do trapézio: `y=60`, `dominant-baseline="middle"`, `font-size="13"`, `text-anchor="middle"`
- Centros X: Sessões=54, No Lock=162, Pronto p/Dep=270, FTD=378
- Cores dos trapézios: #FF7A50, #FF3900, #CC2E00, #8B1500

**Conversões (abaixo do SVG)**:
- CR1 = No Lock / Sessões → posição left:25%
- CR2 = Pronto p/Dep / No Lock → posição left:50%
- CR3 = FTD / Pronto p/Dep → posição left:75%
- WoW: comparar com mesmo período do mês anterior

### Painel: Tabela Métricas de Negócio

**Fonte**: PowerBI (SB + Casino · BRL)

| Coluna | Fonte | Observação |
|--------|-------|------------|
| FullReg | PowerBI · DimPlayer[locked_status]='NOT_LOCKED' | Externos apenas |
| FTDs | PowerBI · FactFirstDeposit | |
| CR% | FTDs / FullReg NOT_LOCKED | Calculado |
| GGR (R$) | PowerBI | Em R$k |
| NGR (R$) | PowerBI | Em R$k |
| Marg. | NGR / GB | Calculado |
| SB% | PowerBI · margem Sports Betting | |
| CS% | PowerBI · margem Casino | |

**CSS fontes (não alterar)**:
- `thead th`: 12px
- `tbody td`: 13px
- `tbody td:first-child`: 12px
- `.hi` / `.hi-g`: 14px
- `.tnote`: 11px

**Linhas especiais**:
- `class="cw"`: mês atual (fundo #FFF5F2, borda-left laranja)
- `class="dr"`: linha delta Δ vs mês anterior (fundo #F5F5F5)
- Mês de pico histórico = `★`; mês atual = `▶`

### Cards Base Ativa (3 cards horizontais)

**Fonte**: PowerBI

| Card | Métrica | Comparação |
|------|---------|------------|
| Apostadores Ativos | Únicos com ≥1 aposta no período | vs mês anterior |
| Gross Bets / Apostador | GB total / apostadores ativos | vs mês anterior |
| Gross Bets Total | Soma GB do período | vs mês anterior |

**CSS fontes dos cards**:
- Label: 10px, #AAAAAA, uppercase, letter-spacing: 1.5px
- Número principal: Archivo Black, 26px
- Delta: 12px, font-weight: 600

---

## P2 — Aquisição por Canal

### Mapeamento de Canais (DimPlayer[utm_medium_signup])

| Canal no relatório | Valores utm_medium_signup |
|--------------------|--------------------------|
| Paid Media | `paid_media` (Meta, TikTok, X — campanhas pagas diretas) |
| Org. / Direct | `(none)`, `organic`, `(direct)` |
| Affiliates | `affiliate` |
| Others | `social_paid`, `email`, demais não mapeados |

**IMPORTANTE**: `social_paid` = publisher/comparador (ex: betdasorte) — problema de atribuição confirmado. Manter em Others até resolução técnica.

**Filtros obrigatórios nas queries**:
- `DimPlayer[internal_external_player] = "External"`
- `DimPlayer[locked_status] = "NOT_LOCKED"` (para FullReg)

### Painel: Full Registration Not Locked

**Fonte**: PowerBI — `FactFullRegistration` + `DimPlayer`  
**Período**: MTD do mês atual  
**Barras**: % relativo ao canal com maior valor (100% = referência)  
**Rodapé**: CR geral = Total FTDs / Total FullReg NOT_LOCKED; Total FullReg absoluto

### Painel: FTDs

**Fonte**: PowerBI — `FactFirstDeposit` + `DimPlayer[utm_medium_signup]`  
**NOTA**: Pode haver discrepância de ±15 FTDs vs P1 tabela por diferença de timing de query. Documentar mas não corrigir — é aceitável.

### Painel: CR% por Canal

**Calculado**: FTDs canal / FullReg NOT_LOCKED canal  
**Ordenação**: decrescente (maior CR no topo)  
**Visual**:
- Canal líder: barra laranja `#FF3900` `hbar-fill.hi`
- Demais acima da média: barra preta `#1C1C1E`
- Abaixo da média: barra cinza `#AAAAAA` com valor em `#AAAAAA`

### Painel: Gross Bets Evolução por Canal (Mar-Abr-Mai)

**Fonte**: PowerBI — GB acumulado 27d normalizados, agrupado por utm_medium_signup  
**Períodos**: 3 meses → Mar (cinza claro #DDDDDD), Abr (cinza médio #999999), Mai (laranja #FF3900)  
**Referência 100%**: maior valor individual entre todos os canais/meses  
**Others**: GB de social_paid + demais somados — manter rótulo "Others"  
**Rodapé**: totais consolidados Mar / Abr / Mai

---

## P3 — Performance de Mídia

### G1: Budget vs FTDs — CPA por Plataforma

**Fonte**: Planilha Diego — PACING-PERFO  
**Câmbio**: fixar câmbio médio do período (Mai/26 = R$5,56 — confirmar com Diego a cada ciclo)  
**Plataformas com CPA atribuível**: Google, Meta, TikTok  
**Plataformas sem atribuição confiável** (mostrar em cinza, FTDs com †): X, Taboola

**Dados necessários por plataforma**:
- Investimento (US$)
- % do budget total executado
- FTDs absolutos
- % dos FTDs totais de mídia paga
- CPA (R$) = (investimento US$ × câmbio) / FTDs

**SVG G1 — mapeamento de posições** (viewBox 0 0 600 320, chartarea x=46..554, y=16..225):
- Escala barras: 1% = 2,09px de altura. Base = y=225.
- Barra budget (cinza): x=68+(canal*100), w=24
- Barra FTD (laranja): x=96+(canal*100), w=24
- Dot CPA (linha preta): x=108+(canal*100)
- Escala CPA: R$1.500 = y=16 (topo). Fórmula: y = 225 − (CPA × (209/1500))
- Linha avg CPA: y calculado pela mesma escala

**Posições x por plataforma**:
| Plataforma | Budget x | FTD x | Dot x | Label x |
|------------|----------|-------|-------|---------|
| Google | 68 | 96 | 108 | 96 |
| Meta | 168 | 196 | 208 | 196 |
| TikTok | 268 | 296 | 308 | 296 |
| X | 368 | 396 | — | 396 |
| Taboola | 468 | 496 | — | 496 |

### G2: Gross Bets + R$/Apostador por Canal

**Fonte**: PowerBI — utm_medium_signup, 27 dias normalizados  
**Canais**: Paid Media, Org/Direct, Affiliates, Others (4 canais, distribuídos uniformemente)

**SVG G2 — posições (viewBox 0 0 600 320, chartarea x=46..554)**:
| Canal | Centro X | Gray rect x | Red rect x | Dot x |
|-------|----------|-------------|------------|-------|
| Paid Media | 110 | 84 | 112 | 124 |
| Org/Direct | 237 | 211 | 239 | 251 |
| Affiliates | 364 | 338 | 366 | 378 |
| Others | 491 | 465 | 493 | 505 |

**Polyline**: conecta os dots (124,y1 251,y2 378,y3 505,y4)  
**Escala y das barras**: proporcional ao maior valor. Base = y=225.  
**Linha avg R$/apostador**: calcular y pela mesma escala de CPA.

**ATENÇÃO**: Others com poucos apostadores (201) tem R$/apostador alta variância — considerar nota de rodapé.

### Painel PACING

**Fonte**: Planilha Diego — PACING-PERFO (atualizado próximo ao fechamento do período)  
**Referência fixa**: % dias transcorridos / dias do mês (ex: 27/31 = 87,1%)

**Por plataforma**:
- % orçamento executado vs total mensal → delta vs referência (em pp)
- % FTDs realizados vs meta mensal → delta vs referência (em pp)
- Detalhes: investimento US$, FTDs absolutos, CPA R$

**Coloração deltas**:
- Δ entre −1pp e +5pp vs referência: `#F59E0B` (âmbar)
- Δ abaixo de −5pp vs referência: `#EF4444` (vermelho)
- Δ acima de +5pp vs referência: `#22C55E` (verde)

**CSS big numbers pacing**: Archivo Black, 28px

---

## P4 — Próximos Passos

**Fonte**: editorial — preencher com base na reunião WPR  
**Ordem**: sempre cronológica, mais próximo primeiro  
**Datas sem prazo fixo**: usar `date-gray` (fundo #F0F0F0, texto #777)  
**Datas com prazo definido**: usar `date-dark` (fundo #111, texto #FFF)

**CSS fontes (após ajuste 28/05, NÃO reverter)**:
- `.action-num`: 25px
- `.action-title`: 15px
- `.action-desc`: 13.5px
- `.action-date`: 13px
- `.action-owner`: 12.5px

---

## Checklist de Coleta — Próximo WPR

### PowerBI (queries DAX — SUMMARIZECOLUMNS)

- [ ] Tabela principal: GGR, NGR, GB, Marg SB, Marg CS por mês (normalizado 27d)
- [ ] FullReg NOT_LOCKED: total e por utm_medium_signup (External only)
- [ ] FTDs: total e por utm_medium_signup
- [ ] CR% por canal: calculado a partir dos dois acima
- [ ] Base Ativa: apostadores únicos com ≥1 aposta no período
- [ ] GB por canal (utm_medium_signup): para G2 e evolução 3 meses
- [ ] Apostadores ativos por canal: para G2
- [ ] Funil KYC: NOT_LOCKED total e READY_FOR_DEPOSIT total
- [ ] Depósito médio por canal: soma depósitos / FTDs por utm_medium_signup

**Filtros obrigatórios em todas as queries**:
- `DimPlayer[internal_external_player] = "External"`
- Período: âncora 1ª sexta do mês, 27 dias corridos

### GA4

- [ ] Sessões totais Brasil no período normalizado (para numerador do funil)

### Planilha Diego — PACING-PERFO

- [ ] Budget executado por plataforma (Google, Meta, TikTok, X, Taboola, Kwai, Programática) em US$
- [ ] % budget executado vs orçamento mensal por plataforma
- [ ] FTDs por plataforma (atribuição plataforma)
- [ ] % FTDs vs meta mensal por plataforma
- [ ] CPA por plataforma (US$ e R$)
- [ ] Câmbio médio do período
- [ ] Meta mensal de FTDs por plataforma (para calcular %)

### Planilha Perfo — BW BR - CPL x Mes | Interno Perfo 2026

- [ ] Metas mensais por canal (Perfo, Patrocínios, Orgânico, etc.) — para pacing geral
- [ ] Validação cruzada de FTDs totais

---

## Pendências do Ciclo Atual (Mai → Jun)

1. **Nota dep. médio em P1**: substituir "Paid Social R$119" por "Others R$119"
2. **Barras FTD (P1)**: segmentos dentro de cada barra são estimativas — calcular % reais por canal via PowerBI e aplicar como alturas no próximo ciclo
3. **Others R$/apostador (P3 G2)**: R$1.846 com apenas 201 apostadores — alta variância. Adicionar nota de rodapé alertando para baixo volume.
4. **Discrepância de FTDs P1 (2.679) vs P2 (2.693)**: documentar como tolerável (diferença de snapshot). Avaliar se padronizar timestamp da query.
5. **KYC / READY_FOR_DEPOSIT**: confirmar se a query correta para "Pronto p/ Dep" é `locked_status = 'READY_FOR_DEPOSIT'` no PowerBI vs evento de conversão no GA4.

---

## Tokens de Design (nunca alterar)

| Elemento | Valor |
|----------|-------|
| Fundo páginas | `#F2F2F2` |
| Fundo painéis | `#FFFFFF` |
| Borda painéis | `#E0E0E0` |
| Accent / Header linha | `#FF3900` |
| Texto principal | `#111111` |
| Texto muted | `#AAAAAA` |
| Sucesso | `#22C55E` |
| Alerta | `#F59E0B` |
| Erro / negativo | `#EF4444` |
| Fonte título | Archivo Black |
| Fonte corpo | Archivo Regular |
| Header height | 80px |
| Footer height | 28-30px |
| Body padding | 14px 20px |
| Gap entre painéis | 12px |

---

## Referências de Arquivos Externos

| Recurso | ID / Localização |
|---------|-----------------|
| Planilha Diego (PACING-PERFO) | Google Sheets — acessar via Drive do Diego |
| Planilha Perfo (CPL x Mes) | Google Sheets — BW BR - CPL x Mes l Interno Perfo 2026 |
| PowerBI BetWarrior | Workspace configurado em agent-powerbi — token via refresh_token |
| GA4 Brasil | Property configurada em agent-ga4 |
