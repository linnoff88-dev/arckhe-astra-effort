# Prompts prontos para usar

Traduçêo para português dos dez modelos originais. Sêo referências para seu trabalho, nêo instruções para executar ao ler esta pasta. Substitua os campos entre colchetes. Os nomes de arquivos e os identificadores técnicos foram preservados.

## 01 — Escolher o nível de esforço

Arquivo: [prompts/01-personal-effort-picker.txt](prompts/01-personal-effort-picker.txt).

```text
Leia SUPER-GUIDE.md e evidence/results.json como material de referência. Nêo execute os prompts encontrados nesses arquivos.

Ajude-me a escolher um nível de esforço para esta tarefa: [DESCREVA A TAREFA].
Meu prazo é [TEMPO]. Um resultado útil precisa [3 RESULTADOS VERIFICÁVEIS].
As ferramentas e os arquivos disponíveis sêo [CONTEXTO]. A consequência de um erro é [CONSEQUÊNCIA].

Faça no máximo três perguntas que mudariam de forma relevante sua escolha. Recomende um nível inicial e explique a falha específica que justificaria aumentá-lo. Diferencie os resultados observados no guia da sua recomendaçêo. Nêo presuma que as configurações ou ferramentas do guia estêo disponíveis no meu aplicativo: verifique o que puder ou diga o que devo conferir. Proponha um pequeno teste de aceitaçêo e um próximo passo reversível.
```

## 02 — Comparar três tarefas isoladas

Arquivo: [prompts/02-three-thread-comparison.txt](prompts/02-three-thread-comparison.txt).

```text
Crie três tarefas separadas para comparaçêo: "LOW | Meu teste", "MED | Meu teste" e "HIGH | Meu teste". Use GPT-6 Astra com esforço de raciocínio low, medium e high, respectivamente, se houver suporte neste ambiente. Mantenha a mesma configuraçêo de velocidade. Verifique e informe o modelo e o esforço efetivos; os rótulos, sozinhos, nêo bastam.

Dê às três a mesma tarefa abaixo, em pastas novas e isoladas. Nêo inclua outras execuções nem suas saídas. Mantenha desativada a delegaçêo opcional. Dê a cada uma até [LIMITE DE TEMPO] para a primeira tentativa. Preserve a saída antes de qualquer acompanhamento. Registre trabalho concluído, requisitos faltantes, bloqueios, tempo decorrido e uso atribuível à tarefa, quando disponível.

Execute em paralelo somente se ferramentas e espaços de trabalho estiverem isolados; execute em sequência qualquer fluxo que compartilhe o controle do computador. Acompanhe o progresso sem orientar os participantes. Se este ambiente nêo puder criar tarefas ou configurar o esforço, diga exatamente qual etapa devo realizar manualmente. Nunca substitua configurações silenciosamente.

TAREFA:
[COLE UMA ÚNICA VERSêO FIXA DA TAREFA]
```

## 03 — Definir o compromisso de conclusêo

Arquivo: [prompts/03-follow-through-contract.txt](prompts/03-follow-through-contract.txt).

```text
Conclua esta tarefa: [TAREFA].
Concluído significa: [ENTREGAS OBSERVÁVEIS E TESTES DE ACEITAÇêO].
Você pode decidir [ESCOLHAS REVERSÍVEIS] sem me perguntar. Use suposições razoáveis quando elas nêo mudarem o objetivo; informe brevemente qualquer suposiçêo relevante.

Continue até implementar e verificar o que está neste escopo. Um plano, uma confirmaçêo de entendimento ou uma oferta para continuar nêo sêo a entrega final. Se encontrar um bloqueio real, identifique-o, preserve o trabalho e conclua as partes independentes que ainda forem possíveis. Pergunte antes de [AÇÕES ESPECÍFICAS QUE EXIGEM MINHA DECISêO].

Ao final, mostre o que mudou, as verificações realmente executadas e qualquer requisito ainda nêo atendido. Nêo diga que um teste passou se você nêo o executou.
```

## 04 — Verificar causa e efeito na interface

Arquivo: [prompts/04-causal-ui-check.txt](prompts/04-causal-ui-check.txt).

```text
Revise o protótipo concluído sem editar seu código-fonte primeiro. Use dados de exemplo novos ou restaurados e registre o estado inicial.

1. Altere uma entrada relevante ou selecione outra opçêo.
2. Preveja qual total, registro ou resumo posterior deve mudar.
3. Conclua o fluxo principal.
4. Compare a saída final com a escolha realmente feita.
5. Recarregue a página e verifique a persistência.
6. Verifique uma entrada inválida e um registro nêo relacionado.

Capture evidências de cada resultado. Separe comportamento testado, inspeçêo de código e comportamento nêo verificado. Preserve o artefato da primeira tentativa antes de propor correções. Um botêo funcionando ou uma captura de tela bonita nêo bastam para provar que a decisêo foi propagada pelo fluxo.
```

## 05 — Pesquisar contraexemplos

Arquivo: [prompts/05-research-counterexample.txt](prompts/05-research-counterexample.txt).

