# Migração de Máquina — Claude Code (Darwin)

> Checklist pra continuar trabalhando com o Bira (Claude Code) num Mac novo **sem perder histórico/memória**.
> Gerado 31/07/2026. Caminhos verificados no Mac atual (user `darwingodoy`, home `/Users/darwingodoy`).

## TL;DR
O **trabalho versionado** vem sozinho no `git clone` — não precisa copiar arquivo por arquivo. O que **quebra** se você esquecer são **3 coisas que ficam FORA do repo**: a **memória**, as **credenciais OAuth do Google** e a **config/MCP**.

> **Jeito mais fácil:** se usar o **Assistente de Migração da Apple** (copia o home inteiro), *tudo* isso já vai junto (repo + memória + credenciais + config) e é só refazer os logins dos conectores. O passo a passo abaixo é pro caso de **setup manual/limpo**.

## O que está onde

| Item | Local | Vem no `git clone`? |
|---|---|---|
| Trabalho (WPR, projetos, docs) | `~/Documents/Claude` | ✅ sim |
| **Memória** (nossos aprendizados) | `~/.claude/projects/-Users-darwingodoy-Documents-Claude/memory/` | ❌ não |
| **Credenciais Google OAuth** | `~/.google_workspace_mcp/` | ❌ não |
| Config global do Claude Code | `~/.claude.json` + `~/.claude/` | ❌ não |
| Servidores MCP do projeto | `.mcp.json` (raiz do repo) | ❌ (gitignored) |
| Dados pesados (xlsx/pdf/PII) | vários (gitignored) | ❌ não |

## Passo a passo (Mac novo, setup manual)

### 0. Pré-requisitos
- Instalar o **Claude Code**.
- Configurar **chave SSH no GitHub** (ou usar HTTPS + token).
- **Manter o mesmo usuário (`darwingodoy`) e o repo em `~/Documents/Claude`.** Isso faz a memória religar sozinha (o nome da pasta de memória codifica esse caminho). Se for diferente, ver a seção final.

### 1. Clonar o repo (traz todo o trabalho versionado)
```bash
git clone git@github.com:ddarwingodoy-cloud/ClaudeCode.git ~/Documents/Claude
```

### 2. Copiar o que fica FORA do repo (do Mac antigo → novo)
Via disco externo, AirDrop ou `rsync` na rede (troque `MACNOVO` pelo host/destino):
```bash
# Memória — CRÍTICO (sem isso o Bira começa amnésico)
rsync -av ~/.claude/ MACNOVO:~/.claude/

# Credenciais Google OAuth (Gmail/Sheets/Drive/Calendar via Bash)
rsync -av ~/.google_workspace_mcp/ MACNOVO:~/.google_workspace_mcp/
```
> `~/.claude/` (~224M) já inclui memória + sessões + config global. Se quiser só o essencial da memória, copie apenas:
> `~/.claude/projects/-Users-darwingodoy-Documents-Claude/memory/` (70 arquivos, ~340K).

### 3. MCP do projeto
O `.mcp.json` da raiz é gitignored — copiar do Mac antigo:
```bash
rsync -av ~/Documents/Claude/.mcp.json MACNOVO:~/Documents/Claude/.mcp.json
```

### 4. Re-login dos conectores
Slack, GA4, Google Workspace, Atlassian etc. são atrelados à **conta Claude/Google**. Abrir o Claude Code e refazer a autorização onde pedir (comando `/mcp` no terminal).

### 5. Dados pesados (opcional, só se for usar)
Não vêm no clone (gitignored): `Semanais/WPR/*.xlsx` e `*.pdf` (Midia, PACING, Gross Bets, Search Evidence), `Financeiro/` (Databook), `Pessoal/` (PII). Copiar manualmente se precisar.

## Verificação (no Mac novo)
1. Abrir o Claude Code em `~/Documents/Claude` — o Bira deve reconhecer o contexto (BetWarrior, WPR, memórias). Se ele "não lembrar", a memória não carregou → conferir o caminho da pasta (seção abaixo).
2. Pedir pro Bira **ler algo do Gmail/Sheets** — testa `~/.google_workspace_mcp`.
3. `git status` limpo + `git pull` OK.
4. Rodar `Semanais/WPR/wpr_pull.py` — confirma o pipeline Power BI (renova token sozinho; se falhar, refazer o Device Code Flow).

## Se o usuário/caminho for DIFERENTE no Mac novo
A pasta de memória tem o **caminho do repo codificado no nome** (`/` viram `-`). Se o novo caminho não for `/Users/darwingodoy/Documents/Claude`, renomeie a pasta pra bater com o novo:
```
~/.claude/projects/-Users-<novo-user>-Documents-Claude/memory/
```
Exemplo: se o repo ficar em `/Users/dgodoy/Claude`, a pasta vira `-Users-dgodoy-Claude`.

---
*Mantido no repo pra estar sempre à mão. Se algum caminho mudar, atualizar aqui.*
