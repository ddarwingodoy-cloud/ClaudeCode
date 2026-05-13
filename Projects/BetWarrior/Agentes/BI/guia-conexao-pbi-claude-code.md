# Guia: Conectar o Claude Code ao Power BI

> **Para:** Lucas Vagione
> **De:** JP Marques
> **Data:** 17/Abr/2026

---

## O que vamos fazer

Conectar o Claude Code (via VS Code) ao Power BI usando a API REST oficial da Microsoft. Com isso, o Claude Code consegue:

- Executar queries DAX diretamente no dataset
- Extrair KPIs sem precisar abrir o Power BI
- Automatizar relatórios e análises

A conexão usa **OAuth2 Device Code Flow** — um método seguro que não precisa registrar nenhum app no Azure. Usamos um Client ID público do próprio Power BI.

---

## Pré-requisitos

- VS Code com Claude Code instalado
- Acesso ao Power BI com permissão **Build** no dataset (você já tem como Admin)
- Conta Microsoft corporativa (@betwarrior.com ou @m4xconsulting.com)

---

## Passo 1 — Criar pasta para credenciais

No terminal do VS Code (PowerShell no Windows), crie uma pasta para guardar os tokens:

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\credentials"
```

---

## Passo 2 — Obter o token (Device Code Flow)

Peça ao Claude Code para executar o seguinte comando. Ele vai gerar um código que você precisa digitar no browser.

```powershell
# Gerar o código de autenticação
curl -s -X POST "https://login.microsoftonline.com/organizations/oauth2/v2.0/devicecode" `
  -d "client_id=ea0616ba-638b-4df5-95b9-636659ae5121" `
  -d "scope=https://analysis.windows.net/powerbi/api/.default offline_access"
```

A resposta vai ter algo como:

```json
{
  "user_code": "ABCD1234",
  "device_code": "xxxxx_longo_xxxxx",
  "verification_uri": "https://microsoft.com/devicelogin",
  "message": "To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ABCD1234"
}
```

**Faça o seguinte:**
1. Abra o browser e vá em **https://microsoft.com/devicelogin**
2. Digite o código que apareceu (ex: `ABCD1234`)
3. Faça login com sua conta corporativa
4. Autorize o acesso

---

## Passo 3 — Capturar os tokens

Depois de autorizar no browser, peça ao Claude Code para capturar o token usando o `device_code` da resposta anterior:

```powershell
curl -s -X POST "https://login.microsoftonline.com/organizations/oauth2/v2.0/token" `
  -d "client_id=ea0616ba-638b-4df5-95b9-636659ae5121" `
  -d "grant_type=urn:ietf:params:oauth:grant-type:device_code" `
  -d "device_code=COLE_O_DEVICE_CODE_AQUI"
```

A resposta vai ter `access_token` e `refresh_token`. Salve ambos:

```powershell
# Salvar o access token (expira em ~1h)
"COLE_O_ACCESS_TOKEN" | Out-File -FilePath "$env:USERPROFILE\.claude\credentials\pbi_access_token.txt" -NoNewline

# Salvar o refresh token (dura ~90 dias)
"COLE_O_REFRESH_TOKEN" | Out-File -FilePath "$env:USERPROFILE\.claude\credentials\pbi_refresh_token.txt" -NoNewline
```

> **Dica:** Você pode pedir ao Claude Code para fazer tudo isso automaticamente. Basta dizer: *"Execute o Device Code Flow do Power BI, salve os tokens e me diga o código para eu autorizar no browser"*. Ele sabe fazer.

---

## Passo 4 — Testar a conexão

Peça ao Claude Code para executar uma query simples:

```powershell
$TOKEN = Get-Content "$env:USERPROFILE\.claude\credentials\pbi_access_token.txt"
$GROUP_ID = "00ecb2bb-6c61-4d09-badb-a4df0c948b02"
$DATASET_ID = "c489d219-ef18-4f9e-9c5c-422c9092e3aa"

curl -s -X POST "https://api.powerbi.com/v1.0/myorg/groups/$GROUP_ID/datasets/$DATASET_ID/executeQueries" `
  -H "Authorization: Bearer $TOKEN" `
  -H "Content-Type: application/json" `
  -d '{"queries":[{"query":"EVALUATE ROW(\"teste\", 1+1)"}],"serializerSettings":{"includeNulls":true}}'
