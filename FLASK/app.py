# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])

def generate():
    if os.path.exists('static/wordcloud.png'):
      os.remove('static/wordcloud.png') 
    
    filename = request.form['filename']
    with open(f"Voeux/{filename}.txt", 'r', encoding='utf-8') as file:
        text = file.read()

    mask = np.array(Image.open("cloud.png"))
    mask = 255 - mask
    exclure_mots = ['d', 'du', 'y', 'nous', "parce", "parce qu'il", "j'y", "qu'il", "n'a", "c'", "son", "j'ai", "sais", "sait", "vos", "mon", "lui", "n", "ils", "donc", "si", "d'une", "cet", "c'est", "ses", "on", "ont", "mes", "votre", "celle", 'avons', 'tout', 'sa', 'notre', 'cette', 'où', 'ceux', 'mais', ",", ".", ';', 'avant', 'pas', 'ne', 'tous', 'nos', 'leur', 'alors', 'car', 'dont', 'cela', 'pu', 'qu', 'je', 'j', 'avec', 'leurs', 'quelles', 'quelle', 'à', 'y', 'nà', 'rà', 'là', 'dà', 'dâ', 'nâ', 'â', 'a', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
    wordcloud = WordCloud(width=mask.shape[1], height=mask.shape[0], background_color='whitesmoke', stopwords=exclure_mots, min_font_size=10, max_words=200, mask=mask, contour_width=4, contour_color='SteelBlue').generate(text)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('static/wordcloud.png')
    
    president_image = f"Photo/{filename}.jpg"
    return render_template('result.html', president_image=president_image)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
