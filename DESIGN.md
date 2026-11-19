---
name: Astra Effort
description: Guia INEMA em português com referência visual de robô preto e dourado.
colors:
  primary: "#E2A23B"
  primary-light-theme: "#85520d"
  background: "#0c0c10"
  surface: "#14141b"
  card: "#16161e"
  line: "#272730"
  text: "#e9e9ee"
  muted: "#9a9aa6"
  inema: "#38bdf8"
  pro: "#cbd5e1"
  background-light: "#f6f7f9"
  text-light: "#1a1a22"
typography:
  display:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(2.2rem,5vw,3.5rem)"
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: "-.025em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "16px"
    lineHeight: 1.65
  code:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: ".86rem"
    lineHeight: 1.6
rounded:
  button: "10px"
  card: "14px"
  figure: "16px"
spacing:
  wrap: "22px"
  section: "62px"
  card: "20px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#1a1206"
    rounded: "{rounded.button}"
    padding: ".6em 1.05em"
  button-primary-light:
    backgroundColor: "{colors.primary-light-theme}"
    textColor: "#ffffff"
    rounded: "{rounded.button}"
    padding: ".6em 1.05em"
  card:
    backgroundColor: "{colors.card}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "{spacing.card}"
---

# Design System: Astra Effort

## Overview

O projeto usa o template estabelecido da skill projetos-landing-guia, com a imagem de robô preto e dourado escolhida pelo usuário. O conteúdo de estudo orienta a navegação: comparação, instruções e biblioteca, com páginas de leitura dedicadas.

## Colors

Âmbar destaca ações e links; sky identifica INEMA.CLUB e a cor PRO identifica o catálogo. O tema claro usa fundo #f6f7f9, texto #1a1a22, secundário #5b5b68, linhas #e1e3ea, INEMA #0369a1 e PRO #b45309. O âmbar claro efetivo é #85520d, após override de acessibilidade.

Botões sólidos e números de etapas no tema claro usam texto branco: contraste medido de 6,54:1. Links permanecem âmbar escuro. O foco usa #f0c070 no tema escuro e #775013 no claro.

## Typography

Sora define títulos e botões; Inter, corpo; JetBrains Mono, código. O hero limita o título a 22ch e a descrição a 65ch. O leitor usa contêiner de 78ch, corpo com altura de linha 1,85 e h2 de 1,7rem. A tabela usa .94rem; nos leitores, .88rem.

## Layout

Contêiner máximo de 1160px, margens automáticas e 22px laterais. O hero final usa uma coluna, 48px de espaçamento vertical e capa panorâmica abaixo do texto. A imagem usa width:100%, height:auto e object-fit:contain; preserve a proporção.

A navegação fica fixa no topo. Abaixo de 980px oculta links de seção; abaixo de 600px permite quebra de linha e reduz os controles. A biblioteca passa de duas colunas para uma. A tabela tem rolagem horizontal interna. As etapas passam de marcador de 46px para 34px.

## Elevation & Depth

A versão final usa superfícies e bordas finas. A sombra da figura do template é anulada por box-shadow:none. A navegação escura mantém transparência e backdrop-filter:blur(12px); a clara usa fundo sólido. Não adicionar halos à capa.

## Shapes

Botões com raio de 10px, cards com 14px, figura com 16px. Código e tabela têm 12px. Chips do fluxo são arredondados. A capa é uma imagem real adaptada da referência, sem reconstrução ilustrativa em CSS.

## Components

Navegação: marca, INEMA.CLUB, PRO, seções, alternância de tema e GitHub. O tema persiste em localStorage quando disponível; a falha de armazenamento não impede o controle.

Prompt copiável: botão com feedback em região role=status. Se a área de transferência falhar, seleciona o texto e orienta a cópia manual.

Tabela: cabeçalhos semânticos, caption, células com espaçamento e wrapper focalizável. O destaque de Medium indica a escolha histórica do autor para a tarefa, sem alegação de superioridade universal.

Leitor: sumário recolhível, links de retorno, texto amplo e estilos de impressão em A4. A folha impressa remove navegação e adota texto escuro sobre branco.

## Do's and Don'ts

- Preserve os links INEMA.CLUB e PRO e a terminologia técnica dos arquivos.
- Preserve a proporção da capa em todos os tamanhos de tela.
- Use foco visível de 3px e respeite prefers-reduced-motion na rolagem.
- Identifique dados históricos, hipóteses e arquivos originais em inglês.
- Não apresente tokens processados como custo nem execuções individuais como médias.
- Não refaça a identidade do template para satisfazer alertas genéricos de estilo.
