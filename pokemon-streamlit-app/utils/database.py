import pymysql
import pymysql.cursors
from config.database_config import DB_CONFIG

def get_connection():
    return pymysql.connect(**DB_CONFIG)

# Pokemon functions
def add_new_pokemon(poke_number, poke_name, height, weight, poke_type, category, xp, gender, hp, level, special_attack, attack, defence, special_defence, speed):
    """Add a new Pokemon with moves and type information"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                # Insert Pokemon
                query = """
                INSERT INTO Owned_Pokemon 
                (Poke_Number, Poke_Name, Height, Weight, Type, Category, XP, Gender, HP, Level, Special_Attack, Attack, Defence, Special_Defence, Speed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cur.execute(query, (poke_number, poke_name, height, weight, poke_type, category, xp, gender, hp, level, special_attack, attack, defence, special_defence, speed))
                con.commit()
                return True
    except Exception as e:
        raise Exception(f"Error adding Pokemon: {str(e)}")

def add_pokemon_moves(pokemon_number, move1_data, move2_data):
    """Add moves for a Pokemon"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                # Insert Move 1
                query = """
                INSERT INTO Moves (Pokemon_Number, Move_Name, Type, Category, Power, Accuracy, Contact, PP)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """
                cur.execute(query, (pokemon_number, move1_data['name'], move1_data['type'], move1_data['category'], 
                                  move1_data['power'], move1_data['accuracy'], move1_data['contact'], move1_data['pp']))
                
                # Insert Move 2
                cur.execute(query, (pokemon_number, move2_data['name'], move2_data['type'], move2_data['category'], 
                                  move2_data['power'], move2_data['accuracy'], move2_data['contact'], move2_data['pp']))
                con.commit()
    except Exception as e:
        raise Exception(f"Error adding moves: {str(e)}")

def add_pokemon_type_info(pokemon_number, poke_type, strong_against, weak_against, immune_to):
    """Add type information for a Pokemon"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                query = """
                INSERT INTO Poke_Type (Pokemon_Number, Type, Strong_Against, Weak_Against, Immune_To)
                VALUES (%s, %s, %s, %s, %s);
                """
                cur.execute(query, (pokemon_number, poke_type, strong_against, weak_against, immune_to))
                con.commit()
    except Exception as e:
        raise Exception(f"Error adding type info: {str(e)}")

def view_pokemon():
    query = "SELECT * FROM Owned_Pokemon;"
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def read_about_pokemon(filter_type, filter_value):
    """Read about Pokemon with filters"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                if filter_type == "name":
                    query = """
                    SELECT P.Poke_Number, P.Poke_Name, P.Type, P.Category, P.Height, P.Weight, P.Gender, P.XP, P.HP, P.Level, 
                           P.Special_Attack, P.Attack, P.Defence, P.Special_Defence, P.Speed, T.Strong_Against, T.Weak_Against, T.Immune_To
                    FROM Owned_Pokemon P
                    JOIN Poke_Type T ON P.Poke_Number = T.Pokemon_Number
                    WHERE LOWER(P.Poke_Name) = LOWER(%s);
                    """
                    cur.execute(query, (filter_value,))
                elif filter_type == "type":
                    query = """
                    SELECT P.Poke_Number, P.Poke_Name, P.Type, P.Category, P.Height, P.Weight, P.Gender, P.XP, P.HP, P.Level, 
                           P.Special_Attack, P.Attack, P.Defence, P.Special_Defence, P.Speed, T.Strong_Against, T.Weak_Against, T.Immune_To
                    FROM Owned_Pokemon P
                    JOIN Poke_Type T ON P.Poke_Number = T.Pokemon_Number
                    WHERE LOWER(P.Type) LIKE LOWER(%s);
                    """
                    cur.execute(query, (f'%{filter_value}%',))
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error reading Pokemon: {str(e)}")

def release_pokemon(pokemon_identifier):
    query = "DELETE FROM Owned_Pokemon WHERE Poke_Number = %s OR LOWER(Poke_Name) = LOWER(%s);"
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, (pokemon_identifier, pokemon_identifier))
            con.commit()
            return cur.rowcount > 0

# Moves functions
def fetch_moves(move_type=None, pokemon_name=None):
    if move_type:
        query = "SELECT * FROM Moves WHERE LOWER(Type) LIKE LOWER(%s);"
        params = (f'%{move_type}%',)
    elif pokemon_name:
        query = """
        SELECT M.* FROM Moves M
        JOIN Owned_Pokemon P ON M.Pokemon_Number = P.Poke_Number
        WHERE LOWER(P.Poke_Name) = LOWER(%s);
        """
        params = (pokemon_name,)
    else:
        query = "SELECT * FROM Moves;"
        params = ()
    
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()

