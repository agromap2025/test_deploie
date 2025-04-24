import streamlit as st

def main():
    st.title("Aide")
    st.write("Besoin d'aide? Consultez notre documentation.")
    
    # Ajoutez ici le contenu de votre page d'aide
    st.subheader("Questions fréquentes")
    
    with st.expander("Comment modifier mon profil?"):
        st.write("Accédez à la page Profil et cliquez sur 'Mettre à jour le profil'.")
    
    with st.expander("Comment changer mes paramètres?"):
        st.write("Accédez à la page Paramètres et modifiez les options selon vos préférences.")
    
    with st.expander("Comment contacter le support?"):
        st.write("Envoyez un email à support@exemple.com")