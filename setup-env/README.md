# Instruções de configuração para usar Generative AI no Google Cloud

Esta pasta contém instruções sobre como configurar o Generative AI no Google Cloud.

## Ambientes de notebook

### Colab
Siga as instruções diretamente nos arquivos do notebook (.ipynb) e observe que você precisará executar a célula a seguir para autenticar seu ambiente Colab com sua conta do Google Cloud.

```
from google.colab import auth
auth.authenticate_user()
```

### Vertex AI Workbench
[Vertex AI Workbench](https://cloud.google.com/vertex-ai-workbench) é o ambiente de notebook gerenciado no Google Cloud, que permite criar e personalizar instâncias de notebook. Você não precisa de etapas extras de autenticação.

#### Criando sua instância de notebook no Vertex AI Workbench
Para criar uma instância, siga as [instruções aqui para criar uma instância de notebooks gerenciados pelo usuário](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/create-new). A menos que especificado no notebook, você pode usar as configurações padrão ao criar sua instância de notebook.

#### Usando este repositório no Vertex AI Workbench
Depois de iniciar a instância do notebook, você pode clonar esse repositório em seu ambiente JupyterLab. Para fazer isso, abra um Terminal no JupyterLab. Em seguida, execute o comando abaixo para clonar o repositório em sua instância:

```
git clone https://github.com/GoogleCloudPlatform/generative-ai.git
```

## Biblioteca Python

Instale o SDK do Python mais recente:
```
!pip install google-cloud-aiplatform --upgrade
```

Você precisará inicializar `vertexai` com seu `project_id` e `location`:

```
PROJECT_ID = "id do seu projeto"
LOCAL = "" #ex. us-central1

import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)
```
