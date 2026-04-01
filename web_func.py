
import os
import gradio as gr
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
def start_backend_spaces():
    try:
        import subprocess
        from time import sleep
        import os
        import torch
    except ModuleNotFoundError:
        print("Subprocess and Time modules not found.")
        exit()
    print("Starting backend server. Takes around 30 seconds")
    print("Cuda status: " + str(torch.cuda.is_available()))
    foldername = r"/demo/gpt-sovits/api_v2.py"
    #command = str("python " + foldername + r"\api_v2.py -Xfrozen_modules=off -d cuda -a 127.0.0.1 -p 9880 -c " + foldername + r"\GPT_SoVITS/configs/tts_infer.yaml")
    try: 
        print("Starting")
        backend = subprocess.Popen(["python", foldername, "-p", "9880", "-a", "127.0.0.1"], shell=False, cwd=os.path.dirname(foldername))
        sleep(30)
    except:
        print("Error when trying to start backend inference server")
        exit()
    print(f"Backend inference server started with PID {backend.pid}")