import streamlit as st

def main():
    st.title("Profil utilisateur")
    st.write("Voici votre profil utilisateur.")
    
    # Ajoutez ici le contenu de votre page de profil
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    with col2:
        st.subheader("Informations personnelles")
        st.text_input("Nom", value="Utilisateur")
        st.text_input("Email", value="utilisateur@exemple.com")
        st.button("Mettre à jour le profil")