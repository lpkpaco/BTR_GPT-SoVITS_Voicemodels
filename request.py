def apiinfer(text, lang, char, url):
    try:
        import requests
    except ModuleNotFoundError:
        print("Required modules not found.")
    if char == "gotoh":
        audiopath = r"H:\github\BTR_GPT-SoVITS_Voicemodels\models\Hitori_Gotoh\reference_audio\人様の前で演奏できるように毎日6時間練習を続けた結果.wav" #Replace with your full path
        prompt = "人様の前で演奏できるように毎日6時間練習を続けた結果"
    elif char == "kita":
        audiopath = r"H:\github\BTR_GPT-SoVITS_Voicemodels\models\Ikuyo_Kita\reference_audio\でも私、いくら練習しても本当にギター弾けなかったの.wav" #Replace with your full path
        prompt = "でも私、いくら練習しても本当にギター弾けなかったの"
    elif char == "nijika":
        audiopath = r"H:\github\BTR_GPT-SoVITS_Voicemodels\models\Ichiji_Nijika\reference_audio\私、下北沢高校2年、いちちにじか.wav" #Replace with your full path
        prompt = "私、下北沢高校2年、いちちにじか"
    else:
        return("Character not recognised")
    ttsurl = url + "/tts"
    payload = {
        "text": text,                  
        "text_lang": lang,               
        "ref_audio_path": audiopath,         
        "aux_ref_audio_paths": [],    
        "prompt_text": prompt,            
        "prompt_lang": "ja",            
        "top_k": 15,                   
        "top_p": 0.9,                   
        "temperature": 0.9,             
        "text_split_method": "cut0",  
        "batch_size": 1,             
        "batch_threshold": 0.75,      
        "split_bucket": True,         
        "speed_factor":1.0,           
        "streaming_mode": True,     
        "seed": -1,                  
        "parallel_infer": True,       
        "repetition_penalty": 1.5,   
        "sample_steps": 32,           
        "super_sampling": False       
    }
    response = requests.post(ttsurl, json=payload)
    if response.status_code == 200:
        with open(r"output.wav", "wb") as f:
            f.write(response.content)
            f.close()
        print("Audio generated and saved to output.wav")
        return response.content, "Action completed. Saved to output.wav."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeGPT(pathname, url):
    try:
        import requests
    except ModuleNotFoundError:
        pass
    cmd = str(url) + "set_gpt_weights?weights_path=" + str(pathname)
    response = requests.get(cmd, timeout=60)
    if response.status_code == 200:
        print("Changed GPT model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeSoVITS(pathname, url):
    try:
        import requests
    except ModuleNotFoundError:
        pass
    cmd = str(url) + "set_sovits_weights?weights_path=" + str(pathname)
    response = requests.get(cmd, timeout=60)
    if response.status_code == 200:
        print("Changed SoVITS model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")

def changeGPT_local(pathname, url, char, scriptpath):
    try:
        import requests
    except:
        pass
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    cmd = str(url) + "set_gpt_weights?weights_path=" + str(scriptpath) + "/active/" + str(dir_char) + str(pathname)
    response = requests.get(cmd)
    if response.status_code == 200:
        print("Changed GPT model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeSoVITS_local(pathname, url, char, scriptpath):
    try:
        import requests
    except:
        pass
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    cmd = str(url) + "set_sovits_weights?weights_path=" + str(scriptpath) + "/active/" + str(dir_char) + str(pathname)
    response = requests.get(cmd)
    if response.status_code == 200:
        print("Changed SoVITS model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
    
def apiinfer_local(text, lang, char, url, current_path, topk, topp, temp):
    try:
        import requests
        from pydub import AudioSegment
    except ModuleNotFoundError:
        print("Required modules not found.")
    if char == "gotoh":
        audiopath = current_path + "/asset/reference_audio/人様の前で演奏できるように毎日6時間練習を続けた結果.wav"
        prompt = "人様の前で演奏できるように毎日6時間練習を続けた結果"
    elif char == "kita":
        audiopath = current_path + "/asset/reference_audio/でも私、いくら練習しても本当にギター弾けなかったの.wav"
        prompt = "でも私、いくら練習しても本当にギター弾けなかったの"
    elif char == "nijika":
        audiopath = current_path + "/asset/reference_audio/私、下北沢高校2年、いちちにじか.wav"
        prompt = "私、下北沢高校2年、いちちにじか"
    else:
        return("Character not recognised")
    ttsurl = url + "/tts"
    payload = {
        "text": text,                  
        "text_lang": lang,               
        "ref_audio_path": audiopath,         
        "aux_ref_audio_paths": [],    
        "prompt_text": prompt,            
        "prompt_lang": "ja",            
        "top_k": topk,                   
        "top_p": topp,                   
        "temperature": temp,
        "text_split_method": "cut0",  
        "batch_size": 1,             
        "batch_threshold": 0.75,      
        "split_bucket": True,         
        "speed_factor":1.0,           
        "streaming_mode": False,     
        "seed": -1,                  
        "parallel_infer": False,       
        "repetition_penalty": 1.5,   
        "sample_steps": 32,           
        "super_sampling": False       
    }
    response = requests.post(ttsurl, json=payload)
    if response.status_code == 200:
        with open("output.wav", "wb") as f:
            f.write(response.content)
            f.close()
        print("Audio generated and saved to output.wav")
        print("Converting to .mp3 for mobile device encoding...")
        audio = AudioSegment.from_wav("output.wav")
        audio.export("output.mp3", format="mp3")
        return "output.mp3", "Action completed."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
    

def apiinfer_spaces(text, lang, char, url, current_path, topk, topp, temp):
    try:
        import requests
        from pydub import AudioSegment
        import uuid
    except ModuleNotFoundError:
        print("Required modules not found.")
    if char == "gotoh":
        audiopath = current_path + "/asset/reference_audio/人様の前で演奏できるように毎日6時間練習を続けた結果.wav"
        prompt = "人様の前で演奏できるように毎日6時間練習を続けた結果"
    elif char == "kita":
        audiopath = current_path + "/asset/reference_audio/でも私、いくら練習しても本当にギター弾けなかったの.wav"
        prompt = "でも私、いくら練習しても本当にギター弾けなかったの"
    elif char == "nijika":
        audiopath = current_path + "/asset/reference_audio/私、下北沢高校2年、いちちにじか.wav"
        prompt = "私、下北沢高校2年、いちちにじか"
    else:
        return("Character not recognised")
    ttsurl = url + "/tts"
    payload = {
        "text": text,                  
        "text_lang": lang,               
        "ref_audio_path": audiopath,         
        "aux_ref_audio_paths": [],    
        "prompt_text": prompt,            
        "prompt_lang": "ja",            
        "top_k": topk,                   
        "top_p": topp,                   
        "temperature": temp,
        "text_split_method": "cut0",  
        "batch_size": 1,             
        "batch_threshold": 0.75,      
        "split_bucket": True,         
        "speed_factor":1.0,           
        "streaming_mode": False,     
        "seed": -1,                  
        "parallel_infer": False,       
        "repetition_penalty": 1.5,   
        "sample_steps": 32,           
        "super_sampling": False       
    }
    response = requests.post(ttsurl, json=payload)
    if response.status_code == 200:
        uuid_wav = f"{uuid.uuid4().hex}.wav"
        with open(uuid_wav, "wb") as f:
            f.write(response.content)
            f.close()
        audio = AudioSegment.from_wav(uuid_wav)
        print(f"Audio generated and saved to {uuid_wav}")
        uuid_mp3 = f"{uuid.uuid4().hex}.mp3"
        audio.export(uuid_mp3, format="mp3")
        print(f"Converting to .mp3 for mobile device encoding... {uuid_mp3}")
        return uuid_mp3, "Action completed."
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeGPT_spaces(pathname, url, char, scriptpath):
    try:
        import requests
    except:
        pass
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    cmd = str(url) + "set_gpt_weights?weights_path=" + str(scriptpath) + "/active/" + str(dir_char) + str(pathname)
    response = requests.get(cmd, timeout=60)
    if response.status_code == 200:
        print("Changed GPT model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeSoVITS_spaces(pathname, url, char, scriptpath):
    try:
        import requests
    except:
        pass
    if char == "gotoh":
        dir_char = "Hitori_Gotoh/"
    elif char == "kita":
        dir_char = "Ikuyo_Kita/"
    elif char == "nijika":
        dir_char = "Ichiji_Nijika/"
    else:
        return "Error"
    cmd = str(url) + "set_sovits_weights?weights_path=" + str(scriptpath) + "/active/" + str(dir_char) + str(pathname)
    response = requests.get(cmd, timeout=60)
    if response.status_code == 200:
        print("Changed SoVITS model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")