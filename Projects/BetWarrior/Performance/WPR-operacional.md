# WPR Brasil — Guia Operacional

> Documento de referência para atualização semanal do Weekly Performance Report.  
> Versão validada em 13/05/2026.

---

## 1. Visão geral

Relatório HTML de 3 páginas, gerado semanalmente com semanas normalizadas (âncora = 1ª sexta-feira do mês).

| Arquivo | Conteúdo |
|---|---|
| `weekly-report-slide.html` | Página 1 + 2 — FTD WoW e Métricas de Negócio |
| `weekly-report-slide-p3.html` | Página 3 — Performance de Mídia |

**Nomenclatura de entrega:** `WPR_Brasil_[Mês][DD-DD]_YYYY.html`  
Exemplo: `WPR_Brasil_Mai01-07_2026.html`

---

## 2. Metodologia de semanas normalizadas

**Âncora:** dia da semana do dia 1 do mês atual.  
Maio começa numa sexta → âncora = sexta.  
Janela = 7 dias a partir da primeira ocorrência desse dia no mês.

| Mês | Janela |
|---|---|
| Janeiro | 02–08/01 |
| Fevereiro | 06–12/02 |
| Março | 06–12/03 |
| Abril | 03–09/04 |
| Maio | 01–07/05 |
| Junho | (calcular: 1/jun = segunda → 1ª segunda = 01 → janela 01–07/06) |

---

## 3. Página 1+2 — FTD WoW + Métricas de Negócio

### 3.1 Layout

```
HEADER  — headline narrativo + meta (período · produto · data)

ROW 1 (flex:1)
  [FTD WoW por Canal — barras empilhadas]  |  [Dep/FTD por Semana — barras simples]

ROW 2 (flex:1)
  [Métricas de Negócio — tabela]  |  [1º Dep Médio por Origem — tabela]  |  [Destaques — 3 cards]
```

### 3.2 Painel: FTD WoW por Canal

**Fonte:** GA4 (property `512299072`)  
**Evento:** `deposit_ftd`  
**Dimensão:** `sessionDefaultChannelGrouping`

**Canais exibidos** (ordenados por volume de Maio decrescente):
1. Paid Social
2. Paid Search
3. Sem Atribuição
4. Direct
5. Affiliates
6. Organic Search
7. Outros (soma de Paid Other + Cross-network + Organic Social + Email + Referral)

**Linha de referência:** total FTDs PowerBI (rodapé do gráfico, para mostrar gap GA4 vs BI).

**Discrepância GA4 vs PowerBI:** ~11% estrutural (ad blockers, app mobile, ITP Safari). Jan/Fev com overcounting por bug corrigido em Mar.

### 3.3 Painel: Dep/FTD por Semana Normalizada

**Fonte:** PowerBI  
**Métrica:** depósito médio = primeiro depósito + redepositos na semana de entrada do player  
**Dimensão:** por player_key, agregado por semana normalizada

**Valores históricos (série 2026):**
- Jan: R$1.239 | Fev: R$789 | Mar: R$352 | Abr: R$205 | Mai: R$278

### 3.4 Painel: Métricas de Negócio — Janela Comparável 7 Dias

**Fonte:** PowerBI (SB + Casino combinado, BRL, Brasil, BWBRA, External players)

| Coluna | Descrição | Fórmula |
|---|---|---|
| FullReg NL | Full registrations NOT_LOCKED | `FactFullRegistration` filtrado |
| FTDs | Primeiros depósitos | `FactFirstDeposit` |
| CR% | Conversão | FTDs / FullReg NOT_LOCKED |
| GGR | Receita bruta | Gross Bets − Gross Wins |
| NGR | Receita líquida | GGR − Bonus Cost |
| Marg. Total | Margem GGR sobre aposta | GGR / Gross Bets |
| Marg. SB | Margem sportsbook | GGR_SB / GrossBets_SB |
| Marg. CS | Margem casino | GGR_CS / GrossBets_CS |

**Nota:** Gross Wins = `GAME_WIN` + `CASH_OUT` + `CORRECTION`. GAME_BET é negativo — usar `ABS()`.

### 3.5 Painel: 1º Depósito Médio por Origem

**Fonte:** PowerBI  
**Métrica:** somente o 1º depósito (sem redepositos)  
**Dimensão:** `utm_source` ou equivalente no DimPlayer  
**Ordenação:** valor de Maio decrescente  
**10 sources + linha Média geral**

### 3.6 Painel: Destaques (3 cards)

Conteúdo editorial — definido pelo analista com base nos achados da semana. Estrutura:
- **Card 1:** FTD · Canal — canal líder e variação notável
- **Card 2:** Dep/FTD · Qualidade — valor e variação vs mês anterior
- **Card 3:** GGR · Negócio — valor e variação vs mês anterior

---

## 4. Página 3 — Performance de Mídia

### 4.1 Layout

```
HEADER  — headline narrativo focado em mídia paga + meta

ROW 1 (flex:7 = 70%)
  [G1: Budget vs FTDs + linha CPA]  |  [G2: Budget vs Turnover + linha R$/Apostador]

ROW 2 (flex:3 = 30%)
  [Pacing: 4 cards — Google | Meta | TikTok | X]
```

