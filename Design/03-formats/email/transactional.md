# Emails Transacionais

> Emails disparados por acao do usuario ou sistema. Tom: claro, direto, neutro.

---

## Tipos cobertos

- Boas-vindas / confirmacao de cadastro
- Verificacao de email (OTP)
- Confirmacao de deposito
- Confirmacao de saque
- Status de saque (em analise, aprovado, rejeitado)
- Recuperacao de senha
- Alertas de seguranca (login novo dispositivo)
- Confirmacao de aposta de alto valor

---

## Padrao visual

Segue o padrao geral de email BW definido em `README.md`:
- **Fonte:** Arial, 10.5pt, cor `#333333`
- **H2:** border-bottom `#FF3900` 1.5pt
- **Tabelas:** 2 colunas (label whitesmoke + valor) para detalhes da transacao

---

## Diretrizes de copy

- **Sem promocao.** Email transacional NAO vende. Nunca.
- **Foco na informacao.** O que aconteceu, proximo passo, contato em caso de duvida.
- **Subject literal.** "Seu saque de R$ X foi aprovado" — nao criativo, nao ambiguo.
- **Sem urgencia fabricada.** Sem "AGE AGORA" ou countdowns.
- **Sem CTA promocional.** Unico CTA: acao diretamente relacionada a transacao.

---

## Estrutura

```
[LOGO]

Ola, {{primeiro_nome}}.

[FRASE DE ABERTURA — 1 linha do que aconteceu]

[BLOCO DE DETALHES — tabela 2 colunas com os dados]

[CTA opcional — so se houver acao esperada do usuario]

[FRASE DE FECHAMENTO + canal de suporte]

Equipe BetWarrior

[FOOTER COMPLIANCE]
```

---

## Exemplo: confirmacao de saque

**Subject:** Seu saque de R$ 250,00 foi aprovado

**Pre-header:** O valor ja foi enviado para sua conta cadastrada.

**Corpo:**
```html
<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  Ola, Joao.
</p>

<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  Seu pedido de saque foi aprovado e o valor ja foi enviado.
</p>

<h2 style="font-size:13.5pt; color:#1A1A1A; border-bottom:solid #FF3900 1.5pt; padding-bottom:4px; margin-top:24px; margin-bottom:12px; font-family:Arial,sans-serif;">
  Detalhes do saque
</h2>

<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Valor</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;"><strong>R$ 250,00</strong></td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Metodo</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">PIX</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Chave</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">***@***</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Data</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">18/04/2026 14:32</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">ID</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">#BW-2026-XXXXXX</td>
  </tr>
</table>

<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  O valor deve aparecer na sua conta em ate 1 hora util.
</p>

<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  Em caso de duvida, fale conosco em suporte@betwarrior.com.br.
</p>

<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6;">
  Equipe BetWarrior
</p>

<!-- FOOTER COMPLIANCE -->
<hr style="border:none; border-top:1px solid #DDDDDD; margin:24px 0;">
<p style="font-family:Arial,sans-serif; font-size:9pt; color:#666666; line-height:1.4;">
  +18 | Aposte com responsabilidade | 0800-721-5050 (Jogadores Anonimos) | 188 (CVV)<br>
  Voce esta recebendo este email porque realizou um saque na BetWarrior.<br>
  <a href="#" style="color:#666666;">Descadastrar</a> | <a href="#" style="color:#666666;">Politica de Privacidade</a>
</p>
```

---

## Cuidados de compliance

- NUNCA incluir CTAs promocionais em emails transacionais (regra LGPD)
- NUNCA sugerir nova aposta apos confirmacao de perda
- Em saques, NUNCA questionar a decisao do usuario
- Sempre incluir footer com disclaimer, descadastro e canal de apoio
- Dados sensiveis (chaves PIX, CPF) sempre parcialmente mascarados
