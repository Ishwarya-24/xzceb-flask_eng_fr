from googletrans import Translator

def englishToFrench(englishText):
    translator = Translator()
    frenchText = translator.translate(englishText, dest='fr').text
    return frenchText

def frenchToEnglish(frenchText):
    translator = Translator()
    englishText = translator.translate(frenchText, dest='en').text
    return englishText

