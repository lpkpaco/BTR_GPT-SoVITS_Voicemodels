def apiinfer(text, lang, char, url):
    try:
        import requests
    except:
        pass
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
    except:
        pass
    cmd = str(url) + "set_gpt_weights?weights_path=" + str(pathname)
    response = requests.get(cmd)
    if response.status_code == 200:
        print("Changed GPT model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")
def changeSoVITS(pathname, url):
    try:
        import requests
    except:
        pass
    cmd = str(url) + "set_sovits_weights?weights_path=" + str(pathname)
    response = requests.get(cmd)
    if response.status_code == 200:
        print("Changed SoVITS model")
        return("Action completed")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return("Unexpected Error")