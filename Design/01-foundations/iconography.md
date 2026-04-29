# Iconografia

> A BetWarrior nao possui biblioteca de icones propria definida. Para documentos internos do Betinho, usamos SVG inline ou texto. Lucide e o padrao recomendado.

---

## Biblioteca padrao: Lucide

**Recomendacao oficial para documentos do Betinho:** [Lucide Icons](https://lucide.dev/)

- Open source (ISC License)
- Consistente, limpa, minimalista
- Compativel com SVG inline em HTML
- 1500+ icones disponiveis
- Estilo: outline, stroke uniforme

### CDN

```html
<!-- Via unpkg -->
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>

<!-- Ou SVG inline (preferido para PDFs) -->
```

---

## Tamanhos padrao

| Token | Tamanho | Uso |
|---|---|---|
| `--icon-sm` | 16px | Inline em texto, badges, indicadores |
| `--icon-md` | 20px | Padrao em listas, tabelas |
| `--icon-lg` | 24px | Navegacao, botoes com icone |
| `--icon-xl` | 32px | Destaques, KPI cards |

---

## Estilo

- **Stroke width:** 2px (padrao Lucide)
- **Cor padrao:** `currentColor` (herda do texto)
- **Estilo:** outline (stroke, nao filled)
- **Alinhamento:** vertical-align middle com texto

---

## Uso nos documentos do Betinho

### Monthly Report / Dashboards
- Icones como indicadores em KPI cards (setas up/down, trending)
- Cor do icone acompanha a semantica: `#22C55E` para positivo, `#EF4444` para negativo

### Emails
- NAO usar icones em emails (compatibilidade limitada)
- Usar emojis Unicode como alternativa quando necessario (ex: checkmark, seta)

### Dossies
- Icones de esporte ao lado do header do jogador
- Icones de status em risk assessment

### Apresentacoes executivas
- Evitar icones. A marca e tipografica. Se necessario, usar SVG inline simples.

---

## Icones especificos de produto (quando definidos)

A BetWarrior nao possui icones customizados definidos no brandbook atual. Quando necessarios:

- Usar Lucide para representacoes genericas de esporte
- Para logos de esportes especificos, usar assets oficiais da plataforma
- NUNCA criar icones customizados sem aprovacao de design
- NUNCA usar icones de terceiros sem verificar licenca

---

## Regras

**Faca:**
- Use SVG inline para PDFs (garante renderizacao)
- Mantenha stroke width consistente (2px)
- Alinhe icones com o texto adjacente

**Nao faca:**
- Use icones como decoracao sem funcao
- Misture bibliotecas de icones no mesmo documento
- Use icon fonts (compatibilidade ruim em PDF)
- Use icones coloridos em material brand-facing (a marca e tipografica)
