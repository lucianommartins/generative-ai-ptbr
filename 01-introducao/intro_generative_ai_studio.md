# Introdução à UI do Vertex AI Generative AI Studio

Este guia fornece instruções sobre como usar o Generative AI Studio por meio do console do Google Cloud, sem usar a API ou o Python SDK.

## Vertex AI Generative AI Studio no Google Cloud

[Vertex AI Generative AI Studio](https://cloud.google.com/generative-ai-studio) é uma plataforma baseada em nuvem que permite aos usuários criar e experimentar modelos generativos de IA. A plataforma fornece uma variedade de ferramentas e recursos que facilitam a introdução à IA generativa, mesmo que você não tenha experiência em aprendizado de máquina.

![image](https://storage.googleapis.com/github-repo/img/gen-ai-studio/overview.jpg)

---

## Linguagem
Há duas maneiras de acessar as funcionalidades de linguagem do Generative AI Studio no Google Cloud:

- Clique no botão **ABRIR** na parte inferior da caixa **Idioma** na página Visão geral do Generative AI Studio.
- Clique em **Language** no menu à esquerda, na guia Generative AI Studio.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/open-language.jpg)

Ao clicar, a seguinte página será apresentada.

![Página de linguagem da IA generativa](img/landing.png)

---

## Iniciar

### Criar prompt

Criar Prompt permite criar prompts para tarefas relevantes para seu caso de uso, incluindo geração de código. Para começar, clique no botão **+ TEXT PROMPT** conforme mostrado na imagem abaixo

![Criar prompt](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/click-create-prompt.jpg)

Ao clicar, você será redirecionado para a página seguinte. Você pode passar o mouse ou clicar nos botões **?** para saber mais sobre cada campo e parâmetro. Além disso, a imagem a seguir foi anotada para fornecer uma visão geral rápida da interface.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-annotated.jpg)

Você pode informar o texto de entrada desejado, por exemplo uma pergunta, para o modelo. O modelo fornecerá uma resposta com base em como você estruturou seu prompt. O processo de descobrir e projetar o melhor texto de entrada (prompt) para obter a resposta desejada do modelo é chamado de **Design de Prompt**.

Atualmente, ainda não existe a melhor maneira de projetar os prompts. Geralmente, existem 3 métodos que você pode usar para moldar a resposta do modelo da maneira que desejar.

- **zero-shot prompting** - Este é um método em que o LLM não recebe dados adicionais sobre a tarefa específica que está sendo solicitado a executar. Em vez disso, é fornecido apenas um prompt que descreve a tarefa. Por exemplo, se você deseja que o LLM responda a uma pergunta, basta perguntar "o que é design de prompt?".
- **one-shot prompting** - Este é um método em que o LLM recebe um único exemplo da tarefa que está sendo solicitado a executar. Por exemplo, se você deseja que o LLM escreva um poema, pode fornecer um único poema de exemplo.
- **few-shot prompting** - Este é um método em que o LLM recebe um pequeno número de exemplos da tarefa que está sendo solicitado a executar. Por exemplo, se você deseja que o LLM escreva um artigo de notícias, você pode fornecer alguns artigos de notícias para ler.

Você também pode observar as guias **FREE-FORM** e **STRUCTURED** na imagem acima. Esses são os dois modos que você pode usar ao projetar seu prompt.

- **FREE-FORM** - Este modo fornece uma abordagem fácil para projetar seu prompt. É adequado para prompts pequenos e experimentais sem exemplos adicionais. Você usará isso para explorar o prompt zero-shot.
- **ESTRUTURADO** - Este modo fornece uma abordagem de modelo fácil de usar para o design imediato. Contexto e vários exemplos podem ser adicionados ao prompt neste modo. Isso é especialmente útil para métodos de prompt one-shot e few-shot que você explorará mais tarde.

---

### Modo FREE-FORM

Você tentará o prompt zero-shot no modo **FREE-FORM**. Para iniciar,

- copie "O que é uma galeria de prompt?" para o campo de entrada de prompt
- clique no botão **ENVIAR** no lado direito da página

O modelo responderá a uma definição abrangente do termo galeria de prompt.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-freeform.jpg)

Aqui estão alguns exercícios exploratórios para você explorar.
- ajuste o parâmetro `Token limit` para `1` e clique no botão **ENVIAR**
- ajuste o parâmetro `Token limit` para `1024` e clique no botão **SUBMIT**
- ajuste o parâmetro `Temperatura` para `0,5` e clique no botão **ENVIAR**
- ajuste o parâmetro `Temperatura` para `1.0` e clique no botão **ENVIAR**

