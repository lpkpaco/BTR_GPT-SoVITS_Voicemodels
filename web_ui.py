import gradio as gr
from inference import start_backend
from request import apiinfer, changeGPT, changeSoVITS
from webbrowser import open as webopen
print("Starting user interface. Importing modules and starting backend inferencing server.")
start_backend()
url = "http://127.0.0.1:9880/"
print("Backend server started. Compiling user interface.")
def set_url(url_value):
    url = url_value
    return ("URL changed to " + url)
with gr.Blocks() as webui:
    with gr.Group():
        global url_input
        url_input = gr.Textbox(label = "Enter backend server url (For default users, do not enter anything.)", value="http://127.0.0.1:9880/")
        button = gr.Button("Change backend server url")
        status = gr.Textbox(label = "Output")
        button.click(fn = set_url, inputs = url_input, outputs=status)
    with gr.Group():
        gr.Markdown("### Generate speech file")
        inf_input = gr.Textbox(label ="Enter text")
        lang_input = gr.Textbox(label = "Enter text language (2-letter code). Use zh for Chinese, ja for Japanese, en for English, etc. (Language must be supported by GPT-SoVITS)")
        char_input = gr.Dropdown(
            choices = ["gotoh", "kita", "nijika"],
            label = "Select character"
        )
        button = gr.Button("Start")
        status = gr.Textbox(label = "Output")
        button.click(
            fn = apiinfer,
            inputs = [inf_input, lang_input, char_input, url_input],
            outputs = status
        )
    with gr.Group():
        gpt_input = gr.Textbox(label = "Enter GPT model full path")
        button = gr.Button("Change GPT model")
        status = gr.Textbox(label = "Output")
        button.click(fn = changeGPT, inputs = [gpt_input, url_input], outputs = status)
    with gr.Group():
        gpt_input = gr.Textbox(label = "Enter SoVITS model full path")
        button = gr.Button("Change SoVITS model")
        status = gr.Textbox(label = "Output")
        button.click(fn = changeSoVITS, inputs = [gpt_input, url_input], outputs = status)
webui.launch(server_name = "0.0.0.0", server_port = 8964)
webopen("localhost:8964")