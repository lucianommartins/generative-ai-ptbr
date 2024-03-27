
import os
import time
import base64
import gradio as gr

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import warnings
warnings.simplefilter("ignore", UserWarning)

import vertexai
from vertexai.generative_models import (
    GenerativeModel,
    Image
)

# cabeçalho da página
TITLE = """<h1 align="center">Chatbot com Gemini 🤖</h1>"""
SUBTITLE = """<h2 align="center">Protótipo de um chatbot multimodal com Gemini e Gradio</h2>"""

# variaveis de projeto e regiao
PROJECT_ID="lucianomartins-demos-345000" # TODO: atualize para o seu PROJECT_ID
LOCATION="us-central1" # TODO: atualize para o seu REGION

# inicializando a SDK da Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# instanciando os clientes de Gemini e Gemini-Pro
model = GenerativeModel("gemini-1.0-pro")
multimodal_model = GenerativeModel("gemini-1.0-pro-vision")


# converte imagens para formato base64
def image_to_base64(image_path):
    with open(image_path, 'rb') as img:
        encoded_string = base64.b64encode(img.read())
    return encoded_string.decode('utf-8')


# mostra a entrada do usuario no historico do chatbot
def query_message(history,txt,img):
    if not img:
        history += [(txt,None)]
        return history
    print("imagem recebida:")
    print(img)
    base64 = image_to_base64(img)
    data_url = f"data:image/jpeg;base64,{base64}"
    history += [(f"{txt} ![]({data_url})", None)]
    return history
    
# usa o input do usuario, interage com o Gemini, gera resposta 
# e mostra no historico do chatbot
def llm_response(history,text,img):
    if not img:
        response = model.generate_content(text)
        history += [(None,response.text)]
        return history
    else:
        print("imagem no llm_response:")
        print(img)
        try:
            img = Image.load_from_file(img)
            response = multimodal_model.generate_content([text,img])
            print("resposta da chamada de API:")
            print(response.text)
            history += [(None,response.text)]
            return history
        except Exception as e:
            print("deu erro na llm_response")
            print(str(e))
            return history
    
    
# interface do gradio
print("Iniciando a construção da app gradio...")
with gr.Blocks() as app:
    gr.HTML(TITLE)
    gr.HTML(SUBTITLE)
    with gr.Row():
        image_box = gr.Image(type="filepath")
        chatbot = gr.Chatbot(
            scale = 2,
            height=750
        )
        
    text_box = gr.Textbox(
            placeholder="Digite sua mensagem e tecle enter ou faça o upload de uma imagem",
            container=False,
        )

    btn = gr.Button("Enviar")
    clicked = btn.click(query_message,
                        [chatbot,text_box,image_box],
                        chatbot
                        ).then(llm_response,
                                [chatbot,text_box,image_box],
                                chatbot
                                )

app.queue()
app.launch(server_name="0.0.0.0", server_port=7860)
