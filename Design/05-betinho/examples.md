# Exemplos Reais — Documentos Produzidos pelo Betinho

> Casos reais com os padroes estabelecidos. Referencia para manter consistencia entre sessoes.

---

## 1. Monthly Report

### Descricao
Relatorio mensal de performance do marketing Brasil, entregue ao Country Manager e EMT.

### Especificacoes tecnicas
- **Formato:** HTML landscape 297x210mm → PDF via Chrome headless
- **Fonte:** Inter (Regular, SemiBold, Bold)
- **Theme:** Dark
  - Fundo: `#1C1C1E`
  - Cards: `#111111` ou `#1A1A1A`
  - Accent: `#FF3900`
  - Texto principal: `#FFFFFF`
  - Texto secundario: `#AAAAAA`
- **Border-radius:** 8px em cards
- **Page-break:** `page-break-inside: avoid` em toda secao

### Estrutura tipica
```
Pagina 1: Capa (titulo, periodo, logo BW)
Pagina 2: Executive Summary (highlights, KPIs top-line)
Pagina 3-4: KPIs detalhados (FTDs, Deposits, GGR, NGR, Bonus Cost)
Pagina 5: Segmentos (Sports vs Casino, por estado, por cohort)
Pagina 6: Trends (graficos WoW/MoM)
Pagina 7: Iniciativas em andamento
Pagina 8: Conclusao e proximos passos
```

### CSS chave
```css
@page { size: A4 landscape; margin: 0; }
body { background: #1C1C1E; color: #FFFFFF; font-family: 'Inter', sans-serif; }
.card { background: #1A1A1A; border-radius: 8px; padding: 24px; page-break-inside: avoid; }
.accent { color: #FF3900; }
.kpi-value { font-size: 36px; font-weight: 700; }
.kpi-label { font-size: 12px; color: #AAAAAA; text-transform: uppercase; letter-spacing: 1px; }
```

---

## 2. Report Executivo (Leandro / Presentacion DAGMA)

### Descricao
Relatorio ad-hoc para o Regional Markets Director (Leandro Rivas) ou apresentacoes para EMT.

### Especificacoes tecnicas
- Mesmo padrao visual do Monthly Report (dark theme, Inter)
- **Idioma:** INGLES (documentos para EMT)
- Conteudo adaptado ao publico executivo: mais conciso, foco em decisoes

### Diferenca do Monthly Report
- Menos paginas (4-6 max)
- Executive summary mais robusto
- Recomendacoes de acao explicitas
- Sem detalhamento granular (mantem top-line)

---

## 3. Apresentacao Brand Evolution

### Descricao
Apresentacao executiva sobre evolucao da marca, guidelines e posicionamento. Brand-facing.

### Especificacoes tecnicas
- **Formato:** HTML landscape 297x210mm → PDF via Chrome headless
- **Fonte:** Archivo Black para titulos (UPPERCASE), Archivo Regular para corpo
- **Cores:** APENAS `#FF3900`, `#000000`, `#FFFFFF`
- **Morfologia:** ZERO border-radius. Tudo retangular, cantos retos, 90 graus.
- **Layout:** paginas alternando fundo preto e fundo branco para leveza visual
- **Dividers de secao:** pagina inteira em fundo preto com titulo em laranja
- **Logo BW:** watermark discreto no canto inferior

### Estrutura tipica
```
Pagina 1: Capa (fundo preto, logo grande, titulo em branco)
Pagina 2: Indice (fundo branco)
Pagina 3: Divider secao (fundo preto, titulo laranja)
Pagina 4-5: Conteudo (alternando P&B)
...
Ultima: Contato / encerramento
```

### CSS chave
```css
@page { size: A4 landscape; margin: 0; }
body { font-family: 'Archivo', sans-serif; margin: 0; }
h1, h2, h3 { font-family: 'Archivo Black', sans-serif; text-transform: uppercase; }
.page-dark { background: #000000; color: #FFFFFF; }
.page-light { background: #FFFFFF; color: #000000; }
.accent { color: #FF3900; }
.divider-page { background: #000; display: flex; align-items: center; justify-content: center; }
.divider-page h1 { color: #FF3900; font-size: 64px; }
/* ZERO border-radius em tudo */
* { border-radius: 0 !important; }
```

---

## 4. Dossie de Jogador

### Descricao
Perfil completo de um jogador de futebol para analise de patrocinio, embaixador ou parceria.

### Especificacoes tecnicas
- **Formato:** HTML A4 portrait 210x297mm → PDF via Chrome headless
- **Fonte:** Inter
- **Theme:** Clean — fundo branco, acentos em `#FF3900`
- **Border-radius:** 8px em cards

### Estrutura tipica
```
Header: foto + nome + posicao + time + idade
Profile bar: KPI cards em fundo #1C1C1E (seguidores, engajamento, valor de mercado)
Bio: paragrafo curto
Tabela de dados: estatisticas com zebra striping (fundo alternado whitesmoke)
Risk assessment: card escuro com analise de risco (judicial, imagem, contrato)
Footer: classificacao (A/B/C) + recomendacao + data
```

