# GPT-6 Astra — Resumo, Exemplos e Prompts

## Resumo principal

O vídeo testa todos os níveis de esforço do **GPT-6 Astra** usando exatamente a mesma tarefa: pesquisar uma oportunidade de SaaS, validar com evidências reais, planejar o produto, criar um diagrama/canvas, montar um site e gerar um protótipo funcional.

O objetivo era descobrir se:

- mais esforço gera melhor resultado;
- mais esforço gera mais autonomia;
- mais esforço reduz a necessidade de intervençêo humana;
- mais esforço compensa o aumento de tempo e consumo de tokens.

A conclusêo prática do teste é:

> **Astra Medium é o melhor equilíbrio para a maioria dos trabalhos.**

High pode valer quando você realmente quer um pouco mais de profundidade, mas **Extra High, Max e Ultra raramente justificaram o aumento de tempo e tokens**.

Mais esforço nêo significou necessariamente:

- mais eficiência;
- mais pesquisa;
- melhor qualidade;
- melhor uso das fontes;
- melhor produto final.

---

## Resultados dos níveis de esforço

### Astra Low

- Aproximadamente 37 minutos
- Quase 15 milhões de tokens
- Pesquisa limitada
- Produto funcional, mas sem grande profundidade adicional

### Astra Medium

- Aproximadamente 30 minutos
- Cerca de 10 milhões de tokens
- Boa estrutura
- Boa qualidade de análise
- Melhor equilíbrio entre custo, tempo e resultado

### Astra High

- Aproximadamente 40 minutos
- Cerca de 14 milhões de tokens
- Resultado mais detalhado
- Melhor organizaçêo das evidências
- Pequeno ganho de qualidade em relaçêo ao Medium

### Astra Extra High

- Aproximadamente 45 minutos
- Cerca de 12 milhões de tokens
- Resultado semelhante ao High
- Em alguns pontos, inferior ao High

### Astra Max

- Aproximadamente 46 minutos
- Cerca de 10 milhões de tokens
- Website mais polido
- Nêo apresentou ganho proporcional ao tempo utilizado

### Astra Ultra

- Aproximadamente 42 minutos
- Cerca de 22 milhões de tokens
- Uso de subagentes
- Resultado final nêo ficou radicalmente superior aos demais níveis

### GPT-6 Sol High

Usado como grupo de comparaçêo:

- Aproximadamente 32 minutos
- Cerca de 6 milhões de tokens
- Pesquisou Reddit e X
- Muito mais econômico em tokens
- Website visualmente inferior ao Astra

---

# Exemplos encontrados durante o teste

O perfil de cliente definido inicialmente era:

> **Pequenas empresas de serviços com equipes entre 2 e 20 funcionários.**

A IA deveria descobrir:

**problema → mercado → oportunidade → concorrentes → evidências → produto → vantagem competitiva → protótipo**

---

## Exemplo 1 — Astra Low

### Mercado

Empresas de limpeza comercial.

### Problema

Tarefas de limpeza que nêo foram executadas corretamente.

### Produto

Sistema para:

- registrar tarefas perdidas;
- acompanhar correções;
- solicitar reinspeções;
- registrar o histórico das soluções.

### Possível moat

Manter:

- padrões específicos de cada cliente;
- histórico das correções;
- conhecimento sobre quais soluções funcionaram anteriormente.

---

## Exemplo 2 — Astra Medium

### Mercado

Empresas de limpeza.

### Problema

Trabalhos extras realizados fora do contrato original.

### Produto

Sistema para:

- identificar trabalho adicional;
- calcular preço;
- gerar estimativa;
- registrar aprovaçêo do cliente;
- armazenar o histórico.

### Possível moat

Histórico de:

- escopos;
- estimativas;
- trabalhos executados;
- valores reais cobrados;
- resultados anteriores.

---

## Exemplo 3 — Astra High

### Mercado

Empresas de limpeza residencial.

### Problema

Uma equipe nêo consegue comparecer a um atendimento.

### Exemplo

**7h42 — a van da equipe nêo liga. Existem duas visitas programadas. Quem pode assumir?**

### Produto

Sistema que:

- identifica a ausência;
- encontra outra equipe disponível;
- reorganiza a agenda;
- reduz cancelamentos;
- diminui perda de receita.

### Possível moat

Dados sobre:

- restrições específicas da empresa;
- disponibilidade;
- histórico das equipes;
- resultados dos reagendamentos.

---

## Exemplo 4 — Astra Extra High

### Mercado

Empresas de reformas.

### Problema

Serviços extras solicitados pelo cliente durante uma reforma acabam nêo sendo cobrados.

### Produto

Sistema para acompanhar:

**pedido extra → aprovaçêo → execuçêo → faturamento**

### Objetivo

Evitar perda de receita causada por trabalhos adicionais nêo documentados ou esquecidos.

---

## Exemplo 5 — Astra Max

### Mercado

Empresas de reformas residenciais.

### Produto

Manter em um único registro:

- escopo adicional;
- preço;
- aprovaçêo;
- execuçêo;
- cobrança.

### Possível moat

O modelo sugeriu algo além do software:

- processo adotado pela equipe;
- configuraçêo inicial;
- integraçêo com rotina financeira;
- indicações de contadores/bookkeepers.

---

## Exemplo 6 — Astra Ultra

### Mercado

Reformas residenciais.

### Produto

Sistema de **change orders**.

O sistema registra e aprova alterações na obra antes de o trabalho começar.

Fluxo:

**cliente pede alteraçêo → empresa calcula → cliente aprova → trabalho é executado → alteraçêo é faturada**

