# Assets

Todos os arquivos binarios e referencias visuais do Design System BetWarrior Brasil.

---

## Estrutura Atual

```
04-assets/
├── logos/                    # Logos oficiais BetWarrior
│   ├── betwarrior_v1.rar    # Pack v1 (isotipo + logotipo, todas as versoes)
│   └── betwarrior_v2.rar    # Pack v2 (versao atualizada)
│
├── brandbooks/               # Manuais de marca oficiais
│   ├── BetWarrior_brandbook_brasil_v1.pdf    # Brandbook Brasil (Out/2025, 22 pags)
│   └── BetWarrior_brandbook_es_v3_logo_con_ejemplos.pdf  # Manual de marca global v3 (30 pags)
│
├── banners-referencia/       # Banners reais do site (referencia visual)
│   ├── BWBR_BANNERS-SITE-2026_ANDROID-APP_REV1.jpg
│   ├── BWBR_BANNERS-SITE-2026_BRASILEIRAO_REV1.jpg
│   └── BWBR_BANNERS-SITE-2026_COPA_REV1.jpg
│
└── README.md                 # Este arquivo
```

## Logos Usados em Documentos HTML

Alem dos packs RAR, os logos em PNG para uso direto em documentos estao copiados nas pastas HTML de cada projeto:

| Arquivo | Uso | Onde encontrar |
|---|---|---|
| `bw-logo.png` | Logo branco (fundos escuros) | `Projetos/Monthly Report/`, `Projetos/Branding/Html/` |
| `bw-logo-preto.png` | Logo preto (fundos claros) | `Projetos/Monthly Report/`, `Projetos/Branding/Html/` |
| `bw-icon.png` | Isotipo W laranja | `Projetos/Monthly Report/`, `Projetos/Branding/Html/` |

## Brandbooks — Referencia Rapida

| Documento | Conteudo | Consultar para |
|---|---|---|
| **brandbook_brasil_v1** | Posicionamento BR, contexto cultural, persona, tom de voz, fotografia | Estrategia de marca, insights culturais |
| **brandbook_es_v3** | Identidade visual global: logo, cores, tipografia, morfologia, fotografia | Regras de logo, cores (#FF3900), tipografia (Integral CF), morfologia (90°) |

## Banners — Referencia Visual

3 banners reais do site BetWarrior Brasil (2026). Uteis como referencia de:
- Tom visual da marca em acao
- Uso de cores (fundo escuro, tipografia laranja/branca)
- CTAs ("CRIAR CONTA", "ENTRAR")
- Tagline atual: "ENTRA, JOGA E MOSTRA!"
- Layout de carrossel de jogos

## Convencoes

- kebab-case para arquivos novos
- Sufixos: `-primary`, `-dark`, `-light`, `-preto`
- Sempre otimizar (TinyPNG para PNG, SVGO para SVG)
