# Astra Effort — oito complementos úteis

Data de referência: 8 de setembro de 2026. O autor consultou as páginas oficiais pela documentação da OpenAI. Os prompts abaixo são adaptações práticas originais, não citações do fornecedor. São capacidades documentadas na pesquisa original e sugestões de fluxo, não experimentos adicionais às sete execuções do vídeo. Esta tradução não atualiza nem revalida a documentação citada.

## 1. Diagnostique a parada antes de buscar mais raciocínio

**Ideia principal:** se Astra pausar sem necessidade, pergunte qual instrução causou a pausa. O guia oficial citado descreve sensibilidade a skills e `AGENTS.md` e recomenda explicitar a instrução que bloqueia o trabalho. Isso torna inspecionável um problema aparentemente vago de “modelo preguiçoso”.

**Quando usar:** ele oferece continuar repetidamente, pede autorização para trabalho já solicitado ou devolve um plano em vez do resultado.

```text
Conclua o resultado solicitado usando o escopo que já combinamos. Faça suposições razoáveis para detalhes reversíveis e informe as importantes. Se estiver bloqueado, identifique o fato exato ausente ou a instrução exata e o arquivo que causam a parada. Conclua o trabalho independente possível antes de me perguntar. Termine conferindo as entregas contra meu pedido.
```

**Limite:** raciocínio adicional não está documentado como solução para paradas precoces. Esta intervenção muda instruções e comportamento; não contorna permissões reais. Evite “nunca me pergunte nada”.

