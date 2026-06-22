# Semanal Pedro — Playbook

> Report recorrente (segunda, antes das **10h** / reunião de liderança). Tracker multi-departamento: cada owner preenche a sua.

## Destinos da segunda (1 run do script alimenta tudo)

São **3 lugares** — **2 planilhas que atualizo** + 1 cópia manual do Darwin:

1. **Planilha mensal do Pedro** (*Weekly KPI Tracker — BetWarrior Brazil*; **link NOVO a cada mês, o Darwin informa**) — **DUAS abas:**
   - **📈 Marketing** — coluna da semana corrente + Comments (col H).
   - **🏠 Dashboard** — row 4 (semana/datas) + row 6 (Marketing: Target / Current / Δ / Status / Trend).
2. **Planilha Tracking Semanal (Linha 5)** no Drive (`1r1BKEPoIRKm_H-xletID8mav3L3-Wh0ZewlvZn6mXTY`, aba Tracking) — preencher a linha da semana (REAL\|TARGET, WoW Diff%, Comentários). **É DAQUI que o Darwin copia pro Confluence.**
3. **Confluence DB Row 5** (database "KPIs Tracker", space PM) — **cópia manual** da planilha do passo 2. Database não tem API limpa de escrita → **copiar e colar à mão** (detalhe na última seção).

## Planilha de destino — arquivo NOVO a cada mês

O Pedro (Country Manager BR) replica o tracker **mensalmente** ("same structure, clean slate"). Usar sempre o arquivo do mês corrente:
- **Junho/2026:** `1TduQ6IlTYYWN3knpGXYMch9Pgl0_C4FrcLiSIanvSDc`
- Maio/2026 (antigo): `1QjKMEtJ2X8_7bRFFOvc4RDZ2F_ErTz8D2Hp1yBJtosk`
- Aba de produção: **📈 Marketing**.

**Layout mensal:** A=KPI · B=Target · **C–G = semanas do mês (W23…W27)** · H=Comments. Colunas e Targets já vêm prontos — **só preencher a coluna da semana + Comments. Não inserir coluna.**

- **Editar SOMENTE linhas 4–11** (Acquisition / Efficiency / Business Performance). Linhas 12+ são de Giuliano e Ana — **nunca tocar**.
- Aba **🏠 Dashboard** (June file `1TduQ6Il`): **row 4** ⚡ CURRENT WEEK = atualizar **B4** (semana, ex W25) + **F4** (datas, ex "Jun 15 – 21, 2026"). **Row 6 = 📈 Marketing** (A6/B6/C6 fixos: Marketing · JP Marques · FTDs), **manual** (outras áreas usam fórmula): **D6**=Target da semana (W25=2.011), **E6**=Current (FTDs da semana), **F6**=`=E6/D6-1` (Δ), **G6**=Status (`🔴 Below target` / `🟡 At risk` / `🟢 On track`), **H6**=Trend (editorial). **Status + Trend = pedido explícito do Pedro, toda semana.**
- **Frequência:** atualizar antes das **10h** de segunda (mudou de 9h em jun/2026).

## Os 5 KPIs (linhas)

| Linha | KPI | Cálculo |
|---|---|---|
| 5 | Full Registrations (KYC) | `COUNTROWS(FactFullRegistration)` · filtro External · Step 4 Onboarding Finished |
| 6 | FTDs | `COUNTROWS(FactFirstDeposit)` · filtro External · total (não por canal) |
| 8 | CPA Blended (USD) | Investimento total ÷ FTDs totais |
| 10 | GGR (BRL) | GB − GW (GW = GAME_WIN + CASH_OUT + CORRECTION) |
| 11 | GGR / FTD (BRL) | GGR ÷ FTDs da semana |

## Fontes de dados

