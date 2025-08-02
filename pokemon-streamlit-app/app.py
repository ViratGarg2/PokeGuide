import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="PokéGuide",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "static", "style.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Additional CSS overrides for text contrast
    st.markdown("""
        <style>
        /* Force proper text colors throughout the app */
        .main .block-container {
            color: #2c3e50 !important;
        }
        
        /* Fix any remaining dark text on dark backgrounds */
        .stTabs [data-baseweb="tab"] * {
            color: #ecf0f1 !important;
        }
        
        .stTabs [aria-selected="true"] * {
            color: white !important;
        }
        
        /* Ensure form elements have proper contrast */
        .stForm label {
            color: #2c3e50 !important;
        }
        
        /* Fix expander text */
        .streamlit-expanderHeader {
            color: #ecf0f1 !important;
        }
        
        .streamlit-expanderContent {
            color: #2c3e50 !important;
        }
        
        /* Fix all text in white backgrounds */
        .stTabs [data-baseweb="tab-panel"],
        .stForm,
        .custom-container {
            color: #2c3e50 !important;
        }
        
        /* Fix button text */
        .stButton button {
            color: white !important;
        }
        
        /* Fix dataframe text */
        .stDataFrame table {
            color: #2c3e50 !important;
        }
        
        .stDataFrame th {
            color: #ecf0f1 !important;
        }
        
        /* Fix metric text */
        .stMetric {
            color: #2c3e50 !important;
        }
        
        /* Fix any remaining text elements */
        div[data-testid="stMarkdownContainer"] {
            color: #2c3e50 !important;
        }
        
        /* Ensure success/error messages are white text */
        .stSuccess, .stError, .stWarning, .stInfo {
            color: white !important;
        }
        
        .stSuccess *, .stError *, .stWarning *, .stInfo * {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

load_css()

# Custom header with improved contrast
st.markdown("""
    <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                border-radius: 20px; margin-bottom: 30px; border: 3px solid #1a252f; box-shadow: 0 10px 30px rgba(0,0,0,0.4);">
        <h1 style="color: #ecf0f1; font-size: 4em; text-shadow: 3px 3px 6px rgba(0,0,0,0.8); 
                   font-family: 'Courier New', monospace; margin: 0; letter-spacing: 3px;">
            ⚡ POKÉGUIDE ⚡
        </h1>
        <p style="color: #f39c12; font-size: 1.4em; font-weight: bold; margin: 15px 0; 
                  text-shadow: 2px 2px 4px rgba(0,0,0,0.6);">
            🎮 Your Ultimate Pokémon Management System 🎮
        </p>
    </div>
""", unsafe_allow_html=True)

# Main navigation tabs with enhanced styling
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔥 Pokémon", "⚡ Moves", "⚔️ Battles", "🎒 Bag", "🩹 Ailments", "👥 Rivals", "🏟️ Gyms"
])

# Import all the page functions
from pages.pokemon import run_pokemon_page
from pages.moves import run_moves_page
from pages.battles import run_battles_page
from pages.bag import run_bag_page
from pages.ailments import run_ailments_page
from pages.rivals import run_rivals_page
from pages.gyms import run_gyms_page

# Tab content
with tab1:
    run_pokemon_page()

with tab2:
    run_moves_page()

with tab3:
    run_battles_page()

with tab4:
    run_bag_page()

with tab5:
    run_ailments_page()

with tab6:
    run_rivals_page()

with tab7:
    run_gyms_page()

# Footer with enhanced styling and better contrast
st.markdown("""
    <div style="text-align: center; padding: 25px; margin-top: 50px; 
                background: linear-gradient(45deg, #2c3e50, #34495e); 
                border-radius: 15px; border: 2px solid #1a252f; box-shadow: 0 8px 25px rgba(0,0,0,0.3);">
        <p style="color: #ecf0f1; font-weight: bold; margin: 0; font-size: 1.1em; 
                  text-shadow: 2px 2px 4px rgba(0,0,0,0.6);">
            🎮 Made with ❤️ for Pokémon Trainers | Built with Streamlit ⚡
        </p>
        <p style="color: #f39c12; font-size: 0.9em; margin: 5px 0 0 0; 
                  text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
            Gotta catch 'em all! 🌟
        </p>
    </div>
""", unsafe_allow_html=True)