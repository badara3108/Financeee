import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression  # Example model
from sklearn.linear_model import LinearRegression # Import a regression model

import pickle
data = pd.read_csv('Financial_inclusion_dataset.csv')

#importer les données pretraité
with open('donnees_pre traitees (1).pkl', 'rb') as fichier:
    data = pickle.load(fichier)

# importer le module
with open('modele_enregistre (2).sav', 'rb') as fichier:
    model = pickle.load(fichier)

# Créer l'application Streamlit
st.title("Prédiction de l'inclusion financière")
#Sélectionner les colonnes pour la saisie de l'utilisateur
colonnes_saisie = data.drop('bank_account', axis=1).columns

# Créer des champs de saisie pour chaque colonne
saisie_utilisateur = {}
for colonne in colonnes_saisie:
    saisie_utilisateur[colonne] = st.number_input(f"Entrez la valeur pour {colonne}:")


# Créer un bouton pour effectuer la prédiction
if st.button("Prédire"):
    # Convertir les entrées de l'utilisateur en DataFrame
    saisie_df = pd.DataFrame([saisie_utilisateur])

    # Effectuer la prédiction
    prediction = model.predict(saisie_df)

    # Afficher la prédiction
    st.write(f"Prédiction bank account {prediction[0]}")

    if prediction == 1:
        st.success("Cette personne est susceptible d'avoir un compte bancaire.")
    else:
        st.warning("Cette personne n'est pas susceptible d'avoir un compte bancaire.")