Fonte: [Orientações de prompts para Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#instruction-following).

## 2. Teste o caminho da decisão, não apenas a captura de tela

**Ideia principal:** um protótipo pode parecer completo enquanto ignora uma escolha do usuário. Na verificação do produtor, o aplicativo de Sol permitiu selecionar “Split with Crew 1”, mas a próxima tela ainda descrevia mover Fernbank com Crew 2. Esse é um teste de qualidade melhor que contar elementos de um quadro.

**Quando usar:** ao revisar aprovações, preços, agendamentos, filtros ou preferências salvas.

```text
Use o aplicativo como um cliente. Escolha uma opção diferente da padrão, altere um número relevante e siga o fluxo até o resultado final. Mostre que a escolha e o número realmente mudam o resultado. Recarregue e confira o que persistiu. Experimente também uma entrada inválida. Informe entrada exata, resultado esperado e resultado observado. Corrija falhas e repita somente as verificações afetadas.
```

**Limite:** é um padrão de verificação recomendado e apoiado por uma descoberta preservada do produtor. Não prova que Sol sempre falha ou que Astra sempre passa. A orientação oficial de uso do computador recomenda examinar os resultados reais do aplicativo em vez de confiar na resposta final do agente.

Fontes: seção Sol de [evidence/PRODUCER-CHECKS.md](evidence/PRODUCER-CHECKS.md); [Uso do computador: verificar o resultado](https://developers.openai.com/api/docs/guides/tools-computer-use#5-continue-and-verify-the-result).

## 3. O limiar de 272 mil vale por requisição, não como orçamento do projeto inteiro

**Ideia principal:** segundo as notas consultadas pelo autor, prompts da API Astra acima de 272.000 tokens de entrada usam, na requisição inteira, tarifas de entrada/cache de 2× e saída de 1,5×. Não é apenas o excedente, nem simplesmente “tudo dobra”. Uma tarefa que processa milhões de tokens em chamadas repetidas pode não cruzar esse limite em nenhuma chamada individual.

**Quando usar:** em fluxos longos de API ou para investigar a afirmação de que mudar uma configuração de contexto do Codex reduzirá pela metade o uso da assinatura.

```text
Audite as configurações de contexto e cobrança deste fluxo sem alterá-las. Identifique se ele usa login do ChatGPT ou cobrança de API. Para chamadas de API, informe a maior contagem individual de tokens de entrada e se alguma requisição ultrapassou o limiar de 272.000 tokens de entrada do Astra. Separe isso do total acumulado da tarefa. Se recomendar compactação ou alteração de configuração, mostre primeiro a opção suportada, o valor atual e o diff proposto.
```

**Limite:** o limiar da API não estabelece desconto equivalente na assinatura do Codex. Não forneça uma edição universal de TOML sem conferir as opções suportadas pelo cliente instalado. Compactar também troca detalhes retidos por contexto menor.

Fonte: [Notas de preços do modelo Astra](https://developers.openai.com/api/docs/models/gpt-6-astra).

## 4. Fast e Medium são decisões separadas

**Ideia principal:** com login do ChatGPT, o modo Astra Fast consome créditos à taxa de 2,5× Standard onde disponível, segundo a pesquisa original. É um multiplicador de créditos, não uma promessa de terminar tarefas 2,5 vezes mais rápido. A afirmação de velocidade de 1,5× na página citada nomeia explicitamente outras famílias de modelos. A API tem tarifas próprias: Astra Fast usa 2× as tarifas aplicáveis por token.

**Quando usar:** você gosta da saída de Medium, mas quer decidir se iterar mais rápido vale o consumo extra da franquia.

```text
Inspecione meu modelo atual, esforço de raciocínio, modo de velocidade e forma de autenticação. Explique a relação de uso aplicável usando a documentação oficial atual. Mantenha o esforço de raciocínio inalterado. Mostre como mudar somente a velocidade para comparar uma tarefa representativa em Standard e Fast.
```

O guia cita `/fast status`, `/fast off` e `/fast on` no Codex CLI para consultar e alterar essa opção.

**Limite:** a preferência de Mark por Medium + Fast é uma preferência de fluxo. A tabela das sete execuções não mede um experimento Standard versus Fast nem o gasto real de créditos.

Fontes: [Velocidade no Codex](https://learn.chatgpt.com/docs/agent-configuration/speed); [Modelo Astra na API](https://developers.openai.com/api/docs/models/gpt-6-astra).

## 5. Milhões de tokens processados podem ser, em grande parte, contexto relido

**Ideia principal:** entrada em cache e saída de raciocínio são subconjuntos dos contadores, não categorias extras a somar duas vezes. Os totais acumulados do vídeo incluem entrada em cache repetida; Ultra inclui também seus três subagentes. Descrevem trabalho processado, não palavras novas geradas nem uma cobrança.

**Quando usar:** ao comparar execuções ou tentar explicar por que uma resposta curta apresentou um total alto de tokens.

```text
Audite estes registros de execução. Informe entrada comum, entrada em cache, gravação de cache quando disponível, saída e subconjuntos de saída de raciocínio. Concilie os totais sem duplicar subconjuntos. Inclua agentes filhos exatamente uma vez. Separe tokens processados, créditos realmente cobrados e custo financeiro de API. Se faltarem dados reais de cobrança, marque o custo como indisponível em vez de estimá-lo apenas pelo total de tokens.
```

**Limite:** cache na API tem condições e preços próprios de leitura e gravação. Preserve os campos brutos de uso; não deduza uma conta exata a partir de uma captura ou da quantidade de palavras da resposta final.

Fontes: [Medição de cache de prompts](https://developers.openai.com/api/docs/guides/prompt-caching); [evidence/results.json](evidence/results.json) e [verificações do produtor](evidence/PRODUCER-CHECKS.md). No original, esta última referência aparece como `PRODUCER-REVIEW.md`; nesta distribuição o arquivo se chama `PRODUCER-CHECKS.md`.

## 6. Aumente o esforço na fase difícil sem quebrar o cache da API

**Ideia principal:** o original descreve um item de entrada `configuration_update` na Responses API do Astra que muda o esforço mantendo a configuração original da requisição e seu prefixo em cache. É possível rascunhar em low e aumentar o esforço para analisar falhas na mesma conversa.

```json
{
  "type": "configuration_update",
  "reasoning": { "effort": "high" }
}
```

Coloque-o antes da próxima mensagem do usuário; mantenha o `reasoning.effort` da requisição no valor original.

```text
Revise a migração proposta em busca de cenários de perda de dados, falhas de concorrência e lacunas de reversão. Para cada risco relevante, aponte a parte correspondente do plano e proponha uma verificação ou alteração concreta. Mantenha o escopo já combinado.
```

**Limite:** recurso de desenvolvimento da API, não uma frase mágica em uma conversa do Codex. O suporte descrito é para Astra em modo padrão de agente único. A atualização persiste até ser substituída. O campo `reasoning.effort` da resposta continua informando a configuração da requisição e, sozinho, não basta para auditar o esforço efetivo. Após compactar, adicione uma atualização nova com o valor desejado. Isso não produz uma comparação independente e isolada: o histórico é compartilhado deliberadamente.

Fonte: [Mudar o raciocínio durante a conversa](https://developers.openai.com/api/docs/guides/reasoning#change-reasoning-mid-conversation).

## 7. Dê uma pergunta diferente a cada subagente

**Ideia principal:** delegar é útil quando frentes independentes de pesquisa podem avançar simultaneamente. O guia citado de Astra diz que ele pode delegar menos que o desejado se não receber instruções sobre quando fazê-lo. Na execução preservada de Ultra, três frentes especializadas acrescentaram 7,12 milhões de tokens processados; não foram uma equipe de pesquisa gratuita.

```text
Use até três subagentes para perguntas independentes: um para evidências de dores dos clientes, um para produtos concorrentes e um para motivos pelos quais a ideia pode falhar. Dê a cada um uma entrega delimitada com fontes diretas. Mantenha a decisão de produto e a síntese com o agente principal. Evite pesquisas duplicadas. Se não houver trabalho independente útil, continue sem delegar.
```

**Limite:** mais agentes não são automaticamente mais baratos ou melhores. Registre modelos e inclua seu consumo. É uma sugestão de fluxo, não um resultado universal de desempenho.

Fontes: [Delegação a subagentes no Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra#subagent-delegation); seção Ultra de [evidence/PRODUCER-CHECKS.md](evidence/PRODUCER-CHECKS.md).

## 8. Use Grok para encontrar a objeção que você preferiria não ver

**Ideia principal:** em vez de pedir “as melhores ideias” a Grok, peça pessoas que já resolvem a dor proposta com software barato ou IA. A pesquisa de Scopekeep encontrou a afirmação de um dono de empresa de telhados de que Grok e uma ferramenta de código aberto já atendiam às solicitações de alteração de serviços. É uma evidência contrária relevante para um SaaS desse tipo.

```text
Estou avaliando [produto] para [cliente específico]. Encontre publicações recentes de primeira mão no X mostrando como esses clientes já resolvem [dor], especialmente com planilhas, software estabelecido ou IA. Priorize evidências que possam tornar este produto desnecessário. Retorne links diretos, datas, a solução realmente usada e o que cada fonte comprova ou não. Não invente demanda de compra a partir de curtidas. Se uma fonte não abrir, informe isso.
```

Acompanhamento no Codex:

```text
Abra os originais citados. Quais afirmações resistem à verificação? Revise a oportunidade com base nas dificuldades que os clientes ainda enfrentam depois de usar essas soluções. Separe uma funcionalidade copiável de uma hipótese de vantagem defensável que precisa de validação.
```

**Limite:** respostas de Grok são pistas de pesquisa. O exemplo histórico do X foi lido pelo participante, mas o produtor não conseguiu reabri-lo de forma independente; não o apresente como verificado novamente aqui. Reclamações não provam disposição para pagar nem vantagem competitiva duradoura.

Fonte: seção XHigh de [evidence/PRODUCER-CHECKS.md](evidence/PRODUCER-CHECKS.md). O método é uma recomendação editorial original.
