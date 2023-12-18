# Como contribuir

Adoraríamos aceitar seus patches e contribuições para este projeto. Há
apenas algumas pequenas diretrizes que você precisa seguir.

## Contributor License Agreement

As contribuições para este projeto devem ser acompanhadas de uma Contributor License Agreement. 
Você (ou seu empregador) retém os direitos autorais de sua contribuição;
isso simplesmente nos dá permissão para usar e redistribuir suas contribuições como
parte do projeto. Acesse <https://cla.developers.google.com/> para ver
seus acordos atuais arquivados ou assinar um novo.

Geralmente, você só precisa enviar um CLA uma vez, portanto, se já tiver enviado um
(mesmo que seja para um projeto diferente), você provavelmente não precisará fazer isso
de novo.

## Checagens de qualidade de código

Todos os notebooks neste projeto são verificados quanto à formatação e estilo, para garantir uma
experiência consistente. Para testar notebooks antes de enviar uma solicitação pull,
você pode seguir estas etapas.

Em um terminal de linha de comando (por exemplo, do Vertex Workbench ou localmente), instale
as ferramentas de análise de código:

```shell
pip3 install --user -U nbqa black flake8 isort pyupgrade git+https://github.com/tensorflow/docs
```

Você terá que incluir o diretório onde a ferramenta foi instalada em seu PATH:

```shell
export PATH="$HOME/.local/bin:$PATH"
```

Defina uma variável com a localização de seu notebook a ser avaliado:

```shell
export notebook="your-notebook.ipynb"
```

Finalmente, execute este bloco de código para verificar se há erros. Cada etapa tentará
corrija automaticamente quaisquer problemas. Se as correções não puderem ser executadas automaticamente,
então você precisará abordá-los manualmente antes de enviar seu PR.

```shell
docker run -v ${PWD}:/setup/app gcr.io/cloud-devrel-public-resources/notebook_linter:latest your_notebook
```

Nota: Apenas submeta um notebook por PR.


## Revisão de código

Todos os envios, incluindo os envios de membros do projeto, exigem revisão. Nós
usamos *pull requests* do GitHub para essa finalidade. Consulte a
[Ajuda do GitHub](https://help.github.com/articles/about-pull-requests/) para mais
informações sobre o uso de *pull requests*.

## Guia de Comunidade

Este projeto segue [as diretrizes de Open Source Community
do Google](https:git//opensource.google/conduct/).

## Guia do contribuidor

Se você é novo na contribuição para código aberto, poderá encontrar informações úteis neste guia do contribuidor.

Você pode seguir estas etapas para contribuir:

1. <b>Fork do repositório oficial.</b> Isso criará uma cópia do repositório oficial em sua própria conta.
2. <b>Sincronize as branches.</b> Isso garantirá que sua cópia do repositório esteja atualizada com as últimas alterações do repositório oficial.
3. <b>Trabalhe no branch dev do seu fork local.</b> É aqui que você fará as alterações no código.
4. <b>Commite suas atualizações no branch de dev do seu fork local.</b> Isso salvará suas alterações em sua cópia do repositório.
5. <b>Envie uma solicitação pull para o branch de dev do repositório oficial.</b> Isso solicitará que suas alterações sejam mescladas no repositório oficial.

![image](https://storage.googleapis.com/github-repo/img/contributing/contributor-guide-diagram.jpg)

Aqui estão algumas coisas adicionais que você deve ter em mente durante o processo:

- <b>Leia [as diretrizes de Open Source Community
do Google](https:git//opensource.google/conduct/).</b> As diretrizes de contribuição fornecerão mais informações sobre o projeto e como contribuir.
- <b>Teste suas alterações.</b> Antes de enviar uma solicitação pull, certifique-se de que suas alterações funcionem conforme o esperado.
- <b>Seja paciente.</b> Pode levar algum tempo para que sua solicitação pull seja revisada e mesclada.
