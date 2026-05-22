# PowerBI BetWarrior — Guia Definitivo de Queries (Bira)

> Gerado e validado em 22/05/2026 durante sessão WPR 01–21/mai/2026.
> Todas as queries abaixo foram executadas com sucesso via REST API e os resultados foram confrontados com o quadro do Betinho.

---

## Conexão REST API

```
Group ID:   00ecb2bb-6c61-4d09-badb-a4df0c948b02
Dataset ID: c489d219-ef18-4f9e-9c5c-422c9092e3aa
Endpoint:   POST https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/executeQueries
```

Token via `~/.claude/credentials/pbi_access_token.txt` (renovar com pbi_refresh_token.txt se expirado).

---

## Filtros Base — OBRIGATÓRIOS em todas as queries

```dax
DimPlayer[internal_external_player] = "External"
DimPlayer[player_country] = "BR"
DimPlayer[brand_name] = "BWBRA"
```

**NUNCA usar `DimPlayer[locked_status] = "NOT_LOCKED"`** — esse filtro exclui jogadores que depositaram mas foram bloqueados depois, causando subcontagem de ~10–15% nos FTDs.

---

## Períodos MTD Normalizados (21 dias — âncora: 1ª sexta-feira do mês)

| Mês | De | Até | dim_date_key (int) |
|-----|----|-----|--------------------|
| JAN | 02/01/2026 | 22/01/2026 | 20260102 – 20260122 |
| FEV | 06/02/2026 | 26/02/2026 | 20260206 – 20260226 |
| MAR | 06/03/2026 | 26/03/2026 | 20260306 – 20260326 |
| ABR | 03/04/2026 | 23/04/2026 | 20260403 – 20260423 |
| MAI | 01/05/2026 | 21/05/2026 | 20260501 – 20260521 |

---

## Tabelas Principais

| Tabela | Uso |
|--------|-----|
| `FactFirstDeposit` | FTDs, ticket médio |
| `FactFullRegistration` | Registros completos |
| `FactAGGAccountTransaction` | GGR, NGR, Gross Bets |
| `DimPlayer` | Filtros de país, marca, canal (`utm_medium`) |
| `DimDate` | Filtro de data via `dim_date_key` (int YYYYMMDD) |

---

## Queries

### 1. FTDs — Total por período

```dax
EVALUATE
ROW(
  "FTDs",
  CALCULATE(
    COUNTROWS(FactFirstDeposit),
    FILTER(
      FactFirstDeposit,
      FactFirstDeposit[payment_processed_ONLY_date] >= DATE(2026,5,1) &&
      FactFirstDeposit[payment_processed_ONLY_date] <= DATE(2026,5,21)
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  )
)
```

> Data via `FactFirstDeposit[payment_processed_ONLY_date]` com função `DATE()`.
> Para outros meses, ajustar as datas.

---

### 2. FullReg — Total por período

```dax
EVALUATE
ROW(
  "FullReg",
  CALCULATE(
    COUNTROWS(FactFullRegistration),
    FILTER(
      DimDate,
      DimDate[dim_date_key] >= 20260501 &&
      DimDate[dim_date_key] <= 20260521
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  )
)
```

> Data via `DimDate[dim_date_key]` como inteiro YYYYMMDD.

---

### 3. GGR e NGR — Total por período

```dax
EVALUATE
ROW(
  "GGR",
  CALCULATE(
    ABS(
      SUMX(
        FILTER(
          FactAGGAccountTransaction,
          FactAGGAccountTransaction[account_transaction_type] = "GAME_BET"
        ),
        FactAGGAccountTransaction[amount]
      )
    ) -
    SUMX(
      FILTER(
        FactAGGAccountTransaction,
        FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN", "CASH_OUT", "CORRECTION"}
      ),
      FactAGGAccountTransaction[amount]
    ),
    FILTER(
      DimDate,
      DimDate[dim_date_key] >= 20260501 &&
      DimDate[dim_date_key] <= 20260521
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  ),
  "NGR",
  CALCULATE(
    ABS(
      SUMX(
        FILTER(
          FactAGGAccountTransaction,
          FactAGGAccountTransaction[account_transaction_type] = "GAME_BET"
        ),
        FactAGGAccountTransaction[amount]
      )
    ) -
    SUMX(
      FILTER(
        FactAGGAccountTransaction,
        FactAGGAccountTransaction[account_transaction_type] IN {"GAME_WIN", "CASH_OUT", "CORRECTION"}
      ),
      FactAGGAccountTransaction[amount]
    ) -
    SUMX(
      FILTER(
        FactAGGAccountTransaction,
        FactAGGAccountTransaction[account_transaction_type] IN {"CRE_BONUS", "PRODUC_BON", "MAN_BONUS"}
      ),
      FactAGGAccountTransaction[amount]
    ),
    FILTER(
      DimDate,
      DimDate[dim_date_key] >= 20260501 &&
      DimDate[dim_date_key] <= 20260521
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  )
)
```

