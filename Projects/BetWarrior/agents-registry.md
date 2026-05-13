# Registro de Sub-Agentes — BetWarrior

Arquivo carregado automaticamente pelo orquestrador (Bira) no início de cada sessão.  
Atualizado em: 13/05/2026

---

## Catálogo de Sub-Agentes

### agent-ga4
| Campo | Valor |
|---|---|
| Propósito | Puxar `deposit_ftd` por `sessionDefaultChannelGrouping` no GA4 |
| Input | `data_inicio` (YYYY-MM-DD), `data_fim` (YYYY-MM-DD) |
| Output | JSON `{ "Paid Social": 120, "Paid Search": 163, ... }` |
| Ferramenta | MCP `google-analytics` · property `512299072` |
| Observação | Google FTDs para P3 = Paid Search + Cross-network. Jan/Fev overcounting (bug corrigido Mar). |
| Workflows | `WPR-update` |

---

### agent-powerbi
| Campo | Valor |
|---|---|
| Propósito | Renovar token OAuth2 + executar queries DAX para métricas de negócio e turnover por `utm_source` |
| Input | `data_inicio`, `data_fim` |
| Output | JSON com duas chaves: `metricas_negocio` (FullReg, FTDs, GGR, NGR, margens) e `turnover_por_canal` (`utm_source` → gross bets + apostadores únicos) |
| Ferramenta | Bash (Python REST API) |
| Credenciais | `~/.claude/credentials/pbi_access_token.txt` · `pbi_refresh_token.txt` |
| Regras críticas | Ver `BI/pbi-overview-bira.md` — filtros obrigatórios: External, NOT_LOCKED, BR, BWBRA |
| Observação | GGR/NGR via API tem ~10% de desvio vs PowerBI (medidas DAX customizadas do Betinho não replicadas). Para P1+P2 usar XLSX export enquanto DAX não for compartilhado. |
| Workflows | `WPR-update` |

---

### agent-xlsx
| Campo | Valor |
|---|---|
| Propósito | Ler dados de spend, FTDs e pacing das planilhas da equipe de Perfo |
| Input | `data_inicio`, `data_fim`, pasta `.WEEKLY/` |
| Output | JSON com três chaves: `spend_por_plataforma`, `ftd_por_plataforma`, `pacing` |
| Ferramenta | Bash (Python `openpyxl`) |
| Arquivo 1 | `BW BR - CPL x Mes l Interno Perfo 2026.xlsx` · aba `Daily ACQ` (fornecido: Equipe Perfo Argentina) |
| Arquivo 2 | `PACING - PERFO.xlsx` · aba `Página1` (fornecido: Diego) |
| Mapeamento cols | Google spend col 13 (USD), Meta col 23 (USD), TikTok col 34 (BRL), Taboola col 56 (BRL), X col 105 (BRL). FX: col 83. FTDs: Meta col 25, TikTok col 36, X col 101. Google FTD NÃO usar (col 15 = estimativa) |
| Observação | Google FTDs vêm do agent-ga4, não dessa planilha |
| Workflows | `WPR-update` |

---

### agent-html
| Campo | Valor |
|---|---|
| Propósito | Receber todos os payloads de dados e gerar os arquivos HTML finais do WPR |
| Input | Outputs de agent-ga4 + agent-powerbi + agent-xlsx + inputs editoriais (headline, destaques, contexto) |
| Output | `weekly-report-slide.html` (P1+P2) e `weekly-report-slide-p3.html` (P3) com valores atualizados |
| Ferramenta | Write (edição dos HTMLs de template) |
| Templates | `Projects/BetWarrior/Performance/weekly-report-slide.html` e `weekly-report-slide-p3.html` |
| Nomenclatura entrega | `WPR_Brasil_[Mês][DD-DD]_YYYY.html` · ex: `WPR_Brasil_Mai08-14_2026.html` |
| Workflows | `WPR-update` |

---

## Workflows

### WPR-update — Atualização Semanal do Weekly Performance Report

**Trigger exato** (Darwin digita):
```
WPR [DD-DD/mês/YYYY]. Headline: [frase narrativa]. Destaques: [card1 | card2 | card3]
```

Exemplo:
```
WPR 08-14/mai/2026. Headline: "Qualidade de FTD em recuperação — Dep/FTD acima de abril." Destaques: Paid Social lidera com 38% dos FTDs | Dep/FTD R$312 +12% vs abr | GGR R$4,2M estável
```

**Pré-condições** — verificar antes de iniciar:

| # | Arquivo | Onde | Quem fornece |
|---|---|---|---|
| 1 | `BW BR - CPL x Mes l Interno Perfo 2026.xlsx` | `.WEEKLY/` | Equipe Perfo (Argentina) |
| 2 | `PACING - PERFO.xlsx` | `.WEEKLY/` | Diego |
| 3 | `2026_SB_CS.xlsx` (ou SB + CS separados) | `Performance/` | Darwin (export PowerBI) |

Se algum arquivo estiver ausente, o orquestrador solicita antes de prosseguir.

**Fluxo de execução:**

```
BIRA (orquestrador)
  │
  ├── [PARALELO] ──────────────────────────────────────────────────────┐
  │   ├── agent-ga4    → FTDs por canal (janela normalizada)           │
  │   ├── agent-powerbi → métricas de negócio + turnover utm_source    │
  │   └── agent-xlsx   → spend/FTD/pacing das planilhas Perfo          │
  │                                                                     │
  └── [SEQUENCIAL — após receber os 3 outputs] ────────────────────────┘
      └── agent-html  → gera HTML P1+P2 e P3 com todos os valores

  └── [ENTREGA PARA DARWIN]
      └── HTML aberto para revisão editorial (headline já inserida, destaques inseridos)
```

**Inputs editoriais** (fornecidos no trigger, inseridos pelo agent-html):

| # | Campo | Onde aparece |
|---|---|---|
| 4 | Headline | Header das 3 páginas |
| 5 | Destaques (3 cards) | Painel P1+P2 — Card FTD, Card Dep/FTD, Card GGR |
| 6 | Contexto da semana (opcional) | Rodapé / nota dos gráficos |

**Output final:**
- 2 arquivos HTML prontos para apresentação
- Sugestão de nome de entrega com a nomenclatura padrão

---

## Índice rápido — qual agente faz o quê

| Preciso de... | Agente |
|---|---|
| FTDs por canal (GA4) | agent-ga4 |
| GGR, NGR, FTDs, margens (PowerBI) | agent-powerbi |
| Turnover por plataforma de mídia (PowerBI) | agent-powerbi |
| Spend e pacing por plataforma (planilhas Perfo) | agent-xlsx |
| FTDs por plataforma de mídia (planilhas Perfo) | agent-xlsx |
| Gerar / atualizar HTML do WPR | agent-html |
| Atualização semanal completa | WPR-update (todos os 4) |
