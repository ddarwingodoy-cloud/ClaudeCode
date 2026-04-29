# Emails — Regras Gerais e Padrao BW

> Este documento define o padrao visual de emails usado pelo Betinho para comunicacoes da BetWarrior Brasil.

---

## Padrao de email BW (Betinho)

O padrao visual foi estabelecido ao longo das sessoes e e a assinatura do time de marketing Brasil.

### Especificacoes tecnicas
- **Largura:** sem restricao fixa (email corpo, nao template)
- **Encoding:** UTF-8
- **HTML:** inline styles obrigatorio (Outlook nao le `<style>` no head)
- **Layout:** tabelas para estrutura (NUNCA flexbox ou grid)
- **Envio:** via MCP Google — `draft_gmail_message` com `body_format="html"`

### Tipografia
| Elemento | Propriedade | Valor |
|---|---|---|
| Body | font-family | Arial, sans-serif |
| Body | font-size | 10.5pt |
| Body | color | `#333333` |
| Body | line-height | 1.6 |
| H2 | font-size | 13.5pt |
| H2 | color | `#1A1A1A` |
| H2 | border-bottom | solid `#FF3900` 1.5pt |
| H2 | padding-bottom | 4px |
| H2 | margin-top | 24px |
| H3 | font-size | 13.5pt |
| H3 | color | `#333333` |
| Caption/footer | font-size | 9pt |
| Caption/footer | color | `#666666` |

### Cores permitidas
| Cor | Hex/Nome | Uso |
|---|---|---|
| Laranja BW | `#FF3900` | Borda inferior H2, header de tabela de dados |
| Texto titulo | `#1A1A1A` | H2 |
| Texto corpo | `#333333` | H3, paragrafos, celulas de tabela |
| Bordas | `#DDDDDD` | Bordas de tabela |
| Fundo alternado | `whitesmoke` | Labels de tabela 2 colunas, zebra striping |
| Fundo | `white` | Background geral |

### Componentes

#### H2 (titulo de secao)
```html
<h2 style="font-size:13.5pt; color:#1A1A1A; border-bottom:solid #FF3900 1.5pt; padding-bottom:4px; margin-top:24px; margin-bottom:12px; font-family:Arial,sans-serif;">
  Titulo da Secao
</h2>
```

#### H3 (subtitulo)
```html
<h3 style="font-size:13.5pt; color:#333333; margin-top:18px; margin-bottom:8px; font-family:Arial,sans-serif;">
  Subtitulo
</h3>
```

#### Paragrafo
```html
<p style="font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; line-height:1.6; margin:8px 0;">
  Texto aqui.
</p>
```

#### Tabela 2 colunas (label + valor)
Usada para exibir pares de informacao (dados do usuario, detalhes de operacao, specs).

```html
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD; vertical-align:top;">Label</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Valor</td>
  </tr>
  <tr>
    <td style="width:140px; padding:8px 12px; background:whitesmoke; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD; vertical-align:top;">Label 2</td>
    <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Valor 2</td>
  </tr>
</table>
```

#### Tabela de dados (com header laranja)
Usada para tabelas de metricas, comparacoes, listas.

```html
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
  <thead>
    <tr>
      <th style="background:#FF3900; color:#FFFFFF; padding:8px 12px; text-align:left; font-family:Arial,sans-serif; font-size:10.5pt; font-weight:bold;">Coluna 1</th>
      <th style="background:#FF3900; color:#FFFFFF; padding:8px 12px; text-align:left; font-family:Arial,sans-serif; font-size:10.5pt; font-weight:bold;">Coluna 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Dado</td>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD;">Dado</td>
    </tr>
    <tr>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD; background:whitesmoke;">Dado</td>
      <td style="padding:8px 12px; font-family:Arial,sans-serif; font-size:10.5pt; color:#333333; border:1px solid #DDDDDD; background:whitesmoke;">Dado</td>
    </tr>
  </tbody>
</table>
```

---

## Tipos de email

### Email interno / EMT
- Idioma: Ingles
- Sem header/footer de marca (e email de trabalho, nao campanha)
- Usa o padrao visual acima (H2 com borda laranja, tabelas formatadas)
- Enviado via `draft_gmail_message`

### Email para time BR
- Idioma: Portugues
- Mesmo padrao visual
- Tom mais informal, direto

### Email transacional (ao usuario final)
- Ver `transactional.md`
- Footer de compliance OBRIGATORIO

### Email CRM/promocional (ao usuario final)
- Ver `crm-promocional.md`
- Footer de compliance OBRIGATORIO
- Regulamento de promocao linkado

---

## Regras

**Faca:**
- SEMPRE inline styles (nao `<style>` no head)
- SEMPRE `font-family: Arial, sans-serif` em cada elemento
- SEMPRE tabelas para layout (nao div/flex/grid)
- H2 com border-bottom `#FF3900` como assinatura visual

**Nao faca:**
- Flexbox ou Grid (Outlook nao suporta)
- Fontes externas (nao carregam em email)
- Imagens sem alt text
- Cores fora da lista permitida
- Esquecer border em celulas de tabela (fica sem estrutura visual)
