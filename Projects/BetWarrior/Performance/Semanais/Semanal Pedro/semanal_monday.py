#!/usr/bin/env python3
# Semanal Pedro + Tracking Semanal + Confluence — coletor de SEGUNDA (numero final, pos-backfill)
# Uso:  python3 semanal_monday.py            (default W24 = 8-14/jun)
#       python3 semanal_monday.py 15 21      (outra semana do mes: d1 d2)
# Metodos TRAVADOS (ver semanal-pedro-playbook.md, nao reinventar):
#   - Filtro sempre External; GGR = GB(ABS GAME_BET) - GW(GAME_WIN+CASH_OUT+CORRECTION)
#   - NGR = RealGGR(sub_account AMOUNT_REAL) - ReleasedBonus(BONUS_REL @ AMOUNT_RELEASED_BONUS)
#   - Backfill: rodar SEGUNDA de manha; dado fecha ate a manha seguinte ao fim da semana
#   - Meta semanal: curva de sazonalidade Copa +80% (playbook). Targets ja gravados.
import subprocess, json, os, sys
TOKEN_F=os.path.expanduser("~/.claude/credentials/pbi_access_token.txt")
REF_F=os.path.expanduser("~/.claude/credentials/pbi_refresh_token.txt")
CID="ea0616ba-638b-4df5-95b9-636659ae5121"
GROUP="00ecb2bb-6c61-4d09-badb-a4df0c948b02"; DATASET="c489d219-ef18-4f9e-9c5c-422c9092e3aa"

# --- parametros da semana ---
MES=6
D1=int(sys.argv[1]) if len(sys.argv)>1 else 8
D2=int(sys.argv[2]) if len(sys.argv)>2 else 14
SEM_LABEL="W25 (15-21 FINAL)"
SEM_COL="E"          # coluna da semana na aba Marketing (C=W23 D=W24 E=W25 F=W26 G=W27)
SEM_DATES="Jun 15 - 21, 2026"   # F4 do Dashboard
# semana anterior (para WoW). W24 = 8-14/jun (reais do tracker; NGR aprox, nao usado p/ Marketing)
PREV={"WK":"W24","FTD":740,"NGR":17309,"GGR":21844,"FullReg":2836,"GGRFTD":30,"CPA":316.96}
PREV_RANGE=(6,8,14)
# targets da curva +80% (playbook) para W25 (semana inteira 15-21)
TGT={"FullReg":8745,"FTD":2011,"GGR":120011,"NGR":105610,"CPA":159.05,"GGRFTD":60}
# CPA: gasto real da semana em USD (Midia/PACING). Se None, usa proporcional do budget.
SPEND_USD=None
MONTHLY_BUDGET_USD=343670   # budget total junho (PACING). W25 inteira (15-21): share da curva = 12.6/46
WEEK_SHARE=0.2739

def refresh():
    r=subprocess.run(["curl","-s","-X","POST","https://login.microsoftonline.com/organizations/oauth2/v2.0/token",
        "-d","client_id="+CID,"-d","grant_type=refresh_token","-d","refresh_token="+open(REF_F).read().strip(),
        "-d","scope=https://analysis.windows.net/powerbi/api/.default offline_access"],capture_output=True,text=True)
    d=json.loads(r.stdout)
    if "access_token" not in d: sys.exit("REFRESH FALHOU (Device Code Flow): "+str(d)[:200])
    open(TOKEN_F,"w").write(d["access_token"]); open(REF_F,"w").write(d.get("refresh_token",""))

def q(query):
    t=open(TOKEN_F).read().strip()
    payload=json.dumps({"queries":[{"query":query}],"serializerSettings":{"includeNulls":True}})
    r=subprocess.run(["curl","-s","-X","POST",
        f"https://api.powerbi.com/v1.0/myorg/groups/{GROUP}/datasets/{DATASET}/executeQueries",
        "-H","Authorization: Bearer "+t,"-H","Content-Type: application/json","-d",payload],capture_output=True,text=True)
    d=json.loads(r.stdout)
    if "results" not in d: sys.exit("ERRO DAX: "+r.stdout[:300])
    return d["results"][0]["tables"][0]["rows"][0]

