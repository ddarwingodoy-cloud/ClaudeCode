# PDFs — Relatorios

> Formatos reais usados pelo Betinho para gerar relatorios em PDF.

---

## Regra geral

- **Ferramenta:** SEMPRE Chrome headless (Puppeteer). NUNCA WeasyPrint.
- **Motivo:** WeasyPrint nao renderiza flexbox, CSS Grid, charts SVG/Canvas.
- **Script base:** `BWChalenge/Outros/gerar-pdf.py`
- **Comando tipico:** `chromium --headless --print-to-pdf=output.pdf --no-margins --disable-gpu --no-sandbox file.html`
- **Page breaks:** `page-break-inside: avoid` em TODA secao, card, tabela e container.

---

## Formato 1: Monthly Report

### Especificacoes
| Propriedade | Valor |
|---|---|
| Orientacao | Landscape |
| Dimensoes | 297x210mm (A4 landscape) |
| Margem | 0 (controlada via padding CSS interno) |
| Fonte | Inter (Regular, SemiBold, Bold) |
| Import | `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900` |

### Cores
| Elemento | Cor |
|---|---|
| Fundo principal | `#1C1C1E` |
| Cards / superficies | `#111111` ou `#1A1A1A` |
| Accent (bordas, destaques, KPIs) | `#FF3900` |
| Texto principal | `#FFFFFF` |
| Texto secundario | `#AAAAAA` |
| Texto terciario | `#666666` |
| Bordas internas | `#2A2A2A` |

### Layout
- Border-radius: 8px em cards (permitido em docs internos)
- KPI cards: valor grande (36px bold), label pequeno (12px uppercase, letter-spacing 1px)
- Graficos: cores da paleta semantica (verde crescimento, vermelho queda, laranja BW accent)
- Tabelas: header em `#FF3900` com texto branco, zebra striping `#111111` / `#1A1A1A`

### CSS base
```css
@page { size: A4 landscape; margin: 0; }
body {
    background: #1C1C1E;
    color: #FFFFFF;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    line-height: 1.5;
    margin: 0;
    padding: 0;
}
.page {
    width: 297mm;
    height: 210mm;
    padding: 30px 40px;
    box-sizing: border-box;
    page-break-after: always;
    position: relative;
}
.card {
    background: #1A1A1A;
    border-radius: 8px;
    padding: 24px;
    page-break-inside: avoid;
}
.section { page-break-inside: avoid; }
h1 { font-size: 28px; font-weight: 700; }
h2 { font-size: 22px; font-weight: 600; color: #FF3900; }
h3 { font-size: 16px; font-weight: 600; }
```

---

## Formato 2: Report Executivo (EMT)

Mesmo padrao visual do Monthly Report com ajustes:

| Propriedade | Valor |
|---|---|
| Paginas | 4-6 max (conciso) |
| Idioma | Ingles |
| Foco | Executive summary robusto, recomendacoes de acao |
| Publico | Leandro Rivas, Santiago, Zeno, Pedro |

### Diferenca pratica
- Executive summary ocupa pagina inteira (nao apenas bullets)
- Menos tabelas detalhadas, mais KPIs visuais
- Slide de recomendacoes com 3-5 acoes concretas
- Sem detalhamento granular por campanha/segmento

---

## Formato 3: Apresentacao Executiva (brand-facing)

> Ver arquivo dedicado: `03-formats/pdf/apresentacoes-executivas.md`

---

## Formato 4: Dossie de Jogador

> Ver arquivo dedicado: `03-formats/pdf/dossies.md`

---

## Regras criticas para todos os PDFs

### Page breaks
```css
/* OBRIGATORIO em todo CSS de PDF */
.section, .card, .kpi-group, .kpi-row, table, .chart-container, .profile-section {
    page-break-inside: avoid;
}
```

### Fonts
- Incluir `<link>` do Google Fonts no `<head>` do HTML
- Chrome headless carrega fontes externas corretamente
- Sempre definir fallback: `'Inter', 'Roboto', -apple-system, sans-serif`

### Imagens
- Usar base64 inline OU URLs absolutas (nao caminhos relativos)
- Logos BW: embedar como SVG inline ou base64
- 150 DPI para digital, 300 DPI se for impresso

### Checklist antes de gerar PDF
1. Todas as secoes tem `page-break-inside: avoid`?
2. Fontes Google carregam via `<link>`?
3. Imagens em base64 ou URL absoluta?
4. CSS em `<style>` no head (nao arquivo externo)?
5. `@page` com size e margin corretos?
6. Testou no Chrome headless?
7. Nenhuma secao quebra no meio da pagina?

### Linguagem
- Formal mas claro
- Citar fonte de dados sempre
- Datas: DD/MM/AAAA
- Valores monetarios: R$ com separador de milhar (R$ 1.234.567,89)
- Percentuais: com 1 casa decimal (12.3%)

### Classificacao
Em cada pagina, no rodape:
- "INTERNAL" — uso interno geral
- "CONFIDENTIAL" — apenas direcao / especificos
- "PUBLIC" — pode circular externamente