def read_moves(filter_type=None, filter_value=None):
    """Read moves with different filters"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                if filter_type == "move_type":
                    query = """
                    SELECT Move_Name, Type, Category, Power, Accuracy, Contact, PP
                    FROM Moves WHERE LOWER(Type) LIKE LOWER(%s);
                    """
                    cur.execute(query, (f'%{filter_value}%',))
                elif filter_type == "pokemon_name":
                    query = """
                    SELECT M.Move_Name, M.Type, M.Category, M.Power, M.Accuracy, M.Contact, M.PP
                    FROM Moves M
                    JOIN Owned_Pokemon P ON M.Pokemon_Number = P.Poke_Number
                    WHERE LOWER(P.Poke_Name) = LOWER(%s);
                    """
                    cur.execute(query, (filter_value,))
                else:
                    query = "SELECT Move_Name, Type, Category, Power, Accuracy, Contact, PP FROM Moves;"
                    cur.execute(query)
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error reading moves: {str(e)}")

# Battle functions
def get_battle_data():
    query = "SELECT * FROM Battle;"
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def view_battle_data_filtered(battle_type=None, outcome=None, pokemon_name=None, pokemon_type=None, date_start=None, date_end=None):
    """View battle data with filters"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                query = """
                SELECT B.Battle_Number, B.Battle_Type, B.Pokemon_Used, B.Date, B.Outcome, G.Gym, G.Gym_Leader
                FROM Battle B
                LEFT JOIN Gym_Battle G ON B.Battle_Number = G.Battle_Number
                WHERE 1=1
                """
                params = []
                
                if battle_type and battle_type.lower() != "na":
                    query += " AND LOWER(B.Battle_Type) = %s"
                    params.append(f'{battle_type.lower()} battle')
                
                if outcome and outcome.lower() != "na":
                    query += " AND LOWER(B.Outcome) = %s"
                    params.append(outcome.lower())
                
                if pokemon_name and pokemon_name.lower() != "na":
                    query += " AND B.Pokemon_Used = (SELECT Poke_Number FROM Owned_Pokemon WHERE LOWER(Poke_Name) = %s)"
                    params.append(pokemon_name.lower())
                
                if pokemon_type and pokemon_type.lower() != "na":
                    query += " AND B.Pokemon_Used IN (SELECT Poke_Number FROM Owned_Pokemon WHERE LOWER(Type) LIKE %s)"
                    params.append(f'%{pokemon_type.lower()}%')
                
                if date_start and date_start.lower() != "na":
                    query += " AND B.Date >= %s"
                    params.append(date_start)
                
                if date_end and date_end.lower() != "na":
                    query += " AND B.Date <= %s"
                    params.append(date_end)
                
                cur.execute(query, params)
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error viewing battle data: {str(e)}")

def add_battle(battle_id, pokemon_used, battle_type, outcome, date):
    query = """
    INSERT INTO Battle (Battle_Number, Pokemon_Used, Battle_Type, Outcome, Date)
    VALUES (%s, %s, %s, %s, %s);
    """
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, (battle_id, pokemon_used, battle_type.lower(), outcome.lower(), date))
            con.commit()

def add_new_battle(battle_data):
    """Add a new battle with all related data"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                # Start transaction
                cur.execute("START TRANSACTION")
                
                # Insert into Battle table
                query = """
                INSERT INTO Battle (Battle_Number, Pokemon_Used, Battle_Type, Outcome, Date)
                VALUES (%s, %s, %s, %s, %s);
                """
                cur.execute(query, (battle_data['battle_id'], battle_data['pokemon_used'], 
                                  battle_data['type'], battle_data['outcome'], battle_data['date']))
                
                if battle_data['type'] == 'gym':
                    # Insert into Gym_Battle table
                    query = """
                    INSERT INTO Gym_Battle (Battle_Number, Gym, Gym_Leader)
                    VALUES (%s, %s, %s);
                    """
                    cur.execute(query, (battle_data['battle_id'], battle_data['location'], battle_data['gym_leader']))
                    
                    # Insert into Battling_Gym_Leader table
                    query = """
                    INSERT INTO Battling_Gym_Leader (Battle_Number, Pokemon_Number, Location)
                    VALUES (%s, %s, %s);
                    """
                    cur.execute(query, (battle_data['battle_id'], battle_data['pokemon_used'], battle_data['location']))
                    
                    # Update gym badge if battle was won
                    if battle_data['outcome'] == 'win':
                        query = """
                        UPDATE Pokemon_Gym SET Badge_Won = TRUE WHERE Location = %s;
                        """
                        cur.execute(query, (battle_data['location'],))
                
                else:  # Trainer battle
                    # Insert into Normal_Battle table
                    query = """
                    INSERT INTO Normal_Battle (Battle_Number, Location, Rival_ID)
                    VALUES (%s, %s, %s);
                    """
                    cur.execute(query, (battle_data['battle_id'], battle_data['location'], battle_data['rival_id']))
                    
                    # Insert into Battling_Rival_Trainer table
                    query = """
                    INSERT INTO Battling_Rival_Trainer (Battle_Number, Pokemon_Number, Trainer_No)
                    VALUES (%s, %s, %s);
                    """
                    cur.execute(query, (battle_data['battle_id'], battle_data['pokemon_used'], battle_data['rival_id']))
                
                # Update Pokemon XP
                update_xp(battle_data['pokemon_used'], battle_data['outcome'])
                
                con.commit()
                return True
    except Exception as e:
        con.rollback()
        raise Exception(f"Error adding battle: {str(e)}")