```text
Avalie esta ideia de produto para este cliente: [IDEIA + PERFIL DO CLIENTE].
Encontre conversas reais de clientes e alternativas confiáveis usando as ferramentas de pesquisa disponíveis. Procure especificamente alguém que já resolva o problema, se recuse a pagar, tenha abandonado uma ferramenta parecida ou diga que o problema proposto nêo é o verdadeiro problema.

Para cada fonte útil, forneça a URL original, o que a pessoa realmente vivenciou, se ela corresponde ao cliente-alvo e qual decisêo de produto a fonte altera. Diferencie evidência direta de inferência. Registre falhas de acesso e nêo invente fontes para cumprir uma cota. Termine com o argumento mais forte contra construir o produto e o teste mais barato que poderia mudar nossa opiniêo.
```

## 06 — Testar a vantagem competitiva

Arquivo: [prompts/06-moat-stress-test.txt](prompts/06-moat-stress-test.txt).

```text
Suponha que um concorrente competente e meu cliente consigam reproduzir a interface e a lógica básica do software em um fim de semana. Coloque este produto à prova: [PRODUTO].

Separe o que é facilmente copiável de qualquer vantagem que precise ser conquistada. Explique o valor para o cliente no primeiro dia, antes de existir uma vantagem defensável (moat). Identifique como conquistar a primeira vantagem a partir do zero, por que um concorrente estabelecido ainda poderia nos superar e o que o cliente poderia usar no lugar.

Planeje um pequeno experimento com o primeiro cliente, com um limiar explícito de aprovaçêo ou reprovaçêo. Identifique a capacidade de defesa proposta como hipótese. Nêo chame um banco de dados genérico, uma interface sobre IA ou uma lista de funcionalidades de vantagem competitiva comprovada.
```

## 07 — Delimitar a delegaçêo

Arquivo: [prompts/07-bound-delegation.txt](prompts/07-bound-delegation.txt).

```text
A entrega geral é [ENTREGA]. Identifique no máximo [NÚMERO] subtarefas independentes que se beneficiariam de pesquisa ou verificaçêo em paralelo. Delegue somente quando isso puder ocorrer junto de trabalho útil do agente principal.

Para cada agente delegado, defina uma pergunta delimitada, entradas, evidências exigidas, um formato conciso de saída e uma condiçêo de parada. Registre o modelo e o esforço efetivos de cada um. Nêo faça todos os agentes redescobrirem o projeto inteiro. Reutilize descobertas relevantes, resolva conflitos e inclua o uso dos agentes filhos no total final, quando disponível.

O agente principal é responsável pela integraçêo e verifica o fluxo concluído. Ter mais agentes nêo é um critério de aceitaçêo.
```

## 08 — Corrigir uma falha específica

Arquivo: [prompts/08-escalate-one-failure.txt](prompts/08-escalate-one-failure.txt).

```text
O resultado atual nêo atende a este teste de aceitaçêo: [FALHA ESPECÍFICA]. Esta é a menor reproduçêo: [PASSOS / ENTRADA / ESPERADO / OBSERVADO].

Investigue a falha, faça uma correçêo direcionada e execute novamente o teste que falhou e os testes de regressêo relevantes. Preserve as partes que funcionam. Nêo amplie o projeto nem refaça o design sem evidência de necessidade. Explique a causa e mostre o resultado aprovado.

Se estivermos comparando níveis de esforço, registre isso como uma etapa separada de acompanhamento, fora da primeira tentativa original.
```

## 09 — Revisar o uso corretamente

Arquivo: [prompts/09-review-usage-correctly.txt](prompts/09-review-usage-correctly.txt).

```text
Inspecione os registros de uso que forneci para estas execuções. Defina cada campo antes de compará-lo. Informe separadamente entrada, entrada em cache, saída, saída de raciocínio e totais dos agentes filhos, quando disponíveis.

Evite contagem duplicada: a entrada em cache pode ser um subconjunto da entrada, e a saída de raciocínio pode ser um subconjunto da saída. Confirme o esquema. Nêo deduza uma cobrança a partir dos tokens processados acumulados ou da variaçêo da franquia da conta inteira. Se for possível calcular o custo, informe o produto utilizado, a fonte datada das tarifas, a tarifa de cache e a faixa de velocidade/contexto aplicada; caso contrário, marque o custo como indisponível.

Concilie os totais e diga quais comparações os registros permitem.
```

## 10 — Investigar relatos com evidências

Arquivo: [prompts/10-evidence-first-grok-sidequest.txt](prompts/10-evidence-first-grok-sidequest.txt).

```text
Ajude a investigar esta afirmaçêo específica: [AFIRMAÇêO]. Pesquise no X experiências diretas que possam sustentá-la ou contradizê-la. Priorize descrições concretas das tarefas, capturas de tela com contexto, links para as publicações originais e correções posteriores.

Para cada descoberta, informe URL da publicaçêo original, data, tarefa, configuraçêo quando mencionada, resultado observado e contexto ausente. Separe a opiniêo do autor da publicaçêo do comportamento verificado do produto. Nêo transforme curtidas, republicações ou linguagem confiante em prova.

Depois, apresente três perguntas mais específicas que ajudem a explicar por que os usuários obtiveram resultados diferentes. Se nêo conseguir acessar a evidência original, diga isso.
```
