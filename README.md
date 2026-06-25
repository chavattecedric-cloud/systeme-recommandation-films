# 🎬 Système de Recommandation de Films

Application de recommandation de films basée sur le Machine Learning (algorithme KNN), enrichie avec les données de l'API OMDB.

### 🚀 Démo en ligne

**[▶️ Tester l'application (Hugging Face Space)](https://huggingface.co/spaces/chavattecedric/systeme-recommandation-films)**

Aucune installation requise : choisis un film et reçois 5 recommandations avec affiches, résumés traduits en français, notes et informations.

---

## 📋 Description

À partir d'un dataset de films, ce projet récupère des données enrichies via l'API OMDB (genre, acteurs, réalisateur, note IMDB, affiche...), puis entraîne un modèle KNN pour recommander 5 films similaires à celui choisi par l'utilisateur.

---

## 📁 Structure du projet

| Fichier | Description |
|---------|-------------|
| `preparation_data_projet2.py` | Préparation des données et entraînement du modèle ML |
| `projet2_V2.py` | Application Streamlit de recommandation |
| `requirements.txt` | Librairies nécessaires |
| `data_patrickV2.csv` | Dataset source |
| `dfimdbML3_V2.csv` | Dataset final après nettoyage (généré) |
| `modele_reco_V2.joblib` | Modèle KNN entraîné (généré) |

> ℹ️ **Note** : les fichiers générés `dfimdbML3_V2.csv` (~85 Mo) et `modele_reco_V2.joblib` (~331 Mo) ne sont pas inclus dans ce dépôt car trop volumineux pour GitHub. Ils sont régénérés en exécutant `preparation_data_projet2.py`.

---

## ⚙️ Comment ça marche ?

### Fichier 1 : `preparation_data_projet2.py`

Ce fichier prépare les données en 8 étapes :

1. **Import du dataset** et création d'une colonne ID à partir des liens IMDB
2. **Récupération des données API** — le dataset est divisé en 6 tranches de 1000 films (limite de 1000 requêtes/jour par clé API OMDB)
3. **Concaténation** des 6 extractions API en un seul DataFrame
4. **Fusion** du dataset original avec les données API via l'ID IMDB
5. **Filtrage** — conservation uniquement des films (suppression des séries et jeux)
6. **Sélection des colonnes** utiles (suppression des colonnes non pertinentes)
7. **Nettoyage** — standardisation de la colonne `Rated`, complétion des valeurs manquantes
8. **Création du DataFrame ML et entrainement du modèle KNN** — encodage des genres, acteurs et réalisateurs en colonnes binaires, export du modèle

⚠️ **Note** : Si vous avez déjà exécuté la partie API, vous pouvez repartir directement du fichier `data_API_V2.csv` à l'étape 4.

### Fichier 2 : `projet2_V2.py`

Application Streamlit qui :
- Charge le dataset final (`dfimdbML3_V2.csv`) et le modèle entraîné (`modele_reco_V2.joblib`)
- Propose un menu de sélection de film (titre + année pour différencier les homonymes)
- Affiche le poster du film choisi
- Recommande 5 films similaires (filtrés parmi les 10 plus proches par note IMDB) et affiche les posters et informations des films

---

## 🚀 Installation et utilisation

### Prérequis

```bash
pip install -r requirements.txt
```

### Étape 1 — Préparer les données

1. Obtenir une clé API gratuite sur [OMDB API](http://www.omdbapi.com/apikey.aspx)
2. Renseigner votre clé dans `preparation_data_projet2.py` :
```python
cle_API = "VOTRE_CLE_API"
```
3. Exécuter le fichier (**attention** : lancer les parties API une par une, 1000 films/jour maximum)

### Étape 2 — Lancer l'application

```bash
streamlit run projet2_V2.py
```

---

## 👥 Auteurs

Projet réalisé par Cédric C., Claire G., Elisa G., Eloïse G.