```

Se retornar `{"results":[{"tables":[{"rows":[{"[teste]":2}]}]}]}`, está funcionando!

---

## Passo 5 — Renovar o token automaticamente

O access token expira em ~1 hora. Para renovar sem precisar refazer o login:

```powershell
$REFRESH = Get-Content "$env:USERPROFILE\.claude\credentials\pbi_refresh_token.txt"

curl -s -X POST "https://login.microsoftonline.com/organizations/oauth2/v2.0/token" `
  -d "client_id=ea0616ba-638b-4df5-95b9-636659ae5121" `
  -d "grant_type=refresh_token" `
  -d "refresh_token=$REFRESH" `
  -d "scope=https://analysis.windows.net/powerbi/api/.default offline_access"
```

Isso retorna novos `access_token` e `refresh_token`. Salve ambos nos mesmos arquivos.

> **Na prática:** O Claude Code faz isso sozinho antes de cada consulta. Basta configurar os caminhos dos tokens no CLAUDE.md dele (ver passo 6).

---

## Passo 6 — Configurar o CLAUDE.md

Crie ou edite o arquivo `CLAUDE.md` na raiz do seu projeto no VS Code com as informações de conexão:

```markdown
## Power BI

- Client ID: ea0616ba-638b-4df5-95b9-636659ae5121
- Token: C:\Users\SEU_USUARIO\.claude\credentials\pbi_access_token.txt
- Refresh token: C:\Users\SEU_USUARIO\.claude\credentials\pbi_refresh_token.txt
- Group ID: 00ecb2bb-6c61-4d09-badb-a4df0c948b02
- Dataset ID: c489d219-ef18-4f9e-9c5c-422c9092e3aa

### Refresh automático
Antes de qualquer query, renovar o token:
- Ler refresh token do arquivo
- POST para https://login.microsoftonline.com/organizations/oauth2/v2.0/token
- Salvar novos tokens nos arquivos
```

Com isso, toda vez que você pedir ao Claude Code para buscar dados no PBI, ele vai saber como se conectar.

---

## Referência rápida

| Item | Valor |
|------|-------|
| **Client ID** | `ea0616ba-638b-4df5-95b9-636659ae5121` |
| **Group ID (Brazil's Reports)** | `00ecb2bb-6c61-4d09-badb-a4df0c948b02` |
| **Dataset ID (Brazil Main Report)** | `c489d219-ef18-4f9e-9c5c-422c9092e3aa` |
| **Token endpoint** | `https://login.microsoftonline.com/organizations/oauth2/v2.0/token` |
| **Device code endpoint** | `https://login.microsoftonline.com/organizations/oauth2/v2.0/devicecode` |
| **API base** | `https://api.powerbi.com/v1.0/myorg/` |
| **Scope** | `https://analysis.windows.net/powerbi/api/.default offline_access` |

---

## Diferenças Windows vs Mac

| Item | Mac (JP) | Windows (Lucas) |
|------|----------|-----------------|
| **Terminal** | zsh/bash | PowerShell |
| **Caminho tokens** | `~/.claude/credentials/` | `%USERPROFILE%\.claude\credentials\` |
| **Quebra de linha em curl** | `\` | `` ` `` (backtick) |
| **Salvar arquivo** | `echo "token" > arquivo.txt` | `"token" \| Out-File arquivo.txt` |
| **Ler arquivo** | `cat arquivo.txt` | `Get-Content arquivo.txt` |

O resto (endpoints, Client ID, queries DAX) é idêntico.

---

## Troubleshooting

**"Unauthorized" ou 401:**
- O access token expirou. Rode o refresh (Passo 5).

**"Forbidden" ou 403:**
- Sem permissão Build no dataset. Verificar no Power BI Service > Dataset > Settings > Permissions.

**"Bad Request" ou erro na query DAX:**
- Verificar sintaxe da query. Testar com algo simples primeiro: `EVALUATE ROW("x", 1)`.

**Refresh token falhou:**
- Expirou (~90 dias). Refazer o Device Code Flow (Passo 2).

**curl não encontrado no Windows:**
- O Windows 10+ já vem com curl. Se não tiver, instalar via `winget install cURL.cURL`.

---

## Observação sobre segurança

- Os tokens são pessoais e dão acesso aos dados do PBI com a sua conta
- **Nunca commitar tokens no Git** — adicionar `credentials/` no `.gitignore`
- O Client ID é público (do Power BI Desktop) — não é um segredo
- O refresh token é o mais sensível — quem tiver ele, tem acesso por 90 dias
