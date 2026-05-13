# Power BI BetWarrior Brasil — Overview para o Bira

> **Para:** Bira (Claude Code do Lucas Vagione — Data Analyst BR)
> **De:** Betinho (Claude Code do JP Marques — Head of Marketing Brasil)
> **Atualizado:** 08/Mai/2026
>
> Este documento é o que você precisa saber para acessar e consultar o Power BI da BetWarrior Brasil corretamente. Leia inteiro antes da primeira query. Salve na sua memória as regras críticas da seção 3.

---

## 1. Conexão

### Autenticação OAuth2

O Power BI usa OAuth2 com refresh_token. Não há client_secret — o Client ID é público.

| Item | Valor |
|---|---|
| **Client ID** | `ea0616ba-638b-4df5-95b9-636659ae5121` |
| **Group ID** | `00ecb2bb-6c61-4d09-badb-a4df0c948b02` |
| **Dataset ID** | `c489d219-ef18-4f9e-9c5c-422c9092e3aa` |
| **Scope** | `https://analysis.windows.net/powerbi/api/.default offline_access` |
| **Token endpoint** | `https://login.microsoftonline.com/organizations/oauth2/v2.0/token` |

### Onde ficam os tokens (Mac — caminho do JP)

```
~/.claude/credentials/pbi_access_token.txt   ← expira em ~1h
~/.claude/credentials/pbi_refresh_token.txt  ← dura ~90 dias
```

No Windows (Lucas), trocar `~` por `%USERPROFILE%`.

### Refresh antes de cada sessão

Sempre renovar o token antes de qualquer query:

```bash
REFRESH=$(cat ~/.claude/credentials/pbi_refresh_token.txt)
RESPONSE=$(curl -s -X POST "https://login.microsoftonline.com/organizations/oauth2/v2.0/token" \
  -d "client_id=ea0616ba-638b-4df5-95b9-636659ae5121" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=$REFRESH" \
  -d "scope=https://analysis.windows.net/powerbi/api/.default offline_access")

# Salvar novos tokens (a resposta traz AMBOS — sempre salvar os dois)
echo $RESPONSE | python3 -c "import sys,json; d=json.load(sys.stdin); open(os.path.expanduser('~/.claude/credentials/pbi_access_token.txt'),'w').write(d['access_token']); open(os.path.expanduser('~/.claude/credentials/pbi_refresh_token.txt'),'w').write(d['refresh_token'])" 2>/dev/null || \
  python3 -c "
import sys, json, os
d = json.load(sys.stdin)
open(os.path.expanduser('~/.claude/credentials/pbi_access_token.txt'),'w').write(d['access_token'])
open(os.path.expanduser('~/.claude/credentials/pbi_refresh_token.txt'),'w').write(d['refresh_token'])
print('Tokens salvos OK')
" <<< "$RESPONSE"
```

Se o refresh falhar (token expirado após ~90 dias), precisa fazer Device Code Flow manual. Ver `guia-conexao-pbi-claude-code.md` na mesma pasta.

### Executar uma query DAX

```bash
TOKEN=$(cat ~/.claude/credentials/pbi_access_token.txt)
GROUP="00ecb2bb-6c61-4d09-badb-a4df0c948b02"
DATASET="c489d219-ef18-4f9e-9c5c-422c9092e3aa"

curl -s -X POST \
  "https://api.powerbi.com/v1.0/myorg/groups/$GROUP/datasets/$DATASET/executeQueries" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries":[{"query":"EVALUATE ROW(\"test\",1+1)"}],"serializerSettings":{"includeNulls":true}}'
```

Resposta: `{"results":[{"tables":[{"rows":[{"[test]":2}]}]}]}`

Para queries mais longas, passar a query como variável Python:

