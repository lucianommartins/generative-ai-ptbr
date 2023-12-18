# A jornada de Generative AI na Google Cloud com Vertex AI

Bem vindo ao repositório com exemplos e cenários de [Generative AI](https://cloud.google.com/ai/generative-ai) na Google Cloud.

<a href="gemini"><img src="https://lh3.googleusercontent.com/eDr6pYKs1tT0iK0nt3pPhvVlP2Wn96fbGqbWgBAARRZ7isej037g_tWobjV8zQkxOsWzJuEH8p-fksczXUOeqxGZZIo_HUCdkn8q-a4fuwATD7Q9Xrs=w2456-l100-sg-rj-c0xffffff" style="width:35em"></a>

Aqui você encontrará notebooks, exemplos de códigos e aplicações de exemplo que demonstrarão como utilizar, desenvolver e gerenciar fluxos de [IA Generativa na Google Cloud](https://cloud.google.com/ai/generative-ai), utilizando a plataforma [Vertex AI](https://cloud.google.com/vertex-ai).

Para mais exemplos de utilização da Vertex AI, visite o repositório oficial [Vertex AI samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples/).

## Estrutura de Diretórios

```
generative-ai-ptbr/
├── gemini/                                     - exemplos com o modelo Gemini
   ├── 01.introducao/                           - notebooks de introdução ao uso do modelo
   ├── 02.usecases/                             - exemplos de casos de uso para indústrias
      ├── 2.1-retail/                           - utilizando o Gemini em cenários de varejo 
      ├── 2.2-education/                        - utilizando o Gemini em cenários de educação
      ├── 2.3-retrieval-augmented-generation/   - cenários de RAG com o Gemini
   ├── 03.function-calling/                     - utilizando funções externas com o Gemini
   ├── 04.responsible-ai/                       - exemplos de análise de vieses
   ├── 05.chatbot/
├── palm2/                                      - exemplos com o modelo PaLM2 
   ├── 01.introducao/                           - notebooks de introdução ao uso do modelo
   ├── 02.linguagem/                            - exemplos utilizando linguagem natural
      ├── 2.1-prompt-design/                    - cenários de prompt design (como extração de informações, Q&A, etc) 
      ├── 2.2-document-summarization/           - cenários de sumarização de texto
   ├── 03.geração_codigo/                       - exemplos utilizando geração de código
   ├── 04.chatbot/                              - exemplo de um chatbot que utiliza as API do PaLM2
└── setup-env/     
```

## Configurando um projeto na Google Cloud
Você precisará de um projeto na Google Cloud para utilizar estes recursos.

1. [Selecione ou crie um projeto na Google Cloud](https://console.cloud.google.com/cloud-resource-manager). Quando você criar sua conta, você terá U$300,00 de créditos para suas atividades iniciais .

2. [Configure uma billing account em seu projeto](https://cloud.google.com/billing/docs/how-to/modify-project).

3. [Ative a API da Vertex AI](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com). 

## Configure seu ambiente Python ou Jupyter
Leia o arquivo README localizado no diretório [setup-env](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/setup-env) sobre informações de como utilizar estes recursos no Google Colab ou diretamente na Vertex AI Workbench.

## Recursos de Generative AI na Google Cloud
Cheque a list de [recursos de Google Generative AI](RESOURCES.md) como páginas oficiais de produtos, documentações, vídeos, cursos gratuitos e mais.

## Contribuindo
Contribuições são super bem vindas! Verifique como em [Contributing Guide](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/CONTRIBUTING.md) no repositório oficial de Google Cloud.

## Buscando ajuda
Por favor use a [página de issues](https://github.com/GoogleCloudPlatform/generative-ai/issues) do repositório oficial de Google Cloud para compartilhar feedbacks ou submeter relatórios de bugs.

## Disclaimer
Esse repositório não é um produto Google oficialmente suportado. Os códigos aqui presentes são puramente para demontração.
