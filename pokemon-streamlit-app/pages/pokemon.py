import streamlit as st
from utils.database import (add_new_pokemon, add_pokemon_moves, add_pokemon_type_info, 
                           view_pokemon, read_about_pokemon, release_pokemon)

def run_pokemon_page():
    # Custom header for Pokemon page
    st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(45deg, #ff6b6b, #feca57); 
                    border-radius: 20px; margin-bottom: 30px; border: 3px solid #2c2c54;">
            <h1 style="color: white; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); 
                       font-family: 'Courier New', monospace; margin: 0;">
                🔥 POKÉMON MANAGEMENT 🔥
            </h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced tabs with custom styling
    tab1, tab2, tab3 = st.tabs(["🆕 Add New Pokémon", "🔍 View & Search", "🚪 Release Pokémon"])
    
    with tab1:
        with st.container():
            st.markdown("""
                <div style="background: rgba(255,255,255,0.9); border-radius: 15px; padding: 20px; 
                            border: 2px solid #2c2c54; margin-bottom: 20px;">
                    <h2 style="color: #2c2c54; text-align: center; margin-bottom: 20px;">
                        ⭐ Add Your New Pokémon ⭐
                    </h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Pokemon basic info in a styled container
            with st.expander("📋 Basic Information", expanded=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    poke_number = st.number_input("🔢 Pokémon Number", min_value=1, step=1)
                    poke_name = st.text_input("📝 Pokémon Name", placeholder="Enter Pokémon name")
                    height = st.number_input("📏 Height (m)", min_value=0.0, step=0.1, format="%.1f")
                    weight = st.number_input("⚖️ Weight (kg)", min_value=0.0, step=0.1, format="%.1f")
                    poke_type = st.selectbox("🌟 Type", ["Fire", "Water", "Grass", "Electric", "Rock", "Ground", "Flying", "Psychic", "Bug", "Ghost", "Dark", "Steel", "Fighting", "Poison", "Normal", "Ice", "Dragon", "Fairy"])
                    category = st.text_input("📂 Category", placeholder="e.g., Seed Pokémon")
                
                with col2:
                    xp = st.number_input("💎 XP", min_value=0, step=100)
                    gender = st.selectbox("⚧️ Gender", ["M", "F"])
                    hp = st.number_input("❤️ HP", min_value=1, step=1)
                    level = st.number_input("📊 Level", min_value=1, max_value=100, step=1)
                    special_attack = st.number_input("✨ Special Attack", min_value=0, step=1)
                    attack = st.number_input("⚔️ Attack", min_value=0, step=1)
                    defence = st.number_input("🛡️ Defence", min_value=0, step=1)
                    special_defence = st.number_input("✨ Special Defence", min_value=0, step=1)
                    speed = st.number_input("💨 Speed", min_value=0, step=1)
            
            # Moves section
            with st.expander("🎯 Moves Information", expanded=True):
                col3, col4 = st.columns(2)
                
                with col3:
                    st.markdown("**⚡ Move 1**")
                    move1_name = st.text_input("Move 1 Name", placeholder="e.g., Thunderbolt")
                    move1_type = st.text_input("Move 1 Type", placeholder="e.g., Electric")
                    move1_category = st.text_input("Move 1 Category", placeholder="e.g., Special")
                    move1_power = st.number_input("Move 1 Power", min_value=0, step=1)
                    move1_accuracy = st.number_input("Move 1 Accuracy", min_value=0, max_value=100, step=1)
                    move1_contact = st.selectbox("Move 1 Contact", ["0", "1"])
                    move1_pp = st.number_input("Move 1 PP", min_value=0, step=1)
                
                with col4:
                    st.markdown("**🔥 Move 2**")
                    move2_name = st.text_input("Move 2 Name", placeholder="e.g., Quick Attack")
                    move2_type = st.text_input("Move 2 Type", placeholder="e.g., Normal")
                    move2_category = st.text_input("Move 2 Category", placeholder="e.g., Physical")
                    move2_power = st.number_input("Move 2 Power", min_value=0, step=1)
                    move2_accuracy = st.number_input("Move 2 Accuracy", min_value=0, max_value=100, step=1)
                    move2_contact = st.selectbox("Move 2 Contact", ["0", "1"])
                    move2_pp = st.number_input("Move 2 PP", min_value=0, step=1)
            
            # Type effectiveness
            with st.expander("🔄 Type Effectiveness", expanded=True):
                col5, col6, col7 = st.columns(3)
                
                with col5:
                    strong_against = st.text_input("💪 Strong Against", placeholder="e.g., Water, Flying")
                with col6:
                    weak_against = st.text_input("😵 Weak Against", placeholder="e.g., Ground, Rock")
                with col7:
                    immune_to = st.text_input("🛡️ Immune To", placeholder="e.g., Ground")
            
            # Submit button with enhanced styling
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🎉 Add Pokémon to Team! 🎉", use_container_width=True):
                if poke_name and move1_name and move2_name:
                    try:
                        # Add Pokemon
                        add_new_pokemon(poke_number, poke_name, height, weight, poke_type, category, 
                                      xp, gender, hp, level, special_attack, attack, defence, special_defence, speed)
                        
                        # Add moves
                        move1_data = {
                            'name': move1_name, 'type': move1_type, 'category': move1_category,
                            'power': move1_power, 'accuracy': move1_accuracy, 'contact': move1_contact, 'pp': move1_pp
                        }
                        move2_data = {
                            'name': move2_name, 'type': move2_type, 'category': move2_category,
                            'power': move2_power, 'accuracy': move2_accuracy, 'contact': move2_contact, 'pp': move2_pp
                        }
                        add_pokemon_moves(poke_number, move1_data, move2_data)
                        
                        # Add type info
                        add_pokemon_type_info(poke_number, poke_type, strong_against, weak_against, immune_to)
                        
                        st.success(f"🎊 Congratulations! {poke_name} has joined your team! 🎊")
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"❌ Oops! Something went wrong: {str(e)}")
                else:
                    st.error("⚠️ Please fill in all required fields (Name, Move 1, Move 2)")
    
    with tab2:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.9); border-radius: 15px; padding: 20px; 
                        border: 2px solid #2c2c54; margin-bottom: 20px;">
                <h2 style="color: #2c2c54; text-align: center; margin-bottom: 20px;">
                    👁️ View & Search Your Team 👁️
                </h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Search options with enhanced styling
        search_option = st.selectbox("🔍 Search Options", ["View All", "Search by Name", "Search by Type"])
        
        if search_option == "View All":
            if st.button("📋 Show All My Pokémon!", use_container_width=True):
                try:
                    pokemon_list = view_pokemon()
                    if pokemon_list:
                        st.success(f"🎯 Found {len(pokemon_list)} Pokémon in your team!")
                        st.dataframe(pokemon_list, use_container_width=True)
                    else:
                        st.info("📋 Your team is empty! Add some Pokémon first.")
                except Exception as e:
                    st.error(f"❌ Error loading team: {str(e)}")
        
        elif search_option == "Search by Name":
            pokemon_name = st.text_input("🔍 Enter Pokémon Name", placeholder="e.g., Pikachu")
            if st.button("🎯 Search by Name!", use_container_width=True):
                if pokemon_name:
                    try:
                        results = read_about_pokemon("name", pokemon_name)
                        if results:
                            st.success(f"🎯 Found {pokemon_name}!")
                            st.dataframe(results, use_container_width=True)
                        else:
                            st.info(f"📋 No Pokémon found with name: {pokemon_name}")
                    except Exception as e:
                        st.error(f"❌ Error searching: {str(e)}")
                else:
                    st.warning("⚠️ Please enter a Pokémon name")
        
        elif search_option == "Search by Type":
            pokemon_type = st.text_input("🔍 Enter Pokémon Type", placeholder="e.g., Electric")
            if st.button("🎯 Search by Type!", use_container_width=True):
                if pokemon_type:
                    try:
                        results = read_about_pokemon("type", pokemon_type)
                        if results:
                            st.success(f"🎯 Found {len(results)} {pokemon_type}-type Pokémon!")
                            st.dataframe(results, use_container_width=True)
                        else:
                            st.info(f"📋 No {pokemon_type}-type Pokémon found")
                    except Exception as e:
                        st.error(f"❌ Error searching: {str(e)}")
                else:
                    st.warning("⚠️ Please enter a Pokémon type")
    
    with tab3:
        st.markdown("""
            <div style="background: rgba(255,100,100,0.9); border-radius: 15px; padding: 20px; 
                        border: 2px solid #ff3838; margin-bottom: 20px;">
                <h2 style="color: white; text-align: center; margin-bottom: 20px;">
                    🚪 Release Pokémon 🚪
                </h2>
                <p style="color: white; text-align: center; font-weight: bold;">
                    ⚠️ This action cannot be undone! ⚠️
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        release_option = st.selectbox("🎯 Release by:", ["Name", "Number"])
        
        if release_option == "Name":
            poke_to_release = st.text_input("💔 Enter Pokémon Name to Release", placeholder="e.g., Pikachu")
        else:
            poke_to_release = st.number_input("💔 Enter Pokémon Number to Release", min_value=1, step=1)
        
        if st.button("🚪 Release Pokémon 😢", use_container_width=True):
            if poke_to_release:
                try:
                    if release_pokemon(poke_to_release):
                        st.success(f"✅ {poke_to_release} has been released back to the wild... 🌿")
                        st.info("🕊️ Your Pokémon is now free and happy!")
                    else:
                        st.error("❌ Pokémon not found in your team")
                except Exception as e:
                    st.error(f"❌ Error releasing Pokémon: {str(e)}")
            else:
                st.warning("⚠️ Please enter a Pokémon name or number")

if __name__ == "__main__":
    run_pokemon_page()