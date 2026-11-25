# Revisêo do produtor — primeiras tentativas

Revisêo encerrada em 7 de setembro de 2026, horário de Toronto (8 de setembro em UTC). As sete primeiras tentativas foram congeladas antes dos testes do produtor. Nenhuma correçêo ou orientaçêo foi enviada aos participantes. Os arquivos-fonte originais nêo foram editados. Os servidores foram reiniciados para a revisêo; várias inicializações simultâneas colidiram nas portas de inspeçêo e depois funcionaram em sequência. O tempo de reinicializaçêo nêo está incluído na duraçêo dos participantes.

Esta é a traduçêo da revisêo histórica, nêo uma nova execuçêo dos testes. A versêo inglesa está em [../original-en/evidence/PRODUCER-CHECKS.md](../original-en/evidence/PRODUCER-CHECKS.md).

## Mediçêo

**Tempo:** o primeiro `task_complete.duration_ms` de cada tarefa, arredondado para o segundo mais próximo. Inclui espera por ferramentas, pesquisa e construçêo, nêo apenas geraçêo do modelo. As sete execuções rodaram simultaneamente na mesma máquina; compare as execuções observadas, nêo velocidade universal.

**Tokens:** `total_token_usage` acumulado final na primeira conclusêo, conciliado de forma independente com a soma de `last_token_usage` das atualizações acumuladas distintas. As sete conciliam. `total = input + output`; `reasoning_output` é subconjunto de `output`, e `cached_input` é subconjunto de `input`. Nêo some nenhum deles duas vezes. Ultra inclui o principal e três totais de tarefas filhas, cada um limitado ao instante de conclusêo do principal. Os contadores dos filhos começam de forma independente perto de 30 mil, sem herdar o acumulado do principal. A soma é 21.730.368. Sêo tokens processados, majoritariamente entrada em cache ou reutilizada, nêo contexto novo, créditos, dinheiro ou cobrança.

**Fonte primária:** [results.json](results.json); os hashes das sessões de origem foram preservados. Contagens exatas e links brutos/normalizados estêo nesse arquivo. XHIGH contém oito URLs de publicações ou conversas, mas apenas sete conversas: o segundo status do X é uma resposta do autor na mesma conversa. Os demais coincidem com a contagem de conversas identificada no registro. Uma fonte original do Reddit de Low e Medium foi reaberta; a fonte de Medium realmente descreve cômodos, escadas e dutos adicionais fora do contrato. As contagens medem a extensêo do registro de pesquisa, nêo demanda de compra validada.

**Quadros:** elementos nativos ativos, nêo excluídos, do Excalidraw. Imagens incorporadas foram contadas nos arquivos; desenhos e formas nêo contam como imagens incorporadas. Os sete JSONs dos quadros sêo válidos; seus textos foram lidos para conferir seis zonas exigidas e conexões entre evidências, decisões de produto, jornada, telas, arquitetura e MVP. Sol separa a direçêo visual como zona adicional e nêo incorpora imagens rasterizadas. As contagens sêo descritivas, nêo notas de qualidade.

## LOW · Astra / Clearshift

No navegador, o produtor abriu CS-1042, editou a instruçêo de correçêo, salvou a atribuiçêo e carregou uma nova verificaçêo de exemplo. O encerramento ficou desabilitado até que o padrêo sinalizado fosse conferido. Após concluir e recarregar, o painel mostrou Open 2 e Closed 1. Aprovado nesse caminho de correçêo, nova verificaçêo e salvamento.

Oito conversas no Reddit; nenhuma no X. O quadro tem 161 elementos e três capturas reais do aplicativo. O fluxo delimitado do dono é coerente, com alternativas explícitas e uma vantagem proposta de serviço/dados. Mais tempo e tokens processados registrados que Medium, apesar do esforço menor.

## MED · Astra / Scopewell

No navegador, em uma verificaçêo anterior preservada, o produtor alterou a mêo de obra de 45 para 60 minutos; a proposta mensal passou de $164 para $212. Preparou a proposta, registrou uma aceitaçêo fictícia e recarregou: uma alteraçêo registrada e $212 em adicionais permaneceram. Aprovado em mudança de preço, aprovaçêo e persistência.

Seis conversas no Reddit; nenhuma no X. O quadro tem 133 elementos e um esboço de interface incorporado. Evidências contrárias detalhadas, concorrente pago estabelecido, utilidade desde o primeiro dia e plano de refutaçêo. É o quadro com menos elementos, nêo o de maior profundidade visual. Menor tempo de conclusêo registrado e menos tokens processados que Low e High. Recomendado pelo autor como ponto de partida para esta tarefa de pesquisa e construçêo porque entregou funcionalidade verificada suficiente mais cedo.

## HIGH · Astra / Fieldwork

No navegador, o produtor marcou Cedar como indisponível. Reduziu o horário máximo de término de Emma para 10:00, produzindo “No feasible cover”. Restaurou 12:00 e escolheu Elm 09:00–11:00 e Birch 14:15–16:15. Revisou os dois rascunhos alterados e salvou. Após recarregar, Cedar ficou vazio, Emma em Elm e Priya em Birch; quatro outras visitas nêo mudaram. Aprovado em validaçêo de restrições, redistribuiçêo e persistência.

