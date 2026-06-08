# Semanal Pedro — Playbook

> Report recorrente (sexta / antes da reunião de liderança de segunda). É preencher a aba **📈 Marketing** do *Weekly KPI Tracker — BetWarrior Brazil*.
> Tracker multi-departamento: cada owner preenche sua aba. Regra do tracker: **update every Monday before 9am**.

## Planilha de destino — arquivo NOVO a cada mês

O Pedro (Country Manager BR) replica o tracker **mensalmente** ("same structure, clean slate"). Usar sempre o arquivo do mês corrente:
- **Junho/2026:** `1TduQ6IlTYYWN3knpGXYMch9Pgl0_C4FrcLiSIanvSDc`
- Maio/2026 (antigo): `1QjKMEtJ2X8_7bRFFOvc4RDZ2F_ErTz8D2Hp1yBJtosk`
- Aba de produção: **📈 Marketing**.

**Layout mensal:** A=KPI · B=Target · **C–G = semanas do mês (W23…W27)** · H=Comments. Colunas e Targets já vêm prontos — **só preencher a coluna da semana + Comments. Não inserir coluna.**

- **Editar SOMENTE linhas 4–11** (Acquisition / Efficiency / Business Performance). Linhas 12+ são de Giuliano e Ana — **nunca tocar**.
- Aba **🏠 Dashboard**: B4/F4 (semana e datas) já vêm prontos. Linha Marketing (row 6) é **manual** (as outras áreas usam fórmula): E6=FTDs da semana, F6=`=E6/D6-1`, **G6=Status, H6=Trend** (Status+Trend são pedido explícito do Pedro, toda semana).
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
6. Atualizar a aba 🏠 Dashboard, linha Marketing: Current (E6), Δ (F6), **Status (G6) e Trend (H6)**.

## ACHADO CRÍTICO — backfill retroativo (07/06/2026)

`FactFullRegistration` e `FactFirstDeposit` recebem dados **retroativos** dias após a data. Rodar no próprio fim de semana **subestima**. Ex.: W22 lançado 3.160 FullReg / 631 FTDs; a mesma query 4–7 dias depois deu 3.659 / 769 (+16% / +22%). **Rodar o número final na segunda de manhã.** O último dia da janela, se for "hoje", vem incompleto.

## Tom do Status / Trend (Dashboard)

- **Status** = expectativa estratégica do mês, não o Δ literal de uma semana parcial vs meta mensal (artefato — sempre muito negativo no início do mês). Não pintar cenário ruim no 1º report do mês; pesar ramp/sazonalidade (Copa, Casa Mundialista, afiliados, investimento maior).
- **Trend** pode ser discursiva: comunicar a convicção (direção + por quê), não só uma seta — mantendo um ponto de atenção honesto (ex.: qualidade do FTD).

## Atenção a incidentes

Picos atípicos de registros/FTDs num dia podem ser incidentes (ex.: promo/bônus vazado ao público fora do target). Verificar RCA na própria pasta `.SEMANAL PEDRO/` e sinalizar no comentário que o pico é aquisição oportunista, não saudável.
