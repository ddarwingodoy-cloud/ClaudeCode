#!/usr/bin/env python3
# WPR - Coletor P1 (Power BI). Janelas NORMALIZADAS por dia da semana, ultimos 3 meses, meta pela curva Copa.
# Uso:  python3 wpr_pull.py <mes_atual> <dia_fim_MTD>      ex: python3 wpr_pull.py 6 17
#   -> compara os 3 ultimos meses (mes-2, mes-1, mes), cada um na sua janela normalizada:
#      1a ocorrencia, no mes, do dia-da-semana do dia 1 do mes atual + (len-1) dias.
#      Jun 01-17 (seg-qua) -> Mai 04-20 -> Abr 06-22.
# Metodos travados (nao reinventar):
#   - ESCOPO (corrigido 13/07): Brazil + BWBRA + int/ext TODOS. Filtrar DimPlayer[player_country_name]="Brazil"
#       && DimPlayer[brand_name]="BWBRA" (NAO filtrar internal_external, o Main KPIs Report usa "Todos").
#       SEM Brazil+BWBRA o GGR (dif de numeros grandes) estoura/inverte. TODO numero tem que bater EXATO
#       com o Main KPIs Report (reports/dc2acead-4b72-4c88-99c0-d150938b8ced): GB/GW/GGR/FullReg/FTD.
#       (13/07 External dava 514/R$5.704; Todos da 516/R$5.909 = igual ao report.)
#   - GGR = GB(ABS GAME_BET, TODAS sub-contas) - GW(GAME_WIN+CASH_OUT+CORRECTION). NAO filtrar AMOUNT_REAL.
#   - NGR = GGR - BonusCost, onde BonusCost = CRE_BONUS + PRODUC_BON + CANC_BONUS (bate com The Dashboard ~-4,5K).
#       (metodo ANTIGO "RealGGR(AMOUNT_REAL) - ReleasedBonus" estava ERRADO: dava +8,8k vs -4k real. Reconciliado
#        01-08/jul: GrossBets 557.389, GrossWins 550.924, GGR 6.464, todos exatos com o report Power BI.)
#   - Funil "Registros" (1o step) = DISTINCTCOUNT(username) @ status_onboarding=PENDING_CONFIRMATION
#       bate com o The Dashboard (Betinho). NAO usar COUNTROWS (reenvio VERIFICATION_CODE_RESENT infla);
#       party_id e nulo no 1o step, por isso conta-se username distinto.
#   - Funil "Pronto p/Dep" = kyc_onboardings_logs READY_FOR_DEPOSIT
#   - Tabela FullReg = FactFullRegistration (NAO muda p/ onboarding; isonomia historica)
#   - Meta: Forecast Dada aba "Simulator - New (Cambio Margenes)" -> FTD=linha8+9, GGR=44, NGR=47,
#       MargSports=42, MargCasino=43, MixSports=41; col do mes (B=Abr,C=Mai,D=Jun...).
#       Distribuida pela curva Copa (Jun: +80% a partir 11/06); Abr/Mai linear. CR alvo 23%.
#       >>> ATUALIZAR META_MES abaixo todo mes, lendo o Forecast via MCP <<<
import subprocess, json, os, sys, calendar, datetime
TOKEN_F=os.path.expanduser("~/.claude/credentials/pbi_access_token.txt")
REF_F=os.path.expanduser("~/.claude/credentials/pbi_refresh_token.txt")
CID="ea0616ba-638b-4df5-95b9-636659ae5121"
GROUP="00ecb2bb-6c61-4d09-badb-a4df0c948b02"; DATASET="c489d219-ef18-4f9e-9c5c-422c9092e3aa"

