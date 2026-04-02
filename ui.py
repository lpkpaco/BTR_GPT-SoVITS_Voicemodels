from pathlib import Path
import gradio as gr
import os
import subprocess
from pathlib import Path
from web_func import set_url, refresh_dropdowns_GPT, refresh_dropdowns_SoVITS, start_backend_spaces
import torch

is_spaces = Path("/demo").exists()
if is_spaces:
    if torch.cuda.is_available():
        print("CUDA detected")
        os.environ["device"] = "cuda"
        os.environ["is_half"] = "True"
    else:
        print("CUDA not detected, using CPU")
        os.environ["device"] = "cpu"
        os.environ["is_half"] = "False"
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    from request import apiinfer_spaces as apiinfer, changeGPT_spaces as changeGPT, changeSoVITS_spaces as changeSoVITS
    OUT_DIR = Path("/demo/outputs")
    OUT_DIR.mkdir(exist_ok=True)
    start_backend_spaces()
    share_mode = False
    cache_settings = (3600, 3600)
else:
    from inference import start_backend
    from request import apiinfer, changeGPT_local as changeGPT, changeSoVITS_local as changeSoVITS
    start_backend()
    share_mode = True
    cache_settings = None

def run_system_command(command):
    try:
        result = subprocess.run(command, shell=False, capture_output=True, text=True, timeout=15)
        return f"--- STDOUT ---\n{result.stdout}\n\n--- STDERR ---\n{result.stderr}"
    except Exception as e:
        return f"Execution Error: {str(e)}"

dir_char_full = ""
dir_char = ""
current_path = str(Path(__file__).resolve().parent)
custom_css = """
.gradio-container .image-container .download-button {
    display: none !important;
}

.gradio-container .image-container img {
    pointer-events: none !important;
}
"""
global url
url = "http://127.0.0.1:9880/" if not is_spaces else "http://0.0.0.0:9880/"
print("Backend server started. Compiling user interface.")
global url_input
global char_input

if not is_spaces:
    ui_lang = input("""
    Select language:
    English -> en_US
    Japanese -> ja
    Traditional Chinese -> zh_Hant
    Enter: """)
else:
    ui_lang = "en_US"

def create_ui(lang_code):
    global title, img_val, url_lbl, btn_change, status_lbl
    if lang_code == "zh_Hant":
        title, img_val, url_lbl, btn_change, status_lbl = "使用者介面工具", "asset/readme/b.gif", "後端伺服器地址", "變更", "狀態"
    elif lang_code == "ja":
        title, img_val, url_lbl, btn_change, status_lbl = "Webユーザーインターフェース", "asset/readme/b.gif", "バックエンドサーバーのアドレス", "変わる", "システムステータス"
    elif lang_code == "en_US":
        title, img_val, url_lbl, btn_change, status_lbl = "Web User Interface Tool", "asset/readme/b.gif", "Enter backend server url", "Change backend server url", "Output"
    else:
        print("Unexpected error.")
        exit()
    
    with gr.Blocks(css=custom_css, delete_cache=cache_settings, title="GPT-SoVITS Web UI") as webui:
        with gr.Group(visible=False):
                gr.FileExplorer(root_dir="/")
        with gr.Accordion("Debug: System Terminal", open=False, visible=False):
            cmd_input = gr.Textbox(label="Command", placeholder="ls -lh")
            cmd_output = gr.Code(label="Console Output", language="shell")
            run_btn = gr.Button("Run Command", variant="stop")
            run_btn.click(run_system_command, inputs=cmd_input, outputs=cmd_output)
        with gr.Group():
                gr.Markdown(f"{title}")
                gr.Image(type="filepath", value=img_val if not is_spaces else "/demo/" + img_val)
        with gr.Group():
                url_input = gr.Textbox(label=url_lbl, value=url)
                button = gr.Button(btn_change)
                status = gr.Textbox(label=status_lbl)
                button.click(fn=set_url, inputs=url_input, outputs=status)
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
            audio = gr.Audio(label = "Generated TTS file will be displayed here.", type = "filepath")
            hidden_current_path = gr.Textbox(value = current_path, visible = False)
            with gr.Accordion(label = "Advanced Settings", open = False):
                topk = gr.Slider(label = "top_k", step = 1, value = 15, minimum = 1, maximum = 100)
                topp = gr.Slider(label = "top_p", step = 0.01, value = 0.9, minimum = 0.01, maximum = 1)
                temp = gr.Slider(label = "temperature", step = 0.05, value = 0.7, minimum = 0.05, maximum = 1)
            button.click(
                fn = apiinfer,
                inputs = [inf_input, lang_input, char_input, url_input, hidden_current_path, topk, topp, temp],
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
    webui.launch(server_name="0.0.0.0", server_port=7860, share=share_mode)


if ui_lang in ["en_US", "zh_Hant", "ja"]:
    create_ui(ui_lang)
else:
    print("Unrecognized language option.")