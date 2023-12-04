# Importer les bibliothèques nécessaires
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import Image


# Définir la fonction pour créer le nuage de mots
def create_wordcloud():
    # Charger l'image de la carte comme masque et inverser les couleurs
    mask = np.array(Image.open("cloud.png"))
    mask = 255 - mask

    try:
        nom = str(nom_selectionne.get())
        with open(f'Voeux/{nom}.txt', 'r', encoding='utf-8') as file:
            text = file.read()

    except:
        nom_selectionne.delete(0, tk.END)
        label_error.config(text="Nom invalide, réessayez.")
        return
    
    # Mot à exclure du nuage
    exclure_mots = ['d', 'du', 'y', "qu'elle", "qu'elles", 'nous', "parce", "s'est", "peu", "qu'ils", "ni", "qu'en", "lequel", "n'est", "parce qu'il", "j'y", "ma", "j'en", "d'un", "eux", "me", "elles", "qu'il", "n'a", "c'", "son", "j'ai", "sais", "sait", "vos", "mon", "lui", "n", "ils", "donc", "si", "d'une", "cet", "c'est", "ses", "on", "ont", "mes", "votre", "celle", 'avons', 'tout', 'sa', 'notre', 'cette', 'où', 'ceux', 'mais', ",", ".", ';', 'avant', 'pas', 'ne', 'tous', 'nos', 'leur', 'alors', 'car', 'dont', 'cela', 'pu', 'qu', 'je', 'j', 'avec', 'leurs', 'quelles', 'quelle', 'à', 'y', 'nà', 'rà', 'là', 'dà', 'dâ', 'nâ', 'â', 'a', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
    # Créer un nuage de mots avec le masque de la carte
    wordcloud = WordCloud(width=mask.shape[1], height=mask.shape[0], background_color='whitesmoke', stopwords=exclure_mots, min_font_size=10, max_words=200, mask=mask, contour_width=4, contour_color='SteelBlue').generate(text)


    # Afficher le nuage de mots avec la carte comme arrière-plan
    plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Voeux de {nom}", style='italic', color='SteelBlue', family='serif', fontsize=30)
    plt.tight_layout(pad=0)
    plt.show()


# Créer la fenêtre principale
root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='marianne.ico'))
root.title("Générateur de nuages Voeux de Présidents")

image1 = tk.PhotoImage(file="Drapeau.png")
w = image1.width()
h = image1.height()
root.geometry(f"{w}x{h}+250+100" )

panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')

panel1.image = image1


# Créer les widgets pour le nom et le bouton
label_nom = tk.Label(root, text="Choisissez un président de la 5ème République :", width=60)
label_nom.pack()

# Liste déroulante des noms de présidents
liste_presidents = ["Valéry Giscard d'Estaing", "François Mitterrand", "Jacques Chirac", "Nicolas Sarkozy", "François Hollande", "Emmanuel Macron"]
nom_selectionne = tk.StringVar()
nom_selectionne.set(liste_presidents[0])
menu_deroulant = tk.OptionMenu(root, nom_selectionne, *liste_presidents)
menu_deroulant.pack()

button_generer = tk.Button(root, text="Générer", command=create_wordcloud, width=60, height=5)
button_generer.pack()

label_nom.place(relx=0.5, rely=0.4, anchor='center')
menu_deroulant.place(relx=0.5, rely=0.5, anchor='center')
button_generer.place(relx=0.5, rely=0.6, anchor='center')



label_error = tk.Label(root, text="", fg="red")
label_error.pack()

# Lancer la fenêtre
root.mainloop()