# === METAS MENSAIS (Forecast Dada, atualizar todo mes) ===
META_MES={
 4:{"FTD":4369,"GGR":259570,"NGR":230758,"MargSB":0.0550,"MargCS":0.0239,"MixSB":0.32},
 5:{"FTD":3216,"GGR":327423,"NGR":294681,"MargSB":0.0600,"MargCS":0.0400,"MixSB":0.40},
 6:{"FTD":7343,"GGR":438137,"NGR":385561,"MargSB":0.0600,"MargCS":0.0400,"MixSB":0.40},
 7:{"FTD":2294,"GGR":269836,"NGR":240592,"MargSB":0.0600,"MargCS":0.0400,"MixSB":0.495},  # Jul: Targets Reforecast Luiz (Jul26) — FTD 1.682+612 afiliados
 8:{"FTD":1842,"GGR":239737,"NGR":214823,"MargSB":0.0600,"MargCS":0.0400,"MixSB":0.507},  # Ago: Targets Reforecast Luiz (Jul26) — FTD 1.331+511 afiliados
}
CR_ALVO=0.25   # CR alvo agosto = 25% (mesmo do deck Jul/Ago 01-20; memoria project_wpr_meta_julho). O 14,27% YTD era de jun.
COPA={"mes":6,"lift":0.80,"inicio":11}   # lift +80% a partir do dia 11 (inicio da Copa)

def refresh():
    r=subprocess.run(["curl","-s","-X","POST","https://login.microsoftonline.com/organizations/oauth2/v2.0/token",
        "-d","client_id="+CID,"-d","grant_type=refresh_token","-d","refresh_token="+open(REF_F).read().strip(),
        "-d","scope=https://analysis.windows.net/powerbi/api/.default offline_access"],capture_output=True,text=True)
    d=json.loads(r.stdout)
    if "access_token" not in d:
        sys.exit("REFRESH FALHOU (refazer Device Code Flow): "+str(d)[:200])
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

def dr(m,d1,d2): return f'FILTER(DimDate,DimDate[Date]>=DATE(2026,{m},{d1})&&DimDate[Date]<=DATE(2026,{m},{d2}))'
EXT='FILTER(DimPlayer,DimPlayer[player_country_name]="Brazil"&&DimPlayer[brand_name]="BWBRA"&&DimPlayer[internal_external_player]="External")'
A='SUM(FactAGGAccountTransaction[account_transaction_amount])'
TY='FactAGGAccountTransaction[account_transaction_type]'
SA='FactAGGAccountTransaction[dim_sub_account_key]'

def window(month, anchor_wd, length):
    """1a ocorrencia, em `month`, do dia-da-semana `anchor_wd` (0=seg) + (length-1) dias."""
    d=datetime.date(2026,month,1)
    while d.weekday()!=anchor_wd: d+=datetime.timedelta(days=1)
    return d.day, d.day+length-1

def meta_share(m,d1,d2):
    """fracao da meta mensal que cai na janela [d1,d2], pela curva Copa (flat fora do mes de Copa)."""
    dim=calendar.monthrange(2026,m)[1]
    w=lambda day:(1+COPA["lift"]) if (m==COPA["mes"] and day>=COPA["inicio"]) else 1.0
    return sum(w(x) for x in range(d1,d2+1))/sum(w(x) for x in range(1,dim+1))

def registros(m,d1,d2):
    # "New Registrations" = FactRegistration[registration_count], escopo BR+BWBRA (EXT). CORRIGIDO 24/07/2026.
    # Bate EXATO com o report Weekly KPIs by Brand / The Dashboard do Betinho (Jul 01-22 = 3.499, CR 25,0%).
    # >>> ANTES usava DISTINCTCOUNT(kyc_onboardings_logs[username]) @ PENDING_CONFIRMATION: era all-brand
    #     (misturava brand_id 1002, ~+322 em jul) e nao batia o Dashboard (dava 4.020/3.698). NAO voltar pro kyc.
    D=dr(m,d1,d2)
    return q(f'EVALUATE ROW("r",CALCULATE(SUM(FactRegistration[registration_count]),{D},{EXT}))').get("[r]") or 0

