import streamlit as st
import pandas as pd
import joblib 
# pour la musique Netflix
import base64
# pour traduire en français le résumé
from deep_translator import GoogleTranslator

# téléchargement du fichier ML avec beaucoup de colonnes (+/- 8000)
dfimdbML = pd.read_csv('dfimdbML3_V2.csv', sep=",")

#création de nos features avec toutes les lignes et les clonnes encodées
X = dfimdbML.iloc[:, 21:]

# ajout du modèle entrainté 
model4 = joblib.load("modele_reco_V2.joblib")

# création du X_final avec le modèle entrainé + la colonne Titre de film
X_final = X.copy()
X_final["Titre"] = dfimdbML["Title"]
X_final["TitreAnnee"] = dfimdbML["Title"] + " (" + dfimdbML["Year"].astype(str) + ")"
X_final["ID"] = dfimdbML["ID"]

# Tadame de Netflix
def autoplay_audio(filepath: str):
    with open(filepath, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    st.markdown(f"""
        <audio autoplay>
            <source src="data:audio/mpeg;base64,{b64}" type="audio/mpeg">
        </audio>
    """, unsafe_allow_html=True)

autoplay_audio("Netflix.mp3")

# Streamlit : création du site
# Pour une mise en page large
st.set_page_config(layout="wide")
st.image("image_Netflix.webp")
film_choisi = st.selectbox("Indique le film dont tu veux recevoir des recommandations", X_final["TitreAnnee"])
id_film_choisi = X_final.loc[X_final["TitreAnnee"] == film_choisi, "ID"].values[0]
#création des colonnes pour pouvoir centré l'image
col1, col2 = st.columns([1, 3])
with col1:
     # Récupère l'affiche en fonction de l'ID (car titres en doublons et index différents selon les df)
    image = dfimdbML.loc[dfimdbML["ID"] == id_film_choisi, "Poster"].values[0] 
    st.image(image, use_container_width=True)
with col2:
    resume_choix = dfimdbML.loc[dfimdbML["ID"] == id_film_choisi, "Plot"].iloc[0]
    resume_choix_trad = GoogleTranslator(source="en", target="fr").translate(resume_choix)
    st.write(resume_choix_trad)
    


#je ne veux garder que la ligne dont le film est écrit
# .values transforme le df en array numpy, et le drop supprime la colonne titre pour le ML
caracteristique_film_choisi = X_final[X_final["ID"] == id_film_choisi].drop(columns = ["Titre","ID","TitreAnnee"]).values 

# le [1] correpond à l'index des films recommandés, le [0] correspond à la distance depuis le film choisi
# le [0] correcpond au premier crochet du deuxième array
# le [1:] correspond à la liste des films recommandés en excluant le film de départ.
# index_des_reco = (array([[0.        , 2.44948974, 2.44948974, 2.82842712, 2.82842712,
# 2.82842712, 2.82842712, 2.82842712, 2.82842712, 2.82842712,
# 2.82842712]]), array([[  0, 131, 207,  43,  50,  47,  71,  48,   1,  17,  12]]))

index_des_reco = model4.kneighbors(caracteristique_film_choisi)[1][0][1:]

# on filtre les 10 resultats obtenus pour ne garde que les 5 meilleurs notés

top5reco = dfimdbML.loc[index_des_reco,["Title","Year","imdbRating","ID"]].sort_values('imdbRating', ascending = False).head(5)
top5 = top5reco.loc[:,"ID"].values
top5_titre = top5reco.loc[:,"Title"]

st.subheader(f"Comme tu as aimé {film_choisi}, je te recommande : ")
# Créer les tabs avec les titres des films
tabs = st.tabs(top5_titre.tolist())

# CSS pour grossir le texte des onglets
st.markdown("""
    <style>
        button[data-baseweb="tab"] p {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Itérer sur chaque tab et son film correspondant
for tab, titre, id_film in zip(tabs, top5_titre, top5):
    # Récupère toutes les infos en une seule ligne
    film_info = dfimdbML.loc[dfimdbML["ID"] == id_film].iloc[0]
    
    image = film_info["Poster"]
    resume = film_info["Plot"]
    note = film_info["imdbRating"]
    realisateur = film_info["Director"]
    acteurs = film_info["Actors"]
    rated = film_info["Rated"]
    annee = film_info["Year"]
    nomination = film_info["Awards"]
    duree = film_info["Runtime"]
    genre = film_info["Genre"]

    with tab :
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(image, use_container_width=True)
        with col2:
            resume_traduit = GoogleTranslator(source="en", target="fr").translate(resume)
            st.write(resume_traduit)
        with col3:
            genre_traduit = GoogleTranslator(source="en", target="fr").translate(genre)
            st.write(f"🎞️ Genre : {genre_traduit}")
            st.write(f"📅 Année : {annee}")
            st.write(f"⏳ Durée : {duree}")
            st.write(f"🎭 Acteurs : {acteurs}")
            st.write(f"🎬 Réalisateur : {realisateur}")
            st.write(f"⭐ Note : {note}/10")
            st.write(f"🔞 Rated : {rated}")
            if nomination != None:
                nomination_traduit = GoogleTranslator(source="en", target="fr").translate(nomination)
                st.write(f"🏆 Nomination : {nomination_traduit}")
            else : 
                continue
            

