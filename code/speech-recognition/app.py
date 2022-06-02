from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
import torch
import os
import librosa
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

## Download the pretrained model
#tokenizer = Wav2Vec2Tokenizer.from_pretrained('facebook/wav2vec2-base-960h')
#model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')
#tokenizer.save_pretrained('./model')
#model.save_pretrained('./model')

cur_dir = os.getcwd()
dir_path = os.path.join(cur_dir, "models")
tokenizer = Wav2Vec2Tokenizer.from_pretrained(dir_path)
model = Wav2Vec2ForCTC.from_pretrained(dir_path)

def transcribe(file):
    audio, rate = librosa.load(file, sr=16000)
    input_values = tokenizer(audio, padding='longest', return_tensors='pt').input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)
    return transcription[0]



@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Data received")
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            transcript = transcribe(file)
    return render_template('index.html', transcript=transcript)


s2t = ''

@app.route("/record", methods=['POST', 'GET'])
def record():
    global s2t
    if request.method == 'POST':
        print('audio received')
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')
        transcription = transcribe('audio.wav')
        s2t = transcription

        return render_template('record.html', request='POST', s2t=s2t)
    
    else:
        return render_template('record.html', s2t=s2t)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0')

