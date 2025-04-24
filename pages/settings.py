import streamlit as st

def main():
    st.title("Paramètres")
    st.write("Configurez vos paramètres ici.")
    
    # Ajoutez ici le contenu de votre page de paramètres
    st.subheader("Préférences d'affichage")
    st.checkbox("Mode sombre")
    st.checkbox("Notifications")
    
    st.subheader("Confidentialité")
    st.radio("Visibilité du profil", ["Public", "Privé", "Contacts uniquement"])
    
    st.button("Enregistrer les paramètres")