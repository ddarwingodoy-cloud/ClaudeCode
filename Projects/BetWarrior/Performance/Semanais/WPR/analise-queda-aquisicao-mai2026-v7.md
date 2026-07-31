# Analise de Queda de Aquisicao: Abr 3-21 vs Mai 1-19

**Preparado por:** Darwin Godoy · Performance Brasil
**Data:** 19/mai/2026
**Periodo:** Abr 3-21 vs Mai 1-19 (normalizados por dia da semana: ambos iniciam na sexta-feira)
**Fontes:** Power BI (PBI), Google Analytics 4 (GA4), MyAffiliates

---

## 1. O funil

| Etapa | Abr 3-21 | Mai 1-19 | Var. | Taxa conv. Abr | Taxa conv. Mai |
|---|---|---|---|---|---|
| Sessoes (GA4) | 311.443 | 285.851 | -8% | n/a | n/a |
| NoLock (PBI) | 7.255 | 6.229 | -14% | 2,3% sessoes | 2,2% sessoes |
| Ready for Deposit (PBI) | 4.524 | 3.296 | -27% | 62,4% NoLock | 52,9% NoLock |
| FTDs (PBI) | 2.870 | 1.938 | -32% | 63,4% RFD | 58,8% RFD |

No periodo normalizado, as sessoes cairam apenas 8%. A taxa de conversao sessao para cadastro se manteve estavel (2,3% para 2,2%), indicando que o topo do funil nao e o problema central. A queda de NoLock (-14%) supera a queda de sessoes: o mix de trafego mudou, com canais de menor conversao ganhando peso. O problema se aprofunda no passo seguinte. A taxa de conversao NoLock para Ready for Deposit caiu 9,4 p.p., de 62,4% para 52,9%: apostadores que passaram por compliance e chegaram ao formulario de dados bancarios nao avancaram. Isso puxou o FTD para uma queda de 32%, bem acima da queda de sessoes. A queda nao e apenas de volume: os apostadores que chegaram tiveram mais resistencia para depositar.

**Gap total de FTDs:** 2.870 menos 1.938 = 932 FTDs de diferenca no periodo.

---

## 2. Os impactos

**Impacto 1: Friccao no meio do funil**

A queda de 9,4 p.p. na conversao NoLock para RFD e o ponto critico. Sao apostadores aprovados em compliance que abandonam no formulario de dados bancarios.

Cenario: se a taxa NoLock para RFD tivesse se mantido em 62,4% (nivel de abril), maio teria gerado 591 RFDs adicionais. Aplicando a taxa RFD para FTD de maio (58,8%), isso representa **+347 FTDs deixados na mesa, 37% do gap total de 932.**

**Impacto 2: Canal de afiliados**

A queda de sessoes de -8% no periodo normalizado nao explica o gap de 932 FTDs. O dado relevante esta na abertura por medium:

FTDs via GA4 (deposit_ftd): indicativo, valido para comparacao entre periodos.

| Medium | Sessoes Abr | Sessoes Mai | Var. % | FTDs Abr | FTDs Mai | Var. FTDs |
|---|---|---|---|---|---|---|
| paid_media | 169.608 | 136.927 | -19% | 391 | 365 | -7% |
| affiliate | 32.386 | 46.882 | +45% | 593 | 278 | -53% |
| referral | 29.628 | 29.115 | -2% | 23 | 12 | -48% |
| (none) | 29.272 | 27.608 | -6% | 222 | 129 | -42% |
| cpc | 25.808 | 23.365 | -9% | 462 | 407 | -12% |
| (not set) | 7.798 | 3.000 | -62% | 106 | 69 | -35% |
| organic | 7.155 | 5.928 | -17% | 91 | 78 | -14% |
| email | 2.863 | 5.633 | +97% | 19 | 43 | +126% |
| social_paid | 1.865 | 1.861 | flat | 55 | 48 | -13% |
| social_organic | 1.223 | 1.037 | -15% | 21 | 34 | +62% |
| **Total** | **311.443** | **285.851** | **-8%** | | | |

O paid_media perdeu 19% de sessoes e manteve os FTDs praticamente intactos (-7%): o trafego eliminado convertia proximo de zero e nao e o fator explicativo do gap. O contraste esta no medium affiliate: cresceu 45% em sessoes e caiu 53% em FTDs. No GA4, o identificador do tracking de afiliados diretos e a campanha conv_direct; na verificacao cruzada com o periodo normalizado de abril (Abr 3-21), esse identificador registrou 593 deposit_ftd, numero identico ao total do medium affiliate no mesmo periodo, confirmando que os dois representam o mesmo fluxo de trafego. O diagnostico converge: a queda de FTD tem origem no canal de afiliados.

---

## 3. Onde a friccao esta concentrada (PBI)

Para identificar qual origem teve maior resistencia no step NoLock para RFD, consultamos o Power BI cruzando a tabela de onboarding com os dados de UTM de cada jogador:

