# WPR Playbook — BetWarrior Brasil

> Guia operacional para construção do Weekly Performance Report.
> Atualizado após sessão de revisão em 22/05/2026.
> Objetivo: reproduzir o relatório sem pontos de discussão recorrentes.
> Última atualização: 22/05/2026 — adicionadas P4, capa e HTML unificado.

---

## 1. Periodicidade e Entrega

- Entrega: toda **terça-feira**
- Período coberto: MTD normalizado até o domingo anterior
- Arquivos individuais: `weekly-report-slide.html` (P1), `weekly-report-slide-p2.html` (P2), `weekly-report-slide-p3.html` (P3), `weekly-report-slide-p4.html` (P4)
- Arquivo unificado para apresentação: `WPR_Brasil_[Período].html` — capa + P1 + P2 + P3 + P4 empilhados, escalagem automática via JS
- Fonte de mídia paga (P3): solicitar PACING-PERFO.xlsx ao Diego na segunda-feira

---

## 2. Períodos MTD Normalizados

**Regra:** janela de 21 dias com âncora na 1ª sexta-feira do mês.

| Mês | De | Até | dim_date_key |
|-----|----|-----|--------------|
| JAN | 02/01/2026 | 22/01/2026 | 20260102–20260122 |
| FEV | 06/02/2026 | 26/02/2026 | 20260206–20260226 |
| MAR | 06/03/2026 | 26/03/2026 | 20260306–20260326 |
| ABR | 03/04/2026 | 23/04/2026 | 20260403–20260423 |
| MAI | 01/05/2026 | 21/05/2026 | 20260501–20260521 |
| JUN | 05/06/2026 | 25/06/2026 | 20260605–20260625 |
| JUL | 03/07/2026 | 23/07/2026 | 20260703–20260723 |
| AGO | 07/08/2026 | 27/08/2026 | 20260807–20260827 |
| SET | 04/09/2026 | 24/09/2026 | 20260904–20260924 |
| OUT | 02/10/2026 | 22/10/2026 | 20261002–20261022 |
| NOV | 06/11/2026 | 26/11/2026 | 20261106–20261126 |
| DEZ | 04/12/2026 | 24/12/2026 | 20261204–20261224 |

---

## 3. Fontes de Dados

| Dado | Fonte | Observação |
|------|-------|------------|
| Sessões | GA4 | Filtro: país=BR, brand=BWBRA, externo |
| FullReg | PowerBI — FactFullRegistration | Sem filtro locked_status |
| FTDs | PowerBI — FactFirstDeposit | Sem filtro locked_status |
| GGR / NGR / Gross Bets | PowerBI — FactAGGAccountTransaction | Ver fórmulas em pbi-overview-bira.md |
| No Lock (funil) | PowerBI — DimPlayer[locked_status]="NOT_LOCKED" | Snapshot — aproximação |
| Pronto p/Dep (funil) | PowerBI — NOT_LOCKED + KYC_PASS | Snapshot — aproximação |
| Canais | PowerBI — DimPlayer[utm_medium] | Nunca usar utm_source ou ta_affiliate |
| Apostadores / R$/ap | PowerBI — FactAGGAccountTransaction | Por utm_medium |
| Invest / Budget / CPA | PACING-PERFO.xlsx (Diego) | **Valores em USD** → converter |
| Câmbio | Verificar na semana da entrega | Usar câmbio do dia da entrega |

### Filtros obrigatórios em todas as queries PowerBI

```
DimPlayer[internal_external_player] = "External"
DimPlayer[player_country] = "BR"
DimPlayer[brand_name] = "BWBRA"
```

**NUNCA adicionar** `DimPlayer[locked_status] = "NOT_LOCKED"` — exclui players que depositaram mas foram bloqueados depois, causando subcontagem de ~10–15% em FTDs e FullReg.

---

## 4. P1 — Visão Geral

### 4.1 Funil de Ativação

**Sempre 4 steps — nunca menos:**

```
Sessões → No Lock → Pronto p/ Dep → FTD
```

