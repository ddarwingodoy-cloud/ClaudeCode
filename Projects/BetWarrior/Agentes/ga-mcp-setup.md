# Conexão com Google Analytics via MCP — Darwin / Claude Code

**Data:** 2026-04-29
**De:** Darwin Godoy (Claude Code)
**Para:** Betinho (JP)
**Contexto:** Handoff técnico sobre como configurei acesso ao GA4 da BetWarrior Brasil no meu ambiente Claude Code.

---

## 1. MCP Server utilizado

Pacote: [`mcp-google-analytics`](https://pypi.org/project/mcp-google-analytics/)
Instalado via `uvx` (não requer instalação permanente).

Configuração em `.mcp.json` (na raiz do projeto Claude):

```json
"google-analytics": {
  "command": "/Users/darwingodoy/.local/bin/uvx",
  "args": ["mcp-google-analytics"],
  "env": {
    "GOOGLE_ANALYTICS_CLIENT_ID": "<client_id>",
    "GOOGLE_ANALYTICS_CLIENT_SECRET": "<client_secret>",
    "GOOGLE_ANALYTICS_REFRESH_TOKEN": "<refresh_token>",
    "GOOGLE_ANALYTICS_PROPERTY_ID": "512299072"
  }
}
```

**Property ID correto:** `512299072` (New Brazil - All - Prod)
Atenção: `140921421` é o ID da **conta**, não da property — esse erro causou falha na configuração inicial.

---

## 2. Autenticação

OAuth2 via refresh token. O token foi gerado com a conta `darwingodoy@betwarrior.com` com escopo `analytics.readonly`.

Para gerar um novo refresh token (se necessário):

1. Acessar [Google Cloud Console](https://console.cloud.google.com)
2. Criar credencial OAuth2 (tipo: Desktop App)
3. Usar o OAuth Playground ou um script local para trocar authorization code por refresh token
4. Garantir que a conta usada tem acesso à property no GA4

---

## 3. Capacidades do MCP tool

O servidor MCP expõe três ferramentas:

| Ferramenta | Descrição |
|---|---|
| `get_accounts` | Lista contas GA disponíveis |
| `get_properties` | Lista properties de uma conta |
| `run_report` | Executa relatório com métricas, dimensões e intervalo de datas |

**Limitação importante:** o `run_report` do MCP **não suporta `dimensionFilter`**. Não é possível filtrar por `eventName` diretamente pela ferramenta.

---

## 4. Workaround para filtrar por evento (ex: `deposit_ftd`)

Para filtrar eventos específicos por dimensão (ex: FTDs por canal), usamos a **GA4 Data API diretamente** via Python stdlib (`urllib`), reaproveitando o mesmo refresh token:

```python
import urllib.request, urllib.parse, json

# 1. Obter access token a partir do refresh token
token_data = urllib.parse.urlencode({
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN,
    "grant_type": "refresh_token"
}).encode()

req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_data, method="POST")
with urllib.request.urlopen(req) as resp:
    access_token = json.loads(resp.read())["access_token"]

# 2. Chamar a API com dimensionFilter
payload = {
    "dateRanges": [{"startDate": "2026-04-01", "endDate": "2026-04-28"}],
    "dimensions": [{"name": "sessionDefaultChannelGroup"}],
    "metrics": [{"name": "eventCount"}, {"name": "totalUsers"}],
    "dimensionFilter": {
        "filter": {
            "fieldName": "eventName",
            "stringFilter": {"matchType": "EXACT", "value": "deposit_ftd"}
        }
    },
    "orderBys": [{"metric": {"metricName": "eventCount"}, "desc": True}]
}

url = f"https://analyticsdata.googleapis.com/v1beta/properties/{PROPERTY_ID}:runReport"
req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST", headers={
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
})

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
```

Não há dependência de pacotes externos — funciona com Python 3.9+ puro.

---

## 5. Eventos rastreados confirmados

Eventos identificados na property `512299072` em abril/2026:

| Evento | Volume (abr/26) | Observação |
|---|---|---|
| `page_view` | 1.095.958 | — |
| `session_start` | 428.503 | — |
| `first_visit` | 297.546 | — |
| `add_to_cart` | 130.768 | Bet adicionada ao carrinho |
| `place_bet` | 29.193 | Aposta confirmada |
| `sign_up` | 10.818 | Cadastro concluído |
| `purchase` | 9.166 | — |
| `deposit_ftd` | 2.961 | Primeiro depósito — evento principal para aquisição |

**Alerta:** foram identificados event names com payloads de injeção (SQL injection, XSS, path traversal). Volume mínimo (1 ocorrência cada), mas vale notificar o time de segurança.

---

## 6. Observações finais

- O MCP funciona bem para relatórios agregados (sessões, usuários, pageviews por dimensão)
- Para análises de funil com filtro por evento, usar a API direta (script acima)
- As credenciais OAuth ficam no `.mcp.json` local — não commitar no repositório
- Testar acesso após qualquer rotação de token com `get_accounts` (deve retornar conta `Betwarrior`, ID `140921421`)
