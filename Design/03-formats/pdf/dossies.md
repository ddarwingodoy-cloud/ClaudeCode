# PDFs — Dossies de Jogador

> Formato para perfis completos de jogadores de futebol. Usado para analise de patrocinio, embaixadores ou parcerias.

---

## Especificacoes

| Propriedade | Valor |
|---|---|
| Orientacao | Portrait |
| Dimensoes | 210x297mm (A4) |
| Margem | 20mm |
| Fonte | Inter (Regular, SemiBold, Bold) |
| Import | `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900` |
| Geracao | Chrome headless. NUNCA WeasyPrint. |

---

## Cores

| Elemento | Cor | Uso |
|---|---|---|
| Fundo principal | `#FFFFFF` | Background da pagina |
| Header borda | `#FF3900` | Borda inferior do header (3px) |
| Profile bar fundo | `#1C1C1E` | Barra de KPIs do jogador |
| Profile bar texto | `#FFFFFF` | Texto sobre barra escura |
| KPI value | `#FF3900` | Numero destaque nos KPI cards |
| Texto principal | `#1A1A1A` | Corpo de texto |
| Texto secundario | `#666666` | Captions, metadados |
| Zebra striping | `#F5F5F5` | Linhas alternadas em tabelas |
| Header tabela | `#FF3900` fundo, `#FFFFFF` texto | Cabecalho de tabelas de dados |
| Risk card fundo | `#1C1C1E` | Card de risk assessment |
| Risk card texto | `#FFFFFF` | Texto sobre card escuro |
| Success | `#22C55E` | Risco baixo |
| Warning | `#F59E0B` | Risco medio |
| Error | `#EF4444` | Risco alto |

---

## Estrutura

```
PAGINA 1:
├── HEADER
│   ├── Foto do jogador (circular ou retangular, 120x120px)
│   ├── Nome completo (Inter Bold, 28px)
│   ├── Posicao | Time | Idade
│   └── Borda inferior #FF3900 (3px)
│
├── PROFILE BAR (fundo #1C1C1E, border-radius 8px)
│   ├── KPI Card: Seguidores Instagram
│   ├── KPI Card: Engajamento medio
│   ├── KPI Card: Valor de mercado (Transfermarkt)
│   └── KPI Card: Gols na temporada (ou metrica relevante)
│
├── BIO
│   └── Paragrafo curto (3-5 linhas) sobre o jogador
│
└── TABELA DE DADOS
    ├── Header: #FF3900 com texto branco
    ├── Zebra striping: linhas alternadas #F5F5F5
    └── Dados: estatisticas, historico, contratos

PAGINA 2 (se necessario):
├── RISK ASSESSMENT (card fundo #1C1C1E)
│   ├── Risco judicial (badge colorido)
│   ├── Risco de imagem (badge colorido)
│   ├── Risco contratual (badge colorido)
│   └── Observacoes
│
├── ANALISE DE MARCA PESSOAL
│   └── Fit com BetWarrior, publico, alinhamento
│
└── FOOTER
    ├── Classificacao: A / B / C (badge)
    ├── Recomendacao: Prosseguir / Aguardar / Descartar
    ├── Autor: Marketing BR
    └── Data de emissao
```

---

## CSS base

```css
@page { size: A4; margin: 20mm; }

body {
    font-family: 'Inter', sans-serif;
    color: #1A1A1A;
    font-size: 14px;
    line-height: 1.5;
    margin: 0;
}

/* HEADER */
.header {
    border-bottom: 3px solid #FF3900;
    padding-bottom: 16px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 20px;
}

.header img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 8px;
}

.header h1 {
    font-size: 28px;
    font-weight: 700;
    margin: 0 0 4px 0;
}

.header .meta {
    font-size: 14px;
    color: #666666;
}

/* PROFILE BAR */
.profile-bar {
    background: #1C1C1E;
    color: #FFFFFF;
    border-radius: 8px;
    padding: 20px;
    display: flex;
    justify-content: space-around;
    margin-bottom: 24px;
    page-break-inside: avoid;
}

.kpi-card {
    text-align: center;
}

.kpi-value {
    font-size: 28px;
    font-weight: 700;
    color: #FF3900;
    display: block;
}

.kpi-label {
    font-size: 11px;
    color: #AAAAAA;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* BIO */
.bio {
    margin-bottom: 24px;
    line-height: 1.6;
}

.bio h2 {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
}

/* TABELAS */
table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
    page-break-inside: avoid;
}

table th {
    background: #FF3900;
    color: #FFFFFF;
    padding: 8px 12px;
    text-align: left;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

table td {
    padding: 8px 12px;
    border-bottom: 1px solid #E5E5E5;
    font-size: 13px;
}

table tr:nth-child(even) {
    background: #F5F5F5;
}

/* RISK ASSESSMENT */
.risk-card {
    background: #1C1C1E;
    color: #FFFFFF;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 24px;
    page-break-inside: avoid;
}

.risk-card h2 {
    font-size: 18px;
    font-weight: 600;
    color: #FFFFFF;
    margin-bottom: 16px;
}

.risk-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid #2A2A2A;
}

.risk-item:last-child {
    border-bottom: none;
}

.badge-low {
    background: #22C55E;
    color: #FFFFFF;
    padding: 2px 10px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
}

.badge-medium {
    background: #F59E0B;
    color: #FFFFFF;
    padding: 2px 10px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
}

.badge-high {
    background: #EF4444;
    color: #FFFFFF;
    padding: 2px 10px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
}

/* FOOTER */
.footer {
    margin-top: 32px;
    padding-top: 16px;
    border-top: 1px solid #DDDDDD;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 12px;
    color: #666666;
}

.classification {
    font-size: 14px;
    font-weight: 700;
}

.classification-a { color: #22C55E; }
.classification-b { color: #F59E0B; }
.classification-c { color: #EF4444; }

/* PAGE BREAKS */
.section, .profile-bar, .risk-card, table {
    page-break-inside: avoid;
}
```

---

## Exemplo de HTML (header + profile bar)

```html
<div class="header">
    <img src="[foto-jogador-base64]" alt="Nome do Jogador">
    <div>
        <h1>NOME DO JOGADOR</h1>
        <div class="meta">Atacante | Flamengo | 27 anos</div>
    </div>
</div>

<div class="profile-bar">
    <div class="kpi-card">
        <span class="kpi-value">2.4M</span>
        <span class="kpi-label">Seguidores IG</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-value">3.2%</span>
        <span class="kpi-label">Engajamento</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-value">EUR 8M</span>
        <span class="kpi-label">Valor Mercado</span>
    </div>
    <div class="kpi-card">
        <span class="kpi-value">12</span>
        <span class="kpi-label">Gols 2026</span>
    </div>
</div>
```

---

## Checklist antes de gerar

1. Header com borda `#FF3900` (3px)?
2. Profile bar com fundo `#1C1C1E`?
3. KPI values em `#FF3900`?
4. Tabelas com zebra striping?
5. Risk assessment em card escuro?
6. Footer com classificacao A/B/C?
7. `page-break-inside: avoid` em toda secao?
8. Foto do jogador em base64 ou URL absoluta?
9. Gerado com Chrome headless?
10. Dados verificados (NAO inventados)?