| Dado | Fonte | Detalhe |
|---|---|---|
| Full Reg, FTDs, GGR (realizado) | **Power BI** dataset Brazil Main Report | `c489d219-ef18-4f9e-9c5c-422c9092e3aa` · group `00ecb2bb-6c61-4d09-badb-a4df0c948b02` · token em `~/.claude/credentials/` (device code flow, renovar antes). Guia: `Agentes/BI/pbi-overview-bira.md` |
| **Metas do mês** (Target) | **Forecast Dada** | `1UtdEyu8MhpfADMF7TOUDj2SeSaJcf6gR_yXxThTUnno` · coluna do mês. FTDs (linha 8), CPA Blended (linha 6), GGR R$ (linha 44), GGR/FTD (linha 53). **Full Reg não existe lá → derivar FTD ÷ CR 23%** |
| **Investimento** (p/ CPA, quando não há real lançado) | **Distribuição Orçamentária por Canal** | `11X5KEcvUgsMRMFcc4vAkiv7WB-cNaAZQpeXSA2VRwvY` · linha TOTAL do mês (com contingência) · **rateio proporcional: budget mensal × dias da semana ÷ dias do mês** |
| Investimento real diário (quando existir) | **PACING-PERFO** (Diego/Pipol) | `1LnnVk3mtjmx6ibXXtyA7_JqIxu0gf8DyeCK9MGve53w` · cria aba do mês. Midia.xlsx (`1FBhZ4HoAp-QTrI4LXoX73Q--XrIYVB_v99FpuWzj3Go`) tem PLAN/REAL mensal |

Metas Jun/2026: FTDs **6.343** · CPA **$159,05** · GGR **R$438.137** · GGR/FTD **R$69** · Full Reg derivado **27.578**.

## Processo

1. **Renovar token Power BI** (refresh; se expirado, device code flow — exige o Darwin autenticar no browser).
2. Rodar DAX por dia da semana (External): Full Reg, FTDs, GB, GW. GGR = GB − GW.
3. Calcular CPA (investimento proporcional ÷ FTDs) e GGR/FTD.
4. **Preencher a coluna da semana corrente** (já existe; não inserir) + Comments (col H), em **texto** (RAW): `5,966` / `$319.00` / `R$51,345` / `R$63`.
5. Conferir os Targets do mês (já vêm preenchidos; ajustar se a realidade do mês mudou).
6. Atualizar a aba 🏠 Dashboard: row 4 (B4 semana, F4 datas) + linha Marketing row 6 — Current (E6), Δ (F6), **Status (G6) e Trend (H6)**.
7. Preencher a **planilha Tracking Semanal (Drive)** na linha da semana (REAL\|TARGET, WoW, Comentários) e **copiar/colar essa linha na Row 5 do Confluence** (à mão; database não tem write).
8. **Ao terminar de atualizar as duas planilhas, abrir as duas no navegador do Darwin** (macOS `open`) — primeiro link = planilha mensal do mês corrente (trocar a cada mês):
   ```
   open "https://docs.google.com/spreadsheets/d/1TduQ6IlTYYWN3knpGXYMch9Pgl0_C4FrcLiSIanvSDc/edit" \
        "https://docs.google.com/spreadsheets/d/1r1BKEPoIRKm_H-xletID8mav3L3-Wh0ZewlvZn6mXTY/edit"
   ```

> O `semanal_monday.py` já cospe os **3 blocos rotulados na ordem de colagem** ([1] Marketing, [2] Dashboard, [3] Tracking Semanal/Confluence). Rodar e colar.

## ACHADO CRÍTICO — backfill retroativo (07/06/2026)

`FactFullRegistration` e `FactFirstDeposit` recebem dados **retroativos** dias após a data. Rodar no próprio fim de semana **subestima**. Ex.: W22 lançado 3.160 FullReg / 631 FTDs; a mesma query 4–7 dias depois deu 3.659 / 769 (+16% / +22%). **Rodar o número final na segunda de manhã.** O último dia da janela, se for "hoje", vem incompleto.

> **REGRA: todo número acompanha a DATA DE CORTE.** O **GGR/NGR liquida MAIS DEVAGAR que FTD** (settlement vs depósito) — mesmo segunda de manhã, o **domingo (último dia) pode vir incompleto** e mudar o GGR sem mexer no FTD. Caso real W25 (22/06): rodei e deu GGR −R$15,8k; o finance (Luiz) tinha **−R$25,2k** — a diferença era exatamente o GGR não-liquidado do dia 21. **Antes de travar: cruzar o GGR do último dia com o finance/Power BI.** Sempre rotular números com a janela + o cutoff. Ver [[feedback_data_de_corte]].

