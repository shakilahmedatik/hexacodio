from gtts import gTTS
from playsound import playsound

audio = 'output.mp3'
language = 'en'

f = open("text.txt", "r")
sp = gTTS(f.read(), lang=language, slow=False)
sp.save(audio)
