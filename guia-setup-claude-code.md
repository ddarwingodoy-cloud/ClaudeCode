# Guia de Setup — Claude Code + VSCode

> Como organizar seu Claude Code para ele funcionar como um assistente permanente, com memoria, contexto e automacoes.

---

## 1. CLAUDE.md — O cerebro do agente

### O que e

Um arquivo markdown na raiz do seu projeto que o Claude le automaticamente toda vez que uma sessao comeca. E como um briefing permanente — voce escreve uma vez e ele sempre sabe quem e, onde esta e o que fazer.

Sem esse arquivo, toda sessao comeca do zero. Com ele, o Claude ja chega sabendo seu nome, seu cargo, seus projetos, suas regras e suas preferencias.

### Onde criar

```
seu-projeto/
  CLAUDE.md    <-- aqui, na raiz
  pasta1/
  pasta2/
```

### O que colocar

Pense no CLAUDE.md como o onboarding de um funcionario novo que vai trabalhar com voce todo dia. Ele precisa saber:

**Bloco 1 — Quem voce e e o que o agente faz**
```markdown
# Meu Projeto

Voce e o assistente do [seu nome], [seu cargo] na [empresa].
Seu papel e ajudar com [lista de tarefas principais].
Sempre responda em [idioma].
```

**Bloco 2 — Estrutura do projeto**
```markdown
## Estrutura de Pastas

projeto/
  Docs/        — documentos e reports
  Dados/       — datasets, exports
  Scripts/     — automacoes
```

Isso evita que ele fique perdido procurando arquivos.

**Bloco 3 — Pessoas-chave**
```markdown
## Pessoas

- Maria — CEO, tom direto, prefere bullet points
- Carlos — Tech Lead, detalhista, quer ver codigo
- Ana — Cliente principal, comunicacao sempre em ingles
```

Quando voce pedir "manda um email pro Carlos", ele ja sabe o tom certo.

**Bloco 4 — Regras de negocio**
```markdown
## Regras

- Moeda padrao: BRL
- Nunca enviar mensagens sem minha aprovacao
- Documentos internos em portugues, externos em ingles
```

**Bloco 5 — Ferramentas e integracoes**
```markdown
## Ferramentas

- Slack: conectado via MCP, pode ler canais
- GitHub: repo privado, pode commitar
- Google: Gmail, Calendar, Drive conectados
```

### Dicas

- **Seja especifico.** "Responda de forma concisa" e melhor que "seja bom".
- **Atualize conforme evolui.** O CLAUDE.md e vivo — quando mudar algo no projeto, atualize.
- **Nao coloque dados sensiveis** (tokens, senhas). Use referencias a arquivos separados.
- O arquivo pode ter 100-500 linhas tranquilamente. O Claude le tudo.

---

## 2. Sistema de Memoria — Aprendizado entre sessoes

### O que e

O Claude Code tem um sistema de memoria persistente que salva informacoes entre conversas. E como se ele tivesse um caderno de anotacoes que consulta no inicio de cada sessao.

A memoria funciona com arquivos markdown organizados em uma pasta dedicada, indexados por um arquivo central (`MEMORY.md`).

### Estrutura

```
~/.claude/projects/[hash-do-projeto]/memory/
  MEMORY.md              <-- indice (carregado automaticamente)
  user_perfil.md          <-- quem voce e
  feedback_estilo.md      <-- correcoes e preferencias
  project_xyz.md          <-- contexto de projetos
  reference_links.md      <-- ponteiros para recursos
```

### Tipos de memoria

**User** — informacoes sobre voce que ajudam a personalizar respostas
```markdown
---
name: Perfil do usuario
description: Cargo, expertise e preferencias do usuario
type: user
---

Senior developer com 10 anos de Go, primeira vez mexendo em React.
Prefere respostas diretas sem explicacao excessiva.
```