## Tom do Status / Trend (Dashboard)

- **Status** = expectativa estratégica do mês, não o Δ literal de uma semana parcial vs meta mensal (artefato — sempre muito negativo no início do mês). Não pintar cenário ruim no 1º report do mês; pesar ramp/sazonalidade (Copa, Casa Mundialista, afiliados, investimento maior).
- **Trend** pode ser discursiva: comunicar a convicção (direção + por quê), não só uma seta — mantendo um ponto de atenção honesto (ex.: qualidade do FTD).

## Atenção a incidentes

Picos atípicos de registros/FTDs num dia podem ser incidentes (ex.: promo/bônus vazado ao público fora do target). Verificar RCA na própria pasta `Semanais/Semanal Pedro/` e sinalizar no comentário que o pico é aquisição oportunista, não saudável.

## Curva de sazonalidade: META SEMANAL (FONTE ÚNICA, usar em TODOS os trackers)

> Decidido com Darwin (14/06/2026). **Não comparar real semanal com meta mensal cru** (artefato). A meta mensal é distribuída por uma curva de sazonalidade da Copa. Usar a MESMA curva no tracker do Pedro, na Tracking Semanal (Linha 5) e no WPR.

**Modelo (junho/2026, Copa):** peso diário **1,0 pré-Copa (1-10/jun)** e **1,8 nos dias de Copa (a partir de 11/jun, lift L=+80%)**. Soma por semana, normaliza pra 100%. O lift L e a data de início da Copa são os únicos parâmetros, re-derivar por mês.

| Semana | Peso | % do mês |
|---|---|---|
| W23 (1-7) | 7,0 | 15,22% |
| W24 (8-14) | 10,2 | 22,17% |
| W25 (15-21) | 12,6 | 27,39% |
| W26 (22-28) | 12,6 | 27,39% |
| W27 (29-30) | 3,6 | 7,83% |

**Metas mensais junho (corrigidas):**
- **FTD = 7.343** (6.343 base linha 8 do Forecast **+ 1.000 afiliados** linha 9, o real External inclui afiliados, então a meta também)
- **NGR = R$385.561** (Forecast linha 47)
- **GGR = R$438.137** (Forecast linha 44)
- **Full Reg = 31.926** (= FTD ÷ CR 23%)
- **GGR/FTD = R$60** (= GGR ÷ FTD; razão, não distribui na curva, é flat)
- **CPA = $159,05** (taxa de eficiência, não distribui na curva, é flat semanal)

**Metas semanais resultantes (aplicar curva a FTD/NGR/GGR/FullReg):**
| Semana | FullReg | FTD | GGR | NGR |
|---|---|---|---|---|
| W23 | 4.857 | 1.117 | 66.673 | 58.672 |
| W24 | 7.079 | 1.628 | 97.152 | 85.494 |
| W25 | 8.745 | 2.011 | 120.011 | 105.610 |
| W26 | 8.745 | 2.011 | 120.011 | 105.610 |
| W27 | 2.500 | 575 | 34.289 | 30.174 |

**Onde isto vive:** Pedro tracker → col B "Target Semanal (W24)" = a semana corrente, meta mensal vai no comentário. Tracking Semanal (Linha 5) → coluna Target de cada semana. WPR → meta dos painéis.

## Tracking Semanal — Confluence DB (Row 5 = Marketing)

> O 2º destino da segunda: os KPIs semanais que a liderança lê no **Confluence**. **NÃO é Google Sheet, é um database do Confluence** → atualizar **copiando e colando** na linha (não tem API limpa de database).

- **URL:** `https://betwarrior.atlassian.net/wiki/spaces/PM/database/5814222859` (space PM).
- **Row 5 = Marketing**, Owner Darwin Godoy. As outras linhas são de outros owners, **não tocar**.
- **Conteúdo da Row 5 (colunas):**
  - **Status Update:** pill **"Updated"** (verde).
  - **MTD KPIs Updates | [período]** — bloco `REAL | TARGET`:
    - `FTDs → {real} | {target}`
    - `CPA → {real} | {target}`
    - `NGR → R${real} | R${target}`
  - **WoW Diff - [Wxx x Wxx] %:**
    - `FTD → {±%} (vs {FTD da semana anterior})`
    - `CPA → {±%} (vs {CPA da semana anterior})`
    - `NGR → {±%} (vs R${NGR da semana anterior})`
  - **Next Steps / Owner:** editorial (próximos passos).
