import streamlit as st
from utils.database import read_moves

def run_moves_page():
    st.title("⚡ Moves Management")
    
    st.header("🎯 View Moves")
    
    # Filter options
    filter_option = st.selectbox("Filter by:", ["All Moves", "Move Type", "Pokémon Name"])
    
    if filter_option == "All Moves":
        if st.button("🔄 Load All Moves", use_container_width=True):
            try:
                moves = read_moves()
                if moves:
                    st.dataframe(moves, use_container_width=True)
                else:
                    st.info("📋 No moves found in database")
            except Exception as e:
                st.error(f"❌ Error loading moves: {str(e)}")
    
    elif filter_option == "Move Type":
        move_type = st.text_input("Enter Move Type:")
        if st.button("🔍 Search by Type", use_container_width=True):
            if move_type:
                try:
                    moves = read_moves("move_type", move_type)
                    if moves:
                        st.subheader(f"🎯 Moves of Type: {move_type.title()}")
                        st.dataframe(moves, use_container_width=True)
                    else:
                        st.info(f"📋 No moves found for type: {move_type}")
                except Exception as e:
                    st.error(f"❌ Error searching moves: {str(e)}")
            else:
                st.warning("⚠️ Please enter a move type")
    
    elif filter_option == "Pokémon Name":
        pokemon_name = st.text_input("Enter Pokémon Name:")
        if st.button("🔍 Search by Pokémon", use_container_width=True):
            if pokemon_name:
                try:
                    moves = read_moves("pokemon_name", pokemon_name)
                    if moves:
                        st.subheader(f"🎯 Moves for Pokémon: {pokemon_name.title()}")
                        st.dataframe(moves, use_container_width=True)
                    else:
                        st.info(f"📋 No moves found for Pokémon: {pokemon_name}")
                except Exception as e:
                    st.error(f"❌ Error searching moves: {str(e)}")
            else:
                st.warning("⚠️ Please enter a Pokémon name")

if __name__ == "__main__":
    run_moves_page()