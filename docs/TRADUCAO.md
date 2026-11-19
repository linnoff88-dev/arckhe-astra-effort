# Tradução e termos técnicos

## O que está em português

Guia completo, introdução, dez prompts (individuais e reunidos), tarefa do experimento, condições de execução, oito notas de fontes, revisão do produtor, demonstração aritmética e transcrição do vídeo. Os arquivos `results.pt-BR.json` e `results.pt-BR.csv` traduzem as descrições dos sete resultados, mantendo o esquema e os números originais.

A página pública em `guia/` reúne os materiais e uma leitura HTML do guia completo. Os materiais complementares enviados pelo usuário já estavam em português, exceto a transcrição, agora traduzida.

## O que permanece em inglês

- **Identificadores e comandos:** `low`, `medium`, `high`, `xhigh`, `max`, `ultra`, `reasoning.effort`, `configuration_update`, `/fast`, nomes de campos JSON/CSV, nomes de arquivos e URLs. Traduzir esses valores poderia impedir buscas, execução ou integração.
- **Nomes próprios e produtos:** Astra, Sol, Codex, ChatGPT, Excalidraw, Clearshift, Scopewell, Fieldwork, Scopekeep, Fieldnote, RelayOps, Accord, entre outros.
- **Rótulos das interfaces testadas:** “Split with Crew 1”, “No feasible cover” e similares, para permitir localizar exatamente o comportamento descrito nas capturas e na revisão original.
- **Evidências originais:** PDF, ZIP, imagens, quadros Excalidraw, CSV e JSON brutos e metadados de origem. São registros históricos preservados, com explicações em português nos arquivos adjacentes.
- **Cópia integral descompactada:** `original-en/` mantém o kit em inglês e seu manifesto original, além da transcrição automática recebida.

## Glossário

| Termo preservado | Significado neste material |
|---|---|
| reasoning effort | esforço dedicado ao raciocínio |
| Low / Medium / High | baixo / médio / alto; nomes das configurações |
| Extra High / xhigh | esforço extra alto; rótulo e identificador técnico |
| Max / Ultra | nomes das configurações máximas descritas pelo autor |
| Standard / Fast | modos de velocidade, separados do esforço |
| prompt | instrução ou pedido fornecido ao modelo |
| tokens | unidades de processamento de texto do modelo |
| cached input | entrada reutilizada a partir de cache |
| moat | vantagem competitiva defensável |
| workflow | fluxo de trabalho |
| canvas | quadro visual editável |
| follow-up | acompanhamento ou pedido posterior |
| follow-through | continuidade até concluir a entrega |
| acceptance check | teste de aceitação com resultado observável |
| clean-room comparison | comparação independente, com contextos isolados |
| first attempt | primeira tentativa, preservada antes de correções |
| rollback | reversão de uma alteração |
| diff | comparação das alterações entre versões |

## Dicionário dos resultados

Os cabeçalhos são os mesmos nos arquivos ingleses e portugueses.

| Campo | Leitura em português |
|---|---|
| `key`, `label`, `app` | identificador, nome da configuração e nome do protótipo |
| `time`, `elapsed_seconds` | duração em minutos:segundos e em segundos |
| `input_tokens` | entrada acumulada, incluindo cache |
| `cached_input_tokens` | subconjunto da entrada que veio de cache |
| `output_tokens` | saída acumulada |
| `processed_tokens` | soma de entrada e saída; não representa custo financeiro |
| `cached_share` | percentual da entrada vindo de cache |
| `reddit`, `x` | contagens de conversas nas plataformas |
| `canvas_elements` | quantidade de elementos ativos do quadro |
| `what`, `avatar` | descrição do produto e público-alvo |
| `moat` | hipótese de vantagem competitiva |
| `proved`, `gap`, `takeaway` | verificação observada, lacuna e aprendizado do autor |

Na planilha vazia `experiment/YOUR-RUN-LOG.csv`, `run_id` identifica a execução; `date` e `task` registram data e tarefa; `model`, `effort`, `speed` e `delegation` registram as condições; `start_state` e `attempt` identificam estado inicial e tentativa; `child_tokens` registra uso dos filhos; `acceptance_passed`, `acceptance_failed`, `blockers` e `evidence_path` registram verificações, bloqueios e evidências. `cost_if_verified` só deve ser preenchido se houver custo efetivamente verificável.

## Fidelidade e procedência

A tradução preserva os números e as limitações do experimento. Na prosa em português, ponto separa milhares e vírgula separa decimais; nos arquivos estruturados, os números mantêm a sintaxe original. Nenhum valor monetário foi convertido de moeda.

A primeira pessoa dos textos traduzidos se refere a Mark Kashef, autor original. A transcrição mantém opiniões e aproximações do vídeo; os dados exatos do kit têm prioridade para comparação. O resumo, a planilha e a imagem de referência fornecidos pelo usuário são materiais complementares: afirmações como “tempo médio” ou “melhor custo-benefício” não substituem a medição das primeiras tentativas nem comprovam custo financeiro.

O `MANIFEST.json` da raiz descreve a edição atual e é gerado por `scripts/verify.py --write-manifest`. O manifesto original fica em `original-en/MANIFEST.json`. `source/provenance.json` preserva os hashes da importação anterior à tradução; seu campo `path` descreve o destino naquela importação. Para conferir esses hashes hoje, o verificador usa `original-en/` para o kit e os caminhos originais para `source/` e `files/`.