> **GGR** = `ABS(GAME_BET) - (GAME_WIN + CASH_OUT + CORRECTION)`
> **NGR** = `GGR - (CRE_BONUS + PRODUC_BON + MAN_BONUS)`

---

### 4. Gross Bets — Total por período

```dax
EVALUATE
ROW(
  "GrossBets",
  CALCULATE(
    ABS(
      SUMX(
        FILTER(
          FactAGGAccountTransaction,
          FactAGGAccountTransaction[account_transaction_type] = "GAME_BET"
        ),
        FactAGGAccountTransaction[amount]
      )
    ),
    FILTER(
      DimDate,
      DimDate[dim_date_key] >= 20260501 &&
      DimDate[dim_date_key] <= 20260521
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  )
)
```

---

### 5. Ticket Médio de Primeiro Depósito

```dax
EVALUATE
ROW(
  "AvgFirstDeposit",
  CALCULATE(
    AVERAGEX(
      FactFirstDeposit,
      FactFirstDeposit[payment_amount]
    ),
    FILTER(
      FactFirstDeposit,
      FactFirstDeposit[payment_processed_ONLY_date] >= DATE(2026,5,1) &&
      FactFirstDeposit[payment_processed_ONLY_date] <= DATE(2026,5,21)
    ),
    FILTER(
      DimPlayer,
      DimPlayer[internal_external_player] = "External" &&
      DimPlayer[player_country] = "BR" &&
      DimPlayer[brand_name] = "BWBRA"
    )
  )
)
```

---

### 6. FTDs por Canal (utm_medium)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  DimPlayer[utm_medium],
  FILTER(
    FactFirstDeposit,
    FactFirstDeposit[payment_processed_ONLY_date] >= DATE(2026,5,1) &&
    FactFirstDeposit[payment_processed_ONLY_date] <= DATE(2026,5,21)
  ),
  FILTER(
    DimPlayer,
    DimPlayer[internal_external_player] = "External" &&
    DimPlayer[player_country] = "BR" &&
    DimPlayer[brand_name] = "BWBRA"
  ),
  "FTDs", COUNTROWS(FactFirstDeposit)
)
ORDER BY [FTDs] DESC
```

---

### 7. FullReg por Canal (utm_medium)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  DimPlayer[utm_medium],
  FILTER(
    DimDate,
    DimDate[dim_date_key] >= 20260501 &&
    DimDate[dim_date_key] <= 20260521
  ),
  FILTER(
    DimPlayer,
    DimPlayer[internal_external_player] = "External" &&
    DimPlayer[player_country] = "BR" &&
    DimPlayer[brand_name] = "BWBRA"
  ),
  "FullReg", COUNTROWS(FactFullRegistration)
)
ORDER BY [FullReg] DESC
```

---

### 8. Gross Bets + Apostadores por Canal (utm_medium)

```dax
EVALUATE
SUMMARIZECOLUMNS(
  DimPlayer[utm_medium],
  FILTER(
    DimDate,
    DimDate[dim_date_key] >= 20260501 &&
    DimDate[dim_date_key] <= 20260521
  ),
  FILTER(
    DimPlayer,
    DimPlayer[internal_external_player] = "External" &&
    DimPlayer[player_country] = "BR" &&
    DimPlayer[brand_name] = "BWBRA"
  ),
  "GrossBets", ABS(
    SUMX(
      FILTER(
        FactAGGAccountTransaction,
        FactAGGAccountTransaction[account_transaction_type] = "GAME_BET"
      ),
      FactAGGAccountTransaction[amount]
    )
  ),
  "Apostadores", DISTINCTCOUNT(DimPlayer[dim_player_key])
)
ORDER BY [GrossBets] DESC
```

