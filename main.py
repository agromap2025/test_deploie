import streamlit as st
import importlib
import os
from streamlit_option_menu import option_menu

# Configuration de la page
st.set_page_config(
    page_title="Application avec Menu",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fonction pour charger dynamiquement les pages
def load_page(page_name):
    try:
        # Importer le module de la page
        module = importlib.import_module(f"pages.{page_name}")
        # Appeler la fonction principale du module
        module.main()
    except ImportError:
        st.error(f"Impossible de charger la page {page_name}. Vérifiez que le fichier pages/{page_name}.py existe.")
    except AttributeError:
        st.error(f"La page {page_name}.py doit contenir une fonction 'main()'.")

# Menu principal dans la barre latérale
with st.sidebar:
    st.title("Navigation")
    
    # Création du menu avec streamlit_option_menu
    selected = option_menu(
        menu_title=None,  # pas de titre pour le menu
        options=["Accueil", "Profil", "Paramètres", "Aide"],  # Noms affichés
        icons=["house", "person", "gear", "question-circle"],  # icônes Bootstrap
        menu_icon="cast",
        default_index=0,
    )
    
    # Mapper les noms affichés aux noms de fichiers
    page_mapping = {
        "Accueil": "home",
        "Profil": "profile",
        "Paramètres": "settings",
        "Aide": "help"
    }
    
    st.write("---")
    st.write("© 2025 AGRO-MAP")

# Charger la page sélectionnée
load_page(page_mapping[selected])