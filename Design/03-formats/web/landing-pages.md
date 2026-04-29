# Landing Pages

## Princípios

- **1 objetivo por página.** Conversão clara (cadastro, depósito, etc).
- **Mobile-first.** 60%+ do tráfego BR é mobile.
- **Above the fold:** valor + CTA visíveis sem rolar.
- **Performance:** LCP < 2.5s, CLS < 0.1, INP < 200ms.

## Estrutura padrão

```
1. Header minimalista (logo + CTA secundário)
2. HERO
   - Headline (benefício principal)
   - Subheadline (clarificação)
   - CTA principal
   - Visual de apoio
3. PROVA SOCIAL (opcional)
   - Stats, logos de provedores, depoimentos
4. BLOCOS DE BENEFÍCIO (3-4)
5. CTA SECUNDÁRIO + APOIO
6. FAQ (opcional)
7. FOOTER COMPLETO (compliance)
```

## Hero

- **Headline:** máximo 8 palavras, foco no benefício
- **Subheadline:** 1-2 linhas explicando como
- **CTA:** verbo + benefício ("Cadastre-se e ganhe R$ X")
- **Visual:** evitar stock photos genéricas, preferir produto real ou ilustração proprietária

## Botões

| Tipo | Estilo | Uso |
|---|---|---|
| Primário | bg `--color-primary`, texto branco, radius `--radius-md` | CTA principal |
| Secundário | bg transparente, borda `--color-primary`, texto `--color-primary` | CTA secundário |
| Terciário | apenas texto sublinhado | Links em texto |

Tamanhos:
- Desktop: padding 12px 24px, fonte 16px
- Mobile: padding 14px 28px, fonte 16px (touch target mínimo 44px altura)

## Formulários

- Labels acima do input (não placeholder-only)
- Validação inline em blur
- Mensagens de erro em vermelho `--color-error` com ícone
- Senha com toggle de visualização
- Botão submit nunca desabilitado por padrão (mostrar erro ao tentar)

## SEO básico

- `<title>` único, 50-60 chars, com keyword principal
- Meta description 150-160 chars
- 1 H1 por página
- Estrutura semântica (header, main, section, footer)
- Open Graph para compartilhamento

## Performance

- Imagens: WebP/AVIF, lazy load abaixo da fold
- CSS crítico inline
- JS deferred
- Fontes com `font-display: swap`
- CDN para todos os assets

## Footer obrigatório

```
[LOGO]
[MENUS DE NAVEGAÇÃO]
[REDES SOCIAIS]
[BLOCO COMPLIANCE]
- CNPJ + Licença SPA
- Endereço operacional
- Política de Privacidade | Termos | Jogo Responsável | Contato
- "+18 | Aposte com responsabilidade"
- Logos de jogo responsável (CVV, etc)
[COPYRIGHT]
```
