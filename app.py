from flask import Flask, render_template
from googletrans import Translator

app = Flask(__name__)
ts = Translator()

@app.route('/trans/<word>')
def translate(word):
    txt = ts.translate(word, dest='hi')
    return '<h1> translated word: {}</h1>'.format(txt.text)