def metrics(m,d1,d2):
    D=dr(m,d1,d2); G=lambda r,k:(r.get("["+k+"]") or 0)
    r=q(f'''EVALUATE ROW(
"FullReg",CALCULATE(COUNTROWS(FactFullRegistration),{D},{EXT}),
"FTD",CALCULATE(COUNTROWS(FactFirstDeposit),{D},{EXT}),
"DepMed",CALCULATE(AVERAGE(FactFirstDeposit[payment_amount]),{D},{EXT}),
"GB",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT}),
"GW",CALCULATE({A},{D},{TY} IN {{"GAME_WIN","CASH_OUT","CORRECTION"}},{EXT}),
"BonusCost",CALCULATE({A},{D},{TY} IN {{"CRE_BONUS","PRODUC_BON","CANC_BONUS","MAN_BONUS","BONUS_REL","EXP_BONUS","MAN_ADJUST"}},{EXT}),
"SBGB",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT},FILTER(DimGame,DimGame[game_platform_name]="Sports")),
"SBGW",CALCULATE({A},{D},{TY} IN {{"GAME_WIN","CASH_OUT","CORRECTION"}},{EXT},FILTER(DimGame,DimGame[game_platform_name]="Sports")),
"CSGB",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT},FILTER(DimGame,DimGame[game_platform_name]="Casino")),
"CSGW",CALCULATE({A},{D},{TY} IN {{"GAME_WIN","CASH_OUT","CORRECTION"}},{EXT},FILTER(DimGame,DimGame[game_platform_name]="Casino")),
"Bettors",CALCULATE(DISTINCTCOUNT(FactAGGAccountTransaction[dim_player_key]),{D},{TY}="GAME_BET",{EXT}),
"GBnew",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT},FactAGGAccountTransaction[customer_new_or_returning]="New Customer"),
"GBret",CALCULATE(ABS({A}),{D},{TY}="GAME_BET",{EXT},FactAGGAccountTransaction[customer_new_or_returning]="Returning Customer")
)''')
    gb,gw=G(r,"GB"),G(r,"GW"); ggr=gb-gw
    ngr=ggr-G(r,"BonusCost")   # NGR = GGR total - BonusCost(CRE+PRODUC+CANC). Escopo BR+BWBRA+Ext (ver EXT).
    sbgb,sbgw=G(r,"SBGB"),G(r,"SBGW"); csgb,csgw=G(r,"CSGB"),G(r,"CSGW")
    kyc=q(f'EVALUATE ROW("rd",CALCULATE(COUNTROWS(kyc_onboardings_logs),FILTER(kyc_onboardings_logs,kyc_onboardings_logs[created_date_only]>=DATE(2026,{m},{d1})&&kyc_onboardings_logs[created_date_only]<=DATE(2026,{m},{d2})),kyc_onboardings_logs[status_onboarding]="READY_FOR_DEPOSIT"))').get("[rd]") or 0
    return dict(FullReg=G(r,"FullReg"),FTD=G(r,"FTD"),DepMed=G(r,"DepMed"),
        GB=gb,GGR=ggr,NGR=ngr,Marg=ggr/gb if gb else 0,
        SB=(sbgb-sbgw)/sbgb if sbgb else 0,CS=(csgb-csgw)/csgb if csgb else 0,
        CR=G(r,"FTD")/G(r,"FullReg") if G(r,"FullReg") else 0,
        Bettors=G(r,"Bettors"),GBnew=G(r,"GBnew"),GBret=G(r,"GBret"),
        Reg1=registros(m,d1,d2),KYC=kyc)

