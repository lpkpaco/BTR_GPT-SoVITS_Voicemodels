import gradio as gr
from inference import start_backend
from request import apiinfer, changeGPT, changeSoVITS
from subprocess import run
from platform import system
print("Starting user interface. Importing modules and starting backend inferencing server.")
start_backend()
url = "http://127.0.0.1:9880/"
print("Backend server started. Compiling user interface.")
def set_url(url_value):
    url = url_value
    return ("URL changed to " + url)
global url_input
ui_lang = input("""
Select language:
English -> en_US
Traditional Chinese -> zh_Hant                

Enter: 
""")
if ui_lang == "en_US":
    with gr.Blocks() as webui:
        with gr.Group():
            url_input = gr.Textbox(label = "Enter backend server url (For default users, do not enter anything.)", value="http://127.0.0.1:9880/")
            button = gr.Button("Change backend server url")
            status = gr.Textbox(label = "Output")
            button.click(fn = set_url, inputs = url_input, outputs=status)
        with gr.Group():
            gr.Markdown("### Generate speech file")
            inf_input = gr.Textbox(label ="Enter text")
            lang_input = gr.Textbox(label = "Enter text language (2-letter code). Use ja for Japanese, en for English, zh for Chinese etc. (Language must be supported by GPT-SoVITS)")
            char_input = gr.Dropdown(
                choices = ["gotoh", "kita", "nijika"],
                label = "Select character"
            )
            button = gr.Button("Start")
            status = gr.Textbox(label = "Output")
            audio = gr.Audio(label = "Generated TTS file will be displayed here.")
            button.click(
                fn = apiinfer,
                inputs = [inf_input, lang_input, char_input, url_input],
                outputs = [audio, status]
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
    webui.launch(server_name = "0.0.0.0", server_port = 8964, share=True)
    print("User interface loaded. Please open it in your browser.")

elif ui_lang == "zh_Hant":
    with gr.Blocks() as webui:
        with gr.Group():
            url_input = gr.Textbox(label = "後端伺服器地址（如使用預設設置請勿變更）", value="http://127.0.0.1:9880/")
            button = gr.Button("變更")
            status = gr.Textbox(label = "狀態")
            button.click(fn = set_url, inputs = url_input, outputs=status)
        with gr.Group():
            gr.Markdown("### 生成語音")
            inf_input = gr.Textbox(label ="輸入文本")
            lang_input = gr.Textbox(label = "輸入文本語言。（目前僅支持日語和國語。如為日語，請輸入ja，國語請輸入zh，英語請輸入en）", value="ja")
            char_input = gr.Dropdown(
                choices = ["gotoh", "kita", "nijika"],
                label = "選擇角色"
            )
            button = gr.Button("生成")
            status = gr.Textbox(label = "狀態")
            audio = gr.Audio(label = "生成的語音會展示在此")
            button.click(
                fn = apiinfer,
                inputs = [inf_input, lang_input, char_input, url_input],
                outputs = [audio, status]
            )
        with gr.Group():
            gpt_input = gr.Textbox(label = "輸入GPT模型的full path")
            button = gr.Button("變更GPT模型")
            status = gr.Textbox(label = "狀態")
            button.click(fn = changeGPT, inputs = [gpt_input, url_input], outputs = status)
        with gr.Group():
            gpt_input = gr.Textbox(label = "輸入SoVITS模型的full path")
            button = gr.Button("變更SoVITS模型")
            status = gr.Textbox(label = "狀態")
            button.click(fn = changeSoVITS, inputs = [gpt_input, url_input], outputs = status)
    webui.launch(server_name = "0.0.0.0", server_port = 8964, share=True)
    print("使用者頁面完成加載。請在瀏覽器中打開。")

else:
    print("Unrecognized language option.")
    exit()