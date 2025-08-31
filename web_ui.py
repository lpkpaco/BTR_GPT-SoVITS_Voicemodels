import gradio as gr
from inference import start_backend
from request_webui import apiinfer, changeGPT, changeSoVITS
import os
from pathlib import Path
dir_char_full = ""
dir_char = ""
current_path = str(Path(__file__).resolve().parent)
print("Starting user interface. Importing modules and starting backend inferencing server.")
start_backend()
url = "http://127.0.0.1:9880/"
print("Backend server started. Compiling user interface.")
def list_gpt(char):
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    dir_char = "active/" + dir_char
    GPT_files = [f for f in os.listdir(dir_char) if f.endswith(".ckpt")]
    GPT_files.sort()
    return GPT_files
def list_sovits(char):
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    dir_char = "active/" + dir_char
    SoVITS_files = [f for f in os.listdir(dir_char) if f.endswith(".pth")]
    SoVITS_files.sort()
    return SoVITS_files
def set_url(url_value):
    url = url_value
    return ("URL changed to " + url)
def refresh_dropdowns_GPT(char):
    filelist = list_gpt(char)
    return gr.Dropdown(
        choices = filelist
    )
def refresh_dropdowns_SoVITS(char):
    filelist = list_sovits(char)
    return gr.Dropdown(
        choices = filelist
    )
global url_input
global char_input
ui_lang = input("""
Select language:
English -> en_US
Traditional Chinese -> zh_Hant                

Enter: 
""")
if ui_lang == "en_US":
    with gr.Blocks() as webui:
        with gr.Group():
            gr.Markdown("Web User Interface Tool")
            gr.Image(type = "filepath", value = "asset/readme/b.gif")
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
            hidden_current_path = gr.Textbox(value = current_path, visible = False)
            button.click(
                fn = apiinfer,
                inputs = [inf_input, lang_input, char_input, url_input, hidden_current_path],
                outputs = [audio, status]
            )
        with gr.Group():
            gpt_input = gr.Dropdown(
                choices = [],
                label = "Select GPT model from list"
            )
            refresh = gr.Button("Refresh list")
            button = gr.Button("Change GPT model")
            status = gr.Textbox(label = "Output")
            hidden_path = gr.Textbox(value = current_path, visible = False)
            button.click(fn = changeGPT, inputs = [gpt_input, url_input, char_input, hidden_path], outputs = status)
            refresh.click(
                fn = refresh_dropdowns_GPT,
                inputs = char_input,
                outputs = gpt_input
            )
        with gr.Group():
            sovits_input = gr.Dropdown(
                choices = [],
                label = "Select SoVITS model from list"
            )
            refresh = gr.Button("Refresh list")
            button = gr.Button("Change SoVITS model")
            status = gr.Textbox(label = "Output")
            hidden_path = gr.Textbox(value=current_path, visible=False)
            button.click(fn = changeSoVITS, inputs = [sovits_input, url_input, char_input, hidden_path], outputs = status)
            refresh.click(
                fn = refresh_dropdowns_SoVITS,
                inputs = char_input,
                outputs = sovits_input
            )
    webui.launch(server_name = "0.0.0.0", server_port = 8100, share=True)
    print("User interface loaded. Please open it in your browser.")

elif ui_lang == "zh_Hant":
    with gr.Blocks() as webui:
        with gr.Group():
            gr.Markdown("Web User Interface Tool")
            gr.Image(type = "filepath", value = "asset/readme/b.gif")
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
            gpt_input = gr.Dropdown(
                choices = [],
                label = "從選單中選擇GPT模型"
            )
            refresh = gr.Button("更新模型清單")
            button = gr.Button("變更GPT模型")
            status = gr.Textbox(label = "狀態")
            hidden_path = gr.Textbox(value=current_path, visible=False)
            button.click(fn = changeGPT, inputs = [gpt_input, url_input, char_input, hidden_path], outputs = status)
            refresh.click(
                fn = refresh_dropdowns_GPT,
                inputs = char_input,
                outputs = gpt_input
            )
        with gr.Group():
            sovits_input = gr.Dropdown(
                choices = [],
                label = "從選單中選擇SoVITS模型"
            )
            refresh = gr.Button("更新模型清單")
            button = gr.Button("變更SoVITS模型")
            status = gr.Textbox(label = "狀態")
            hidden_path = gr.Textbox(value=current_path, visible=False)
            button.click(fn = changeSoVITS, inputs = [sovits_input, url_input, char_input, hidden_path], outputs = status)
            refresh.click(
                fn = refresh_dropdowns_SoVITS,
                inputs = char_input,
                outputs = sovits_input
            )
    webui.launch(server_name = "0.0.0.0", server_port = 8100, share=True)
    print("使用者頁面完成加載。請在瀏覽器中打開。")

else:
    print("Unrecognized language option.")
    exit()