**O que cada step representa:**
- **Sessões**: usuários únicos (GA4)
- **No Lock**: FullReg com DimPlayer[locked_status]="NOT_LOCKED" (snapshot)
- **Pronto p/Dep**: NOT_LOCKED + DimPlayer[player_kyc_status]="PASS" (snapshot)
- **FTD**: FactFirstDeposit (sem filtro locked_status)

**Taxas de conversão** — obrigatório em cada interseção:
- Step 1→2: No Lock / Sessões
- Step 2→3: Pronto p/Dep / No Lock
- Step 3→4: FTD / Pronto p/Dep

**Δ vs mês anterior MTD** — obrigatório em cada taxa:
- Formato: `Δ ±X,Xpp` (pontos percentuais)
- Comparar com mesmo período normalizado do mês anterior

**Implementação técnica:** todos os elementos do funil (labels, polígonos, volumes, taxas, nota) devem estar em um único `<svg>`. Nunca separar em múltiplos elementos HTML — causa desalinhamento inevitável.

### 4.2 Tabela Métricas de Negócio

**Colunas fixas — nunca alterar sem aprovação explícita:**

| Mês | FullReg | FTDs | CR% | GGR | NGR | Marg. | SB | CS |
|-----|---------|------|-----|-----|-----|-------|----|----|

- **CR%** = FTDs / FullReg (sem NOT_LOCKED — isonomia com P2)
- **Marg.** = NGR / Gross Bets (margem geral)
- **SB** = margem NGR do produto Sports Betting
- **CS** = margem NGR do produto Casino
- **GGR** = ABS(GAME_BET) – (GAME_WIN + CASH_OUT + CORRECTION)
- **NGR** = GGR – (CRE_BONUS + PRODUC_BON + MAN_BONUS)

Valores de GGR/NGR negativos aparecem em vermelho `#EF4444`, positivos em verde `#22C55E`.

### 4.3 CRM Block — Base Ativa

Posição: espaço abaixo da tabela Métricas de Negócio.
Propósito: explicar por que GGR/NGR podem subir mesmo com queda em FTDs.

**3 cards obrigatórios, comparativo mai MTD vs abr MTD:**

1. **Apostadores Ativos** — apostadores únicos com GAME_BET no período
2. **Gross Bets / Apostador** — R$/apostador médio (verde se ↑)
3. **% GB Base Existente** — share do GB gerado por jogadores adquiridos ANTES do período atual (verde se ↑)

Fonte: PowerBI — FactAGGAccountTransaction + TREATAS para filtrar base existente.

---

## 5. P2 — Aquisição por Canal

### 5.1 Ordenação — Regra Universal

**Todos os gráficos de P2 devem estar ordenados do maior para o menor valor**, sem exceção. Gráficos com ordenações diferentes entre si causam confusão na leitura cruzada linha a linha.

### 5.2 Gráfico: Full Registration por Canal

- Fonte: PowerBI — FactFullRegistration por DimPlayer[utm_medium]
- **Sem filtro locked_status**
- Título: "Full Registration por Canal" (não "Not Locked")
- Ordenação: maior → menor (por volume de FullReg)

### 5.3 Gráfico: FTDs por Canal

- Fonte: PowerBI — FactFirstDeposit por DimPlayer[utm_medium]
- **Sem filtro locked_status**
- Ordenação: maior → menor

### 5.4 Gráfico: CR% por Canal

**CR% = FTDs / FullReg do mesmo canal — calculado da própria página.**

Antes de publicar: conferir se cada valor do gráfico CR% bate com FTD/FullReg das outras duas tabelas da mesma página. Se não bater, há erro de fonte ou filtro.

- Ordenação: maior → menor (por CR%)
- **Isonomia com P1**: usar mesma definição de CR% (FTD/FullReg sem NOT_LOCKED)

### 5.5 Gráfico: Gross Bets Evolução por Canal

- Evolução de 3 meses: Mar, Abr, Mai (períodos normalizados)
- Mapeamento de canais (DimPlayer[utm_medium]):
  - `paid_media` → Paid Media
  - `affiliate` → Affiliates
  - `social_paid` → Paid Social
  - `(none)` / `direct` / vazio → Org./Direct
  - demais → Others

