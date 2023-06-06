from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    french_translation = translator.english_to_french(text_to_translate)
    return f"Translated text, {text_to_translate} to French is {french_translation}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    english_translation = translator.french_to_english(text_to_translate)
    return f"Translated text, {text_to_translate} to English is {english_translation}"

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
