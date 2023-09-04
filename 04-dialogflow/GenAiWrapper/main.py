import os
from vertexai.preview.language_models import ChatModel
from flask import Flask, request, make_response, jsonify

# iniciando a infra do microsserviço
app = Flask(__name__)

# variaveis do ambiente de teste
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './creds.json' # TODO: gerar credenciais
parent='projects/' #TODO adicionar project id


# rota default
@app.route('/')
def index():
    return('Rota default para testes')


@app.route('/warmup')
def warmup():
    # função de warmup
    # TODO: criar uma lógica de warmup mais completo
    return '', 200, {}


# rota de utilização com o Dialogflow
@app.route('/webhook', methods=['GET', 'POST'])
def palmWrapper():
    req = request.get_json(force=True)
    texto = req['text']
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()

    contexto='você é um bot que se chama FlorisBot.\n' \
        'Você só responde sobre assuntos relacionados a flores e floriculturas.\n' \
        'Para os demais assuntos você responde: Desculpe, eu só consigo ajudar com assuntos relacionados à floriculturas.\n' \
        'Gere uma resposta curta e sem bullets.\n'

    prompt=contexto+texto
    resposta = chat.send_message(prompt)
    resposta = {"fulfillment_response": {"messages": [{"text": {"text": [resposta.text]}}], "merge_behavior": "REPLACE"}}
    return resposta

if __name__ == "__main__":
    app.run()
