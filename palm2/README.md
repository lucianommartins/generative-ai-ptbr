# Generative AI - PaLM2

Bem vindo aos exemplos de código de [Generative AI](https://cloud.google.com/ai/generative-ai/) com o PaLM2.

### Vertex AI PaLM2 API

Na Google Cloud, a Vertex AI PaLM2 API provê acesso para interagir com os modelos baseados no PaLM2. Atualmente há os seguintes modelos disponíveis:

Os nomes de modelos de base têm dois componentes: caso de uso e tamanho do modelo. A convenção de nomenclatura está no formato `<use case>-<model size>`. Por exemplo, `text-bison` representa o modelo de texto Bison.

Os tamanhos do modelo são:

- `Unicorn`: o maior modelo da família PaLM. Os modelos de unicórnio se destacam em tarefas complexas, como codificação e cadeia de pensamento (CoT), devido ao amplo conhecimento incorporado a eles e aos recursos de raciocínio dele.

- `Bison`: o modelo PaLM de melhor valor que processa uma ampla variedade de tarefas de linguagem, como classificação e resumo. Ele é otimizado para precisão e latência a um custo razoável. As interfaces de texto, chat, código e chat de código simplificam a implantação e a integração do aplicativo.

- `Gecko`: modelo menor para tarefas simples.

Você pode usar a versão estável ou mais recente de um modelo. Para mais informações, consulte [Versões e ciclo de vida do modelo](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/model-versioning?hl=pt-br).

Os notebooks e exemplos neste diretórios focam na utilizam da **SDK Python para a Vertex AI** para fazer chamadas a Vertex AI PaLM2 API.