def update_xp(pokemon_id, battle_outcome):
    """Update XP and level of a Pokemon after battle"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                xp_increase = 200 if battle_outcome.lower() == "win" else 100
                
                # Update XP
                query = "UPDATE Owned_Pokemon SET XP = XP + %s WHERE Poke_Number = %s;"
                cur.execute(query, (xp_increase, pokemon_id))
                
                # Get current XP
                query = "SELECT XP FROM Owned_Pokemon WHERE Poke_Number = %s;"
                cur.execute(query, (pokemon_id,))
                current_xp = cur.fetchone()['XP']
                
                # Calculate new level
                new_level = current_xp // 4000
                
                # Update level
                query = "UPDATE Owned_Pokemon SET Level = %s WHERE Poke_Number = %s;"
                cur.execute(query, (new_level, pokemon_id))
                
                con.commit()
                return new_level, current_xp
    except Exception as e:
        raise Exception(f"Error updating XP: {str(e)}")

# Bag functions
def get_items_in_bag(item_type):
    if item_type.lower() == "pokéballs" or item_type.lower() == "pokeballs":
        query = "SELECT Type as Item_Name, Cost, Count, Catch_Rate as Effect FROM Pokeball;"
    elif item_type.lower() == "berries":
        query = "SELECT Berry_Name as Item_Name, Effect, Found_At as Cost, Count FROM Berries;"
    else:  # Normal Items
        query = "SELECT Item_Name, Effect, Cost, Count FROM Normal_Item;"
    
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def view_items_in_bag(item_type):
    """View items in bag with proper formatting"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                if item_type.lower() == "pokeballs":
                    query = "SELECT Type, Cost, Count, Catch_Rate FROM Pokeball;"
                elif item_type.lower() == "berries":
                    query = "SELECT Berry_Name, Effect, Found_At, Count FROM Berries;"
                else:  # Normal Items
                    query = "SELECT Item_Name, Effect, Cost, Count FROM Normal_Item;"
                
                cur.execute(query)
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error viewing items: {str(e)}")

# Ailments functions
def fetch_ailments_and_cures():
    query = "SELECT * FROM Ailment_and_Cure;"
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def read_ailments():
    """Read all ailments and their cures"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                query = "SELECT Berry_Name, Item_Name, Ail_Name FROM Ailment_and_Cure;"
                cur.execute(query)
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error reading ailments: {str(e)}")

def check_cures_for_ailments(ailment):
    """Check cures for specific ailments"""
    try:
        with get_connection() as con:
            with con.cursor(pymysql.cursors.DictCursor) as cur:
                query = """
                SELECT 
                    B.Berry_Name AS Cure_Name, 
                    B.Effect AS Effect, 
                    NULL AS Cost, 
                    B.Count AS Count, 
                    B.Found_At AS Location
                FROM Berries B
                WHERE LOWER(B.Effect) LIKE LOWER(%s)
                UNION ALL
                SELECT 
                    N.Item_Name AS Cure_Name, 
                    N.Effect AS Effect, 
                    N.Cost AS Cost, 
                    N.Count AS Count, 
                    NULL AS Location
                FROM Normal_Item N
                WHERE LOWER(N.Effect) LIKE LOWER(%s);
                """
                cur.execute(query, (f'%{ailment}%', f'%{ailment}%'))
                return cur.fetchall()
    except Exception as e:
        raise Exception(f"Error checking cures: {str(e)}")

# Rivals functions
def get_rival_trainers():
    query = "SELECT * FROM Rival_Trainer;"
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def list_rival_trainers():
    """List all rival trainers"""
    return get_rival_trainers()

def add_rival_trainer(trainer_no, name):
    query = "INSERT INTO Rival_Trainer (Trainer_No, Name) VALUES (%s, %s);"
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, (trainer_no, name))
            con.commit()

def delete_rival_trainer(name):
    query = "DELETE FROM Rival_Trainer WHERE Name = %s;"
    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(query, (name,))
            con.commit()

def delete_rival_trainer_by_number(trainer_no):
    """Delete rival trainer by trainer number"""
    try:
        with get_connection() as con:
            with con.cursor() as cur:
                query = "DELETE FROM Rival_Trainer WHERE Trainer_No = %s;"
                cur.execute(query, (trainer_no,))
                con.commit()
                return cur.rowcount > 0
    except Exception as e:
        raise Exception(f"Error deleting rival trainer: {str(e)}")

# Gyms functions
def get_gyms_data():
    query = "SELECT * FROM Pokemon_Gym;"
    with get_connection() as con:
        with con.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

def view_gyms():
    """View all gyms data"""
    return get_gyms_data()