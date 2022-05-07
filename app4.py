#pip install googletrans==3.1.0a0
from googletrans import Translator
translator = Translator()
translation = translator.translate("你好", dest='id')
print(translation.text)