Inspecione se como as respostas mudam para alterar os parâmetros?

---

### Modo STRUCTURED

Com o modo **STRUCTURED**, você pode criar prompts de maneiras mais organizadas. Você também pode fornecer **Contexto** e **Exemplos** em seus respectivos campos de entrada. Esta é uma boa oportunidade para aprender os prompts one e few-shot.

Nesta seção, você pedirá ao modelo para completar uma frase. Volte para a janela **Prompt de texto** e
- clique na guia **STRUCTURED** se ainda não tiver
- copie "a cor do céu é" no campo **INPUT**
- clique no botão **ENVIAR** no lado direito da página

Você veria um resultado semelhante ao mostrado na imagem abaixo.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-structured-zero-shot.jpg)

Em vez de completar a frase, o modelo deu uma frase completa como resposta que não era o que queríamos. Você pode tentar influenciar a resposta do modelo com uma solicitação única. Desta vez, você adicionará um exemplo para o modelo basear sua saída.

No campo **Exemplos**,
- copie "a cor da grama é" para o campo **INPUT**
- copie "verde" para o campo **OUTPUT**
- clique no botão **ENVIAR** no lado direito da página.

Agora o modelo responderá para completar a frase.
A resposta deve ser algo semelhante a isso.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-structured-one-shot.jpg)

Parabéns! Você configurou com sucesso a maneira como o modelo produz resposta.

---

Para a próxima tarefa, você usará o modelo para executar a análise de sentimento em uma frase, como determinar se uma crítica de filme é positiva ou negativa. Volte para a janela **Prompt de texto** e
- copie o prompt "Foi uma boa experiência!" para o campo **INPUT**
- clique no botão **ENVIAR** no lado direito da página

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-structured-sentiment-zero-shot.jpg)

Como você pode ver, o modelo não tinha informações suficientes para saber se você estava solicitando uma análise de sentimento. Isso pode ser melhorado fornecendo ao modelo alguns exemplos do que você está procurando.

Tente adicionar estes exemplos conforme mostrado na imagem abaixo:

| **ENTRADA**                       | **SAÍDA**  |
|-----------------------------------|------------|
| Um filme bem feito e divertido    | positivo   |
| Adormeci depois de 10 minutos     | negativo   |
| O filme foi ok                    | neutro     |

e clique no botão **ENVIAR** no lado direito da página

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-structured-sentiment-few-shot.jpg)

O modelo agora responderá da maneira que você queria. Deve responder como **positivo**.

Você também pode salvar o prompt recém-projetado. Para salvar o prompt, clique no botão **SALVAR** e nomeie-o como quiser.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-prompt-save-prompt.jpg)

O prompt salvo aparecerá na guia **MY PROMPTS**.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/my-prompts-saved.jpg)
---

### Criar prompt de chat

Volte para a página **Idioma** e clique no botão **+ CHAT DE TEXTO** para criar um novo prompt de bate-papo.

![Prompt de texto](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/click-create-chat-prompt.jpg)

Você verá a nova página de prompt de chat. É relativamente semelhante à [página de prompt](#new-prompt) pela qual você passou anteriormente.

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-chat-prompt.jpg)

Nesta seção, você adicionará contexto ao chat e permitirá que o modelo responda com base no contexto fornecido. Vamos adicionar esses contextos ao campo **Context**.

- copie esses contextos para o campo **Context**
>> Seu nome é João. <br/>
>> Você é um técnico de suporte de um departamento de TI. <br/>
>> Você só responde com "Você tentou desligar e ligar novamente?" a qualquer dúvida.

- copie "meu computador está tão lento" para o chatbox e
- pressione a tecla **Enter** ou clique no botão enviar mensagem (o botão de seta para a direita)

![imagem](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/prompt-gallery/new-chat-prompt-with-context.jpg)

O modelo consideraria o contexto adicional fornecido e responderia às perguntas dentro das restrições.

## Galeria de prompts

A Galeria de Prompts (*Prompt Gallery* em inglês) permite explorar como modelos generativos de IA podem funcionar para uma variedade de casos de uso. Há uma variedade de tópicos: Resumo, Classificação, Extração, Redação e Ideação de conteúdos para você explorar. Volte para a página **Primeiros passos** e explore-os no seu próprio ritmo.

![Página de idioma da IA generativa](https://storage.googleapis.com/github-repo/img/gen-ai-studio/language/landing.jpg)
