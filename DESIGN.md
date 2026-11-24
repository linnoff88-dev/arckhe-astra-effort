---
name: Astra Effort
description: Guia ARCKHÉ em portuguÃªs com referÃªncia visual de robÃ´ preto e dourado.
colors:
  primary: "#E2A23B"
  primary-light-theme: "#85520d"
  background: "#0c0c10"
  surface: "#14141b"
  card: "#16161e"
  line: "#272730"
  text: "#e9e9ee"
  muted: "#9a9aa6"
  ARCKHÉ: "#38bdf8"
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

O projeto usa o template estabelecido da skill projetos-landing-guia, com a imagem de robÃ´ preto e dourado escolhida pelo usuÃ¡rio. O conteÃºdo de estudo orienta a navegaÃ§Ã£o: comparaÃ§Ã£o, instruÃ§Ãµes e biblioteca, com pÃ¡ginas de leitura dedicadas.

## Colors

Ã‚mbar destaca aÃ§Ãµes e links; sky identifica ARCKHÉ AI e a cor PRO identifica o catÃ¡logo. O tema claro usa fundo #f6f7f9, texto #1a1a22, secundÃ¡rio #5b5b68, linhas #e1e3ea, ARCKHÉ #0369a1 e PRO #b45309. O Ã¢mbar claro efetivo Ã© #85520d, apÃ³s override de acessibilidade.

BotÃµes sÃ³lidos e nÃºmeros de etapas no tema claro usam texto branco: contraste medido de 6,54:1. Links permanecem Ã¢mbar escuro. O foco usa #f0c070 no tema escuro e #775013 no claro.

## Typography

Sora define tÃ­tulos e botÃµes; Inter, corpo; JetBrains Mono, cÃ³digo. O hero limita o tÃ­tulo a 22ch e a descriÃ§Ã£o a 65ch. O leitor usa contÃªiner de 78ch, corpo com altura de linha 1,85 e h2 de 1,7rem. A tabela usa .94rem; nos leitores, .88rem.

## Layout

ContÃªiner mÃ¡ximo de 1160px, margens automÃ¡ticas e 22px laterais. O hero final usa uma coluna, 48px de espaÃ§amento vertical e capa panorÃ¢mica abaixo do texto. A imagem usa width:100%, height:auto e object-fit:contain; preserve a proporÃ§Ã£o.

A navegaÃ§Ã£o fica fixa no topo. Abaixo de 980px oculta links de seÃ§Ã£o; abaixo de 600px permite quebra de linha e reduz os controles. A biblioteca passa de duas colunas para uma. A tabela tem rolagem horizontal interna. As etapas passam de marcador de 46px para 34px.

## Elevation & Depth

A versÃ£o final usa superfÃ­cies e bordas finas. A sombra da figura do template Ã© anulada por box-shadow:none. A navegaÃ§Ã£o escura mantÃ©m transparÃªncia e backdrop-filter:blur(12px); a clara usa fundo sÃ³lido. NÃ£o adicionar halos Ã  capa.

## Shapes

BotÃµes com raio de 10px, cards com 14px, figura com 16px. CÃ³digo e tabela tÃªm 12px. Chips do fluxo sÃ£o arredondados. A capa Ã© uma imagem real adaptada da referÃªncia, sem reconstruÃ§Ã£o ilustrativa em CSS.

## Components

NavegaÃ§Ã£o: marca, ARCKHÉ AI, PRO, seÃ§Ãµes, alternÃ¢ncia de tema e GitHub. O tema persiste em localStorage quando disponÃ­vel; a falha de armazenamento nÃ£o impede o controle.

Prompt copiÃ¡vel: botÃ£o com feedback em regiÃ£o role=status. Se a Ã¡rea de transferÃªncia falhar, seleciona o texto e orienta a cÃ³pia manual.

Tabela: cabeÃ§alhos semÃ¢nticos, caption, cÃ©lulas com espaÃ§amento e wrapper focalizÃ¡vel. O destaque de Medium indica a escolha histÃ³rica do autor para a tarefa, sem alegaÃ§Ã£o de superioridade universal.

Leitor: sumÃ¡rio recolhÃ­vel, links de retorno, texto amplo e estilos de impressÃ£o em A4. A folha impressa remove navegaÃ§Ã£o e adota texto escuro sobre branco.

## Do's and Don'ts

- Preserve os links ARCKHÉ AI e PRO e a terminologia tÃ©cnica dos arquivos.
- Preserve a proporÃ§Ã£o da capa em todos os tamanhos de tela.
- Use foco visÃ­vel de 3px e respeite prefers-reduced-motion na rolagem.
- Identifique dados histÃ³ricos, hipÃ³teses e arquivos originais em inglÃªs.
- NÃ£o apresente tokens processados como custo nem execuÃ§Ãµes individuais como mÃ©dias.
- NÃ£o refaÃ§a a identidade do template para satisfazer alertas genÃ©ricos de estilo.