```python
import subprocess, json

TOKEN = open(os.path.expanduser("~/.claude/credentials/pbi_access_token.txt")).read().strip()
GROUP = "00ecb2bb-6c61-4d09-badb-a4df0c948b02"
DATASET = "c489d219-ef18-4f9e-9c5c-422c9092e3aa"

query = """
EVALUATE SUMMARIZECOLUMNS(
    DimPlayer[utm_source],
    FILTER(DimDate, DimDate[Date] = DATE(2026,5,7)),
    FILTER(DimPlayer, DimPlayer[internal_external_player] = "External"),
    "Regs", CALCULATE(COUNTROWS(FactRegistration)),
    "FTDs", CALCULATE(COUNTROWS(FactFirstDeposit))
)
ORDER BY [Regs] DESC
"""

payload = json.dumps({"queries": [{"query": query}], "serializerSettings": {"includeNulls": True}})
result = subprocess.run(
    ["curl", "-s", "-X", "POST",
     f"https://api.powerbi.com/v1.0/myorg/groups/{GROUP}/datasets/{DATASET}/executeQueries",
     "-H", f"Authorization: Bearer {TOKEN}",
     "-H", "Content-Type: application/json",
     "-d", payload],
    capture_output=True, text=True
)
rows = json.loads(result.stdout)["results"][0]["tables"][0]["rows"]
```

---

## 2. Estrutura das tabelas principais

### Tabelas de fatos

| Tabela | O que contém |
|---|---|
| `FactRegistration` | Um registro por jogador que se cadastrou |
| `FactFullRegistration` | Jogadores que completaram o onboarding (KYC) |
| `FactFirstDeposit` | Um registro por primeiro depósito de cada jogador |
| `FactAGGAccountTransaction` | Todas as transações: apostas, ganhos, depósitos, bônus |
| `FactPayment` | Pagamentos — usar SOMENTE para Withdrawals (saques) |

### Tabelas de dimensão

| Tabela | Campos importantes |
|---|---|
| `DimDate` | `Date` (tipo DATE) |
| `DimPlayer` | `dim_player_key`, `internal_external_player`, `locked_status`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` |
| `DimGame` | `game_name`, `game_platform_name` ("Sports" ou "Casino"), `game_sub_platform_name` (campeonato/provider) |
| `DimLogin` | `device_group` ("Android Web", "Android App", "iOS Web", "Desktop") |
| `KYC_Onboardings_Logs` | `created_date_only`, status de onboarding — **nome exato, case-sensitive** |

### Tipos de transação em FactAGGAccountTransaction

| `account_transaction_type` | O que é |
|---|---|
| `GAME_BET` | Apostas realizadas (valor negativo → usar ABS) |
| `GAME_WIN` | Prêmios pagos |
| `CASH_OUT` | Cash out |
| `CORRECTION` | Correções |
| `BONUS_REL` | Bônus liberado (sub_account = AMOUNT_RELEASED_BONUS) |
| `DEPOSIT` | Depósitos |

---

## 3. Regras críticas — salvar na memória

Estas regras são erros que acontecem com frequência. Memorize.

### 3.1 Filtro de jogadores — SEMPRE aplicar

```dax
FILTER(DimPlayer, DimPlayer[internal_external_player] = "External")
```

Sem esse filtro, os resultados incluem contas internas (testes, compliance, etc.) e inflam todos os números.

### 3.2 locked_status — sintaxe EXATA

```dax
-- CORRETO:
DimPlayer[locked_status] = "NOT_LOCKED"

-- ERRADO (não usar):
DimPlayer[locked_status] <> "LOCKED"
```

O campo tem valores além de "LOCKED" e "NOT_LOCKED". A segunda forma retorna resultados errados silenciosamente.

### 3.3 Gross Wins = 3 tipos de transação

```dax
FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN", "CASH_OUT", "CORRECTION"}
```

Nunca usar só `GAME_WIN`. Cash Out e Correction fazem parte do valor que a casa paga.

### 3.4 Withdrawals — usar FactPayment, não FactAGGAccountTransaction

```dax
-- CORRETO:
CALCULATE(
    SUM(FactPayment[payment_amount]),
    FactPayment[payment_type] = "WITHDRAWAL",
    FactPayment[payment_status] = "COMPLETED",
    DimPlayer[internal_external_player] = "External"
)

-- ERRADO: usar FactAGGAccountTransaction para saques
```

### 3.5 GGR, NGR e Bonus Cost — como calcular

```
GGR = Gross Bets - Gross Wins
GGR Margin = GGR / Gross Bets × 100

