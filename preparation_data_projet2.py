# Librairies à importer
import pandas as pd
import requests
import joblib
from sklearn.neighbors import NearestNeighbors

# 0. Import Dataset Patrick + création colonne ID
lien = "data_patrickV2.csv"
data_patrickV2 = pd.read_csv(lien, sep=",")

# Créer une colonne ID avec juste l'ID sans le lien internet imdb
def creationID(lien):
    lien = lien.replace("http://www.imdb.com/title/", "")
    lien = lien.replace("/?ref_=fn_tt_tt_1", "")
    return lien

data_patrickV2["ID"] = data_patrickV2["movie_imdb_link"].apply(creationID)

# 1. Récupération données API

# Mise au propre des titres de films pour recherche API
# Split du DF pour ne garder que 1000 film max car clé API ne permet de recueillir que 1000 films par jour
# Pour éviter de relancer tout la recherche API à chaque fois, on peut repartir directement du fichier data_API (fin de l'étape 3)

#Partie 1
listeDeFilms_1 = data_patrickV2["movie_imdb_link"]
listeDeFilms_1 = listeDeFilms_1.iloc[:1000]
listeDeFilms_1 = listeDeFilms_1.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_1)) :
  listeDeFilms_1[i] = listeDeFilms_1[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_1)) :
    listeDeFilms_1[x] = listeDeFilms_1[x].replace("/?ref_=fn_tt_tt_1","")
resultats_1 = []

#Partie 2
listeDeFilms_2 = data_patrickV2["movie_imdb_link"]
listeDeFilms_2 = listeDeFilms_2.iloc[1000:2000]
listeDeFilms_2 = listeDeFilms_2.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_2)) :
  listeDeFilms_2[i] = listeDeFilms_2[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_2)) :
    listeDeFilms_2[x] = listeDeFilms_2[x].replace("/?ref_=fn_tt_tt_1","")
resultats_2 = []

#Partie 3
listeDeFilms_3 = data_patrickV2["movie_imdb_link"]
listeDeFilms_3 = listeDeFilms_3.iloc[2000:3000]
listeDeFilms_3 = listeDeFilms_3.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_3)) :
  listeDeFilms_3[i] = listeDeFilms_3[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_3)) :
    listeDeFilms_3[x] = listeDeFilms_3[x].replace("/?ref_=fn_tt_tt_1","")
resultats_3 = []

#Partie 4
listeDeFilms_4 = data_patrickV2["movie_imdb_link"]
listeDeFilms_4 = listeDeFilms_4.iloc[3000:4000]
listeDeFilms_4 = listeDeFilms_4.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_4)) :
  listeDeFilms_4[i] = listeDeFilms_4[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_4)) :
    listeDeFilms_4[x] = listeDeFilms_4[x].replace("/?ref_=fn_tt_tt_1","")
resultats_4 = []

#Partie 5
listeDeFilms_5 = data_patrickV2["movie_imdb_link"]
listeDeFilms_5 = listeDeFilms_5.iloc[4000:5000]
listeDeFilms_5 = listeDeFilms_5.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_5)) :
  listeDeFilms_5[i] = listeDeFilms_5[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_5)) :
    listeDeFilms_5[x] = listeDeFilms_5[x].replace("/?ref_=fn_tt_tt_1","")
resultats_5 = []

#Partie 6
listeDeFilms_6 = data_patrickV2["movie_imdb_link"]
listeDeFilms_6 = listeDeFilms_6.iloc[5000:]
listeDeFilms_6 = listeDeFilms_6.tolist()
#extraire les ID de films
for i in range(len(listeDeFilms_6)) :
  listeDeFilms_6[i] = listeDeFilms_6[i].replace("http://www.imdb.com/title/","")
  for x in range(len(listeDeFilms_6)) :
    listeDeFilms_6[x] = listeDeFilms_6[x].replace("/?ref_=fn_tt_tt_1","")
resultats_6 = []

# 2. Extraction des données de l'API

cle_API = "RENSEIGNER_CLE_API"
# Chaque partie doit être exécutée une par une car la clé API ne couvre que 1000 films/jour

# Récupération des données par API - partie 1 :
resultats_1 = []
for ID in listeDeFilms_1:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_1.append(data)
# Passage en data frame
df_resultat_1 = pd.DataFrame(resultats_1)

# Récupération des données par API - partie 2 :
resultats_2 = []
for ID in listeDeFilms_2:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_2.append(data)
# Passage en data frame
df_resultat_2 = pd.DataFrame(resultats_2)

# Récupération des données par API - partie 3 :
resultats_3 = []
for ID in listeDeFilms_3:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_3.append(data)
# Passage en data frame
df_resultat_3 = pd.DataFrame(resultats_3)

# Récupération des données par API - partie 4 :
resultats_4 = []
for ID in listeDeFilms_4:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_4.append(data)
# Passage en data frame
df_resultat_4 = pd.DataFrame(resultats_4)

# Récupération des données par API - partie 5 :
resultats_5 = []
for ID in listeDeFilms_5:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_5.append(data)
# Passage en data frame
df_resultat_5 = pd.DataFrame(resultats_5)

# Récupération des données par API - partie 6 :
resultats_6 = []
for ID in listeDeFilms_6:
  data = requests.get(f"http://www.omdbapi.com/?apikey={cle_API}&i={ID}").json()
  resultats_6.append(data)
# Passage en data frame
df_resultat_6 = pd.DataFrame(resultats_6)

# 3. Joindre les extractions de l'API avec concat

data_API = pd.concat([df_resultat_1, df_resultat_2, df_resultat_3, df_resultat_4, df_resultat_5, df_resultat_6], ignore_index=True)
data_API.to_csv("data_API_V2.csv", index=False)