### 4.2 Gráfico G1 — Budget vs FTDs · CPA por Plataforma

**Eixo Y:** % do budget total | % dos FTDs totais  
**Linha:** CPA (R$) por plataforma  
**Plataformas:** Google, Meta, TikTok, X, Taboola  

**Fontes por métrica:**

| Métrica | Fonte | Detalhe |
|---|---|---|
| % Budget | Argentina Perfo (`.WEEKLY/BW BR - CPL x Mes l Interno Perfo 2026.xlsx`, aba `Daily ACQ`) | Google col 13 (USD), Meta col 23 (USD), TikTok col 34 (BRL), Taboola col 56 (BRL), X col 105 (BRL). FX: col 83 |
| % FTDs Google | GA4 `deposit_ftd` canal Paid Search + Cross-network | Property 512299072 |
| % FTDs demais | Argentina Perfo col FTD BI (PowerBI) | Meta col 25, TikTok col 36, X col 101 |
| CPA | Spend / FTDs | Calculado |

### 4.3 Gráfico G2 — Budget vs Turnover · R$/Apostador

**Eixo Y:** % do budget total | % do turnover total da mídia paga  
**Linha:** R$ apostado por apostador ativo por plataforma  

| Métrica | Fonte |
|---|---|
| % Budget | Mesmo da G1 |
| Turnover por plataforma | PowerBI — `FactAGGAccountTransaction` filtrado por `utm_source` / canal de origem |
| R$/apostador | Turnover / Apostadores únicos ativos por canal |

**Nota conceitual:** turnover = gross bets. Inclui ciclos (player pode depositar R$200 e gerar R$2.000 em gross bets). Não é receita.

### 4.4 Painel de Pacing — 4 Cards

**Fonte:** `PACING - PERFO.xlsx` (Diego/Perfo) — arquivo salvo em `.WEEKLY/`  
**Aba:** `Página1`  
**Dados MTD** (acumulado desde dia 1 do mês até data de atualização do arquivo)

| Plataforma | Col usada | Orçamento (USD) | FTDs |
|---|---|---|---|
| Google | `Investimento`, `Consumo`, `Resultado`, `% verba real`, `% resultados reais` | USD × R$5,56 | resultado vs meta |
| Meta | idem | idem | idem |
| TikTok | idem | idem | idem |
| X | idem | idem | idem |

**Linha de referência:** `% verba ideal` = dias veiculados / duração do flight (ex: 12/31 = 38,7%)

**Lógica de cores:**
- Orçamento %: sempre preto — direção sem veredicto
- Delta orçamento: verde se acima, âmbar se 0–10pp abaixo, vermelho se >10pp abaixo
- FTD %: âmbar se >15pp abaixo da ref, vermelho se >25pp abaixo
- **Atenção:** orçamento acima do ritmo não é positivo sem respaldo em FTDs

---

## 5. Checklist semanal — o que Darwin precisa fornecer

### Arquivos que precisam estar em `.WEEKLY/` antes de iniciar a atualização:

| Arquivo | Conteúdo | Fornecido por | Observação |
|---|---|---|---|
| `BW BR - CPL x Mes l Interno Perfo 2026.xlsx` | Spend diário por plataforma + FTDs BI | Equipe de Perfo (Argentina) | Verificar se semana de interesse está fechada na aba `Daily ACQ` |
| `PACING - PERFO.xlsx` | Consumo % de orçamento e FTDs vs meta mensal | Diego | Atualizado na data de geração do relatório |

### Dados que precisam estar em `.WEEKLY/` OU acessíveis via PowerBI:

| Dado | Fonte | Formato ideal |
|---|---|---|
| Métricas de negócio (FullReg, FTDs, GGR, NGR, margens) | PowerBI export | `2026_SB_CS.xlsx` — ou direto via API quando tokens estiverem ativos |
| Dep/FTD por player e por semana | PowerBI export | idem |
| 1º Depósito por origem/source | PowerBI export | idem |
| Turnover por canal de origem | PowerBI export | Requer query player-level por `utm_source` |

### Informações editoriais (inseridas manualmente):

- **Headline das 3 páginas** — frase narrativa principal
- **Destaques (3 cards da P1+P2)** — achado mais relevante da semana por dimensão
- **Anotações contextuais** — ex: Semana Santa, anomalia de canal (NFA), eventos de produto

---

## 6. O que Claude consegue obter automaticamente

| Dado | Ferramenta disponível | Status |
|---|---|---|
| FTDs por canal GA4 (`deposit_ftd`) | MCP `google-analytics` (property 512299072) | **Disponível agora** |
| Semanas normalizadas calculadas | Script Python (lógica já implementada) | **Disponível agora** |
| Leitura de XLSX locais | Python `openpyxl` via Bash | **Disponível agora** |
| Queries PowerBI (BI metrics) | REST API OAuth2 — tokens em `~/.claude/credentials/` | **Operacional** (refresh automático a cada sessão) |

---