NGR = RM Account GGR - Released Bonus
  onde:
    RM Account GGR = (GB filtrado por sub_account IN {"AMOUNT_REAL","AMOUNT_RELEASED_BONUS"})
                   - (GW filtrado pelo mesmo sub_account)
    Released Bonus = SUM de BONUS_REL onde dim_sub_account_key = "AMOUNT_RELEASED_BONUS"

Bonus Cost = GGR - NGR   ← NUNCA somar CRE_BONUS diretamente
```

### 3.6 Sports movers — usar DimGame, não DimBetOffer

```dax
-- CORRETO: agrupar por DimGame[game_name]
FILTER(DimGame, DimGame[game_platform_name] = "Sports")
-- DimGame[game_name] = nome do evento/jogo
-- DimGame[game_sub_platform_name] = campeonato/liga

-- ERRADO: DimBetOffer[bet_offer_event_name]
-- DimBetOffer tem cobertura incompleta — perde os maiores eventos
-- Validado em 08/05/2026 após divergência no dashboard
```

### 3.7 Filtro padrão — jogadores externos sem lock

Para análises de base ativa (Unique Bettors, ARPU, retenção):

```dax
FILTER(DimPlayer, DimPlayer[internal_external_player] = "External")
FILTER(DimPlayer, DimPlayer[locked_status] = "NOT_LOCKED")
```

Para aquisição (Regs, FTDs): usar só `internal_external_player = "External"` (jogadores bloqueados ainda contam como aquisição).

---

## 4. Queries por caso de uso

### 4.1 Aquisição (por dia)

```dax
-- Registros, Full Reg, FRNL, FTDs
EVALUATE ROW(
    "Regs",   CALCULATE(COUNTROWS(FactRegistration),    FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)), FILTER(DimPlayer, DimPlayer[internal_external_player]="External")),
    "FullReg",CALCULATE(COUNTROWS(FactFullRegistration),FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)), FILTER(DimPlayer, DimPlayer[internal_external_player]="External")),
    "FRNL",   CALCULATE(COUNTROWS(FactFullRegistration),FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)), FILTER(DimPlayer, DimPlayer[internal_external_player]="External"), DimPlayer[locked_status]="NOT_LOCKED"),
    "FTDs",   CALCULATE(COUNTROWS(FactFirstDeposit),    FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)), FILTER(DimPlayer, DimPlayer[internal_external_player]="External"))
)
```

### 4.2 Financeiro (por dia)

```dax
EVALUATE ROW(
    "GB", CALCULATE(ABS(SUM(FactAGGAccountTransaction[account_transaction_amount])),
          FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
          FactAGGAccountTransaction[account_transaction_type]="GAME_BET",
          DimPlayer[internal_external_player]="External"),

    "GW", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),
          FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
          FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN","CASH_OUT","CORRECTION"},
          DimPlayer[internal_external_player]="External"),

    "DEP", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),
           FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
           FactAGGAccountTransaction[account_transaction_type]="DEPOSIT",
           DimPlayer[internal_external_player]="External"),

    "WD", CALCULATE(SUM(FactPayment[payment_amount]),
          FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
          FactPayment[payment_type]="WITHDRAWAL",
          FactPayment[payment_status]="COMPLETED",
          DimPlayer[internal_external_player]="External")
)
-- GGR = GB - GW (calcular em Python após a query)
```

### 4.3 Split Sports / Casino

```dax
-- Sports
EVALUATE ROW(
    "SB_GB", CALCULATE(ABS(SUM(FactAGGAccountTransaction[account_transaction_amount])),
             FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
             FactAGGAccountTransaction[account_transaction_type]="GAME_BET",
             DimPlayer[internal_external_player]="External",
             FILTER(DimGame, DimGame[game_platform_name]="Sports")),
    "SB_GW", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),
             FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
             FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN","CASH_OUT","CORRECTION"},
             DimPlayer[internal_external_player]="External",
             FILTER(DimGame, DimGame[game_platform_name]="Sports"))
)
-- Idem trocando "Sports" por "Casino"
```

### 4.4 Unique Bettors e Bet Count

```dax
EVALUATE ROW(
    "Bettors", CALCULATE(DISTINCTCOUNT(FactAGGAccountTransaction[dim_player_key]),
               FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
               FactAGGAccountTransaction[account_transaction_type]="GAME_BET",
               DimPlayer[internal_external_player]="External"),

    "Bets", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_record_count]),
            FILTER(DimDate, DimDate[Date]=DATE(2026,5,7)),
            FactAGGAccountTransaction[account_transaction_type]="GAME_BET",
            DimPlayer[internal_external_player]="External")
)
```

### 4.5 Top jogos Casino (por GGR, Turnover, Margem)

```dax
-- Top 10 por GGR
EVALUATE TOPN(10,
    ADDCOLUMNS(
        SUMMARIZECOLUMNS(
            DimGame[game_name], DimGame[game_sub_platform_name],
            FILTER(DimDate, DimDate[Date] >= DATE(2026,4,1) && DimDate[Date] <= DATE(2026,4,30)),
            FILTER(DimPlayer, DimPlayer[internal_external_player]="External"),
            FILTER(DimGame, DimGame[game_platform_name]="Casino"),
            "GB", CALCULATE(ABS(SUM(FactAGGAccountTransaction[account_transaction_amount])), FactAGGAccountTransaction[account_transaction_type]="GAME_BET"),
            "GW", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),       FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN","CASH_OUT","CORRECTION"})
        ),
        "GGR", [GB]-[GW]
    ),
    [GGR], DESC
)
-- Para Turnover: ordenar por [GB]
-- Para Margem: calcular GGR/GB depois e ordenar em Python
```

### 4.6 Análise por UTM source

```dax
EVALUATE SUMMARIZECOLUMNS(
    DimPlayer[utm_source],
    FILTER(DimDate, DimDate[Date] >= DATE(2026,4,1) && DimDate[Date] <= DATE(2026,4,30)),
    FILTER(DimPlayer, DimPlayer[internal_external_player]="External"),
    "Regs", CALCULATE(COUNTROWS(FactRegistration)),
    "FTDs", CALCULATE(COUNTROWS(FactFirstDeposit)),
    "GB",   CALCULATE(ABS(SUM(FactAGGAccountTransaction[account_transaction_amount])), FactAGGAccountTransaction[account_transaction_type]="GAME_BET"),
    "GW",   CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),      FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN","CASH_OUT","CORRECTION"}),
    "DEP",  CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]),      FactAGGAccountTransaction[account_transaction_type]="DEPOSIT")
)
ORDER BY [Regs] DESC
```

### 4.7 Perfil de jogador individual

```dax
-- Histórico diário de um player (substituir dim_player_key)
EVALUATE SUMMARIZECOLUMNS(
    DimDate[Date],
    FILTER(FactAGGAccountTransaction, FactAGGAccountTransaction[dim_player_key] = 1120651),
    FactAGGAccountTransaction[account_transaction_type],
    "Valor", CALCULATE(SUM(FactAGGAccountTransaction[account_transaction_amount]))
)
ORDER BY DimDate[Date] ASC
```

### 4.8 Retenção M1 (coorte)

```dax
-- Passo 1: jogadores com FTD em março 2026
DEFINE
    VAR _ftd_march = CALCULATETABLE(
        VALUES(FactFirstDeposit[dim_player_key]),
        FILTER(DimDate, DimDate[Date] >= DATE(2026,3,1) && DimDate[Date] <= DATE(2026,3,31)),
        FILTER(DimPlayer, DimPlayer[internal_external_player] = "External")
    )

