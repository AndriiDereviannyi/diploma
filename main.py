from craft_detection import CRAFT
from ocr import Reader

from gtts import gTTS
import os



""" SETUP """
name = 'sample_food3'
image_path = name + '.jpg'

language = 'en'


""" CRAFT DETECTION """
detected = CRAFT(image_path)

""" OCR """
reader = Reader([language])
result = reader.readtext(detected, detail=0, paragraph=True)
#print(result)

result = ''.join(result)
#print(result)


""" TTS """
tts = gTTS(text=result, lang=language, slow=False)

tts.save(name + '.mp3')

os.system(name + '.mp3')