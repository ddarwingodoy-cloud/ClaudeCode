# Começando com o Claude Code no VSCode — Guia pro João Vitor

> Do zero: instalar, entrar e ter a primeira conversa. Leva uns 15 minutos.
> Quando pegar o jeito, tem um **nível 2** no fim (transformar o Claude num assistente que lembra de você).

---

## O que é isso?

O **Claude Code** é o Claude (a IA) rodando **dentro do seu editor de código (VSCode)**. Ele lê seus arquivos, responde perguntas, escreve e edita código, roda comandos e te ajuda em tarefas — tudo conversando em português normal, como se fosse uma pessoa do seu lado.

---

## Antes de começar, você precisa de:

1. **Uma conta Claude com plano** (Pro ou Max). *(Fala com o Darwin que ele te ajuda com isso.)*
2. **Um computador** (Mac ou Windows).
3. **O VSCode instalado e atualizado** (versão **1.98 ou mais nova** — a gente confere isso no passo 1).

---

## Passo 1 — Instalar o VSCode

1. Vai em **https://code.visualstudio.com** e baixa a versão do seu sistema (Mac ou Windows).
2. Instala normalmente (avançar, avançar, concluir).
3. Abre o VSCode. Pra conferir a versão: menu **Help → About** (ou **Ajuda → Sobre**). Se for **1.98 ou maior**, tá certo. Se for mais antiga, atualiza.

---

## Passo 2 — Instalar a extensão do Claude Code

1. Com o VSCode aberto, aperta:
   - **Mac:** `Cmd + Shift + X`
   - **Windows:** `Ctrl + Shift + X`
   
   (Isso abre a aba de **Extensões**.)
2. Na busca, digita **Claude Code**.
3. Clica em **Install** na extensão oficial da **Anthropic** (o publisher aparece como `anthropic.claude-code` — confere que é essa).
4. Se não aparecer na hora, fecha e abre o VSCode de novo.

---

## Passo 3 — Entrar (login)

1. Depois de instalar, aparece um **ícone de faísca ✱** no canto do editor (em cima, à direita) ou embaixo, na barra de status (**✱ Claude Code**). Clica nele.
2. Vai aparecer uma tela pedindo pra entrar. Clica em **Sign in**.
3. Abre o navegador pra você fazer login com a sua **conta Claude**. Autoriza.
4. Volta pro VSCode. Pronto, tá conectado! *(Ele guarda o login; você não precisa repetir toda vez.)*

---

## Passo 4 — Abrir uma pasta e a primeira conversa

1. No VSCode: **File → Open Folder** (**Arquivo → Abrir Pasta**) e escolhe uma pasta qualquer sua (pode ser uma pasta de estudos, um projetinho, o que for).
2. Clica no **ícone da faísca ✱** pra abrir o Claude.
3. Escreve uma pergunta simples, tipo:
   > o que tem nessa pasta?
   
   ou
   > me explica o que esse projeto faz
4. Ele lê os arquivos e responde. A partir daí é só conversar , pede o que quiser em português.

**Ideias de primeiras perguntas:**
- *"cria um arquivo hello.txt com uma mensagem de boas-vindas"*
- *"me ajuda a entender o que faz esse código aqui"*
- *"escreve um programinha em Python que soma dois números"*

---

## Como funcionam as "aprovações" (importante!)

Quando o Claude quer **mexer num arquivo** ou **rodar um comando**, ele **pergunta antes** e te mostra o que vai fazer (tipo um "antes e depois"). Você escolhe:
- ✅ **Aceitar** (ele faz)
- ❌ **Recusar** (ele não faz)
- ✏️ **Pedir mudança** (você explica o que quer diferente)

Isso é de propósito: **você está sempre no controle**. No comecinho, vai aceitando com calma e lendo o que ele faz , é assim que se aprende.

---

## Comandos úteis (digita a barra `/` pra ver todos)

| Comando | O que faz |
|---|---|
| `/help` | Mostra os comandos disponíveis |
| `/login` | Entrar / trocar de conta |
| `/clear` | Limpar a conversa e começar do zero |
| `/usage` | Ver seu uso e limites |
| `/exit` | Sair (no terminal) |

**Atalhos legais:**
- **`@nomedoarquivo`** , pergunta sobre um arquivo específico (ex: `@main.py`).
- Selecionar um trecho e apertar **`Cmd+K` (Mac)** / **`Alt+K` (Windows)** , inclui aquele pedaço na conversa.

---

## Dica de ouro

Fala com o Claude **como você falaria com uma pessoa**. Não precisa saber "os termos certos". Se ele fizer algo diferente do que você queria, **é só corrigir** ("não era bem isso, eu queria assim…") , ele entende e ajusta.

Erra sem medo. Você não quebra nada , e com git dá pra desfazer tudo depois.

---

## Nível 2 (pra quando você pegar o jeito)

Depois de usar um tempo, tem como transformar o Claude num **assistente que lembra de você entre as conversas** , que sabe seu nome, seus projetos e suas preferências, e não começa do zero toda vez. Isso se faz com um arquivo chamado **`CLAUDE.md`** e com o **sistema de memória**.

Tem um guia completo disso (foi ele que configurou o assistente do Darwin): **`guia-setup-claude-code.md`**. Mas isso é pro futuro , primeiro curte instalar, conversar e brincar com o básico.

Bem-vindo, João Vitor! Qualquer dúvida, é só perguntar pro próprio Claude , ou pro Darwin. 🚀
