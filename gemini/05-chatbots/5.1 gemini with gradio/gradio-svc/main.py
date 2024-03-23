import os
import time
import base64
import PIL.Image
import gradio as gr
from io import BytesIO

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import warnings
warnings.simplefilter("ignore", UserWarning)

import vertexai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Image,
    Part
)

PROJECT_ID="lucianomartins-demos-345000"
LOCATION="us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-1.0-pro")
multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

# Image to Base 64 Converter
def image_to_base64(image_path):
    with open(image_path, 'rb') as img:
        encoded_string = base64.b64encode(img.read())
    return encoded_string.decode('utf-8')


# Function that takes User Inputs and displays it on ChatUI
def query_message(history,txt,img):
    if not img:
        history += [(txt,None)]
        return history
    base64 = image_to_base64(img)
    data_url = f"data:image/jpeg;base64,{base64}"
    history += [(f"{txt} ![]({data_url})", None)]
    
# Function that takes User Inputs, generates Response and displays on Chat UI
def llm_response(history,text,img):
    if not img:
        response = model.generate_content(text)
        history += [(None,response.text)]
        return history

    else:
        im = BytesIO()
        img.save(im, format="JPEG")
        im_bytes = im.getvalue()
        img = base64.b64encode(im_bytes)
        response = multimodal_model.generate_content([im_bytes,text])
        history += [(None,response.text)]
        return history

# UI Code
with gr.Blocks() as app:
    with gr.Row():
        image_box = gr.Image(type="pil")
        chatbot = gr.Chatbot(
            scale = 2,
            height=750
        )
    text_box = gr.Textbox(
            placeholder="Digite sua mensagem e tecle enter ou faça o upload de uma imagem",
            container=False,
        )

    btn = gr.Button("Submit")
    clicked = btn.click(query_message,
                        [chatbot,text_box,image_box],
                        chatbot
                        ).then(llm_response,
                                [chatbot,text_box,image_box],
                                chatbot
                                )

app.queue()
app.launch(server_name="0.0.0.0", server_port=7860)