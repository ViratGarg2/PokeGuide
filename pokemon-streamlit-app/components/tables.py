from tabulate import tabulate
import streamlit as st
from utils.database import fetch_pokemon, fetch_moves, fetch_battles, fetch_items, fetch_ailments, fetch_rivals, fetch_gyms

def display_pokemon_table():
    pokemon_data = fetch_pokemon()
    if pokemon_data:
        st.write("### Pokémon Data")
        st.table(pokemon_data)
    else:
        st.write("No Pokémon data available.")

def display_moves_table():
    moves_data = fetch_moves()
    if moves_data:
        st.write("### Moves Data")
        st.table(moves_data)
    else:
        st.write("No moves data available.")

def display_battles_table():
    battles_data = fetch_battles()
    if battles_data:
        st.write("### Battle Data")
        st.table(battles_data)
    else:
        st.write("No battle data available.")

def display_items_table():
    items_data = fetch_items()
    if items_data:
        st.write("### Items in Bag")
        st.table(items_data)
    else:
        st.write("No items found in the bag.")

def display_ailments_table():
    ailments_data = fetch_ailments()
    if ailments_data:
        st.write("### Ailments and Cures")
        st.table(ailments_data)
    else:
        st.write("No ailments data available.")

def display_rivals_table():
    rivals_data = fetch_rivals()
    if rivals_data:
        st.write("### Rival Trainers")
        st.table(rivals_data)
    else:
        st.write("No rival trainers found.")

def display_gyms_table():
    gyms_data = fetch_gyms()
    if gyms_data:
        st.write("### Gyms Data")
        st.table(gyms_data)
    else:
        st.write("No gym data available.")