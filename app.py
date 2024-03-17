from flask import Flask, render_template, request, redirect, url_for, send_file
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    language = request.form['language']
    voice = 'com.apple.speech.synthesis.voice.Zarvox' if language == 'urdu' else 'com.apple.speech.synthesis.voice.Alex'

    engine.setProperty('voice', voice)
    engine.save_to_file(text, 'static/output.mp3')
    engine.runAndWait()

    return redirect(url_for('result', language=language))

@app.route('/result')
def result():
    language = request.args.get('language')
    return render_template('result.html', language=language)

@app.route('/download')
def download():
    return send_file('static/output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