# 4. Joindre les deux dataframes avec merge (+ supprimer les lignes en doublon)

lien = "data_API_V2.csv"
data_API = pd.read_csv(lien, sep=",")

# Joindres toutes les données de l'API
datatotal2 = pd.merge(data_patrickV2, data_API, how="inner", left_on="ID", right_on="imdbID")

# Supprimer les lignes en doublon
datatotal2 = datatotal2.drop_duplicates(subset='ID')

# 5. Conserver que les films (supprimer les jeux et séries)

datatotal2 = datatotal2.loc[datatotal2["Type"] == "movie"].copy()

# 6. Choisir les KPI et sélectionnes les colonnes à garder = supprimer les colonnes non utiles

# Suppression colonnes :
# Colonnes supprimées : (2)num_critic_for_reviews, (4)director_facebook_likes, (5)actor_3_facebook_likes, (7)actor_1_facebook_likes, (13)cast_total_facebook_likes, (15)facenumber_in_poster,
# (24)actor_2_facebook_likes, (26)aspect_ratio, (27)movie_facebook_likes, (32)Released, (43)Ratings, (47)imdbID, (48)Type, (49)DVD, (51)Production
# (52)Website, (53)Response, (54)Season, (55)Episode, (56)seriesID, (57)totalSeasons
datatotal2.drop(columns=["director_facebook_likes", "actor_3_facebook_likes", "actor_1_facebook_likes","cast_total_facebook_likes","facenumber_in_poster",
                         "actor_2_facebook_likes","aspect_ratio","movie_facebook_likes","Released","Ratings","imdbID","Type","DVD","Production","Website",
                         "Response","Season","Episode","seriesID","totalSeasons"], axis=1, inplace=True)

# 7. Nettoyer les colonnes

# 7.1 Suppression des colonnes en doublons

dfimdb=datatotal2.drop(columns=['color','director_name','duration','actor_2_name','gross','genres','actor_1_name','movie_title',
                         'num_voted_users','actor_3_name','plot_keywords','num_user_for_reviews','language','country',
                         'content_rating','budget','title_year','imdb_score']).copy()

# 7.2 Cleaning Colonne Rated

dfimdb.loc[dfimdb['Rated'] == 'Passed', 'Rated'] = 'Avant notation'
dfimdb.loc[dfimdb['Rated'] == 'Approved', 'Rated'] = 'Avant notation'
dfimdb.loc[dfimdb['Rated'] == 'Not Rated', 'Rated'] = 'Non évalué'
dfimdb.loc[dfimdb['Rated'] == 'Unrated', 'Rated'] = 'NC-17'
dfimdb.loc[dfimdb['Rated'] == 'TV-MA', 'Rated'] = 'NC-17'
dfimdb.loc[dfimdb['Rated'] == 'M', 'Rated'] = 'NC-17'
dfimdb.loc[dfimdb['Rated'] == 'TV-14', 'Rated'] = 'PG-13'
dfimdb.loc[dfimdb['Rated'] == 'TV-PG', 'Rated'] = 'PG'
dfimdb.loc[dfimdb['Rated'] == 'TV-G', 'Rated'] = 'G'
dfimdb.loc[dfimdb['Rated'] == 'M/PG', 'Rated'] = 'PG'
dfimdb.loc[dfimdb['Rated'] == 'GP', 'Rated'] = 'PG'

# 7.3 Complétion des vides

#remplissage des vide généré par le split des acteurs
dfimdb['Rated']=dfimdb['Rated'].fillna('Non évalué')
dfimdb['Actors']=dfimdb['Actors'].fillna('Non actors')

# 8. Creation du Dataframe machine learning

# Définition des 4 critères pour le data frame "machine learning" = Genre, acteur, director, imdbRating sur les 10 plus proche puis filtré sur le score

# 8.1. Création des colonnes d'encodage

genres_split = dfimdb['Genre'].str.split(",", expand=True).apply(lambda x: x.str.strip())
genre_dummies = pd.get_dummies(genres_split.stack()).groupby(level=0).sum()

dfimdbML = pd.concat([dfimdb, genre_dummies], axis=1)

actors_split = dfimdb['Actors'].str.split(",", expand=True).apply(lambda x: x.str.strip())
actors_dummies = pd.get_dummies(actors_split.stack()).groupby(level=0).sum()

Director_split = dfimdb['Director'].str.split(",", expand=True).apply(lambda x: x.str.strip())
Director_dummies = pd.get_dummies(Director_split.stack()).groupby(level=0).sum()

dfimdbML = pd.concat([dfimdbML, Director_dummies, actors_dummies], axis=1)

# 8.2 Suppression ligne acteur vide
dfimdbML3 = dfimdbML.copy()

# dropna fait car la dernière ligne avait des NaN au niveau des acteurs.
dfimdbML3 = dfimdbML3.drop(columns=['Unnamed: 0_x',"Unnamed: 0_y"])
dfimdbML3 = dfimdbML3.drop(index=5303)

# Export fichier dfimdbML3 pour utilisation dans recos
dfimdbML3.to_csv("dfimdbML3_V2.csv", index=False)

# 8.3 Utilisation NearestNeighbors = the best pour nous! + Streamlit sur autre fichier

#création de nos features avec toutes les lignes et les clonnes encodées
X = dfimdbML3.iloc[:, 21:]

#entrainement du modèle NearestNeighbors avec 11 car le film séléctionné sera toujours dans la liste
model4 = NearestNeighbors(n_neighbors = 11)
model4.fit(X)

# Exportation modèle ML
joblib.dump(model4, 'modele_reco_V2.joblib')