-- Passo 2: quantos desses apostaram em abril
EVALUATE ROW(
    "ftd_march", COUNTROWS(_ftd_march),
    "retained_april", CALCULATE(
        DISTINCTCOUNT(FactAGGAccountTransaction[dim_player_key]),
        FILTER(DimDate, DimDate[Date] >= DATE(2026,4,1) && DimDate[Date] <= DATE(2026,4,30)),
        FactAGGAccountTransaction[account_transaction_type] = "GAME_BET",
        TREATAS(_ftd_march, FactAGGAccountTransaction[dim_player_key])
    )
)
-- Retenção M1 = retained_april / ftd_march × 100
```

### 4.9 MTD com período comparativo

```dax
-- MTD atual (1 a 7 de maio)
CALCULATE([métrica], FILTER(DimDate, DimDate[Date] >= DATE(2026,5,1) && DimDate[Date] <= DATE(2026,5,7)), ...)

-- MTD mesmo período mês anterior (1 a 7 de abril)
CALCULATE([métrica], FILTER(DimDate, DimDate[Date] >= DATE(2026,4,1) && DimDate[Date] <= DATE(2026,4,7)), ...)
```

---

## 5. Armadilhas conhecidas

### 5.1 Encoding de nomes com acentos

O Power BI retorna nomes de eventos/times com caracteres corrompidos às vezes. Se receber algo como `Vitória` ou `Cricimá`, fazer decode UTF-8. Em Python: `nome.encode('latin-1').decode('utf-8')` pode ajudar, mas depende do contexto. Sempre verificar nomes que parecem quebrados.

### 5.2 Valores nulos em movers

Queries de Top Movers podem retornar uma linha com `game_name = null` — representa apostas múltiplas (accumulators) sem evento mapeado. Filtrar com `NOT ISBLANK([game_name])` para análises por evento. Se quiser incluir, renomear para "Apostas Múltiplas".

### 5.3 GAME_BET tem valor negativo

`FactAGGAccountTransaction[account_transaction_amount]` para GAME_BET é negativo (saída de dinheiro da conta do jogador). Sempre usar `ABS()` ao somar apostas.

### 5.4 DimDate vs campo de data na tabela de fato

Usar sempre `FILTER(DimDate, DimDate[Date] = ...)` — não filtrar diretamente por campos de data nas tabelas de fato (ex: `FactRegistration[first_reg_datetime]`). O relacionamento passa pela DimDate.

### 5.5 includeNulls na chamada de API

Sempre passar `"serializerSettings": {"includeNulls": true}` no body da API. Sem isso, colunas com null são omitidas da resposta e o código que lê por nome quebra silenciosamente.

### 5.6 Tabela KYC_Onboardings_Logs — case-sensitive

O nome exato é `KYC_Onboardings_Logs`. Maiúsculas e underscores importam. PBI rejeita silenciosamente nomes errados sem retornar erro explícito.

---

## 6. Períodos padrão — como calcular

Nunca hardcodar datas. Usar Python datetime:

```python
from datetime import date, timedelta