EXT='FILTER(DimPlayer,DimPlayer[internal_external_player]="External")'
A='SUM(FactAGGAccountTransaction[account_transaction_amount])'
TY='FactAGGAccountTransaction[account_transaction_type]'
SA='FactAGGAccountTransaction[dim_sub_account_key]'
DC='DISTINCTCOUNT(FactAGGAccountTransaction[dim_player_key])'
SP='FILTER(DimGame,DimGame[game_platform_name]="Sports")'
CS='FILTER(DimGame,DimGame[game_platform_name]="Casino")'
def dr(m,d1,d2): return f'FILTER(DimDate,DimDate[Date]>=DATE(2026,{m},{d1})&&DimDate[Date]<=DATE(2026,{m},{d2}))'
def g(r,k): return r.get("["+k+"]") or 0

def kpis(m,d1,d2):
    D=dr(m,d1,d2)
    r=q(f'''EVALUATE ROW(
"FullReg",CALCULATE(COUNTROWS(FactFullRegistration),{D},{EXT}),
"FTD",CALCULATE(COUNTROWS(FactFirstDeposit),{D},{EXT}),
"GB",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT}),
"GW",CALCULATE({A},{D},{TY} IN {{"GAME_WIN","CASH_OUT","CORRECTION"}},{EXT}),
"GBr",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT},{SA}="AMOUNT_REAL"),
"GWr",CALCULATE({A},{D},{TY} IN {{"GAME_WIN","CASH_OUT","CORRECTION"}},{EXT},{SA}="AMOUNT_REAL"),
"RB",CALCULATE({A},{D},{TY}="BONUS_REL",{EXT},{SA}="AMOUNT_RELEASED_BONUS"))''')
    fr=g(r,"FullReg"); ftd=g(r,"FTD"); ggr=g(r,"GB")-g(r,"GW"); ngr=(g(r,"GBr")-g(r,"GWr"))-g(r,"RB")
    return dict(FullReg=fr,FTD=ftd,GGR=ggr,NGR=ngr,GGRFTD=(ggr/ftd if ftd else 0))

def bettors(m,d1,d2):
    D=dr(m,d1,d2)
    r=q(f'''EVALUATE ROW(
"TOT",CALCULATE({DC},{D},{TY}="GAME_BET",{EXT}),
"SP",CALCULATE({DC},{D},{TY}="GAME_BET",{EXT},{SP}),
"CS",CALCULATE({DC},{D},{TY}="GAME_BET",{EXT},{CS}))''')
    return dict(TOT=g(r,"TOT"),SP=g(r,"SP"),CS=g(r,"CS"))

def wow(real,prev): return (real/prev-1)*100 if prev else 0

refresh()
k=kpis(MES,D1,D2)
# CPA
if SPEND_USD is not None: spend=SPEND_USD; cpa_src="gasto real"
elif MONTHLY_BUDGET_USD is not None: spend=MONTHLY_BUDGET_USD*WEEK_SHARE; cpa_src="proporcional (curva)"
else: spend=None; cpa_src="SEM INVESTIMENTO (preencher SPEND_USD ou MONTHLY_BUDGET_USD)"
cpa=spend/k["FTD"] if spend and k["FTD"] else None

