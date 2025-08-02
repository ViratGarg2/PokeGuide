from streamlit import selectbox, multiselect, checkbox, text_input

def filter_moves():
    move_type = selectbox("Select Move Type", ["All", "Physical", "Special", "Status"])
    return move_type

def filter_battles():
    battle_type = selectbox("Select Battle Type", ["All", "Gym", "Trainer"])
    outcome = selectbox("Select Outcome", ["All", "Win", "Loss"])
    return battle_type, outcome

def filter_items():
    item_type = multiselect("Select Item Types", ["Pokéballs", "Berries", "Normal Items"])
    return item_type

def filter_pokemon():
    poke_name = text_input("Enter Pokémon Name")
    return poke_name