---

## Mapeamento de Canais (utm_medium)

| utm_medium | Canal no WPR |
|------------|--------------|
| `paid_media` | Paid Media (Google, Programático) |
| `affiliate` | Affiliates |
| `social_paid` | Paid Social (Meta, TikTok, X) |
| `organic` / `(none)` / `direct` / vazio | Orgânico/Direto |
| demais | Others |

> **NÃO usar `utm_source`** — não está configurado corretamente no GA4/PowerBI.
> **NÃO usar `ta_affiliate`** — retorna 0 para maio; campo legado.
> Usar sempre `DimPlayer[utm_medium]` como identificador de canal.

---

## Leitura de Resultado via Python

```python
import requests, json

def pbi_query(dax: str, token: str) -> list:
    url = f"https://api.powerbi.com/v1.0/myorg/groups/00ecb2bb-6c61-4d09-badb-a4df0c948b02/datasets/c489d219-ef18-4f9e-9c5c-422c9092e3aa/executeQueries"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {"queries": [{"query": dax}], "serializerSettings": {"includeNulls": True}}
    r = requests.post(url, headers=headers, json=body)
    return r.json()["results"][0]["tables"][0]["rows"]

# Leitura do token
with open("/root/.claude/credentials/pbi_access_token.txt") as f:
    token = f.read().strip()

# Leitura de resultado escalar
rows = pbi_query(DAX_SCALAR, token)
value = rows[0]["[NomeColuna]"]

# Leitura de resultado tabular (SUMMARIZECOLUMNS)
rows = pbi_query(DAX_TABLE, token)
for r in rows:
    canal = r.get("DimPlayer[utm_medium]", "N/A")
    ftds  = r.get("[FTDs]", 0)
```

> Chave de acesso a colunas escalares: `"[NomeDaMedida]"` (com colchetes).
> Chave de acesso a colunas de dimensão: `"NomeTabela[NomeColuna]"` (sem colchetes externos).

---

## Renovação do Token

```bash
# Verificar se token ainda é válido (expires_at em epoch)
cat ~/.claude/credentials/pbi_access_token.txt

# Renovar manualmente via refresh_token
python3 - <<'EOF'
import requests, json
from pathlib import Path

creds_dir = Path.home() / ".claude/credentials"
refresh_token = (creds_dir / "pbi_refresh_token.txt").read_text().strip()

r = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token", data={
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
    "client_id": "<CLIENT_ID>",  # ver agents-registry.md
    "scope": "https://analysis.windows.net/powerbi/api/.default offline_access"
})
data = r.json()
(creds_dir / "pbi_access_token.txt").write_text(data["access_token"])
if "refresh_token" in data:
    (creds_dir / "pbi_refresh_token.txt").write_text(data["refresh_token"])
print(f"Token renovado. Expira em {data['expires_in']}s")
EOF
```

---

## Valores de Referência — WPR 01–21/mai/2026

| Métrica | JAN | FEV | MAR | ABR | MAI |
|---------|-----|-----|-----|-----|-----|
| FullReg | 5.667 | 5.765 | 7.386 | 10.507 | 9.349 |
| FTDs | 1.491 | 879 | 1.099 | 3.160 | 2.156 |
| CR% | 26,3% | 15,3% | 14,9% | 30,1% | 23,1% |
| GGR (R$) | -96k | 46k | 119k | 176k | 268k |
| NGR (R$) | -160k | -23k | 68k | 159k | 248k |
| Margem NGR | -1,8% | 1,9% | 4,6% | 3,4% | 5,5% |
| Gross Bets (R$) | 5.461k | 2.397k | 2.569k | 5.138k | 4.906k |
| Avg 1º Dep (R$) | R$839 | R$387 | R$252 | R$152 | R$125 |

---

*Última atualização: 22/05/2026 — Bira*
