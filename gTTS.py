from gtts import gTTS
import os
import playsound as ps
def save(sentence, lang, name):
    tts=gTTS(text=sentence, lang=lang)
    tts.save('%s.mp3' % os.path.join("E:/all_language",name))

if __name__ == '__main__':

    save('Cuaca hari ini bagus', 'id', "test_id")
    ps.playsound("E:/all_language/test_id.mp3")


    save('今天天氣很好', 'zh', "test_tw")
    ps.playsound("E:/all_language/test_tw.mp3")



    save('this is a test', 'en', "test_en")
    ps.playsound("E:/all_language/test_en.mp3")