---

## 6. P3 — Performance de Mídia

### 6.1 Moeda — Regra Crítica

**Todo dado proveniente do PACING-PERFO.xlsx (Diego) está em USD:**
- Invest por plataforma
- Budget total e por plataforma
- CPA por plataforma

**Conversão obrigatória para BRL antes de incluir no relatório.**
Usar câmbio do dia da entrega (obter de qualquer fonte pública confiável).
Registrar o câmbio usado no `ph-note` do painel: ex. "CPA pond. R$912 (câmbio R$5,56)".

### 6.2 G1 — Budget vs FTDs · CPA por Plataforma

- Barras: % Budget (cinza) e % FTDs (laranja) por plataforma
- Linha: CPA em BRL (após conversão)
- Linha tracejada: CPA médio ponderado
- Plataformas sem atribuição de FTDs (X, Taboola): barra de FTDs tracejada/cinza claro
- Fonte: PACING-PERFO.xlsx — acumulado até o período disponível (geralmente 2 semanas)

### 6.3 G2 — Gross Bets por Canal · R$/Apostador

- Barras: % Apostadores (cinza) e % Gross Bets (laranja) por canal utm_medium
- Linha: R$/apostador por canal
- **Legenda obrigatória** abaixo do gráfico explicando que os valores em destaque no eixo = Gross Bets acumulados no período
- **Nunca duplicar** R$/ap no rótulo do eixo se já aparece na linha do gráfico

### 6.4 Pacing

- Referência do período: X dias de 31 = X% do mês
- Por plataforma: % orçamento realizado, % FTDs realizados, Δ vs referência
- CPA convertido para BRL no rodapé de cada coluna

---

## 7. Regras Transversais

### Isonomia entre páginas

| Métrica | Definição única |
|---------|----------------|
| CR% | FTDs / FullReg — **sem** filtro locked_status em todas as páginas |
| FullReg | Sem filtro locked_status em todas as páginas |
| FTDs | Sem filtro locked_status em todas as páginas |
| Períodos | MTD normalizado — mesma janela de 21 dias em P1, P2 e P3 |

### Design e Layout

- **Fontes**: ajustes máximos de ±1px. Nunca alterar sem necessidade clara de legibilidade
- **Cores**: seguir design system CLAUDE.md — laranja `#FF3900`, sucesso `#22C55E`, erro `#EF4444`
- **Tabelas**: linhas zebra `#111111`/`#1A1A1A`, header laranja
- **Ordenação**: sempre do maior para o menor — em todos os gráficos de barras
- **Legendas**: obrigatórias para qualquer valor que não seja auto-explicativo pelo título do painel

### Moeda

- Padrão do relatório: **BRL**
- Dados de plataformas de mídia (Diego): USD → converter antes de incluir
- Dados do PowerBI: BRL (Gross Bets, GGR, NGR já estão em BRL)
- Dados de GA4: sem moeda (sessões, usuários)

---

## 8. P4 — Próximos Passos

Slide de encerramento da reunião WPR. Criado em 22/05/2026.

### Estrutura
- **Arquivo**: `weekly-report-slide-p4.html`
- **Conteúdo**: lista de ações e responsabilidades priorizadas para as próximas semanas
- **Layout**: lista numerada com barra colorida lateral indicando urgência + date pill + owner tag

### Sistema de cores por urgência
| Cor | Classe | Significado |
|-----|--------|-------------|
| Laranja `#FF3900` | `bar-now` / `date-now` | Esta semana |
| Âmbar `#F59E0B` | `bar-near` / `date-near` | Próximas 2 semanas |
| Cinza `#DDDDDD` | `bar-later` / `date-later` | Estrutural / prazo mais longo |

### Regras editoriais
- Máximo de 8 ações por slide — se houver mais, priorizar
- Título: Archivo Black uppercase, 13px
- Descrição: 12px, cor #888, máximo 2 linhas
- Date pill alinhado ao topo do row (não ao centro) — facilita leitura durante apresentação

---

## 9. Capa e HTML Unificado