print(f"================ {SEM_LABEL} ({D1}-{D2}/0{MES}) REAIS (pos-backfill) ================")
print(f"  Full Reg : {k['FullReg']:>8,}   target {TGT['FullReg']:>7,}   ({k['FullReg']/TGT['FullReg']*100:.0f}% da meta)   WoW {wow(k['FullReg'],PREV['FullReg']):+.1f}%")
print(f"  FTD      : {k['FTD']:>8,}   target {TGT['FTD']:>7,}   ({k['FTD']/TGT['FTD']*100:.0f}%)   WoW {wow(k['FTD'],PREV['FTD']):+.1f}%")
print(f"  GGR R$   : {k['GGR']:>8,.0f}   target {TGT['GGR']:>7,}   ({k['GGR']/TGT['GGR']*100:.0f}%)   WoW {wow(k['GGR'],PREV['GGR']):+.1f}%")
print(f"  NGR R$   : {k['NGR']:>8,.0f}   target {TGT['NGR']:>7,}   ({k['NGR']/TGT['NGR']*100:.0f}%)   WoW {wow(k['NGR'],PREV['NGR']):+.1f}%")
print(f"  GGR/FTD  : R${k['GGRFTD']:>7,.1f}   target R${TGT['GGRFTD']}   WoW {wow(k['GGRFTD'],PREV['GGRFTD']):+.1f}%")
print(f"  CPA      : {('$%.2f'%cpa) if cpa else '--'}   target ${TGT['CPA']}   [{cpa_src}]")

print(f"\n================ ACTIVE BETTORS: {SEM_LABEL} vs semana anterior ================")
def show_bett(lbl,a,b):
    print(f"  {lbl}")
    for nm,key in [("Total","TOT"),("Esportivo","SP"),("Casino","CS")]:
        d=wow(b[key],a[key])
        print(f"    {nm:10}{a[key]:>7} -> {b[key]:>7}  ({d:+.1f}%)")
pr=PREV_RANGE
show_bett("Seg-Sab (justo)", bettors(pr[0],pr[1],pr[2]-1), bettors(MES,D1,D2-1))
show_bett("Semana inteira", bettors(*pr), bettors(MES,D1,D2))

WK=SEM_LABEL.split()[0]
cpa_s=('$%.2f'%cpa) if cpa else '<gasto>'
print(f"\n================ BLOCOS PRA COLAR (na ordem de colagem) ================")

print(f"\n[1] PLANILHA MENSAL PEDRO -> aba MARKETING, coluna {SEM_COL} ({WK}):")
print(f"  {SEM_COL}5  Full Reg : {k['FullReg']:,}")
print(f"  {SEM_COL}6  FTD      : {k['FTD']:,}")
print(f"  {SEM_COL}8  CPA      : {cpa_s}")
print(f"  {SEM_COL}10 GGR      : R${k['GGR']:,.0f}")
print(f"  {SEM_COL}11 GGR/FTD  : R${k['GGRFTD']:.0f}")
print(f"  H   Comments  : <editorial>")

print(f"\n[2] PLANILHA MENSAL PEDRO -> aba DASHBOARD:")
print(f"  B4 (semana) = {WK}      F4 (datas) = {SEM_DATES}")
print(f"  D6 Target FTD  = {TGT['FTD']:,}")
print(f"  E6 Current FTD = {k['FTD']:,}")
print(f"  F6 Delta       = =E6/D6-1")
print(f"  G6 Status      = <Off track / At risk / On track>")
print(f"  H6 Trend       = <editorial>")

print(f"\n[3] PLANILHA DRIVE 'Tracking Semanal' (linha {WK}) -> FONTE do Confluence Row 5")
print(f"    colar na MESMA ordem das colunas da Row 5:")
print(f"  > Status Update      : Updated")
print(f"  > MTD KPIs (REAL | TARGET):")
print(f"      FTDs -> {k['FTD']:,} | {TGT['FTD']:,}")
print(f"      CPA  -> {cpa_s} | ${TGT['CPA']}")
print(f"      NGR  -> R${k['NGR']:,.0f} | R${TGT['NGR']:,}")
print(f"  > WoW Diff% ({WK} vs {PREV.get('WK','ant')}):")
print(f"      FTD -> {wow(k['FTD'],PREV['FTD']):+.1f}% (vs {PREV['FTD']:,})")
cpawow=(f"{(cpa/PREV['CPA']-1)*100:+.1f}% (vs ${PREV['CPA']:.0f})") if (cpa and PREV.get('CPA')) else "(conforme metodo)"
print(f"      CPA -> {cpawow}")
print(f"      NGR -> {wow(k['NGR'],PREV['NGR']):+.1f}% (vs R${PREV['NGR']:,.0f})")
print(f"  > Next Steps         : <editorial>")