if __name__=="__main__":
    m=int(sys.argv[1]); dfim=int(sys.argv[2]) if len(sys.argv)>2 else 10
    dini=int(sys.argv[3]) if len(sys.argv)>3 else 1   # dia inicial (ex: 2 p/ excluir incidente 01/06)
    refresh()
    mn=["","Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    anchor=datetime.date(2026,m,dini).weekday(); length=dfim-dini+1   # ancora = dia-da-semana do dia inicial
    months=[m-2,m-1,m]
    win={mm:(window(mm,anchor,length) if mm!=m else (dini,dfim)) for mm in months}
    data={mm:metrics(mm,*win[mm]) for mm in months}
    cur,prev=data[m],data[m-1]
    print("=== TABELA (3 meses, janelas normalizadas por dia da semana) ===")
    print("Mes Janela  Registros  FTD   CR%   GGR(k) NGR(k)  Marg   SB%    CS%   DepMed  [FullReg]")
    for mm in months:
        x=data[mm]; d1,d2=win[mm]; reg=x['Reg1']; crr=x['FTD']/reg if reg else 0
        print("%s %02d-%02d %9s %5s %5.1f%% %6.0f %6.0f %5.1f%% %5.1f%% %5.1f%% R$%.0f   %s"%(mn[mm],d1,d2,
            format(reg,',.0f'),format(x['FTD'],',.0f'),crr*100,x['GGR']/1000,x['NGR']/1000,
            x['Marg']*100,x['SB']*100,x['CS']*100,x['DepMed'],format(x['FullReg'],',.0f')))
    # Meta do mes atual, distribuida pela curva
    M=META_MES[m]; sh=meta_share(m,dini,dfim)
    ftd_meta=M["FTD"]*sh; ggr_meta=M["GGR"]*sh; ngr_meta=M["NGR"]*sh
    reg_meta=ftd_meta/CR_ALVO; marg_meta=M["MixSB"]*M["MargSB"]+(1-M["MixSB"])*M["MargCS"]
    cr_cur=cur['FTD']/cur['Reg1'] if cur['Reg1'] else 0
    print("\n=== META %s (janela 01-%02d = %.1f%% do mes, curva Copa; CR alvo = YTD 2026) ==="%(mn[m],dfim,sh*100))
    print("  Registros=%s FTD=%s CR=%.1f%% GGR=%.0fk NGR=%.0fk Marg=%.1f%% SB=%.1f%% CS=%.1f%%"%(
        format(reg_meta,',.0f'),format(ftd_meta,',.0f'),CR_ALVO*100,ggr_meta/1000,ngr_meta/1000,
        marg_meta*100,M["MargSB"]*100,M["MargCS"]*100))
    print("  vs Meta: Registros=%.0f%% FTD=%.0f%% GGR=%.0f%% NGR=%.0f%% CR=%+.1fpp"%(
        cur['Reg1']/reg_meta*100,cur['FTD']/ftd_meta*100,cur['GGR']/ggr_meta*100,
        cur['NGR']/ngr_meta*100,(cr_cur-CR_ALVO)*100))
    # FTD vs Meta (grafico): cada mes realizado vs meta da SUA janela
    print("\n=== FTD vs META (grafico, por mes) ===")
    for mm in months:
        d1,d2=win[mm]; fm=META_MES[mm]["FTD"]*meta_share(mm,d1,d2)
        print("  %s: real=%s meta=%s ating=%.0f%%"%(mn[mm],format(data[mm]['FTD'],',.0f'),
            format(fm,',.0f'),data[mm]['FTD']/fm*100))
    print("\n=== FUNIL (Sessoes = GA4 BR via MCP) ===")
    for lbl,d in ((mn[m],cur),(mn[m-1],prev)):
        print("  %s: Registros(1o step)=%s  Pronto/KYC=%s  FTD=%s"%(lbl,
            format(d['Reg1'],',.0f'),format(d['KYC'],',.0f'),format(d['FTD'],',.0f')))
    print("\n=== CARDS BASE ATIVA (atual vs anterior) ===")
    for lbl,d in ((mn[m],cur),(mn[m-1],prev)):
        b=d['Bettors']
        print("  %s: Apostadores=%s  GB/ap=R$%.0f  GBnew=R$%s  GBret=R$%s"%(lbl,format(b,',.0f'),
            (d['GBnew']+d['GBret'])/b if b else 0,format(d['GBnew'],',.0f'),format(d['GBret'],',.0f')))