| Medium | CR Abr | CR Mai | Delta |
|---|---|---|---|
| paid_media | 60,4% | 55,8% | -4,6 p.p. |
| affiliate | 60,1% | 46,1% | -13,9 p.p. |

O medium **affiliate** e o mais afetado: queda de 13,9 p.p. na conversao NoLock para RFD, tres vezes a queda observada em paid_media (-4,6 p.p.). O trafego de afiliados em maio chegou ao formulario de dados bancarios com significativamente mais resistencia do que em abril.

O diagnostico e consistente pelas duas dimensoes: volume (medium affiliate -53% de FTDs, equivalente ao conv_direct do tracking de afiliados) e conversao no meio do funil (medium affiliate -13,9 p.p. em NoLock para RFD).

---

## 4. Afiliados (MyAffiliates)

Nota: dados de afiliados nao normalizados (Abr 1-18 vs Mai 1-18); o MyAffiliates nao permite filtro por data de inicio customizado. Signups = primeiro cadastro via link de afiliado (equivalente a Regs no PBI). Nao comparavel ao NoLock do funil, que exige KYC completo e aprovacao de compliance.

| Afiliado | Signups Abr | Signups Mai | Var. Signups | FTDs Abr | FTDs Mai | Var. FTDs |
|---|---|---|---|---|---|---|
| nfa | 1.235 | 844 | -32% | 736 | 476 | -35% |
| EightroomBR2 | 211 | 304 | +44% | 51 | 74 | +45% |
| raphaelrossi | 412 | 1.372 | +233% | 24 | 72 | +200% |
| costamedia | 119 | 318 | +167% | 20 | 68 | +240% |
| AfiliagamblingBR | 94 | 72 | -23% | 66 | 54 | -18% |
| NorhstarBR | 142 | 366 | +158% | 7 | 40 | +471% |
| BW1703RBR26 | 70 | 390 | +457% | 5 | 26 | +420% |
| dbbtwar | 46 | 60 | +30% | 16 | 26 | +63% |
| Asaph | 490 | 274 | -44% | 33 | 20 | -39% |
| **TOTAL** | **2.872** | **4.030** | **+40%** | **980** | **870** | **-11%** |

**Por que signups subiram +40% mas FTDs cairam -11%?**

O crescimento de signups e concentrado em afiliados com taxa de conversao signup-para-FTD muito baixa. A composicao do programa mudou: o volume veio de parceiros com perfil de trafego de menor qualidade.

| Afiliado | Signups Mai | FTDs Mai | Conversao signup-FTD |
|---|---|---|---|
| nfa | 844 | 476 | 56% |
| AfiliagamblingBR | 72 | 54 | 75% |
| costamedia | 318 | 68 | 21% |
| EightroomBR2 | 304 | 74 | 24% |
| NorhstarBR | 366 | 40 | 11% |
| BW1703RBR26 | 390 | 26 | 7% |
| raphaelrossi | 1.372 | 72 | 5% |

Os +1.158 signups adicionais vindos de raphaelrossi, BW1703RBR26 e NorhstarBR geraram apenas +119 FTDs combinados, conversao media abaixo de 9%. A queda de FTDs (-11%) e consequencia direta dessa mudanca na composicao do programa, com crescimento concentrado em afiliados que trazem apostadores com menor disposicao para avancar no funil de deposito.

---

## 5. Resultado financeiro e base ativa

| Metrica | Abr 3-21 | Mai 1-19 | Var. |
|---|---|---|---|
| Gross Bets (PBI) | R$ 4.518.120 | R$ 4.539.797 | flat |
| GGR (PBI) | R$ 161.879 | R$ 232.724 | +44% |
| Apostadores ativos (PBI) | 4.091 | 3.156 | -23% |
| Depositantes unicos (PBI) | 3.792 | 2.807 | -26% |
| Volume total depositado (PBI) | R$ 1.496.770 | R$ 1.119.430 | -25% |
| Ticket medio por depositante (PBI) | R$ 395 | R$ 399 | flat |
| Redeposits por depositante (PBI) | 1,9x | 2,1x | +11% |
| Turnover (GB / Depositos) | 3,0x | 4,1x | +37% |

O Gross Bets se manteve estavel mesmo com 26% menos depositantes porque os jogadores retidos apostaram cada real depositado com muito mais frequencia. Deposito e volume apostado sao metricas distintas: um jogador pode depositar R$400 e gerar R$1.500 em apostas ao longo do periodo reciclando ganhos parciais em novas apostas. O turnover passou de 3,0x para 4,1x, indicando que a base ativa em maio, menor em numero, tem comportamento de aposta significativamente mais intenso. O redeposit por depositante (+11%) e um sinal complementar disso.

---

*Fontes: Power BI (funil, financeiro, base ativa e RFD por medium) · Google Analytics 4 (sessoes, canais e campanhas) · MyAffiliates (afiliados, FTDs e Signups, periodo nao normalizado: Abr 1-18 vs Mai 1-18). NGR por afiliado nao incluido para garantir consistencia de fonte e moeda.*
