# Cores

> Paleta oficial BetWarrior Brasil. A marca usa APENAS 3 cores: Preto, Branco e Laranja. Nao existe cinza, azul, gradiente ou qualquer outra cor na identidade visual.

---

## Regra fundamental

A BetWarrior usa **exclusivamente 3 cores** em sua identidade visual:

| Cor | Hex | Pantone | CMYK | RGB | Uso |
|---|---|---|---|---|---|
| **Laranja BW** | `#FF3900` | 1655 C | 0/80/100/0 | 255, 57, 0 | Cor primaria da marca. CTAs, destaques, acentos, isotipo |
| **Preto** | `#000000` | Process Black C | 0/0/0/100 | 0, 0, 0 | Fundos, texto principal, logotipo |
| **Branco** | `#FFFFFF` | — | 0/0/0/0 | 255, 255, 255 | Fundos claros, texto invertido |

**NAO existe** cor secundaria, cor de apoio, gradiente, cinza da marca ou azul. Qualquer uso fora dessas 3 cores e desvio do brandbook.

---

## Tokens da marca

| Token | Hex | Uso |
|---|---|---|
| `--color-brand-orange` | `#FF3900` | Cor primaria da marca |
| `--color-brand-black` | `#000000` | Fundos escuros, texto |
| `--color-brand-white` | `#FFFFFF` | Fundos claros, texto invertido |

---

## Neutros derivados (documentos internos)

Para uso em documentos internos, relatorios e interfaces do Betinho — **NAO sao cores da marca**, sao neutros funcionais:

| Token | Hex | Uso |
|---|---|---|
| `--color-bg-dark` | `#1C1C1E` | Fundo dark theme (Monthly Report, dashboards) |
| `--color-bg-dark-alt` | `#111111` | Cards escuros sobre fundo dark |
| `--color-bg-dark-surface` | `#1A1A1A` | Superficie elevada em dark theme |
| `--color-bg-light` | `#FFFFFF` | Fundo light theme |
| `--color-bg-light-alt` | `#F5F5F5` | Fundo alternativo, zebra striping |
| `--color-text-primary` | `#1A1A1A` | Texto principal em light theme |
| `--color-text-secondary` | `#333333` | Texto secundario, corpo de email |
| `--color-text-muted` | `#666666` | Texto terciario, captions |
| `--color-border` | `#DDDDDD` | Bordas e divisores em light theme |
| `--color-border-dark` | `#2A2A2A` | Bordas em dark theme |

---

## Cores semanticas (documentos internos)

Para indicadores de status em relatorios e dashboards:

| Token | Hex | Uso |
|---|---|---|
| `--color-success` | `#22C55E` | Confirmacoes, metricas positivas, crescimento |
| `--color-warning` | `#F59E0B` | Avisos, atencao, metricas neutras |
| `--color-error` | `#EF4444` | Erros, metricas negativas, quedas |

---

## Cores por contexto de uso

### Email padrao BW (via Betinho)
| Elemento | Cor |
|---|---|
| Corpo do texto | `#333333` |
| Titulos H2 | `#1A1A1A` com border-bottom `#FF3900` |
| Titulos H3 | `#333333` |
| Header de tabela de dados | `#FF3900` com texto `#FFFFFF` |
| Label de tabela 2 colunas | fundo `whitesmoke` |
| Bordas | `#DDDDDD` |
| Fundo | `#FFFFFF` |

### Monthly Report / Apresentacoes dark
| Elemento | Cor |
|---|---|
| Fundo principal | `#1C1C1E` |
| Cards / superficie | `#111111` ou `#1A1A1A` |
| Accent | `#FF3900` |
| Texto principal | `#FFFFFF` |
| Texto secundario | `#AAAAAA` |

### Apresentacoes executivas (brand-facing)
| Elemento | Cor |
|---|---|
| Fundo | alternando `#000000` e `#FFFFFF` |
| Accent | `#FF3900` |
| Texto | `#FFFFFF` (sobre preto) ou `#000000` (sobre branco) |

---

## Regras de uso

**Faca:**
- Use APENAS as 3 cores da marca em material brand-facing
- Use neutros derivados apenas em documentos internos
- Garanta contraste WCAG AA minimo (4.5:1 para texto)
- CTAs sempre em `#FF3900`

**Nao faca:**
- Invente cores, cinzas ou gradientes para a marca
- Use azul, verde ou qualquer outra cor como "cor da BetWarrior"
- Chame o `#FF3900` de "vermelho" — e LARANJA (Pantone 1655 C)
- Use gradientes na identidade visual
- Use `--color-error` em contexto positivo ou `--color-success` em negativo

---

## Acessibilidade

| Texto | Fundo | Contraste | Status |
|---|---|---|---|
| `#FFFFFF` | `#000000` | 21:1 | Passa AAA |
| `#FFFFFF` | `#FF3900` | 3.6:1 | Passa AA Large |
| `#000000` | `#FF3900` | 5.8:1 | Passa AA |
| `#FFFFFF` | `#1C1C1E` | 17.4:1 | Passa AAA |
| `#1A1A1A` | `#FFFFFF` | 17.4:1 | Passa AAA |
| `#333333` | `#FFFFFF` | 12.6:1 | Passa AAA |

**Nota:** Texto branco sobre fundo laranja `#FF3900` nao passa AA para texto pequeno. Usar apenas em textos grandes (18pt+), botoes ou headers de tabela.