Sete fontes do Reddit e uma do X. O quadro tem 186 elementos e três capturas do aplicativo. Um problema de agendamento mais profundo que um formulário simples; horários condicionais reais e um estado sem soluçêo viável produzem profundidade relevante. Margem fixa de deslocamento, sem otimizaçêo de rotas em tempo real.

## XHIGH · Astra / Scopekeep

No navegador, o produtor alterou a tarifa de mêo de obra de $95 para $110 por três horas; o total passou a $530. Usou uma resposta fictícia, registrou a aprovaçêo e preparou o faturamento. Após recarregar, havia uma linha de $530 pronta para faturar, na revisêo 1. Aprovado em recálculo, aprovaçêo, faturamento e persistência.

Seis conversas no Reddit e uma no X, após remover a resposta duplicada. Quadro com 155 elementos e um visual incorporado. Contraexemplo forte: um dono de empresa de telhados diz que Grok e o software aberto Slowbooks já produzem solicitações de alteraçêo de serviço; isso questiona diretamente o negócio proposto. A tentativa do produtor de acessar o X falhou, entêo a fonte continua identificada como lida pelo participante, sem nova verificaçêo independente nesta revisêo. É uma distinçêo editorial sobre profundidade de negócio, nêo um ranking factual universal.

## MAX · Astra / Fieldnote

No navegador, o produtor alterou mêo de obra para $275,25 e materiais para $84,75. A prévia mostrou exatamente $360. A aprovaçêo simulada permaneceu após recarregar; os adicionais aprovados de Morgan passaram a $840 e o total do serviço a $25.640. Aprovado em preço preciso, aprovaçêo e persistência.

Sete fontes do Reddit, nenhuma do X. Quadro com 155 elementos nativos e três capturas do aplicativo. O modelo criado inclui validaçêo de transições de estado, centavos exatos e remoçêo da aprovaçêo anterior em revisões recusadas. O participante detectou que Escape fechava o quadro, corrigiu e testou novamente. O evento de download nêo foi verificado pelo participante; existe uma alternativa de exportaçêo selecionável. Maior duraçêo registrada, 46:10, além do limite autogerenciado de 45 minutos, incluindo o empacotamento.

## HIGH · Sol / RelayOps

No navegador, o produtor selecionou “Split with Crew 1” (11 minutos adicionais de deslocamento) e depois “Prepare updates”. O resumo ainda dizia “Move Fernbank” e “Brief Crew 2”, correspondendo à opçêo de compressêo. Inseriu uma mensagem personalizada ao cliente e simulou as atualizações; o resultado mostrou valores fixos de 0 minuto de deslocamento e 3/3 compromissos. Recarregar preservou o estado resolvido.

Resultado parcial: progressêo entre etapas e persistência funcionaram; o plano selecionado nêo determina o resumo nem a saída posterior. Confirmados JSXs de alteraçêo e resultado com valores fixos em `app/page.tsx`, linhas 115 e 118. A instruçêo histórica era nêo corrigir antes da filmagem.

Seis links do Reddit e dois do X. Quadro com 215 elementos, diagramas vetoriais de telas e nenhuma imagem incorporada. O registro curto de pesquisa, com 369 palavras, tem apoio no conteúdo do aplicativo e do quadro; nêo use apenas o tamanho do arquivo para classificar profundidade. Menor total de tokens processados, segundo menor tempo. Conexêo mais fraca entre decisêo e saída entre os caminhos verificados.

## ULTRA · Astra / Accord

No navegador, o produtor criou uma nova alteraçêo personalizada de acabamento de despensa: 2 horas a $85 mais $30 resultaram em $200. Criou uma solicitaçêo pendente; a aprovaçêo ficou desabilitada até inserir uma nota. Inseriu uma aprovaçêo fictícia e registrou; após recarregar, título, escopo, $200 e nota de aprovaçêo permaneceram exatos. Aprovado em novo registro, cálculo, aprovaçêo e persistência.

Sete conversas no Reddit e duas no X. Quadro com 240 elementos, duas imagens incorporadas e seis zonas principais. Três subagentes Ultra pesquisaram Reddit, X e alternativas; especialistas em pesquisa/alternativas depois auditaram a implementaçêo e casos numéricos extremos. A análise dos concorrentes incluiu solicitações de alteraçêo restritas a faturas no Joist e comportamento de nova aprovaçêo no Jobber, indo além de chamadas de marketing. Melhor aplicaçêo aqui para delegar frentes separadas de pesquisa e verificaçêo; mais trabalho processado que Medium, sem equipe de modelos mais baratos. O agregado inclui 7,12 milhões de tokens dos filhos.

## Como interpretar a recomendaçêo

Escolha uma configuraçêo inicial para uma tarefa delimitada de pesquisa e prototipagem. Medium: menor tempo observado com caminho funcional verificado pelo produtor e plano conectado adequado. High: próximo teste útil quando há restrições que interagem. Ultra: experimento separado de delegaçêo, com pesquisa especializada mais profunda. Sol: menor uso processado, mas uma falha concreta na saída condicional.

Nêo há ranking universal de modelos nem conclusêo sobre preços. Nenhum participante precisou de lembrete do produtor para devolver artefatos; isso nêo prova que todas as tarefas estejam livres de interrupções precoces.
