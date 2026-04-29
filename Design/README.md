# BetWarrior Brasil — Design System

> Fonte unica da verdade para todo design, comunicacao e material visual da BetWarrior Brasil.
> Mantido por: Time de Marketing BR | Owner: JP (Joao Paulo Marques)

---

## Para o Betinho (e qualquer agente Claude)

**Antes de gerar QUALQUER design, leia obrigatoriamente:**

1. `05-betinho/instructions.md` — manual operacional completo
2. `00-brand/` — voz, compliance e regras inegociaveis
3. `01-foundations/` — cores, tipografia, espacamento, iconografia

**Depois, conforme o tipo de entrega:**

| Tipo de entrega | Arquivos obrigatorios |
|---|---|
| Monthly Report (PDF dark) | `03-formats/pdf/relatorios.md` |
| Report executivo (EMT) | `03-formats/pdf/relatorios.md` |
| Apresentacao executiva (brand) | `03-formats/pdf/apresentacoes-executivas.md` |
| Dossie de jogador | `03-formats/pdf/dossies.md` |
| Email interno / EMT | `03-formats/email/README.md` |
| Email transacional | `03-formats/email/transactional.md` |
| Email promocional / CRM | `03-formats/email/crm-promocional.md` |
| GTM Update | `05-betinho/examples.md` (secao GTM) |
| KPI Daily | `05-betinho/instructions.md` (secao KPI) |

---

## Identidade da marca (resumo)

- **Cores:** APENAS 3 — Laranja `#FF3900`, Preto `#000000`, Branco `#FFFFFF`
- **Tipografia:** Integral CF (titulos, PAGA), Archivo (corpo), Roboto (fallback)
- **Morfologia:** Retangulos 90 graus. ZERO border-radius em material brand-facing.
- **Fotografia:** P&B com gradiente laranja, alto contraste, brasileiros reais
- **Voz:** Apaixonada, inteligente, cumplice. "A bet de quem sabe que o jogo sempre pode virar."

---

## Estrutura

```
00-brand/          — quem somos, como falamos, o que NAO podemos fazer
01-foundations/    — tokens visuais (cores, tipografia, espaco, icones)
02-components/     — blocos reutilizaveis (botoes, cards, formularios)
03-formats/        — regras especificas por tipo de output (PDF, email, slides)
04-assets/         — arquivos binarios (logos, fontes, imagens)
05-betinho/        — manual operacional e exemplos reais do agente
```

---

## Regras rapidas

| Regra | Detalhe |
|---|---|
| Cor primaria | `#FF3900` — LARANJA, nao vermelho |
| Cores da marca | Apenas 3: laranja, preto, branco |
| Titulos | SEMPRE uppercase |
| Border-radius brand | ZERO. Cantos retos. |
| Border-radius interno | Permitido (4-8px) em relatorios/dashboards |
| PDF | Chrome headless. NUNCA WeasyPrint. |
| Page breaks | `page-break-inside: avoid` em toda secao |
| Email | Inline styles. Arial 10.5pt. Tabelas para layout. |
| Drop shadow | NUNCA em tipografia |
| Compliance | +18, aposte com responsabilidade, canal de apoio |

---

## Como contribuir

1. Toda mudanca via Pull Request
2. Atualizar `CHANGELOG.md` na raiz
3. Aprovacao obrigatoria do owner antes de merge
4. Versionamento semantico (MAJOR.MINOR.PATCH)

---

**Versao atual:** 1.0.0
**Ultima atualizacao:** 18/04/2026
