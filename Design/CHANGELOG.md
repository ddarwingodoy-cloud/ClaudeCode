# Changelog

Todas as mudancas significativas neste design system sao documentadas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/).
Versionamento [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.0.0] — 2026-04-18

### Preenchido com dados reais
- **01-foundations/colors.md** — Paleta real da marca: #FF3900 (laranja), #000000, #FFFFFF. Regra de apenas 3 cores. Neutros derivados para documentos internos. Cores semanticas. Tabela de acessibilidade.
- **01-foundations/typography.md** — Integral CF (primaria, paga), Archivo (secundaria), Roboto (terciaria). Escala tipografica completa. Fontes por tipo de documento. Import Google Fonts.
- **01-foundations/spacing.md** — Morfologia retangular 90 graus. Border-radius zero para brand, permitido para internos. Regra de page-break-inside. Escala base-4.
- **01-foundations/iconography.md** — Lucide como padrao recomendado. Regras de uso por tipo de documento.
- **00-brand/brand-voice.md** — Posicionamento, proposito, conceito criativo "VIRA O JOGO". 3 personas (Torcedor Raiz, Estrategista, Social Bettor). Tom por contexto. Vocabulario completo. Exemplos reais.
- **00-brand/compliance.md** — Lei 14.790/2023, SPA/MF, outorga R$30M, dominio .bet.br. Disclaimers, restricoes por canal, PL 3.563/2025, Bolsa Familia.
- **00-brand/do-and-dont.md** — Regras reais do brandbook v3: sem curvas, sem diagonais, sem drop shadow, sem border-radius, fotos P&B com laranja.
- **05-betinho/instructions.md** — Manual operacional completo. 7 tipos de documento reais. Regras tecnicas aprendidas. Workflow. Referencias.
- **05-betinho/examples.md** — Exemplos reais: Monthly Report, Report executivo, Brand Evolution, Dossie, Email BW, GTM Update, KPI Daily. CSS de referencia.
- **03-formats/pdf/relatorios.md** — Monthly Report (landscape dark), Report executivo (EMT). Especificacoes completas com CSS base. Checklist de geracao.
- **03-formats/email/README.md** — Padrao completo de email BW: tipografia, cores, componentes HTML com codigo inline.
- **03-formats/email/transactional.md** — Exemplo completo com HTML inline, footer compliance.
- **03-formats/email/crm-promocional.md** — Exemplo completo com botao CTA, tabelas, footer compliance.
- **README.md** — Atualizado com identidade real, tabela de tipos de documento, regras rapidas. Versao 1.0.0.

### Adicionado
- **03-formats/pdf/apresentacoes-executivas.md** — Novo formato para apresentacoes brand-facing (landscape, Archivo Black, 3 cores, zero border-radius, paginas alternando P&B).
- **03-formats/pdf/dossies.md** — Novo formato para dossies de jogador (A4 portrait, Inter, header com borda laranja, KPI cards, risk assessment).

### Removido
- Todos os placeholders [PREENCHER] e valores #XXXXXX substituidos por dados reais
- Exemplos genericos substituidos por exemplos reais dos documentos produzidos

---

## [0.1.0] — 2026-04-18

### Adicionado
- Estrutura inicial do repositorio
- README principal com mapeamento de pastas
- 00-brand: brand-voice, compliance, do-and-dont
- 01-foundations: colors, typography, spacing
- 02-components: buttons
- 03-formats: email (geral, transacional, CRM), web (landing pages), pdf (relatorios), slides (pitch deck)
- 05-betinho: instructions.md
- Templates vazios para preenchimento futuro
