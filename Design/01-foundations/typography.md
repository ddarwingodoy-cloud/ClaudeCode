# Tipografia

> "BLACK. BOLD. IMPACT." — A tipografia BetWarrior e compacta, em uppercase, e transmite forca.

---

## Fontes da marca

### Primaria — Integral CF (display / titulos)
- **Familia:** Integral CF
- **Pesos:** Bold, Black (ExtraBold)
- **Uso:** Titulos, headlines, hero sections, capas. SEMPRE em UPPERCASE.
- **Licenca:** Fonte PAGA (Connary Fagan). Nao disponivel no Google Fonts.
- **Caracteristicas:** Compacta, geometrica, sem serifa, alto impacto visual.
- **Regra:** NUNCA usar em lowercase. NUNCA aplicar drop shadow.

### Secundaria — Archivo (corpo / subtitulos)
- **Familia:** Archivo
- **Pesos:** Thin (100), ExtraLight (200), Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700), ExtraBold (800), Black (900)
- **Uso:** Corpo de texto, subtitulos, navegacao, UI geral.
- **Fonte:** Google Fonts — `https://fonts.google.com/specimen/Archivo`
- **Fallback:** `"Archivo", "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`

### Terciaria — Roboto (digital / fallback)
- **Familia:** Roboto
- **Pesos:** Light (300), Regular (400), Medium (500), Bold (700)
- **Uso:** Fallback quando Integral CF e Archivo nao estao disponiveis. Interfaces digitais, dashboards.
- **Fonte:** Google Fonts — `https://fonts.google.com/specimen/Roboto`

---

## Fontes para documentos do Betinho

O Betinho usa fontes diferentes dependendo do tipo de documento:

| Tipo de documento | Titulos | Corpo | Fallback |
|---|---|---|---|
| Monthly Report | Inter Bold | Inter Regular | Roboto |
| Report executivo (Leandro/DAGMA) | Inter Bold | Inter Regular | Roboto |
| Dossie de jogador | Inter Bold | Inter Regular | Roboto |
| Apresentacao executiva (Brand Evolution) | Archivo Black (uppercase) | Archivo Regular | Roboto |
| Email padrao BW | — | Arial 10.5pt | sans-serif |
| GTM Update | — | Markdown nativo | — |
| KPI Dashboard (bwbr.dev.br) | Inter Bold | Inter Regular | Roboto |

**Regra:** Para documentos internos, `Archivo Black` substitui `Integral CF` como fonte de titulos (mais proxima disponivel gratuitamente). `Inter` e usada para relatorios de dados por sua excelente legibilidade em numeros.

---

## Escala tipografica

### Para documentos HTML (relatorios, apresentacoes)

| Token | Tamanho | Line-height | Peso | Fonte | Uso |
|---|---|---|---|---|---|
| `--text-display` | 48px / 3rem | 1.1 | 900 (Black) | Archivo Black | Hero titles, capas |
| `--text-h1` | 36px / 2.25rem | 1.15 | 700 (Bold) | Archivo Bold / Inter Bold | Titulo de pagina |
| `--text-h2` | 28px / 1.75rem | 1.2 | 700 (Bold) | Archivo Bold / Inter Bold | Secoes |
| `--text-h3` | 22px / 1.375rem | 1.3 | 600 (SemiBold) | Archivo SemiBold / Inter SemiBold | Subsecoes |
| `--text-h4` | 18px / 1.125rem | 1.4 | 600 (SemiBold) | Archivo SemiBold / Inter SemiBold | Card titles |
| `--text-body` | 16px / 1rem | 1.6 | 400 (Regular) | Archivo / Inter | Texto corrido |
| `--text-body-lg` | 18px / 1.125rem | 1.6 | 400 (Regular) | Archivo / Inter | Texto de destaque |
| `--text-small` | 14px / 0.875rem | 1.5 | 400 (Regular) | Archivo / Inter | Texto secundario |
| `--text-caption` | 12px / 0.75rem | 1.4 | 400 (Regular) | Archivo / Inter | Captions, disclaimers |
| `--text-overline` | 11px / 0.6875rem | 1.4 | 700 (Bold) | Archivo Bold | Labels uppercase |

### Para emails

| Elemento | Tamanho | Fonte | Peso | Cor |
|---|---|---|---|---|
| H2 | 13.5pt | Arial | Bold | `#1A1A1A` |
| H3 | 13.5pt | Arial | Bold | `#333333` |
| Corpo | 10.5pt | Arial | Regular | `#333333` |
| Label tabela | 10.5pt | Arial | Regular | `#333333` |
| Caption/footer | 9pt | Arial | Regular | `#666666` |

---

## Regras

**Faca:**
- Titulos SEMPRE em UPPERCASE (marca registrada da identidade BW)
- Hierarquia clara: maximo 3 niveis visiveis por secao
- Line-height generoso para texto corrido (1.5+)
- Use Archivo Black como substituto de Integral CF em documentos digitais
- Use Inter para relatorios com muitos numeros/dados
- Use Arial em emails (compatibilidade universal)

**Nao faca:**
- NUNCA use drop shadow em tipografia
- NUNCA use texto justificado em web/email (cria buracos)
- NUNCA use mais de 2 familias por documento
- NUNCA use lowercase em titulos de destaque da marca
- NUNCA use fontes decorativas, script ou serif
- NUNCA use Integral CF sem licenca valida

---

## Import Google Fonts

```html
<!-- Archivo (apresentacoes executivas, brand) -->
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- Archivo Black (substituto de Integral CF para titulos) -->
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap" rel="stylesheet">

<!-- Inter (relatorios, dashboards, dossies) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- Roboto (fallback) -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
```
