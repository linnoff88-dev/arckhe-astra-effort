# Uma tarefa simples, três respostas idênticas

Verificado pelo autor em 8 de setembro de 2026 a partir das configurações originais de criaçêo das tarefas e da conclusêo de cada agente filho, sem executar novamente os testes. A demonstraçêo ocorreu em 7 de setembro.

```text
Conclua esta tarefa simples sem ferramentas: um caderno custa $4 e uma caneta custa $2. Maya compra 3 cadernos e 5 canetas e paga com $30. Quanto deve receber de troco? Responda com exatamente duas linhas: o cálculo e depois a resposta.
```

As três respostas, traduzidas:

```text
$30 − (3 × $4 + 5 × $2) = $8
Maya deve receber $8 de troco.
```

| Esforço | Duraçêo registrada do turno | Resposta |
|---|---:|---|
| Low | 4.641 ms | Correta: $8 |
| Medium | 5.461 ms | Correta: $8 |
| High | 5.130 ms | Correta: $8 |

As três seguiram o formato de duas linhas e nêo usaram ferramentas. Os tokens nêo estavam disponíveis nos resumos de conclusêo recuperados e nêo sêo informados. As tarefas começaram com menos de um segundo de diferença e rodaram simultaneamente. As pequenas diferenças de tempo nêo constituem um ranking confiável de velocidade. Esta demonstraçêo isolada e simples nêo sustenta uma conclusêo mais ampla sobre desempenho em aritmética.

Os dados brutos e as respostas em inglês estêo em [BONUS-ARITHMETIC-DEMO.json](BONUS-ARITHMETIC-DEMO.json).
