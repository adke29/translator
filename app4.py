from googletrans import Translator
translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='id')
print(translation.text)