### CSS chave
```css
@page { size: A4; margin: 20mm; }
body { font-family: 'Inter', sans-serif; color: #1A1A1A; }
.header { border-bottom: 3px solid #FF3900; padding-bottom: 16px; }
.profile-bar { background: #1C1C1E; color: #FFFFFF; border-radius: 8px; padding: 20px; }
.kpi-card { text-align: center; }
.kpi-value { font-size: 28px; font-weight: 700; color: #FF3900; }
table { width: 100%; border-collapse: collapse; }
table th { background: #FF3900; color: #FFFFFF; padding: 8px 12px; text-align: left; }
table tr:nth-child(even) { background: #F5F5F5; }
.risk-card { background: #1C1C1E; color: #FFFFFF; border-radius: 8px; padding: 20px; }
```

---

## 5. Email padrao BW

### Descricao
Emails internos e para EMT seguindo o padrao visual BetWarrior.

### Especificacoes tecnicas
- **Formato:** HTML inline styles
- **Envio:** via MCP Google (`draft_gmail_message` com `body_format="html"`)
- **Fonte:** Arial, 10.5pt

### Estrutura CSS inline

```html
<!-- H2 -->
<h2 style="font-size:13.5pt; color:#1A1A1A; border-bottom:solid #FF3900 1.5pt; padding-bottom:4px; margin-top:24px; margin-bottom:12px; font-family:Arial,sans-serif;">
  Titulo da Secao
</h2>

<!-- H3 -->
<h3 style="font-size:13.5pt; color:#333333; margin-top:18px; margin-bottom:8px; font-family:Arial,sans-serif;">
  Subtitulo
</h3>

<!-- Corpo -->
<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6; margin:8px 0;">
  Texto do corpo aqui.
</p>

<!-- Tabela 2 colunas (label + valor) -->
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Label</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Valor</td>
  </tr>
</table>

<!-- Tabela de dados -->
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <thead>
    <tr>
      <th style="background:#FF3900; color:#FFFFFF; padding:8px 12px; text-align:left; font-family:Arial,sans-serif; font-size:10.5pt;">Coluna</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Dado</td>
    </tr>
    <tr>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD; background:whitesmoke;">Dado alternado</td>
    </tr>
  </tbody>
</table>
```

### Cores permitidas em email
| Cor | Hex | Uso |
|---|---|---|
| Laranja BW | `#FF3900` | Borda h2, header de tabela |
| Texto titulo | `#1A1A1A` | H2 |
| Texto corpo | `#333333` | H3, body, tabelas |
| Borda | `#DDDDDD` | Bordas de tabela |
| Fundo alternado | `whitesmoke` | Zebra striping, labels |
| Fundo | `white` | Background geral |

---

## 6. GTM Update (semanal)

### Descricao
Update semanal de Go-to-Market para a lideranca (Santiago, Leandro, Zeno).

### Especificacoes
- **Formato:** Markdown puro
- **Idioma:** Ingles
- **Entrega:** email ou Slack

### Estrutura tipica
```markdown
# GTM Update — Week XX (DD/MM - DD/MM)

## Highlights
- Bullet 1
- Bullet 2

## KPIs (WoW)
| Metric | This Week | Last Week | Delta |
|---|---|---|---|

## Initiatives Status
| Initiative | Status | Owner | Notes |
|---|---|---|---|

## Next Steps
- ...

## Blockers / Risks
- ...
```

---

## 7. KPI Daily Report

### Descricao
Pipeline automatizado de KPIs diarios.

### Fluxo
```
Power BI Refresh → DAX Queries → Processamento Python → Firestore (kpi_daily) → Slack Notification
```

### Detalhes tecnicos
- **Firestore:** projeto `m4x-projectx`, collection `kpi_daily`
- **Documento:** nomeado por data (ex: `2026-04-15`)
- **Dashboard:** bwbr.dev.br (leitura client-side do Firestore)
- **Agente:** `/kpi` (slash command dedicado)

---

## Padroes observados ao longo das sessoes

- **2026-03** — Chrome headless funciona perfeitamente para PDFs com flexbox e charts. WeasyPrint nao renderiza.
- **2026-03** — Page-break-inside:avoid precisa estar em CADA secao, nao so em tabelas.
- **2026-03** — Inter e a melhor fonte para relatorios com muitos numeros (largura consistente dos digitos).
- **2026-04** — Emails com inline styles sao a unica forma confiavel para Gmail + Outlook.
- **2026-04** — H2 com borda laranja se tornou a assinatura visual dos emails do Betinho.
- **2026-04** — Archivo Black e o substituto mais proximo de Integral CF disponivel gratuitamente.
- **2026-04** — Apresentacoes brand-facing NUNCA usam border-radius. Documentos internos podem usar.
- **2026-04** — Dark theme (#1C1C1E) com accent #FF3900 e o padrao visual mais reconhecivel do time.
