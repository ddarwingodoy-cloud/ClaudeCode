# Emails CRM e Promocionais

> Emails de campanha, ativacao, retencao. Tom: animado, proximo, com beneficio claro.

---

## Tipos cobertos

- Boas-vindas pos-FTD (primeiro deposito)
- Ofertas de bonus (recarga, cashback)
- Eventos esportivos (rodadas, finais, derbis)
- Reativacao de usuario inativo
- Newsletter editorial
- Lancamentos de produto/jogo

---

## Padrao visual

Segue o padrao geral de email BW definido em `README.md`:
- **Fonte:** Arial, 10.5pt, cor `#333333`
- **H2:** border-bottom `#FF3900` 1.5pt
- **Tabelas de dados:** header `#FF3900` com texto branco, zebra striping whitesmoke
- **CTA principal:** botao com fundo `#FF3900`, texto branco, padding 12px 24px

### Botao CTA
```html
<table style="margin:20px 0;">
  <tr>
    <td style="background:#FF3900; padding:12px 24px; text-align:center;">
      <a href="#" style="color:#FFFFFF; font-family:Arial,sans-serif; font-size:11pt; font-weight:bold; text-decoration:none;">APOSTAR AGORA</a>
    </td>
  </tr>
</table>
```

**Nota:** Usar `<table>` para botao (compatibilidade Outlook). Nao usar `<a>` com padding direto.

---

## Diretrizes de copy

- **1 mensagem, 1 CTA.** Foco absoluto.
- **Beneficio no subject.** "Cashback de 20% no Brasileirao" > "Veja nossas novidades".
- **Personalizacao real.** {{primeiro_nome}}, time favorito quando possivel.
- **Urgencia verdadeira.** Se a oferta acaba domingo, dizer. Sem fake countdown.
- **Compliance:** footer + regulamento da oferta linkado. Sem excecao.

---

## Estrutura padrao

```
[HERO BANNER — imagem + titulo]

[FRASE DE BENEFICIO — 1 linha matadora]

[CONDICOES PRINCIPAIS — bullets curtos]
- Valor min. deposito
- Multiplicador (rollover 5x min.)
- Odd min. 1.70
- Validade

[CTA PRINCIPAL]

[BLOCO DE APOIO — opcional, ex: jogos disponiveis]

[LINK PARA REGULAMENTO COMPLETO]

[FOOTER COMPLIANCE]
```

---

## Exemplo: cashback Brasileirao

**Subject:** Cashback de ate R$ 100 no Brasileirao

**Pre-header:** Suas apostas no fim de semana tem protecao. Veja como.

**Corpo:**
```html
<h2 style="font-size:13.5pt; color:#1A1A1A; border-bottom:solid #FF3900 1.5pt; padding-bottom:4px; margin-top:24px; margin-bottom:12px; font-family:Arial,sans-serif;">
  Aposte no Brasileirao com cashback de ate R$ 100
</h2>

<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  Esse fim de semana, suas apostas em qualquer jogo do Brasileirao tem cashback. Se sua aposta perder, parte do valor volta como saldo de bonus.
</p>

<h3 style="font-size:13.5pt; color:#333333; margin-top:18px; margin-bottom:8px; font-family:Arial,sans-serif;">
  Como funciona
</h3>

<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Promocao</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Cashback 20% sobre apostas perdedoras</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Mercado</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Qualquer jogo do Brasileirao (sexta a domingo)</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Limite</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">R$ 100 por usuario</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Odd minima</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">1.70</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Rollover</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">5x</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Credito</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Ate 24h apos o ultimo jogo da rodada</td>
  </tr>
</table>

<!-- CTA -->
<table style="margin:20px 0;">
  <tr>
    <td style="background:#FF3900; padding:12px 24px; text-align:center;">
      <a href="#" style="color:#FFFFFF; font-family:Arial,sans-serif; font-size:11pt; font-weight:bold; text-decoration:none;">APOSTAR AGORA</a>
    </td>
  </tr>
</table>

<p style="font-family:Arial,sans-serif; font-size:9pt; color:#666666;">
  <a href="#" style="color:#666666;">Regulamento completo</a>
</p>

<!-- FOOTER COMPLIANCE -->
<hr style="border:none; border-top:1px solid #DDDDDD; margin:24px 0;">
<p style="font-family:Arial,sans-serif; font-size:9pt; color:#666666; line-height:1.4;">
  +18 | Aposte com responsabilidade | 0800-721-5050 (Jogadores Anonimos) | 188 (CVV)<br>
  <a href="#" style="color:#666666;">Descadastrar</a> | <a href="#" style="color:#666666;">Termos e Condicoes</a> | <a href="#" style="color:#666666;">Politica de Privacidade</a>
</p>
```

---

## Frequencia e segmentacao

- Maximo 3 emails promocionais/semana por usuario ativo
- Maximo 1/semana para usuario em risco de churn
- ZERO para usuarios autoexcluidos ou em pausa
- Respeitar timezone BR (envios entre 9h-21h)

---

## A/B testing

Sempre testar:
- Subject (2 variantes minimo)
- CTA copy ("Apostar agora" vs "Ver odds" vs "Quero cashback")
- Hero image (se campanha grande)

Nao testar simultaneamente tudo. Isolar variavel.

---

## Cuidados de compliance

- TODO email promocional precisa de footer + regulamento linkado
- NUNCA enviar para usuarios autoexcluidos
- NUNCA sugerir que apostar e investimento ou renda
- NUNCA usar urgencia fabricada (fake countdowns, "ULTIMA CHANCE" sem ser real)
- Respeitar opt-in (LGPD) — descadastro em 1 clique
