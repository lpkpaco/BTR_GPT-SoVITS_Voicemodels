# Important Notice
Model files have been fully migrated to this [Hugging Face repository](https://huggingface.co/lpkpaco/BTR_GPT-SoVITS_Voicemodels).\ This repository does not contain any model files but only source codes.
Check the [Installation](#installation) section for guides.

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/lpkpaco/BTR_GPT-SoVITS_Voicemodels)

# Bocchi-The-Rock-GPT-SoVITS-Models
![BTR_logo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Bocchi_the_Rock%21_logo.svg/3840px-Bocchi_the_Rock%21_logo.svg.png)

<img src="asset/readme/b.gif"></img>

Contains text-to-speech voice models of different characters trained from voices from the anime **__"Bocchi the Rock!"__**.

## License 
This repository is licensed under the ***CC BY-NC-SA 4.0*** license. For your information, a short summary of the license is provided [here](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Disclaimer
The contributors to this repository and projects listed in the [Credits](#credits) section bear no liability for any consequences arising from its use. Users are solely responsible for their usage of this repository.

## Description
With the help of the tool provided in this repo: [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS), the .cptk and .pth weight files are fine-tuned to clone the voice of characters in the TV anime series ***Bocchi the Rock!***.

Currently, the released models perform well in generating speech in
- ja

and have acceptable performance in generating speech in
- zh
- en

### Demos (Might not work on mobile devices. Trying viewing from computer or in browser)
#### - Hitori Gotoh: **あ。えっーと。い、1年生の後藤一人です。あ、あの、初めまして。** (gotoh-v1-3-1)
<video src="https://github.com/user-attachments/assets/e447a0e4-9a3c-452f-84fb-303309d6e953"></video>

#### - Ikuyo Kita: **よろしくお願いします！キタちゃんと呼んでくださいよ！** (kita-v1-0-1)
<video src="https://github.com/user-attachments/assets/7d0dc1d0-8e0a-45e6-b743-c4f44bbd4190"></video>

#### - Nijika Ichiji: **おはようございます!  下北沢高校の二年生、いちじにじかです！** (nijika-v1-0-2)
<video src="https://github.com/user-attachments/assets/178bd8e6-aa7a-48ba-92d0-f5db450a38e3"></video>

## Get started

You may refer to [this DeepWiki page](https://deepwiki.com/lpkpaco/BTR_GPT-SoVITS_Voicemodels) with detailed explanations and illustrations for better understanding. Please be reminded that DeepWiki utilizes AI to generate Wiki Pages and can make mistakes. 

The official information and installation guidelines are included below. Please mainly refer to them.

## List of available models

#### Model naming pattern: [character-identifier]-[version]-[subversion]
e.g. gotoh-v1-3 -> Voice model of Hitori Gotoh, version 1.3.1 (better performance than version gotoh-v1-3, which stands for version 1.3)

<img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/9/98/Hitori_Gotoh_Character_Design_2.png/revision/latest?cb=20220915114341" width="82" height="300">

### Hitori Gotoh
#### v2ProPlus models
  - gotoh-v1-3
  	- gotoh-v1-3-1
#### v4 models
  - gotoh-v1
  - gotoh-v1-1
  - gotoh-v1-2
  - gotoh-v1-3
    - gotoh-v1-3-1

 <img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/a/a8/Ikuyo_Kita_Character_Design_2.png/revision/latest?cb=20220915114342" width="82" height="300">
 
### Ikuyo Kita
#### v2ProPlus models
  - kita-v1
    - kita-v1-0-1
#### v4 models
  - kita-v1
    - kita-v1-0-1

<img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/9/92/Nijika_Ijichi_Character_Design_2.png/revision/latest?cb=20220915114343" width="82" height="300">
 
### Nijika Ichiji
#### v2ProPlus models
  - nijika-v1-0-1
  - nijika-v1-1
#### v4 models
  - nijika-v1
    - nijika-v1-0-2

 <img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/4/4a/Ryo_Yamada_Character_Design_2.png/revision/latest?cb=20220915114345" width="82" height="300">
 
### Ryo Yamada
  ~~- ryo-v1 (To be released)~~

### Installation
### Docker
Installing through Docker is the most reliable and convenient way on Windows/Linux. Please check the [Release Page](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/releases) for installation guides and resources.

#### Important
**Downloading model files through Git LFS has been deprecated.**
**Please download through this [Hugging Face repository](https://huggingface.co/lpkpaco/BTR_GPT-SoVITS_Voicemodels). A download script will be provided in the near future.**

### Git clone and Hugging Face
#### For Windows users
**Installing through Docker is the most reliable and convenient way on Windows. Please check the [Release Page](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/releases) for installation guides and resources.**

**Alternative method:**
To use this model, please download the [GPT-SoVITS repository](https://github.com/RVC-Boss/GPT-SoVITS). Please refer to the installation guide of this repository. Remember to get the pretrained models.\
Download the models you wish to use, as well as the characters' corresponding reference audio file.\
**Download the model files through the action/ directory of this [Hugging Face repository](https://huggingface.co/lpkpaco/BTR_GPT-SoVITS_Voicemodels).**
Copy the contents of the whole downloaded active/ directory into the cloned active/ directory of this repository.\
**Remember to match the character names.**\
i.e. Directory structure:
Bocchi-The-Rock-GPT-SoVITS-Models
  -active
    -Hitori_Gotoh
      -gotoh-v1-3-1-e12.ckpt
      -gotoh-v1-3-1-e16.ckpt
      -...
      -gotoh-v1-3-1_e4_s184.pth
      -...
    -Ikuyo_Kita
      -...
    -Ichiji_Nijika
      -...
  -asset
  -docker
  -...
Install [Pytorch](https://pytorch.org/get-started/locally/) and the dependencies in the requirements.txt of this repository.\
Run web_ui.py\
Wait for the service to start on port **7860**\
Go to `localhost:7860` in your browser\
**Firstly, choose the character you wish to use. Then, scroll down and refresh the GPT model list and SoVITS model list. Select the models you want to use for *both* GPT and SoVITS models. Click the buttons to apply the changes.**\
Input the text that you wish to convert to speech. Enter the 2-letter language code (e.g. ja for Japanese, en for English).\
Click start.

#### For macOS users
Please refer to the documentation of the GPT-SoVITS directory and the steps above. Please be reminded that you might encounter compatibility issues.

#### For Linux users
Installing through Docker is the most reliable and convenient way on Linux. Please check the [Release Page](https://github.com/lpkpaco/Bocchi-The-Rock-GPT-SoVITS-Models/releases) for installation guides and resources.

## Future Work
- [x] Upload a few demos (Pure laziness)
- [x] Finish and publish kita-v1
- [ ] Finish and publish ryo-v1
- [X] Add update log
- [ ] Add a more detailed description of this project in readme.md
- [x] Update the Installation section for the new Python scripts
- [ ] Update the models by feeding them with more training data and adjusting parameters
- [ ] Publish a list of recommended parameters tailored for each character when inferencing and generating speech
- [x] Make a UI for generating voice models
- [ ] Publish to the Release page
- [X] Add a requirements.txt
- [X] ~~Hugging Face Model Download Script~~ Docker Image release
- [ ] FAQ section

***The datasets used for training will not be published (at least for now)***

## Changelog
##### 2026-03-27
- Migrated all model files to HF and deprecated Git LFS.
- Added Cuda 12.8 support for Docker installation.

##### 2026-03-25
- Added Dockerfile of different versions for building images
- Fixed web_ui_spaces.py
- Added v1.0.0cpu releases containing Docker images and guides

##### 2026-03-24 Added files for Hugging Face Docker Spaces
- Added specific Python scripts to run with HF Docker Spaces.

##### 2026-03-21 - Updated readme.md
- The title is pretty self-explainatory.

##### 2026-03-20 - Hugging Face Migration
- Migrated models of older versions/archived models to the related Hugging Face repository. [https://huggingface.co/lpkpaco/BTR_GPT-SoVITS_Voicemodels](https://huggingface.co/lpkpaco/BTR_GPT-SoVITS_Voicemodels)

##### 2026-03-20 - Changelog and Requirements.txt
- Implemented Changelog in readme.md
- Added requirements.txt

Known issue: Unable to download model files stored with GitLFS due to bandwidth quota limitations. Will migrate inactive/archived model files to Hugging Face later to reduce bandwidth usage.

##### 2026-01-22 - Hotfix 2
- Improved readme.md formatting.

##### 2026-01-22 - Hotfix
- Improved readme.md formatting and fixed logo not loading.

##### 2026-01-22 - General Updates
- Added DeepWiki and other badges to readme.md.

##### 2025-12-30 - Advanced TTS Features and UI Improvements
- Added advanced TTS sliders (top_k/top_p/temperature).
- Fixed minor UI text/whitespace and added advanced TTS settings.
- Removed Platform module usage.
- Updated the Future Work section in readme.md.

##### 2025-12-25 - Star History Addition
- Added a section for Star History with a chart.

##### 2025-12-25 - File Uploads
- Added files via upload.

##### 2025-11-25 - README Update
- Updated README.md with general improvements.

##### 2025-09-02 - Code Cleanup and Localization
- Removed unused imports.
- Removed unused module import.
- Added Japanese localisation for web UI.

##### 2025-09-02 - Audio Format Fixes and Compatibility
- Fixed .wav file corruption issue on local machine.
- Added mp3 codec support for mobile users.

##### 2025-09-02 - Repository Merge
- Merged branch 'main' from remote repository.

##### 2025-09-01 - Script and Model Updates
- Updated README.md.
- Updated request.py.
- Updated inference.py.
- Added nijika-v1-1 v2ProPlus models.
- Improved script functionality.

##### 2025-08-31 - Web UI Enhancements and Localization
- Added direct model selection list.
- Created request_webui.py for web UI requests.
- Added traditional Chinese localization for web UI.
- Added audio preview functionality.
- Known issue: When downloading audio file from web UI, no extension name is provided but the audio file works properly after manually adding the extension name .wav for it.
- Updated README.md.

##### 2025-08-31 - Project Restructuring and New Models
- Renamed assets/ -> asset/.
- Added kita-v1-0-1 v2ProPlus models.

##### 2025-08-30 - Initial Setup and Auto-Launch
- Updated README.md (multiple updates).
- Created assets directory.
- Added .bat file to instantly launch script (launch_web_ui.bat).
- Modified web_ui.py to auto-open browser based on operating system (Windows, macOS, Linux).

## Credits
Thanks to all the contributors of the following repositories/projects, this repository was made possible.
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS), with the main contributors including
	- 花儿不哭
 	- 红血球AE3803
  	- 白菜工厂1145号员工

- [Cloverworks-__Bocchi the Rock!__ Production team](https://en.cloverworks.co.jp/works/btr/)

If you wish to correct this list, please approach me.

<img src="asset/readme/a.gif"></img>