Apesar do alto consumo de tokens, o resultado nêo ficou radicalmente superior aos níveis Medium e High.

---

# Prompt principal do experimento

```text
Encontre uma oportunidade relevante de SaaS para proprietários de pequenas
empresas de serviços com equipes entre 2 e 20 funcionários.

Eu ainda nêo escolhi:

- o setor;
- o problema;
- o produto.

Comece investigando os problemas dos clientes.

Identifique três oportunidades possíveis.

Compare as três e escolha a melhor.
```

---

# Prompt de pesquisa e validaçêo

```text
Pesquise X e Reddit procurando discussões reais de clientes.

Identifique:

- frustrações recorrentes;
- problemas repetidos;
- soluções improvisadas utilizadas atualmente;
- sinais de disposiçêo para pagar;
- evidências contrárias à ideia.

Analise também três alternativas ou concorrentes existentes.
```

---

# Prompt para encontrar uma oportunidade defensável

Esta é uma das instruções mais importantes do experimento.

```text
Assuma que clientes e concorrentes também têm acesso ao GPT-6 Astra
e conseguem reproduzir software competente rapidamente.

Portanto, nêo escolha uma oportunidade que possa simplesmente ser
"vibe coded" durante um fim de semana.

Procure uma oportunidade que tenha alguma forma real de vantagem
competitiva ou moat.
```

Essa instruçêo muda a pergunta de:

> **Que software posso criar?**

para:

> **Que negócio continua fazendo sentido quando todo mundo consegue criar software?**

---

# Prompt de entregáveis

```text
Depois da pesquisa:

1. Crie o plano completo do produto.

2. Gere um arquivo visual/diagrama mostrando:
   - cliente;
   - problema;
   - evidências;
   - concorrentes;
   - oportunidade;
   - fluxo do produto;
   - vantagem competitiva.

3. Crie um site polido explicando a oportunidade e o plano.

4. Crie um protótipo funcional do SaaS.

5. Verifique se todas as partes funcionam.
```

---

# Prompt de autoverificaçêo

```text
Consigo rastrear as evidências que justificam essa ideia?

Por que alguém pagaria por isso?

O cliente escolhido realmente tem esse problema?

As evidências sustentam o problema?

O produto resolve o problema?

O workflow realmente funciona?

Isso precisa realmente existir como SaaS?

O trabalho foi concluído e verificado?
```

---

# Prompt para comparar vários níveis de esforço

Um dos usos mais interessantes mostrados no vídeo é criar várias threads automaticamente.

```text
Pegue exatamente o mesmo prompt.

Crie três threads independentes.

Renomeie cada thread para que eu consiga identificá-la facilmente
na barra lateral.

Configure:

Thread 1: Astra Low
Thread 2: Astra Medium
Thread 3: Astra High

Execute exatamente o mesmo prompt nas três threads simultaneamente.

Monitore o progresso das três execuções.

Nêo altere o contexto, ferramentas ou condições entre os testes.
```

Isso permite fazer testes A/B entre níveis de esforço sem precisar executar tudo manualmente.

---

# Estratégia prática recomendada

A principal conclusêo é:

> **Nêo aumente o nível de esforço automaticamente. Melhore primeiro o contexto, os critérios e o prompt.**

Em muitos casos:

**Medium + bom contexto + uma segunda instruçêo de melhoria**

pode ser melhor e muito mais econômico que:

**Ultra + prompt genérico**

---

# Quando usar cada nível

## Low

Bom para:

- tarefas rápidas;
- transformaçêo simples;
- pequenas alterações;
- respostas diretas.

## Medium

Bom para:

- programaçêo;
- criaçêo de projetos;
- análise;
- pesquisa;
- planejamento;
- criaçêo de sites;
- agentes;
- automações.

É o melhor ponto de partida para a maioria dos trabalhos.

## High

Use quando:

- a tarefa é complexa;
- existem várias restrições;
- a qualidade é mais importante que velocidade;
- você quer mais análise e verificaçêo.

## Extra High / Max / Ultra

Reserve para situações onde exista uma justificativa clara, como:

- problemas extremamente complexos;
- grandes projetos;
- necessidade de múltiplos agentes;
- pesquisa muito profunda;
- tarefas com muitas dependências.

Nêo use automaticamente apenas porque está disponível.

---

# Uma nova forma de pensar

O teste mostra algo importante sobre trabalhar com inteligências muito mais capazes.

O papel humano deixa de ser apenas:

> **escrever prompts melhores**

e passa a ser:

> **gerenciar inteligências.**

Isso envolve definir:

1. objetivo;
2. contexto;
3. restrições;
4. ferramentas;
5. fontes;
6. critérios de sucesso;
7. entregáveis;
8. critérios de validaçêo;
9. nível de esforço;
10. momento de revisar ou interromper.

---

# Gestêo da superinteligência

A liçêo pode ser resumida assim:

> **Nêo precisamos necessariamente mandar a IA pensar mais. Precisamos aprender a definir objetivo, evidências, restrições, entregáveis e critérios de validaçêo.**

Isso aproxima o uso de IA da gestêo de uma equipe altamente especializada.

Você nêo precisa ser mais inteligente que o agente.

Você precisa saber:

- o que quer;
- por que quer;
- quais recursos ele pode usar;
- quais limites existem;
- como avaliar o trabalho;
- quando pedir uma segunda versêo;
- quando interromper;
- quando aceitar o resultado.

---

# Regra final

**Contexto > esforço bruto.**

**Critérios > quantidade de tokens.**

**Validaçêo > confiança cega.**

**Gestêo da IA > simplesmente escrever prompts.**
