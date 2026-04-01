import gradio as gr
from request import apiinfer_spaces, changeGPT_spaces, changeSoVITS_spaces
from pathlib import Path
import subprocess
from web_func import set_url, refresh_dropdowns_GPT, refresh_dropdowns_SoVITS, start_backend_spaces
global url
url = "http://0.0.0.0:9880/"
dir_char_full = ""
dir_char = ""
current_path = str(Path(__file__).resolve().parent)
print("Starting user interface. Importing modules and starting backend inferencing server.")
start_backend_spaces()
url = "http://0.0.0.0:9880/"
print("Backend server started. Compiling user interface.")
OUT_DIR = Path("/demo/outputs")
OUT_DIR.mkdir(exist_ok=True)
global url_input
global char_input
custom_css = """
.gradio-container .image-container .download-button {
    display: none !important;
}

.gradio-container .image-container img {
    pointer-events: none !important;
}
"""
def run_system_command(command):
    try:
        result = subprocess.run(command, shell=False, capture_output=True, text=True, timeout=15)
        output = f"--- STDOUT ---\n{result.stdout}\n\n--- STDERR ---\n{result.stderr}"
        return output
    except Exception as e:
        return f"Execution Error: {str(e)}"
with gr.Blocks(delete_cache=(3600, 3600)) as webui:
    with gr.Group(visible=False):
        gr.FileExplorer(root_dir="/")
    with gr.Accordion("Debug: System Terminal", open=False, visible=False):
        gr.Markdown("Run shell commands to inspect the container environment.")
        cmd_input = gr.Textbox(label="Command", placeholder="ls -lh /demo/active/Hitori_Gotoh/")
        cmd_output = gr.Code(label="Console Output", language="shell")
        run_btn = gr.Button("Run Command", variant="stop")
        run_btn.click(run_system_command, inputs=cmd_input, outputs=cmd_output)
    with gr.Group():
        gr.Markdown("Web User Interface Tool")
        gr.Image(type = "filepath", value = "/demo/asset/readme/b.gif")
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
        audio = gr.Audio(label = "Generated TTS file will be displayed here.", type = "filepath")
        hidden_current_path = gr.Textbox(value = current_path, visible = False)
        with gr.Accordion(label = "Advanced Settings", open = False):
            topk = gr.Slider(label = "top_k", step = 1, value = 15, minimum = 1, maximum = 100)
            topp = gr.Slider(label = "top_p", step = 0.01, value = 0.9, minimum = 0.01, maximum = 1)
            temp = gr.Slider(label = "temperature", step = 0.05, value = 0.7, minimum = 0.05, maximum = 1)
        button.click(
            fn = apiinfer_spaces,
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
        button.click(fn = changeGPT_spaces, inputs = [gpt_input, url_input, char_input, hidden_path], outputs = status)
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
        button.click(fn = changeSoVITS_spaces, inputs = [sovits_input, url_input, char_input, hidden_path], outputs = status)
        refresh.click(
            fn = refresh_dropdowns_SoVITS,
            inputs = char_input,
            outputs = sovits_input
        )
webui.launch(server_name = "0.0.0.0", server_port = 7860, share=False)
print("User interface loaded. Please open it in your browser.")