**Feedback** — correcoes que voce fez e que ele nao deve repetir
```markdown
---
name: Nunca usar mocks nos testes
description: Testes de integracao devem bater no banco real, nunca usar mocks
type: feedback
---

Testes de integracao devem usar banco real, nao mocks.

**Why:** Mock/prod divergiu e um bug passou para producao.
**How to apply:** Em qualquer teste que envolva banco, usar container Docker com banco real.
```

**Project** — contexto de trabalho em andamento
```markdown
---
name: Migracao para microservicos
description: Projeto de migracao do monolito, deadline em junho
type: project
---

Migracao do monolito para microservicos. Deadline: 15/Jun/2026.

**Why:** Performance degradando com crescimento de usuarios.
**How to apply:** Toda decisao de arquitetura deve considerar o split futuro.
```

**Reference** — onde encontrar informacao
```markdown
---
name: Bugs no Linear
description: Bugs sao rastreados no projeto BACKEND do Linear
type: reference
---

Bugs de backend sao rastreados no Linear, projeto "BACKEND".
Usar antes de criar issues duplicadas.
```

### Como funciona na pratica

1. Voce corrige o Claude: "nao faz assim, faz assado"
2. Ele salva uma memoria de feedback
3. Na proxima sessao (dias depois), ele le o MEMORY.md e sabe que nao deve repetir o erro

O MEMORY.md e um indice simples — cada linha aponta para um arquivo:
```markdown
# Memory

## Perfil
- [Perfil do usuario](user_perfil.md) — Senior Go dev, novo em React

## Feedback
- [Nunca usar mocks](feedback_mocks.md) — testes sempre com banco real
- [Formato de commit](feedback_commits.md) — conventional commits obrigatorio

## Projetos
- [Migracao microservicos](project_migracao.md) — deadline junho, fase 2
```

### Dicas

- **Peca para ele lembrar.** Diga "lembre disso para proximas sessoes" e ele salva.
- **Peca para ele esquecer.** Diga "esquece aquela regra sobre X" e ele remove.
- **Feedback e o tipo mais valioso.** Sao as correcoes que evitam erros recorrentes.
- **Nao salve coisas que estao no codigo.** Memoria e para o que NAO da pra derivar lendo o projeto.
- **Mantenha o MEMORY.md curto.** Ele e carregado em toda sessao — linhas depois de 200 sao truncadas.

---

## 3. Hooks — Automacoes em eventos

### O que e

Hooks sao scripts shell que executam automaticamente quando certos eventos acontecem no Claude Code. Pense neles como triggers: "quando X acontecer, rode Y".

### Onde configurar

Os hooks sao configurados no `settings.json` do Claude:

```
~/.claude/settings.json
```

Ou no settings do projeto:

```
~/.claude/projects/[hash]/settings.json
```

Os scripts ficam numa pasta separada:

```
~/.claude/hooks/
  meu-hook.sh
```

### Eventos disponiveis

| Evento | Quando dispara |
|---|---|
| **PreToolUse** | Antes de qualquer ferramenta ser executada |
| **PostToolUse** | Depois de uma ferramenta executar |
| **PreCompact** | Antes do contexto ser compactado (quando a conversa fica grande) |
| **Stop** | Quando a sessao encerra |
| **SessionStart** | Quando uma nova sessao inicia |
| **SubagentStart/Stop** | Quando um sub-agente inicia ou para |

### Exemplo 1 — Alerta antes de compactacao

O contexto do Claude tem limite. Quando a conversa fica longa demais, ele compacta (resume) o historico. Esse hook avisa antes disso acontecer para que informacoes criticas sejam salvas.

**Arquivo:** `~/.claude/hooks/context-monitor.sh`
```bash
#!/bin/bash
INPUT=$(cat)
jq -n '{
  "continue": true,
  "systemMessage": "AVISO: O contexto vai ser compactado. Salve informacoes criticas antes de continuar."
}'
exit 0
```

**Configuracao no settings.json:**
```json
{
  "hooks": {
    "PreCompact": [
      {
        "hooks": [
          {
            "command": "$HOME/.claude/hooks/context-monitor.sh",
            "type": "command"
          }
        ],
        "matcher": ".*"
      }
    ]
  }
}
```

