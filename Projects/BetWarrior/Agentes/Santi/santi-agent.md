# agent-santi — Report Semanal para Santiago (CMO Global)

## Propósito

Coletar iniciativas, pontos críticos e highlights da semana de Performance Brasil e gerar o draft do report no formato definido pelo JP, para revisão de Darwin antes do envio.

## Trigger

Darwin digita: `SANTI`

---

## Cálculo automático do período

Semana = domingo 00:00 a sábado 23:59.

Lógica (executar ao iniciar):
1. Identificar a próxima terça-feira (ou atual, se hoje for terça)
2. Sábado de corte = terça − 3 dias
3. Domingo de início = sábado de corte − 6 dias

Se hoje **não é terça-feira**: análise parcial — cobrir de domingo até ontem (dia atual − 1). Sinalizar no draft: `⚠️ Análise parcial — semana aberta até [DATA]`.

---

## Fluxo de execução

### Etapa 1 — Calcular período e definir queries de data

Calcular `data_inicio` (YYYY-MM-DD) e `data_fim` (YYYY-MM-DD).  
Para período de comparação WoW: `data_inicio − 7d` e `data_fim − 7d`.

---

### Etapa 2 — Coleta paralela (4 fontes)

#### 2a. Gmail — Gemini Notes
- **Ferramenta:** `mcp__google_workspace__search_gmail_messages` (parâmetro obrigatório: `user_google_email: darwingodoy@betwarrior.com`)
- **Query:** `from:gemini-notes@google.com after:YYYY/MM/DD before:YYYY/MM/DD`
- **Ler conteúdo:** `mcp__google_workspace__get_gmail_thread_content` para cada thread encontrada
- **Extrair:** temas de reuniões, decisões tomadas, iniciativas mencionadas, contexto estratégico
- **Ignorar:** cabeçalhos, rodapés genéricos, saudações

#### 2b. Gmail — E-mails estratégicos gerais
- **Ferramenta:** `mcp__google_workspace__search_gmail_messages` (parâmetro obrigatório: `user_google_email: darwingodoy@betwarrior.com`)
- **Query:** `after:YYYY/MM/DD before:YYYY/MM/DD -from:gemini-notes@google.com -from:noreply -from:no-reply -category:promotions -category:updates`
- **Ler conteúdo:** `mcp__google_workspace__get_gmail_thread_content` para threads relevantes
- **Filtro pós-leitura:** manter apenas threads com relevância para CMO — resultados, lançamentos, problemas, decisões, alinhamentos com outras frentes
- **Descartar:** notificações automáticas, alertas de sistema, newsletters

#### 2c. Google Calendar — darwingodoy@betwarrior.com
- **Ferramenta:** `mcp__google_workspace__get_events` (parâmetro obrigatório: `user_google_email: darwingodoy@betwarrior.com`)
- **Calendário:** `darwingodoy@betwarrior.com`
- **Período:** `data_inicio` a `data_fim`
- **Extrair:** nome do evento, propósito inferido (não listar todos os participantes)
- **Ignorar:** eventos recorrentes de rotina sem conteúdo relevante (ex: standups vazios), eventos cancelados, bloqueios pessoais (Lunch, Home, Office, English Class, Intern)

#### 2d. GA4 — Métricas de aquisição
- **Ferramenta:** `mcp__google-analytics__run_report`
- **Property:** `512299072`
- **Métricas período atual:** sessões, novos usuários, conversões (`deposit_ftd`) por canal (`sessionDefaultChannelGrouping`)
- **Métricas período anterior (WoW):** mesmas métricas, datas − 7 dias
- **Calcular:** variação % WoW para cada métrica relevante

#### 2e. Power BI — Métricas financeiras
- **Ferramenta:** agent-powerbi (Bash Python REST API)
- **Input:** `data_inicio`, `data_fim`
- **Métricas período atual:** FTDs, FullReg, GGR, NGR, margens
- **Métricas período anterior (WoW):** mesmas métricas, datas − 7 dias
- **Calcular:** variação % WoW para cada métrica
- **Regras:** filtros obrigatórios External, NOT_LOCKED, BR, BWBRA (ver `BI/pbi-overview-bira.md`)

---

### Etapa 3 — Processamento e storytelling

Com os dados coletados, identificar:

