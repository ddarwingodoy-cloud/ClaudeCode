# Manual Operacional do Betinho — Design & Documentos

> Este e o arquivo mais importante do Design System para o Betinho. Define como criar cada tipo de documento, quais padroes seguir, e as regras aprendidas ao longo das sessoes.
> Se houver conflito entre este arquivo e qualquer outro, **este prevalece**.

---

## Tipos de documento que produzimos

### 1. Monthly Report
- **Formato:** HTML landscape 297x210mm, convertido para PDF via Chrome headless
- **Fonte:** Inter (Regular 400, SemiBold 600, Bold 700)
- **Theme:** Dark — fundo `#1C1C1E`, cards `#111111` / `#1A1A1A`, accent `#FF3900`
- **Texto:** branco `#FFFFFF` principal, `#AAAAAA` secundario
- **Conteudo:** KPIs de performance mensal (FTDs, NGR, GGR, Deposits, Bonus Cost, etc.)
- **Estrutura:** capa → executive summary → KPIs → segmentos → trends → conclusao
- **Border-radius:** permitido (8px em cards)
- **Page-break:** `page-break-inside: avoid` em TODA secao

### 2. Report Executivo (Leandro / DAGMA / apresentacoes para EMT)
- **Formato:** HTML landscape 297x210mm, Chrome headless para PDF
- **Fonte:** Inter
- **Theme:** Dark — mesmo padrao do Monthly Report
- **Conteudo:** relatorios ad-hoc para o Regional Markets Director ou EMT
- **Idioma:** Ingles (documentos para EMT sao sempre em ingles)

### 3. Apresentacao Executiva (Brand Evolution, pitch decks brand-facing)
- **Formato:** HTML landscape 297x210mm, Chrome headless para PDF
- **Fonte:** Archivo Black para titulos (UPPERCASE), Archivo Regular para corpo
- **Theme:** Brand — alternando paginas preto e branco para leveza
- **Cores:** APENAS `#FF3900`, `#000000`, `#FFFFFF`
- **Morfologia:** ZERO border-radius. Tudo retangular, cantos retos.
- **Dividers:** paginas de secao em fundo preto com titulo em laranja
- **Logo BW:** watermark discreto

### 4. Dossie de Jogador
- **Formato:** HTML A4 portrait 210x297mm, Chrome headless para PDF
- **Fonte:** Inter
- **Theme:** Clean — fundo branco, header com borda `#FF3900`
- **Estrutura:** header com foto + nome → profile bar com KPI cards em `#1C1C1E` → tabela de dados com zebra striping → risk assessment em card escuro → footer com classificacao
- **Border-radius:** permitido (8px em cards)

### 5. Email padrao BW
- **Formato:** HTML inline styles, enviado via MCP Google (`draft_gmail_message` com `body_format="html"`)
- **Fonte:** Arial, 10.5pt
- **Estrutura:**
  - H2: `font-size: 13.5pt; color: #1A1A1A; border-bottom: solid #FF3900 1.5pt; padding-bottom: 4px; margin-top: 24px;`
  - H3: `font-size: 13.5pt; color: #333333;`
  - Body: `font-family: Arial, sans-serif; font-size: 10.5pt; color: #333333; line-height: 1.6;`
  - Tabela 2 colunas: label 140px com fundo `whitesmoke`, conteudo a direita
  - Tabela de dados: header `#FF3900` com texto branco, linhas alternadas `whitesmoke`
  - Cores permitidas: `#FF3900`, `#1A1A1A`, `#333333`, `#DDDDDD`, `whitesmoke`, `white`
- **Idioma:** Ingles para EMT, Portugues para time BR

### 6. GTM Update (semanal)
- **Formato:** Markdown puro
- **Conteudo:** update semanal de Go-to-Market para Santiago, Leandro, Zeno
- **Idioma:** Ingles
- **Estrutura:** highlights → KPIs → iniciativas → proximos passos → blockers
- **Entrega:** via email ou Slack

### 7. KPI Daily Report
- **Formato:** JSON (Firestore) + Dashboard web (bwbr.dev.br)
- **Pipeline:** Power BI refresh → DAX queries → processamento → Firestore (`kpi_daily`) → Slack notification
- **Collection:** `kpi_daily` no projeto `m4x-projectx`
- **Dashboard:** bwbr.dev.br (leitura do Firestore, renderizacao client-side)

---

## Regras tecnicas aprendidas

### Geracao de PDF
- **SEMPRE** usar Chrome headless (Puppeteer). Script base: `Outros/gerar-pdf.py`
- **NUNCA** usar WeasyPrint — nao renderiza flexbox, CSS Grid ou charts em SVG/Canvas
- Comando tipico: `chromium --headless --print-to-pdf=output.pdf --no-margins file.html`
- Flags uteis: `--disable-gpu`, `--no-sandbox`, `--print-to-pdf-no-header`