- **KPIs daqui = FTDs, CPA, NGR** (sem registros, então registros=1º step **não afeta** esta linha).
- **Fonte:** o `semanal_monday.py` já cospe o bloco "Confluence DB (Row 5)" pronto pra colar (Real|Target + WoW com valor da semana anterior).
- **Planilha de trabalho** (rascunho dos números antes de colar no Confluence): `1r1BKEPoIRKm_H-xletID8mav3L3-Wh0ZewlvZn6mXTY` (aba gid 1101930613).

## FORMATO EXATO DA EXECUÇÃO — seguir IGUAL toda semana (travado em W25, 22/06/2026)

> Tudo em **INGLÊS** (convenção da planilha). **Decompor antes de narrar** (casino×esporte via hold/margem) quando GGR/NGR vier estranho. **Gross Bets** (nunca "handle"); hold = GGR ÷ Gross Bets; "high-value players" (nunca "whales").

### Mapa de células — aba 📈 Marketing (arquivo do mês)
- **Col B = target da semana corrente → ROLAR toda semana:** `B3` header "Target Semanal (Wxx)"; `B5` FullReg, `B6` FTD, `B10` GGR (curva, tabela acima). `B8` CPA ($159.05) e `B11` GGR/FTD (R$60) são **flat, não mudam**.
- **Col da semana (C…G; W23=C … W27=G) = actuals:** linha `5` FullReg, `6` FTD, `8` CPA, `10` GGR, `11` GGR/FTD. Formato: `3,069` / `891` / `$105.65` / `-R$15,780` / `-R$18`.
- **Col H = Comments, um por KPI**, estilo: `[Monthly target: X] {valor}, {WoW}, {% pace}. {1 frase de contexto}`. **Nunca escrever nas linhas de seção (4/7/9)** — podem ser merge.

### Mapa de células — aba 🏠 Dashboard
- `B4` = semana (Wxx); `F4` = datas `Jun D – 21, 2026`.
- Row 6 (Marketing): `D6` target FTD, `E6` current FTD, `F6` = `=E6/D6-1` (fórmula, formato %), `G6` status pill (`🔴 Below target` / `🟡 At risk` / `🟢 On track`), `H6` Trend (inglês, começa com seta ↑/↓/→).
- **Status = leitura estratégica do mês** (não Δ literal). FTD longe da meta → manter 🔴.

### Planilha Tracking Semanal (Drive) — 1 linha por semana (`1r1BK…`)
- Col B (`REAL | TARGET`), números pt-BR, multilinha:
  `FTDs → {real} | {target}` / `CPA → {real} | {target}` / `NGR → R${real} | {target}`
- Col C (`WoW Diff%`), **decimais com vírgula**: `FTD → ±x,x% (vs {prev})` / `CPA → …` / `NGR → …`
- Col D (Comentários): narrativa em inglês (profundidade da W24) + `Next steps:` numerado.

### Confluence Row 5 (copiar da Tracking, à mão)
- `Status Update`: pill **Updated** · `MTD KPIs (REAL | TARGET)`: FTDs/CPA/NGR · `WoW Diff%`: FTD/CPA/NGR · `Next Steps`: numerado (o mesmo do col D).

### Convenções de narrativa TRAVADAS
- **CPA sem gasto real:** `estimate; real spend pending - awaiting Perfo's results update that feeds the PACING` (dá o peso a Perfo/Juanca, fonte que o Diego consome). Ver [[perfo-search-escalation]].
- **Receita negativa:** decompor hold casino×esporte; handle subiu + margem negativa = **variância, não volume**; usar "bias to revert". Ver [[feedback_decompose_aggregate]] e [[feedback_no_causal_overclaim]].
- **Afiliados:** `continue the hiring pacing (area manager + partners)` — **nunca** "unlock ramp".
- **Última ação:** abrir as 2 planilhas no navegador (passo 8).