### Capa (`WPR_Brasil_[Período].html` — seção inicial)
- Design em CSS puro, sem imagem externa
- Fundo escuro `#111`, bloco laranja sólido à direita
- Header e footer idênticos aos outros slides
- Conteúdo: tag WPR, título grande, barra laranja, período e metadata

### HTML Unificado — Arquivo de Apresentação
- **Nomenclatura**: `WPR_Brasil_[MêsDe]-[MêsAté]_[Ano].html`
  - Exemplo: `WPR_Brasil_Mai01-21_2026.html`
- **Estrutura**: Capa → Sep → P1 → Sep → P2 → Sep → P3 → Sep → P4
- **Separador**: 32px escuro com 3 pontos — transição visual entre páginas
- **Escalagem**: JS recalcula `transform: scale(clientWidth/1920)` em cada iframe
  - Cada iframe tem `width: 1920px; height: 1080px; transform-origin: top left`
  - O wrapper recebe `height: 1080 * scale` px
- **Uso**: abrir no browser e apresentar diretamente — qualidade nativa, sem blur

### PDF de alta qualidade (quando necessário)
```python
# Geração via Python + Chrome headless
# @page CSS: size: 1920px 1080px; margin: 0
# Flag: --no-pdf-header-footer --window-size=1920,1080
# Ou: screenshot 3840x2160 → Pillow → PDF @ 192dpi
```
- Pillow PNG→PDF produz arquivo sem gaps e sem margens indesejadas
- Resolução equivalente: 3840×2160 @ 192dpi = 20×11.25 in (16:9 exato)

---

## 10. Checklist Pré-Entrega

### P1

- [ ] Funil tem exatamente 4 steps: Sessões → No Lock → Pronto p/Dep → FTD
- [ ] Taxas de conversão em cada interseção do funil
- [ ] Δ vs mês anterior MTD em cada taxa de conversão
- [ ] Labels do funil alinhados com os steps (em SVG único)
- [ ] Tabela tem colunas: Mês | FullReg | FTDs | CR% | GGR | NGR | Marg. | SB | CS
- [ ] CR% = FTDs/FullReg (conferir manualmente: CR_total = total_FTDs/total_FullReg)
- [ ] CRM Block com 3 indicadores: Apostadores Ativos, GB/Apostador, % GB Base Existente
- [ ] Comparativos CRM: mai MTD vs abr MTD

### P2

- [ ] FullReg sem NOT_LOCKED — título "Full Registration por Canal"
- [ ] FTDs sem NOT_LOCKED
- [ ] CR% bate com FTD/FullReg da mesma página (conferir canal por canal)
- [ ] Todos os gráficos ordenados do maior para o menor
- [ ] Todos na mesma ordem (mesmos canais, mesma sequência)

### P3

- [ ] Invest/Budget/CPA do Diego convertidos de USD para BRL com câmbio do dia
- [ ] Câmbio registrado no ph-note do painel G1
- [ ] G2 tem legenda/nota explicando que valores em destaque = Gross Bets
- [ ] R$/apostador não duplicado: só na linha, não no rótulo do eixo

### P4

- [ ] Ações revisadas e atualizadas para o período corrente
- [ ] Date pills e urgência (cores) conferidos
- [ ] Owner tags preenchidos

### HTML Unificado

- [ ] Capa com período correto (tag + cv-period)
- [ ] Data da reunião atualizada no cv-hdr-meta e cv-ftr
- [ ] Todos os 4 iframes apontando para os arquivos corretos
- [ ] Testar abertura no browser antes da reunião

### Geral

- [ ] Todas as métricas usam período MTD normalizado consistente
- [ ] Valores conferidos contra fonte (PowerBI / GA4 / Diego)
- [ ] Commit + push antes da entrega

---

## 11. Referências

- **Queries PowerBI completas**: `Projects/BetWarrior/BI/pbi-overview-bira.md`
- **Design System**: tokens no `CLAUDE.md` (raiz do projeto)
- **Valores de referência Mai 2026**: seção final do `pbi-overview-bira.md`
- **Agentes e automações**: `Projects/BetWarrior/Agentes/agents-registry.md`