### Exemplo 2 — Salvar timestamp da sessao

Quando a sessao encerra (timeout, voce fecha, etc), salva um marcador para a proxima sessao saber quando foi a ultima.

**Arquivo:** `~/.claude/hooks/session-save.sh`
```bash
#!/bin/bash
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
mkdir -p "$HOME/.claude/sessions"
echo "Ultima sessao: $TIMESTAMP" > "$HOME/.claude/sessions/last-session.md"
cat <<EOF
{
  "continue": true,
  "reason": "Sessao salva"
}
EOF
exit 0
```

### Exemplo 3 — Bloquear escritas externas sem aprovacao

Esse e um guardrail. Antes de qualquer ferramenta que modifica sistemas externos (Slack, email, Jira), o hook bloqueia e pede confirmacao.

**Configuracao no settings.json:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "hooks": [
          {
            "command": "echo '{\"decision\": \"block\", \"reason\": \"Escrita externa bloqueada. Peca aprovacao ao usuario.\"}'",
            "type": "command"
          }
        ],
        "matcher": "mcp__slack.*post_message|mcp__google.*send_gmail"
      }
    ]
  }
}
```

O `matcher` usa regex para filtrar quais ferramentas disparam o hook. Nesse caso, so bloqueia post_message do Slack e send_gmail do Google.

### Como funciona tecnicamente

1. O evento acontece (ex: PreCompact)
2. O Claude Code executa o script shell
3. O script recebe dados do evento via stdin (JSON)
4. O script retorna JSON com instrucoes:
   - `"continue": true` — segue normalmente
   - `"continue": false` — bloqueia a acao
   - `"decision": "block"` — bloqueia com motivo (para PreToolUse)
   - `"systemMessage": "..."` — injeta instrucao no contexto

### Dicas

- **Comece com PreCompact.** E o mais util e o mais seguro — so avisa, nao bloqueia nada.
- **Guardrails em PreToolUse sao poderosos** mas cuidado para nao bloquear demais. Use o `matcher` para filtrar.
- **Teste seus hooks** rodando o script manualmente: `echo '{}' | bash meu-hook.sh`
- **Hooks devem ser rapidos.** Se demorar, trava o Claude. Nada de chamadas HTTP nos hooks.
- **jq e util** para gerar JSON valido no bash. Instale se nao tiver: `brew install jq`

---

## 4. Permissoes — Controle do que o agente pode fazer

### O que e

O Claude Code pede aprovacao toda vez que vai executar uma acao (ler arquivo, rodar comando, chamar MCP). Isso e seguro, mas fica cansativo. O sistema de permissoes permite voce pre-aprovar acoes de leitura e manter aprovacao manual so para acoes de escrita.

A ideia e simples: **ler e pesquisar pode sempre, escrever e modificar precisa de OK**.

### Onde configurar

```
~/.claude/settings.json
```

Dentro da chave `permissions`:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash(*)",
      "mcp__slack__slack_get_channel_history",
      "mcp__google__search_gmail_messages"
    ],
    "additionalDirectories": [
      "/tmp",
      "/Users/seu-usuario/.config"
    ]
  }
}
```

### O que cada campo faz

**`allow`** — lista de ferramentas pre-aprovadas. O Claude executa sem perguntar.

**`additionalDirectories`** — pastas fora do projeto que o agente pode acessar (ex: `/tmp` para scripts temporarios, pasta de credenciais).

### Estrategia recomendada

**Liberar leitura total:**
```json
"allow": [
  "Read",
  "Write",
  "Edit",
  "Glob",
  "Grep",
  "WebFetch",
  "WebSearch",
  "Bash(*)"
]
```

Isso libera todas as ferramentas de arquivo e terminal. O Claude le, escreve, edita e roda comandos sem perguntar. Para a maioria dos casos de desenvolvimento, isso e o ideal — voce ve o que ele faz no output e pode reverter com git.

