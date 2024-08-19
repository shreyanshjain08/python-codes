from flask import Flask, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Text-to-Speech API. Use /tts to convert text to speech."

@app.route('/tts')
def text_to_speech():
    # text = input("Enter the text you want to convert to speech")
    text= "hello"
    if not text:
        return "No text provided", 400

    # Create a gTTS object and save the audio
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    return send_file("output.mp3", as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
    