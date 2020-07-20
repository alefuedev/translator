from translate import Translator

location = 'whrite here the location of the file'

with  open(location)as poem:
    translator = Translator(to_lang='ja')
    translation = translator.translate(poem.readline(50))
    print(translation)
