from gtts import gTTS
import os

text = input("Enter the text you want to convert to speech: ")
if not text:

  tts = gTTS(text=text, lang='en')
  tts.save("output.mp3")