**Liberar leitura de MCPs (mas nao escrita):**

Para cada MCP conectado, libere as ferramentas de leitura:

```json
"allow": [
  "mcp__slack__slack_get_channel_history",
  "mcp__slack__slack_get_thread_replies",
  "mcp__slack__slack_list_channels",
  "mcp__slack__slack_get_users",

  "mcp__google__search_gmail_messages",
  "mcp__google__get_gmail_message_content",
  "mcp__google__get_events",
  "mcp__google__list_drive_items",
  "mcp__google__read_sheet_values",

  "mcp__jira__jira_search",
  "mcp__jira__jira_get_issue",

  "mcp__github__list_issues",
  "mcp__github__get_file_contents"
]
```

**Manter com aprovacao manual (NAO colocar no allow):**
- `mcp__slack__slack_post_message` — enviar mensagens
- `mcp__google__send_gmail_message` — enviar emails
- `mcp__google__modify_sheet_values` — alterar planilhas
- `mcp__jira__jira_create_issue` — criar issues
- `mcp__jira__jira_transition_issue` — mover issues

Assim o Claude pesquisa livremente no Slack, Gmail, Jira, Drive, mas sempre pergunta antes de enviar uma mensagem, criar uma issue ou modificar um documento.

### O padrao de nomes dos MCPs

As permissoes seguem o formato:
```
mcp__[nome-do-server]__[nome-da-ferramenta]
```

Para descobrir os nomes exatos das ferramentas disponiveis, peca ao Claude:
```
"liste todas as ferramentas MCP disponiveis"
```

Ele mostra a lista completa com nomes que voce pode copiar para o `allow`.

### Dicas

- **Comece permissivo, restrinja depois.** Libere tudo de leitura no primeiro dia. Quando sentir que algo precisa de controle, adicione restricao.
- **`Bash(*)` e poderoso.** Libera qualquer comando no terminal. Se preferir restringir, pode usar patterns: `Bash(git *)` libera so comandos git.
- **Permissoes sao globais.** Valem para todas as sessoes e projetos. Se quiser permissoes diferentes por projeto, use o settings.json do projeto em vez do global.
- **Quando o Claude pede aprovacao**, voce pode clicar "Always allow" no VS Code — isso adiciona automaticamente ao `allow`.
- **Revise periodicamente.** Conforme voce conecta mais MCPs, vale revisar o que esta liberado. Use `cat ~/.claude/settings.json | jq '.permissions.allow'` para ver a lista atual.

### Exemplo completo de settings.json

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "WebFetch",
      "WebSearch",
      "Bash(*)",

      "mcp__slack__slack_get_channel_history",
      "mcp__slack__slack_get_thread_replies",
      "mcp__slack__slack_list_channels",
      "mcp__slack__slack_get_users",

      "mcp__google__search_gmail_messages",
      "mcp__google__get_gmail_message_content",
      "mcp__google__get_events",
      "mcp__google__read_sheet_values",
      "mcp__google__list_drive_items"
    ],
    "additionalDirectories": [
      "/tmp"
    ]
  }
}
```

---

## Resumo — Por onde comecar

| Prioridade | O que fazer | Tempo |
|---|---|---|
| 1 | Criar CLAUDE.md com contexto basico | 15 min |
| 2 | Configurar permissoes de leitura no settings.json | 10 min |
| 3 | Configurar 1 memoria de feedback apos primeira correcao | 5 min |
| 4 | Adicionar hook PreCompact | 10 min |
| 5 | Ir expandindo CLAUDE.md conforme usa | Continuo |
| 6 | Acumular memorias de feedback naturalmente | Continuo |
| 7 | Adicionar guardrails quando conectar MCPs externos | Quando precisar |

O mais importante: **o CLAUDE.md e o sistema de memoria se alimentam com o uso**. Quanto mais voce usa e corrige, mais inteligente fica. Nao tente criar tudo de uma vez — va construindo conforme a necessidade aparece.
