from gTTS import Text_to_speech as TTS  #字串轉語音
from translate import translate as trans #翻譯
import playsound as ps#播放
if __name__ == '__main__':
    text=input("輸入文字:")#這裡為STT
    language=input("選擇語言:")#未來改成選項式
    trans_text=trans(text, language)
    TTS(trans_text,language,"sound")
    ps.playsound("E:/all_language/sound.mp3")