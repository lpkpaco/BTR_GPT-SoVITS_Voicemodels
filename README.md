# BTR GPT-SoVITS Voicemodels
![BTR_logo](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Bocchi_the_Rock%21_logo.svg/2560px-Bocchi_the_Rock%21_logo.svg.png)
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
#### - Hitori Gotoh: **あ。えっーと。い、1年生の後藤一人です。あ、あの、初めまして。**
<video src="https://github.com/user-attachments/assets/e447a0e4-9a3c-452f-84fb-303309d6e953"></video>

#### - Ikuyo Kita: **よろしくお願いします！キタちゃんと呼んでくださいよ！**
<video src="https://github.com/user-attachments/assets/7d0dc1d0-8e0a-45e6-b743-c4f44bbd4190"></video>

#### - Nijika Ichiji: **おはよう!今日も頑張ります。よし、いくよ！** 
<video src="https://github.com/user-attachments/assets/8cb644c4-f74c-4408-b7b6-4be92995cdcc"></video>

## List of available models
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
#### v4 models
  - kita-v1
    - kita-v1-0-1

<img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/9/92/Nijika_Ijichi_Character_Design_2.png/revision/latest?cb=20220915114343" width="82" height="300">
 
### Nijika Ichiji
#### v2ProPlus models
- nijika-v1-0-1
#### v4 models
  - nijika-v1
    - nijika-v1-0-2

 <img src="https://static.wikia.nocookie.net/bocchi-the-rock/images/4/4a/Ryo_Yamada_Character_Design_2.png/revision/latest?cb=20220915114345" width="82" height="300">
 
### Ryo Yamada
  ~~- ryo-v1 (To be released)~~

### Installation
#### For Windows users
To use this model, please download the [GPT-SoVITS repository](https://github.com/RVC-Boss/GPT-SoVITS).\
Download the models you wish to use, as well as the characters' corresponding reference audio file.\
Copy the model files into the corresponding GPT-SoVITS directories (i.e. .ckpt into SoVITS model folders and .pth into GPT model folders)\
**Remember to match the model versions (v4 models into folders labelled v4, etc.)**\
Start webui.bat (Default language is simplified Chinese. Edit the file by replacing zh_CN with en_US).\
Go to the inference page .\
Select the models you wish to use. Upload the reference audio as instructed. The reference audio text can be copied from the reference audio file names. (e.g. if the file name is xxxx.wav, then the reference text is xxxx)\
Select __ja__ as the reference audio language\
Input the text that you wish to convert to speech. Select the language from the drop-down list.\
Click start.

#### For Mac and Linux users
Please refer to the documentation of the GPT-SoVITS directory. Further details will be added in the future.

## Future Work
- [x] Upload a few demos (Pure laziness)
- [x] Finish and publish kita-v1
- [ ] Finish and publish ryo-v1
- [ ] Add update log
- [ ] Add a more detailed description of this project in readme.md
- [ ] Update the Installation section for the new Python scripts
- [ ] Update the models by feeding them with more training data and adjusting parameters
- [ ] Publish a list of recommended parameters tailored for each character when inferencing and generating speech
- [ ] Make a UI for generating voice models
- [ ] Publish to the Release page

***The datasets used for training will not be published (at least for now)***
## Credits
Thanks to all the contributors of the following repository/project, this repository was made possible.
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS), with the main contributors including
	- 花儿不哭
 	- 红血球AE3803
  	- 白菜工厂1145号员工

- [Cloverworks-__Bocchi the Rock!__ Production team](https://en.cloverworks.co.jp/works/btr/)

If you wish to correct this list, please approach me.
