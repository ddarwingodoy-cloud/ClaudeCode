# PDFs — Apresentacoes Executivas (Brand-Facing)

> Formato para apresentacoes como o Brand Evolution. Material que representa a marca visualmente — segue brandbook v3 a risca.

---

## Especificacoes

| Propriedade | Valor |
|---|---|
| Orientacao | Landscape |
| Dimensoes | 297x210mm (A4 landscape) |
| Margem | 0 (controlada via padding CSS interno, tipicamente 40px) |
| Fonte titulos | Archivo Black (UPPERCASE) |
| Fonte corpo | Archivo Regular |
| Import | `https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=Archivo+Black` |
| Geracao | Chrome headless. NUNCA WeasyPrint. |

---

## Cores

**APENAS 3 cores. Sem excecao.**

| Cor | Hex | Uso |
|---|---|---|
| Laranja BW | `#FF3900` | Accent, titulos de secao, dividers, destaques |
| Preto | `#000000` | Fundo de paginas escuras, texto sobre branco |
| Branco | `#FFFFFF` | Fundo de paginas claras, texto sobre preto |

Nenhuma outra cor e permitida. Sem cinzas, sem semanticas, sem neutros derivados. Isso e material de marca.

---

## Morfologia

- **ZERO border-radius** em qualquer elemento
- Retangulos com angulos de 90 graus APENAS
- Formas permitidas: retangulos, L, U
- NAO usar: curvas, diagonais, circulos, cantos arredondados
- Aplicar `* { border-radius: 0 !important; }` como seguranca

---

## Layout

### Alternancia de paginas
Para dar leveza visual e ritmo, as paginas alternam entre fundo preto e fundo branco:

```
Pagina 1 (CAPA): fundo PRETO, logo grande, titulo em BRANCO
Pagina 2 (INDICE): fundo BRANCO, texto PRETO
Pagina 3 (DIVIDER): fundo PRETO, titulo de secao em LARANJA
Pagina 4 (CONTEUDO): fundo BRANCO, texto PRETO, accent LARANJA
Pagina 5 (CONTEUDO): fundo PRETO, texto BRANCO, accent LARANJA
...
```

### Dividers de secao
Paginas inteiras em fundo preto que servem como separadores entre secoes. Contem apenas o titulo da secao em laranja, centralizado, fonte grande (48-64px).

### Logo BW
Watermark discreto no canto inferior direito de cada pagina. Versao branca sobre fundo preto, versao preta sobre fundo branco.

---

## Tipografia

| Elemento | Fonte | Peso | Tamanho | Transform | Cor |
|---|---|---|---|---|---|
| Titulo capa | Archivo Black | 900 | 64px | uppercase | `#FFFFFF` |
| Titulo secao (divider) | Archivo Black | 900 | 48-64px | uppercase | `#FF3900` |
| H1 | Archivo Black | 900 | 36px | uppercase | herdar do fundo |
| H2 | Archivo Bold | 700 | 28px | uppercase | `#FF3900` |
| H3 | Archivo SemiBold | 600 | 22px | uppercase | herdar do fundo |
| Corpo | Archivo Regular | 400 | 16px | normal | herdar do fundo |
| Caption | Archivo Regular | 400 | 12px | normal | herdar do fundo |

**Regra:** TODO titulo em uppercase. NUNCA drop shadow.

---

## Estrutura tipica

```
1. CAPA
   - Fundo preto
   - Logo BW grande (centralizado ou canto superior)
   - Titulo da apresentacao em branco, uppercase, Archivo Black
   - Subtitulo/data em branco, Archivo Regular

2. INDICE
   - Fundo branco
   - Lista de secoes com numero de pagina
   - Accent laranja nos numeros

3. DIVIDER DE SECAO
   - Fundo preto, pagina inteira
   - Titulo da secao em laranja, centralizado
   - Nada mais na pagina

4-N. PAGINAS DE CONTEUDO
   - Alternando P&B
   - Titulos em laranja ou cor do fundo invertida
   - Bullet points, tabelas retangulares, imagens tratadas (P&B + laranja)
   - Charts simples (barras retangulares, sem curvas)

ULTIMA. ENCERRAMENTO
   - Fundo preto
   - Logo BW
   - Dados de contato
```

---

## CSS base

```css
@page { size: A4 landscape; margin: 0; }

* {
    border-radius: 0 !important;
    box-sizing: border-box;
}

body {
    font-family: 'Archivo', sans-serif;
    margin: 0;
    padding: 0;
}

h1, h2, h3, h4 {
    font-family: 'Archivo Black', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.page {
    width: 297mm;
    height: 210mm;
    padding: 40px;
    page-break-after: always;
    position: relative;
    overflow: hidden;
}

.page-dark {
    background: #000000;
    color: #FFFFFF;
}

.page-light {
    background: #FFFFFF;
    color: #000000;
}

.accent { color: #FF3900; }

.divider-page {
    background: #000000;
    display: flex;
    align-items: center;
    justify-content: center;
}

.divider-page h1 {
    color: #FF3900;
    font-size: 64px;
    text-align: center;
}

.watermark {
    position: absolute;
    bottom: 20px;
    right: 30px;
    opacity: 0.3;
    width: 60px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table th {
    background: #FF3900;
    color: #FFFFFF;
    padding: 10px 14px;
    text-align: left;
    font-family: 'Archivo', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 12px;
    letter-spacing: 0.5px;
}

table td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.page-light table td {
    border-bottom: 1px solid #DDDDDD;
}

.section { page-break-inside: avoid; }
```

---

## Checklist antes de gerar

1. ZERO border-radius em todo o documento?
2. Apenas 3 cores (#FF3900, #000, #FFF)?
3. Titulos em uppercase?
4. Paginas alternando P&B?
5. Dividers de secao em fundo preto?
6. Logo watermark presente?
7. `page-break-inside: avoid` em toda secao?
8. Fontes Google carregam via `<link>`?
9. Gerado com Chrome headless?
10. Sem drop shadow em tipografia?
