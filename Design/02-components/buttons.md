# Botões

## Variantes

### Primary
Para ação principal da tela. Apenas 1 por seção.
```css
background: var(--color-primary);
color: #FFFFFF;
padding: 12px 24px;
border-radius: var(--radius-md);
font-weight: 600;
font-size: 16px;
border: none;
```

### Secondary
Ação alternativa, importância secundária.
```css
background: transparent;
color: var(--color-primary);
border: 1.5px solid var(--color-primary);
padding: 10.5px 22.5px; /* compensa borda */
border-radius: var(--radius-md);
font-weight: 600;
font-size: 16px;
```

### Tertiary / Text
Ações de menor importância, navegação.
```css
background: transparent;
color: var(--color-primary);
border: none;
padding: 8px 12px;
font-weight: 500;
text-decoration: underline;
```

### Destructive
Ações destrutivas (excluir, cancelar saque, etc).
```css
background: var(--color-error);
color: #FFFFFF;
/* resto idêntico ao primary */
```

## Tamanhos

| Tamanho | Padding | Font-size | Min-height | Uso |
|---|---|---|---|---|
| sm | 8px 16px | 14px | 36px | Tabelas, áreas densas |
| md | 12px 24px | 16px | 44px | Padrão |
| lg | 16px 32px | 18px | 52px | Hero, CTAs principais |

**Touch target mínimo:** 44x44px (WCAG)

## Estados

| Estado | Visual |
|---|---|
| Default | Conforme variante |
| Hover | Background `--color-primary-dark` (primary), background `--color-primary-light` (secondary) |
| Active/Pressed | Levemente mais escuro + scale(0.98) |
| Focus | Outline 2px `--color-primary` com offset 2px |
| Disabled | Opacity 0.5, cursor not-allowed |
| Loading | Spinner inline + texto "Carregando..." ou similar |

## Conteúdo

- **Verbo de ação.** "Apostar", "Depositar", "Cadastrar", não "Clique aqui"
- **Curto.** 1-3 palavras ideal
- **Específico.** "Apostar agora" > "Continuar"
- **Sentence case** padrão. ALL CAPS apenas em variante específica de campanha.

## Ícones

- À esquerda do texto (padrão)
- À direita apenas para indicar direção (seta "próximo")
- Tamanho proporcional à fonte (16px para botão md)
- Espaço de 8px entre ícone e texto

## Acessibilidade

- Sempre com `aria-label` se for apenas ícone
- Estado de loading com `aria-busy="true"`
- Foco visível obrigatório (não remover outline sem substituir)
- Contraste mínimo 4.5:1 entre texto e fundo
