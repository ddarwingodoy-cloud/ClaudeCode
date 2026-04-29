# Espacamento, Grid e Morfologia

---

## Regra fundamental — Morfologia BetWarrior

A marca BetWarrior usa **exclusivamente formas retangulares com angulos de 90 graus**.

- Retangulos com cantos retos APENAS
- ZERO border-radius em qualquer elemento de marca
- Formas permitidas: retangulos, L, U
- **NAO usar:** curvas, diagonais, border-radius, circulos, elipses

**Excecao para documentos internos do Betinho:** border-radius e permitido em cards e tabelas de relatorios internos que NAO sao brand-facing (Monthly Report, dossies, dashboards). Nesses casos, usar valores moderados (4-8px).

---

## Escala de espacamento (base 4px)

| Token | Valor | Uso |
|---|---|---|
| `--space-1` | 4px | Espacos minimos, gaps internos |
| `--space-2` | 8px | Padding pequeno, gap entre icone+texto |
| `--space-3` | 12px | Padding medio |
| `--space-4` | 16px | Padding padrao de card, gap padrao |
| `--space-5` | 20px | Margem de secao interna |
| `--space-6` | 24px | Espaco entre componentes |
| `--space-8` | 32px | Espaco entre secoes pequenas |
| `--space-10` | 40px | Espaco entre secoes medias |
| `--space-12` | 48px | Espaco entre secoes grandes |
| `--space-16` | 64px | Espaco entre blocos hero |
| `--space-20` | 80px | Margem de pagina em PDF |
| `--space-24` | 96px | Margens de pagina em desktop |

---

## Grid

- **Desktop:** 12 colunas, gutter 24px, max-width 1200px
- **Tablet:** 8 colunas, gutter 16px
- **Mobile:** 4 colunas, gutter 16px, padding lateral 16px

### Para PDFs

| Formato | Dimensoes | Margem |
|---|---|---|
| A4 Portrait | 210x297mm | 20mm |
| A4 Landscape | 297x210mm | 15-20mm |
| Apresentacao landscape | 297x210mm | 30-40px padding interno |

---

## Breakpoints

| Nome | Min-width | Uso |
|---|---|---|
| `sm` | 640px | Mobile grande |
| `md` | 768px | Tablet |
| `lg` | 1024px | Desktop pequeno |
| `xl` | 1280px | Desktop padrao |
| `2xl` | 1536px | Desktop grande |

---

## Border-radius

### Material brand-facing (publicidade, site, campanhas)

| Token | Valor | Uso |
|---|---|---|
| `--radius-brand` | `0px` | TODOS os elementos. Sem excecao. |

### Documentos internos do Betinho (relatorios, dashboards, dossies)

| Token | Valor | Uso |
|---|---|---|
| `--radius-sm` | 4px | Inputs, badges, tags |
| `--radius-md` | 8px | Cards, tabelas |
| `--radius-lg` | 12px | Containers, modais |
| `--radius-none` | 0px | Elementos que simulam a marca |

---

## Sombras

### Material brand-facing
Sombras NAO sao parte da identidade visual. Evitar.

### Documentos internos do Betinho

| Token | Valor | Uso |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Cards sutis |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | Cards padrao |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.15)` | Elementos flutuantes |

---

## Page breaks (regra critica para PDFs)

- SEMPRE usar `page-break-inside: avoid` em CADA secao, card e tabela
- NUNCA quebrar uma secao no meio da pagina
- Aplicar em containers, nao apenas em tabelas
- Testar sempre com Chrome headless antes de exportar

```css
/* Regra obrigatoria em todo CSS de PDF */
.section, .card, table, .kpi-group {
    page-break-inside: avoid;
}
```
