try:
    from request import apiinfer, changeGPT, changeSoVITS
    import torch
    from platform import Path
except:
    print("Missing function. Download the required files.")
    exit()
def start_backend():
    try:
        import subprocess
        from time import sleep
        import os
    except:
        print("Subprocess and Time modules not found.")
        exit()
    print("Cuda status: " + str(torch.cuda.is_available()))
    sleep(3)
    print("Starting backend server. Takes around 30 seconds")
    global url
    global command
    foldername = r"D:\GPT-SoVITS\api_v2.py" #Paste the directory name of the decompressed GPT-SoVITS directory here. Please use full path. (If the folder name is xxx, then enter \xxx)
    url = "http://127.0.0.1:9880/"
    command = str("python " + foldername + r"\api_v2.py -Xfrozen_modules=off -d cuda -a 127.0.0.1 -p 9880 -c " + foldername + r"\GPT_SoVITS/configs/tts_infer.yaml")
    try: 
        print("Starting")
        backend = subprocess.Popen(["python", foldername], shell=False, cwd=os.path.dirname(foldername))
        sleep(30)
    except:
        print("Error when trying to start backend inference server")
        exit()
    print(f"Backend inference server started with PID {backend.pid}")
cmdlist = """
1. Change model (Must perform if this is your first time running the script)
2. Change character (Perform if this script has just been started)
3. Run inference
4. Exit
"""
character = ""
characterlist = """
Hitori Gotoh -> gotoh
Ikuyo Kita -> kita
Nijika Ichiji - > nijika
Ryo Yamada -> ryo

Enter character: 
"""
language = ""
if __name__ == "__main__":
    current_path = str(Path(__file__).resolve().parent)
    while True:
        print(cmdlist)
        resp = str(input("Select action: "))
        if resp == "1":
            gmodelpath = input("Enter the full GPT model path (e.g. D:/GPT-SoVITS/GPT_weights_v4/gotoh-v1-3-1.ckpt): ")
            smodelname = input("Enter the full SoVITS model name (e.g. D:/GPT-SoVITS/SoVITS_weights_v4/gotoh-v1-3-1.pth): ")
            gchange = changeGPT(gmodelpath, url)
            print(gchange)
            schange = changeSoVITS(smodelname, url)
            print(schange)
            continue
        elif resp == "2":
            character = str(input(characterlist))
        elif resp == "3":
            reqtext = input(str("Input the text (This script only supports Japanese for now): "))
            apiresp = apiinfer(reqtext, "ja", character, url, current_path)
            print(apiresp)
            continue
        elif resp == "4":
            exit()
        else:
            print("Unrecognized response")
            continue