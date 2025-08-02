import streamlit as st
from utils.database import (view_battle_data_filtered, add_new_battle, 
                           get_battle_data, update_xp)

def run_battles_page():
    st.title("⚔️ Battle Management")
    
    # Tabs for different battle operations
    tab1, tab2, tab3 = st.tabs(["View Battle Data", "Add New Battle", "Battle Statistics"])
    
    with tab1:
        st.header("📊 View Battle Data")
        
        # Filter options
        st.subheader("🔍 Filter Options")
        col1, col2 = st.columns(2)
        
        with col1:
            battle_type = st.selectbox("Battle Type", ["All", "Gym", "Normal"])
            outcome = st.selectbox("Outcome", ["All", "Win", "Loss"])
            pokemon_name = st.text_input("Pokémon Name (optional)")
        
        with col2:
            pokemon_type = st.text_input("Pokémon Type (optional)")
            date_start = st.date_input("Start Date (optional)")
            date_end = st.date_input("End Date (optional)")
        
        if st.button("🔍 Apply Filters", use_container_width=True):
            try:
                # Convert "All" to None for database query
                battle_type_filter = None if battle_type == "All" else battle_type.lower()
                outcome_filter = None if outcome == "All" else outcome.lower()
                pokemon_name_filter = pokemon_name if pokemon_name else None
                pokemon_type_filter = pokemon_type if pokemon_type else None
                date_start_filter = str(date_start) if date_start else None
                date_end_filter = str(date_end) if date_end else None
                
                battles = view_battle_data_filtered(
                    battle_type_filter, outcome_filter, pokemon_name_filter, 
                    pokemon_type_filter, date_start_filter, date_end_filter
                )
                
                if battles:
                    st.dataframe(battles, use_container_width=True)
                else:
                    st.info("📋 No battles found with the specified filters")
            except Exception as e:
                st.error(f"❌ Error loading battle data: {str(e)}")
        
        # Load all battles button
        if st.button("🔄 Load All Battles", use_container_width=True):
            try:
                battles = get_battle_data()
                if battles:
                    st.dataframe(battles, use_container_width=True)
                else:
                    st.info("📋 No battles found in database")
            except Exception as e:
                st.error(f"❌ Error loading battles: {str(e)}")
    
    with tab2:
        st.header("➕ Add New Battle")
        
        # Battle basic info
        st.subheader("⚔️ Battle Information")
        col1, col2 = st.columns(2)
        
        with col1:
            battle_id = st.number_input("Battle ID", min_value=1, step=1)
            pokemon_used = st.number_input("Pokémon Number Used", min_value=1, step=1)
            battle_type = st.selectbox("Battle Type", ["gym", "trainer"])
            outcome = st.selectbox("Outcome", ["win", "loss"])
            date = st.date_input("Battle Date")
        
        with col2:
            location = st.text_input("Battle Location")
            if battle_type == "gym":
                gym_leader = st.text_input("Gym Leader Name")
                rival_id = None
            else:
                rival_id = st.number_input("Rival Trainer ID", min_value=1, step=1)
                gym_leader = None
        
        if st.button("⚔️ Add Battle", use_container_width=True):
            if battle_id and pokemon_used and location:
                try:
                    battle_data = {
                        'battle_id': battle_id,
                        'pokemon_used': pokemon_used,
                        'type': battle_type,
                        'outcome': outcome,
                        'date': str(date),
                        'location': location,
                        'gym_leader': gym_leader,
                        'rival_id': rival_id
                    }
                    
                    add_new_battle(battle_data)
                    st.success(f"✅ Battle {battle_id} added successfully!")
                    
                    # Show XP update info
                    new_level, current_xp = update_xp(pokemon_used, outcome)
                    st.info(f"🎯 Pokémon {pokemon_used} updated! New Level: {new_level}, Total XP: {current_xp}")
                    
                except Exception as e:
                    st.error(f"❌ Error adding battle: {str(e)}")
            else:
                st.warning("⚠️ Please fill in all required fields")
    
    with tab3:
        st.header("📈 Battle Statistics")
        
        try:
            battles = get_battle_data()
            if battles:
                # Calculate statistics
                total_battles = len(battles)
                wins = sum(1 for b in battles if b.get('Outcome', '').lower() == 'win')
                losses = total_battles - wins
                win_rate = (wins / total_battles) * 100 if total_battles > 0 else 0
                
                # Display statistics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Total Battles", total_battles)
                with col2:
                    st.metric("Wins", wins)
                with col3:
                    st.metric("Losses", losses)
                with col4:
                    st.metric("Win Rate", f"{win_rate:.1f}%")
                
                # Battle type breakdown
                gym_battles = sum(1 for b in battles if 'gym' in b.get('Battle_Type', '').lower())
                trainer_battles = total_battles - gym_battles
                
                st.subheader("🏟️ Battle Type Breakdown")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Gym Battles", gym_battles)
                with col2:
                    st.metric("Trainer Battles", trainer_battles)
                
            else:
                st.info("📋 No battle data available for statistics")
        except Exception as e:
            st.error(f"❌ Error loading battle statistics: {str(e)}")

if __name__ == "__main__":
    run_battles_page()