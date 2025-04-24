import streamlit as st

def main():
    st.title("Page d'accueil")
    st.write("Bienvenue sur la page d'accueil de l'application!")
    
    # Ajoutez ici le contenu de votre page d'accueil
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.markdown("## Fonctionnalités principales")
    st.write("- Visualisation de données")
    st.write("- Gestion de profil")
    st.write("- Configuration personnalisée")