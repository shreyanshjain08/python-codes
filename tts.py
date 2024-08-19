from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    


@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    
    # Convert the text to speech
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Send the audio file to the client
    return send_file(audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(port = 69)