### Page breaks (regra critica)
- **NUNCA** quebrar uma secao no meio da pagina
- Aplicar `page-break-inside: avoid` em CADA secao, card, tabela e grupo de KPI
- Aplicar no container, nao apenas nos filhos
- Testar visualmente antes de entregar

```css
.section, .card, .kpi-group, table, .chart-container {
    page-break-inside: avoid;
}
```

### HTML/CSS para PDFs
- Usar CSS inline ou `<style>` no `<head>` — nao arquivos externos (podem nao carregar)
- Google Fonts via `<link>` no head funciona com Chrome headless
- Imagens: usar base64 inline ou URLs absolutas
- Flexbox e Grid funcionam bem no Chrome headless
- `@page { size: A4 landscape; margin: 0; }` para controlar tamanho

### Emails HTML
- SEMPRE inline styles (Outlook nao le `<style>` no head)
- NUNCA usar flexbox ou grid em email (Outlook nao suporta)
- Usar `<table>` para layout
- Largura maxima: 600px
- Testar em Gmail web + Outlook desktop (os mais problematicos)
- Enviar via MCP: `draft_gmail_message` com `body_format="html"`

### Fontes
- Google Fonts funciona em Chrome headless (incluir `<link>` no HTML)
- Em emails, usar APENAS fontes de sistema (Arial, Helvetica, sans-serif)
- Archivo Black e o melhor substituto gratuito para Integral CF

### Dados e KPIs
- Moeda: Power BI em BRL, planilha de midia em USD
- Filtro padrao PBI: `DimPlayer[internal_external_player] = "External"`
- locked_status: usar `= "NOT_LOCKED"` (NAO `<> "LOCKED"`)
- Gross Wins = GAME_WIN + CASH_OUT + CORRECTION
- Bonus Cost = GGR - NGR (derivar, nao calcular direto)
- "Quase 200 marcas concorrentes" (NAO "82 operadores licenciados")

---

## Workflow padrao

### 1. Classifique a tarefa
Identifique: tipo de documento (ver lista acima), publico (EMT/time BR/externo), idioma (EN/PT-BR), urgencia.

### 2. Carregue o contexto
Leia, na ordem:
1. `05-betinho/instructions.md` (este arquivo — ja esta lendo)
2. `00-brand/compliance.md` (se material toca em apostas/promocoes)
3. `01-foundations/colors.md` e `typography.md` (se vai gerar HTML)
4. A pasta especifica em `03-formats/` para o tipo de entrega

### 3. Produza
- Sempre em `.md` primeiro na pasta `Md/` do projeto
- HTML vai para pasta `Html/`
- PDF vai para pasta `Pdf/`
- Mantenha consistencia com documentos anteriores do mesmo tipo

### 4. Valide
- Compliance: +18, disclaimers se aplicavel
- Cores: dentro da paleta (brand ou interna, conforme o tipo)
- Tipografia: fonte correta para o tipo de documento
- Page breaks: testar se secoes nao quebram no meio
- Dados: verificar se valores estao corretos e com fonte citada

---

## Regras inegociaveis

**NUNCA:**
- Invente dados, KPIs ou metricas
- Use cores fora da paleta sem aprovacao
- Use fontes fora das definidas para cada tipo de documento
- Gere PDF com WeasyPrint
- Quebre secoes no meio da pagina
- Use drop shadow em tipografia
- Use border-radius em material brand-facing
- Crie copy promocional sem ler `00-brand/compliance.md`
- Use imagens de pessoas sem confirmacao de direitos
- Use IA generativa para gerar rostos

**SEMPRE:**
- Inclua disclaimer de jogo responsavel em material ao publico
- Inclua "+18" em material que mencione apostas
- Use Chrome headless para gerar PDFs
- Use `page-break-inside: avoid` em toda secao
- Documente decisoes criativas
- Confirme com JP antes de desviar do padrao

---

## Referencias uteis

| Recurso | Caminho |
|---|---|
| Script PDF base | `BWChalenge/Outros/gerar-pdf.py` |
| Brandbook Brasil v1 | `BWChalenge/Design/BetWarrior_brandbook_brasil_v1.pdf` |
| Brandbook ES v3 | `BWChalenge/Design/BetWarrior_brandbook_es_v3_logo_con_ejemplos.pdf` |
| Exemplos reais | `05-betinho/examples.md` |
| Pendencias ativas | `BWChalenge/Pendencias.md` |
| Power BI formulas | Memory: `reference_powerbi_formulas.md` |
| Templates visuais | Memory: `reference_templates.md` |
| Dashboard KPI | https://bwbr.dev.br |