## 7. Avaliação de agentes — possibilidade, viabilidade e utilidade

### Possibilidade

Tecnicamente viável com os recursos já disponíveis ou em fase final de setup:

- **GA4** → já funciona via MCP `google-analytics`
- **XLSX locais** → já funciona via Python `openpyxl`
- **PowerBI** → API REST pronta, falta apenas o token gerado pelo Lucas (acesso Builder)
- **Geração de HTML** → já demonstrado nessa série de sessões

### Viabilidade

Alta, com uma ressalva: os dados de turnover por `utm_source` (G2) e o 1º depósito por origem (P1+P2) requerem queries player-level no PowerBI, que ainda não foram testadas. O restante dos dados já tem caminho validado.

**Esforço estimado de setup:** 2–3 sessões de trabalho após a conexão PowerBI estar ativa.

### Utilidade

Alta. Hoje a geração manual de uma edição do WPR leva ~2h (coleta de dados + inserção no HTML). Com agentes:

| Etapa | Manual hoje | Com agentes |
|---|---|---|
| Pull GA4 FTDs por canal | 10 min (dashboard) | Automático |
| Export PowerBI + cálculo de métricas | 40 min | Automático (após tokens) |
| Leitura Argentina Perfo + pacing | 15 min | Automático |
| Inserção e formatação no HTML | 50 min | Automático |
| Revisão + headline + destaques | 20 min | **Manual (editorial)** |
| **Total** | **~2h** | **~20 min** |

### Arquitetura proposta

**Um único agente de atualização** ("Bira atualiza WPR") com 4 passos sequenciais:

```
1. Calcular janela da semana normalizada
        ↓
2. Pull GA4 — deposit_ftd por canal para a janela
        ↓
3. Ler XLSX locais — Argentina Perfo + PACING - PERFO
        ↓
4. Query PowerBI — métricas de negócio (quando tokens ativos)
        ↓
5. Gerar HTML com todos os valores substituídos
        ↓
6. Abrir para revisão editorial (headline, destaques, contexto)
```

**Trigger:** Darwin digita algo como:
> "Atualize o WPR para a semana de [data]. Headline: [frase]. Destaques: [...]"

Ao receber esse pedido, vou solicitar os arquivos abaixo antes de iniciar — ou verificar se já estão na pasta `.WEEKLY/`:

---

**Checklist de arquivos que vou pedir a você:**

| # | Arquivo | O que contém | Quem fornece | Onde salvar |
|---|---|---|---|---|
| 1 | `BW BR - CPL x Mes l Interno Perfo 2026.xlsx` | Investimento e FTDs diários por plataforma (Google, Meta, TikTok, X, Taboola) | Equipe de Perfo — Argentina | `.WEEKLY/` |
| 2 | `PACING - PERFO.xlsx` | Consumo % de orçamento e FTDs vs meta mensal, atualizado até a data do relatório | Diego | `.WEEKLY/` |
| 3 | `2026_SB_CS.xlsx` (ou dois arquivos: `2026_SB.xlsx` + `2026_CS.xlsx`) | Métricas de negócio: FullReg, FTDs, GGR, NGR, margens, depósitos, 1º depósito por source | Export manual do PowerBI (você) | `Performance/` |

**Informações editoriais que vou pedir diretamente:**

| # | Informação | Exemplo |
|---|---|---|
| 4 | Headline das 3 páginas | "GGR sustentado com 2,5× menos FTDs. Qualidade em recuperação." |
| 5 | Destaques P1+P2 (3 cards) | Canal líder · Dep/FTD e variação · GGR e variação |
| 6 | Contexto da semana (se houver) | Semana Santa, anomalia de canal, evento de produto |

> **Nota sobre o arquivo nº 3:** enquanto as medidas DAX exatas do Betinho não estiverem replicadas, as métricas de negócio (GGR, NGR, margens) virão do export XLSX — não diretamente da API. A API já funciona para turnover por `utm_source` (P3) e FTDs por canal (GA4).

---

O agente executa os passos 1–5 automaticamente e apresenta o HTML para revisão final.

### Recomendação

Iniciar com o **agente parcial já hoje**: GA4 + leitura de XLSX (ambos disponíveis). Adicionar PowerBI assim que Lucas conceder o acesso Builder. O esforço de implementação é baixo — a maior parte da lógica já foi desenvolvida nessas sessões.

---

## 8. Glossário rápido

| Termo | Definição |
|---|---|
| FTD | First Time Depositor — player que faz o 1º depósito |
| GGR | Gross Gaming Revenue = Gross Bets − Gross Wins |
| NGR | Net Gaming Revenue = GGR − Bonus Cost |
| Turnover | Gross Bets — volume apostado total (inclui ciclos) |
| Semana normalizada | Janela de 7 dias com âncora no dia da semana do dia 1 do mês |
| Dep/FTD | Depósito médio na semana de entrada = 1º dep + redepositos |
| 1º dep médio | Apenas o primeiro depósito, sem redepositos |
| pp | Pontos percentuais — diferença entre dois percentuais |
| Pacing | Ritmo de consumo do orçamento vs ritmo esperado (dias decorridos) |
