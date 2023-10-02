import streamlit as st
from PIL import Image, ImageFilter

# Fonction pour limiter une valeur à un intervalle spécifié

def constrain(value, lower, upper):

    return min(max(value, lower), upper)
# Définition d'une fonction prenant deux paramètres : une matrice et une image
def convolution(matrix, img):
    # Création d'une nouvelle image ayant la même dimension que l'image d'entrée
    img2 = Image.new('RGB', (img.width, img.height))
    # Boucle sur les pixels de l'image d'entrée (sauf la bordure)
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            # Initialisation des variables pour les canaux R, G et B
            
            rtotal = 0.0
            gtotal = 0.0
            btotal = 0.0
            # Boucle sur les coefficients de la matrice de convolution (3x3)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Calcul de l'indice du pixel correspondant dans l'image d'entrée
                    pixel = img.getpixel((x - i, y - j))
                    # Ajout de la contribution de chaque pixel (pondérée par le coefficient de la matrice) aux totaux pour chaque canal
                    rtotal += pixel[0] * matrix[i + 1][j + 1]
                    gtotal += pixel[1] * matrix[i + 1][j + 1]
                    btotal += pixel[2] * matrix[i + 1][j + 1]
            # Contrainte des valeurs des canaux entre 0 et 255
            rtotal = constrain(rtotal, 0, 255)
            gtotal = constrain(gtotal, 0, 255)
            btotal = constrain(btotal, 0, 255)
            # Création d'une nouvelle couleur à partir des valeurs des canaux
            c = (int(rtotal), int(gtotal), int(btotal))
            # Assignation de la nouvelle couleur au pixel correspondant dans l'image de sortie
            img2.putpixel((x, y), c)
    # Renvoi de l'image de sortie
    return img2

# Titre de l'application Streamlit
st.title("Une application web pour la convolution des images")

# Sélection de l'image à traiter
uploaded_image = st.file_uploader("Téléchargez une image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    # Charger l'image à partir de l'élément uploader
    img = Image.open(uploaded_image)
    
    # Afficher l'image
    st.image(img, caption="Image d'origine", use_column_width=True)
    
    # Sélection de la matrice de convolution
    selected_matrix = st.selectbox("Sélectionnez une matrice de convolution",
                                   ["Matrice 1", "Matrice 2", "Matrice 3", "Matrice 4"])
    
    # Définition des matrices de convolution
    matrices = {
        "Matrice 1": [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]],
        "Matrice 2": [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
        "Matrice 3": [[-1, 2, -1], [0, 0, 0], [-1, 2, -1]],
        "Matrice 4": [[-1, 0, -1], [2, 0, 2], [-1, 0, -1]]
    }
    
    # Appliquer la matrice de convolution sélectionnée
    result_img = convolution(matrices[selected_matrix], img)
    
    # Afficher l'image résultante
    st.image(result_img, caption="Image traitée", use_column_width=True)