hoje = date.today()
D1  = hoje - timedelta(days=1)       # ontem
DS1 = hoje - timedelta(days=8)       # mesmo dia semana passada
MTD_inicio = D1.replace(day=1)       # 1º do mês de D1
MTD1_inicio = (MTD_inicio - timedelta(days=1)).replace(day=1)  # 1º do mês anterior
MTD1_fim    = MTD_inicio - timedelta(days=1)  # último dia do mês anterior até o mesmo dia
```

Para MTD comparativo (mesmo número de dias):
```python
# Se D1 = 07/mai, MTD = 1-7/mai. MTD-1 = 1-7/abr (não o mês inteiro)
mtd1_fim = date(D1.year, D1.month - 1 if D1.month > 1 else 12,
                D1.day if D1.day <= 30 else 30)
```

---

## 7. Referências adicionais

| Documento | Onde está | Para que serve |
|---|---|---|
| `kpi-reference.md` | PowerBI/ | Fórmulas DAX completas do pipeline diário (Betinho) |
| `kpi-pipeline-docs.md` | PowerBI/ | Documentação técnica completa do pipeline KPI |
| `schema-dataset.md` | PowerBI/Md/ | Schema detalhado das tabelas |
| `modelo-relacional.md` | PowerBI/Md/ | Diagrama do modelo de dados |
| `guia-conexao-pbi-claude-code.md` | PowerBI/Md/ | Guia de conexão (Device Code Flow, Windows) |

---

## 8. Checklist antes de responder ao Lucas

Antes de entregar qualquer análise de dados:

- [ ] Filtro `internal_external_player = "External"` aplicado?
- [ ] locked_status usando `= "NOT_LOCKED"` (não `<> "LOCKED"`)?
- [ ] Gross Wins inclui GAME_WIN + CASH_OUT + CORRECTION?
- [ ] Withdrawals vindo de FactPayment (não FactAGGAccountTransaction)?
- [ ] GAME_BET somado com ABS()?
- [ ] Datas calculadas dinamicamente (não hardcoded)?
- [ ] Para Sports movers: usando DimGame (não DimBetOffer)?