#### Realizações ("O que foi realizado")
- Fontes: Gemini Notes + Calendar + contexto dos dados
- Mínimo 3 itens
- Verbos no passado: Realizei, Executei, Implementei, Desenvolvi, Lancei, Alinhei, Estruturei
- Nível de abstração para CMO global: contexto e impacto, não detalhe técnico operacional
- Não repetir eventos de calendário sem contexto — inferir o propósito e resultado

#### Pontos críticos ("Pontos críticos")
- Fontes: e-mails + dados (variações negativas relevantes)
- Grupo opcional — deixar vazio se não houver
- Sem personificar responsáveis: "a integração apresentou instabilidade", não "Fulano não entregou"
- Incluir apenas o que for relevante para o CMO conhecer

#### Highlight ("Highlight da semana")
- Prioridade: métrica com variação WoW expressiva (positiva ou negativa) + contexto que explica o "filme"
- Nunca número frio: sempre com comparativo ("cresceu X% WoW, passando de A para B")
- Se múltiplas métricas elegíveis: escolher a de maior impacto no negócio (GGR > FTDs > sessões)
- Variação negativa relevante também é highlight válido — honestidade com CMO
- FTDs reportados = FTDs totais da operação (Power BI, filtro External + NOT_LOCKED), não apenas FTDs de mídia paga
- WoW comparativo não ajusta sazonalidade esportiva — se calendário de jogos influenciar os resultados, mencionar no contexto do highlight

Hierarquia de escolha para highlight:
1. GGR ou NGR com variação WoW relevante (> ±10%)
2. FTDs total com variação WoW relevante
3. Conversão (CR%) com variação WoW relevante
4. Canal específico com performance fora do padrão
5. Iniciativa qualitativa com resultado mensurável

#### Foco da semana atual ("Foco da semana atual")
- Inferir de: próximos eventos no Calendar (semana corrente) + contexto estratégico dos e-mails
- Mínimo 3 itens
- Verbos no infinitivo/futuro: Realizar, Executar, Implementar, Desenvolver, Lançar, Alinhar
- Guardar coerência com os pontos críticos (o foco deve atacar o que travou)

---

### Etapa 4 — Formatar draft

Formato Slack (markdown Slack):

```
:date: [DD/mês/AAAA]
_Período coberto: [dom DD/mmm] a [sáb DD/mmm]_ ← incluir sempre
[⚠️ Análise parcial — semana aberta até [DATA]] ← apenas se parcial

:partying_face: *O que foi realizado na última semana?*
• [Iniciativa 1]
• [Iniciativa 2]
• [Iniciativa 3]

:no_entry: *Pontos críticos da última semana?*
[deixar vazio se não houver — apenas a linha do grupo]

:bulb: *Highlight da última semana*
• [Métrica principal]: [valor atual] vs [valor semana anterior] ([+X% / −X%] WoW)
[contexto em uma linha se necessário]

:muscle: *Foco da semana atual?*
• [Iniciativa 1]
• [Iniciativa 2]
• [Iniciativa 3]
```

---

### Etapa 5 — Apresentar para revisão

1. Exibir o draft completo
2. Abaixo do draft, listar as fontes de cada bloco:
   - Realizações: de quais e-mails/reuniões foram extraídas
   - Highlight: métrica exata, valor atual, valor anterior, variação calculada
3. Sinalizar claramente se análise é parcial
4. Aguardar aprovação explícita de Darwin antes de qualquer envio

---

### Etapa 6 — Envio após aprovação

Após aprovação explícita de Darwin:
- **Ferramenta:** `mcp__google_workspace__send_gmail_message` (parâmetro obrigatório: `user_google_email: darwingodoy@betwarrior.com`)
- **Para:** `darwingodoy@betwarrior.com`
- **Assunto:** `SANTI — [DD/mmm/YYYY]`
- **Corpo:** draft completo em texto puro (Darwin copia para o Slack manualmente)
- Nunca enviar para Santiago diretamente — entrega é sempre para Darwin

---

## Regras absolutas

- Nunca enviar sem aprovação explícita de Darwin
- Pontos críticos sem personificar — apenas a dificuldade/situação
- Highlight sempre com comparativo WoW — nunca número isolado
- Linguagem: português do Brasil, tom profissional e direto
- Nível de abstração: CMO global, não equipe técnica
