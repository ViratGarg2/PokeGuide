def format_pokemon_data(pokemon):
    # Format Pokémon data for display
    return {
        "Poke Number": pokemon["Poke_Number"],
        "Poke Name": pokemon["Poke_Name"],
        "Type": pokemon["Type"],
        "Height": pokemon["Height"],
        "Weight": pokemon["Weight"],
        "XP": pokemon["XP"],
        "Level": pokemon["Level"],
    }

def validate_pokemon_input(poke_number, poke_name, height, weight):
    # Validate Pokémon input data
    if not isinstance(poke_number, int) or poke_number <= 0:
        raise ValueError("Poke Number must be a positive integer.")
    if not isinstance(poke_name, str) or not poke_name.strip():
        raise ValueError("Poke Name cannot be empty.")
    if not isinstance(height, (int, float)) or height <= 0:
        raise ValueError("Height must be a positive number.")
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be a positive number.")

def format_move_data(move):
    # Format move data for display
    return {
        "Move Name": move["Move_Name"],
        "Type": move["Type"],
        "Power": move["Power"],
        "Accuracy": move["Accuracy"],
        "PP": move["PP"],
    }

def format_battle_data(battle):
    # Format battle data for display
    return {
        "Battle Number": battle["Battle_Number"],
        "Battle Type": battle["Battle_Type"],
        "Outcome": battle["Outcome"],
        "Date": battle["Date"],
    }

def format_item_data(item):
    # Format item data for display
    return {
        "Item Name": item["Item_Name"],
        "Effect": item["Effect"],
        "Cost": item["Cost"],
        "Count": item["Count"],
    }

def format_ailment_data(ailment):
    # Format ailment data for display
    return {
        "Ailment": ailment["Ail_Name"],
        "Cure": ailment["Item_Name"],
        "Berry": ailment["Berry_Name"],
    }

def format_rival_data(rival):
    # Format rival trainer data for display
    return {
        "Trainer No": rival["Trainer_No"],
        "Name": rival["Name"],
    }

def format_gym_data(gym):
    # Format gym data for display
    return {
        "Location": gym["Location"],
        "Gym Leader": gym["Gym_Leader"],
        "Badge Won": gym["Badge_Won"],
    }