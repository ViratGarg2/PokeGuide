import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate


def addNewPokemon():
    """
    Function to add a new Pokémon to the database
    """
    try:
        row = {}
        print("Enter new Pokémon's details: ")
        row["Poke_Number"] = int(input("Poke Number: "))
        row["Poke_Name"] = input("Poke Name: ")
        row["Height"] = float(input("Height: "))
        row["Weight"] = float(input("Weight: "))
        row["Type"] = input("Type: ")
        row["Category"] = input("Category: ")
        row["XP"] = int(input("XP: "))
        row["Gender"] = input("Gender (M/F): ")
        row["HP"] = int(input("HP: "))
        row["Level"] = int(input("Level: "))
        row["Special_Attack"] = int(input("Special Attack: "))
        row["Attack"] = int(input("Attack: "))
        row["Defence"] = int(input("Defence: "))
        row["Special_Defence"] = int(input("Special Defence: "))
        row["Speed"] = int(input("Speed: "))

        query = f"""
        INSERT INTO Owned_Pokemon 
        (Poke_Number, Poke_Name, Height, Weight, Type, Category, XP, Gender, HP, Level, Special_Attack, Attack, Defence, Special_Defence, Speed)
        VALUES
        ({row["Poke_Number"]}, '{row["Poke_Name"]}', {row["Height"]}, {row["Weight"]}, '{row["Type"]}', '{row["Category"]}', 
        {row["XP"]}, '{row["Gender"]}', {row["HP"]}, {row["Level"]}, {row["Special_Attack"]}, {row["Attack"]}, 
        {row["Defence"]}, {row["Special_Defence"]}, {row["Speed"]});
        """

        row2={}
        row2["Pokemon_Number"] = row["Poke_Number"]
        row2["Move_Name"] = input("Move 1 Name: ")
        row2["Type"] = input("Type: ")
        row2["Category"] = input("Category: ")
        row2["Power"] = int(input("Power: "))
        row2["Accuracy"] = int(input("Accuracy: "))
        row2["Contact"] = input("Contact (TRUE(1)/FALSE(0)): ")
        row2["PP"] = int(input("PP: "))

        quer2=f"""
        INSERT INTO Moves   
        (Pokemon_Number, Move_Name, Type, Category, Power, Accuracy, Contact, PP)
        VALUES
        ({row2["Pokemon_Number"]}, '{row2["Move_Name"]}', '{row2["Type"]}', '{row2["Category"]}', {row2["Power"]}, {row2["Accuracy"]}, '{row2["Contact"]}', {row2["PP"]});
        """
        print()
        row3={}
        row3["Pokemon_Number"] = row["Poke_Number"]
        row3["Move_Name"] = input("Move 2 Name: ")
        row3["Type"] = input("Type: ")
        row3["Category"] = input("Category: ")
        row3["Power"] = int(input("Power: "))
        row3["Accuracy"] = int(input("Accuracy: "))
        row3["Contact"] = input("Contact (YES(1)/NO(0)): ")
        row3["PP"] = int(input("PP: "))
        quer3=f"""
        INSERT INTO Moves
        (Pokemon_Number, Move_Name, Type, Category, Power, Accuracy, Contact, PP)
        VALUES
        ({row3["Pokemon_Number"]}, '{row3["Move_Name"]}', '{row3["Type"]}', '{row3["Category"]}', {row3["Power"]}, {row3["Accuracy"]}, '{row3["Contact"]}', {row3["PP"]});
        """
        print()
        row4={}
        row4["Pokemon_Number"] = row["Poke_Number"]
        row4["Type"] = row["Type"]
        row4["Strong_Against"] = input("Strong Against: ")
        row4["Weak_Against"] = input("Weak Against: ")
        row4["Immune_To"] = input("Immune To: ")
        quer4=f"""
        INSERT INTO Poke_Type
        (Pokemon_Number, Type, Strong_Against, Weak_Against, Immune_To)
        VALUES
        ({row4["Pokemon_Number"]}, '{row4["Type"]}', '{row4["Strong_Against"]}', '{row4["Weak_Against"]}', '{row4["Immune_To"]}');
        """


        
        cur.execute(query)
        cur.execute(quer2)
        cur.execute(quer3)
        cur.execute(quer4)
        con.commit()
        print("Pokémon added successfully!")

    except Exception as e:
        con.rollback()
        print("Failed to add Pokémon.")
        print(">>>>>>>>>>>>>", e)

def releasePokemon():
    """
    Function to release (delete) a Pokémon from the database.
    The Pokémon is deleted based on its name or number.
    """
    try:
        choice = input("Do you want to delete by Pokémon Name or Number? (Enter 'Name' or 'Number'): ").strip().lower()
        if choice == 'name':
            poke_name = input("Enter the name of the Pokémon to release: ").strip()
            query = f"DELETE FROM Owned_Pokemon WHERE LOWER(Poke_Name) = LOWER('{poke_name}');"
        elif choice == 'number':
            poke_number = int(input("Enter the Pokémon number to release: "))
            query = f"DELETE FROM Owned_Pokemon WHERE Poke_Number = {poke_number};"
        else:
            print("Invalid choice. Please enter 'Name' or 'Number'.")
            return
        
        cur.execute(query)
        con.commit()

        # Check if any rows were affected (i.e., Pokémon was found and deleted)
        if cur.rowcount > 0:
            print("Pokémon released successfully!")
        else:
            print("No Pokémon found with the given name or number.")
    
    except Exception as e:
        con.rollback()
        print("Failed to release Pokémon.")
        print(">>>>>>>>>>>>>", e)

def readAboutPokemon():
    """
    Function to read about Pokémon and their types.
    Allows filtering by Pokémon name or type.
    """
    try:
        # Ask user for filter criteria
        print("Choose a filter:")
        print("1. Filter by Pokémon Name")
        print("2. Filter by Pokémon Type")
        choice = input("Enter 1 or 2: ")

        # Build the query based on user choice
        if choice == "1":
            poke_name = input("Enter Pokémon name: ")
            query = f"""
            SELECT P.Poke_Number, P.Poke_Name, P.Type, P.Category, P.Height, P.Weight, P.Gender, P.XP, P.HP, P.Level, P.Special_Attack, P.Attack, P.Defence, P.Special_Defence, P.Speed, T.Strong_Against, T.Weak_Against, T.Immune_To
            FROM Owned_Pokemon P
            JOIN Poke_Type T ON P.Poke_Number = T.Pokemon_Number
            WHERE LOWER(P.Poke_Name) = LOWER('{poke_name}');
            """
        elif choice == "2":
            poke_type = input("Enter Pokémon type: ")
            query = f"""
            SELECT P.Poke_Number, P.Poke_Name, P.Type, P.Category, P.Height, P.Weight, P.Gender, P.XP, P.HP, P.Level, P.Special_Attack, P.Attack, P.Defence, P.Special_Defence, P.Speed, T.Strong_Against, T.Weak_Against, T.Immune_To
            FROM Owned_Pokemon P
            JOIN Poke_Type T ON P.Poke_Number = T.Pokemon_Number
            WHERE LOWER(P.Type) LIKE LOWER('%{poke_type}%');
            """
        else:
            print("Invalid choice. Please select 1 or 2.")
            return

        # Execute the query
        # print(query)
        cur.execute(query)
        results = cur.fetchall()

        # Display the results
        if results:
            print("\nPokémon Information:")
            headers = ["Poke Number", "Poke Name", "Type", "Category", "Height", "Weight", "Gender", "XP", "HP", "Level", "Special Attack", "Attack", "Defence", "Special Defence", "Speed", "Strong Against", "Weak Against", "Immune To"]
            data = [list(row.values()) for row in results]  # Convert dict rows to lists
            print(tabulate(data, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo information found matching your criteria.")

    except Exception as e:
        print("Failed to fetch Pokémon details.")
        print(">>>>>>>>>>>>>", e)

def viewBattleData():
    """
    Function to view battle data with optional filters.
    Filters include Battle Type, Outcome, Date range, Pokémon Used (Name or Type).
    """
    try:
        print("Enter filters for battle data (enter 'NA' if not applicable):")
        battle_type = input("Battle Type (Gym/Normal/NA): ").lower()
        outcome = input("Outcome (Win/Loss/NA): ").lower()
        pokemon_name = input("Pokémon Name (Enter name/NA): ").lower()
        pokemon_type = input("Pokémon Type (Enter type/NA): ").lower()
        date_start = input("Start Date (YYYY-MM-DD or NA): ").lower()
        date_end = input("End Date (YYYY-MM-DD or NA): ").lower()

        # Build the base query
        query = """
        SELECT B.Battle_Number, B.Battle_Type, B.Pokemon_Used, B.Date, B.Outcome, G.Gym, G.Gym_Leader
        FROM Battle B
        LEFT JOIN Gym_Battle G ON B.Battle_Number = G.Battle_Number
        WHERE 1=1
        """

        # Add filters dynamically
        if battle_type != "na":
            query += f" AND LOWER(B.Battle_Type) = '{battle_type} battle'"
        if outcome != "na":
            query += f" AND LOWER(B.Outcome) = '{outcome}'"
        if pokemon_name != "na":
            query += f" AND B.Pokemon_Used = (SELECT Poke_Number FROM Owned_Pokemon WHERE LOWER(Poke_NAme) = '{pokemon_name}')"
        if pokemon_type != "na":
            query += f" AND B.Pokemon_Used IN (SELECT Poke_Number FROM Owned_Pokemon WHERE LOWER(Type) LIKE '%{pokemon_type}%')"
        if date_start != "na":
            query += f" AND B.Date >= '{date_start}'"
        if date_end != "na":
            query += f" AND B.Date <= '{date_end}'"

        # Execute the query
        # print(query)
        cur.execute(query)
        results = cur.fetchall()

        # Display the results in a tabular format
        if results:
            print("\nFiltered Battle Data:")
            headers = ["Battle Number", "Battle Type", "Pokemon Used", "Date", "Outcome", "Gym", "Gym Leader"]
            table = [list(row.values()) for row in results]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo data found matching the given filters.")
    except Exception as e:
        print("Failed to fetch battle data.")
        print(">>>>>>>>>>>>>", e)

def viewGyms():
    try:
        query = "SELECT * FROM Pokemon_Gym;"
        cur.execute(query)
        results = cur.fetchall()

        if results:
            print("\nGyms Data:")
            # Extract column names and data for tabulate
            headers = ["Location", "Badge Won?", "Gym Badge", "Gym Type", "Gym Leader", "Previous Gym", "Next Gym"]
            table = [list(row.values()) for row in results]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo gyms data found.")
    except Exception as e:
        print("Failed to fetch gym data.")
        print(">>>>>>>>>>>>>", e)

def viewItemsInBag():
    """
    Function to view items in the player's bag, with the option to filter by Pokéballs, Berries, or Normal Items.
    Also, handles MySQL errors returned by the database.
    """
    try:
        # Ask user for the type of items to view
        item_type = input("Enter item type to view (Pokeballs/Berries/Normal Items): ").lower()

        if item_type not in ["pokeballs", "berries", "normal items"]:
            print("Invalid item type! Please enter one of the following: Pokeballs, Berries, Normal Items.")
            return
        if item_type == "Pokeballs" or item_type == "pokeballs":
            query = "SELECT Type, Cost, Count, Catch_Rate FROM Pokeball;"
        elif item_type == "Berries" or item_type == "berries":
            query = "SELECT Berry_Name, Effect, Found_At, Count FROM Berries;"
        elif item_type == "Normal Items" or item_type == "normal items":
            query = "SELECT Item_Name, Effect, Cost, Count FROM Normal_Item;"
        else:
            print("Invalid item type! Please enter one of the following: Pokéballs, Berries, Normal Items.")
            return

        cur.execute(query)
        results = cur.fetchall()

        if results:
            print(f"\n{item_type.capitalize()} in Bag:")
            # Get headers dynamically based on item type
            if item_type == "Pokeballs" or item_type == "pokeballs":
                headers = ["Ball Type", "Cost", "Quantity", "Catch Rate"]
            elif item_type == "Berries" or item_type == "berries":
                headers = ["Berry_Name", "Effect", "Location", "Quantity"]
            else:
                headers = ["Item_Name", "Effect", "Cost", "Quantity"]
            
            # Format the results for tabulation
            table = [list(row.values()) for row in results]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print(f"\nNo {item_type} found in your bag.")

    except pymysql.MySQLError as e:
        print("MySQL Error occurred!")
        print("Error Code:", e.args[0])
        print("Error Message:", e.args[1])
        print("SQL State:", e.args[2])

    except Exception as e:
        print("An unexpected error occurred.")
        print("Error Details:", e)

def updateXP(pokemon_id, battle_outcome):
    """
    Function to update the XP and level of a Pokémon after a battle.
    - Each level corresponds to 4000 XP.
    - XP increases for a win or loss.
    - Level increases based on total XP exceeding multiples of 4000.
    """
    try:
        if battle_outcome.lower() == "win":
            xp_increase = 200  # XP for a win
        else:
            xp_increase = 100  # XP for a loss
        
        # Update the XP for the Pokémon
        query = f"""
        UPDATE Owned_Pokemon
        SET XP = XP + {xp_increase}
        WHERE Poke_Number = {pokemon_id};
        """
        # print(query)
        cur.execute(query)

        # Fetch the new XP value for the Pokémon
        query = f"""
        SELECT XP FROM Owned_Pokemon WHERE Poke_Number = {pokemon_id};
        """
        # print(query)
        cur.execute(query)
        current_xp = cur.fetchone()['XP']
        print("current xp",current_xp)

        # Calculate the new level based on total XP
        new_level = current_xp // 4000  # Level based on multiples of 4000 XP
        print("new level",new_level)

        # Update the Pokémon's level
        query = f"""
        UPDATE Owned_Pokemon
        SET Level = {new_level}
        WHERE Poke_Number = {pokemon_id};
        """
        # print(query)
        cur.execute(query)

        print(f"Pokémon {pokemon_id} level updated! New Level: {new_level}, Total XP: {current_xp}")

        # Commit changes
        con.commit()

    except Exception as e:
        print("Failed to update XP and level.")
        print(">>>>>>>>>>>>>", e)

def addNewBattle():
    """
    Function to add a new battle to the database with validation and error handling.
    """
    try:
        battle = {}
        print("\nEnter new battle details:")
        # Input validation
        try:
            battle["Battle_ID"] = int(input("Battle ID: "))
            battle["Pokemon_Used"] = int(input("Pokemon Used (Poke Number): "))
            
            # Validate Pokemon exists
            cur.execute(f"SELECT Poke_Number FROM Owned_Pokemon WHERE Poke_Number = {battle['Pokemon_Used']}")
            if not cur.fetchone():
                raise ValueError("Pokemon number does not exist")
                
            battle_type = input("Battle Type (Gym/Trainer): ").lower()
            if battle_type not in ['gym', 'trainer']:
                raise ValueError("Invalid battle type. Must be 'Gym' or 'Trainer'")
            battle["Type"] = battle_type
            
            outcome = input("Outcome (Win/Loss): ").lower()
            if outcome not in ['win', 'loss']:
                raise ValueError("Invalid outcome. Must be 'Win' or 'Loss'")
            battle["Outcome"] = outcome
            
            # Date validation
            date = input("Date (YYYY-MM-DD): ")
            # Simple date format check
            if not len(date.split('-')) == 3:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")
            battle["Date"] = date
            
        except ValueError as e:
            print(f"Input Error: {e}")
            return

        # Begin transaction
        cur.execute("START TRANSACTION")

        # Insert into Battle table
        query = f"""
        INSERT INTO Battle (Battle_Number, Pokemon_Used, Battle_Type, Outcome, Date)
        VALUES ({battle["Battle_ID"]}, {battle["Pokemon_Used"]}, '{battle["Type"]}', 
                '{battle["Outcome"]}', '{battle["Date"]}');
        """
        cur.execute(query)

        if battle["Type"] == "gym":
            gym_leader = input("Gym Leader Name: ")
            location = input("Gym Location: ")

            # Validate gym location exists
            cur.execute(f"SELECT Location FROM Pokemon_Gym WHERE Location = '{location}'")
            if not cur.fetchone():
                raise ValueError("Gym location does not exist")

            # Insert into Gym_Battle table
            query = f"""
            INSERT INTO Gym_Battle (Battle_Number, Gym, Gym_Leader)
            VALUES ({battle["Battle_ID"]}, '{location}', '{gym_leader}');
            """
            cur.execute(query)

            # Insert into Battling_Gym_Leader table
            query = f"""
            INSERT INTO Battling_Gym_Leader (Battle_Number, Pokemon_Number, Location)
            VALUES ({battle["Battle_ID"]}, {battle["Pokemon_Used"]}, '{location}');
            """
            cur.execute(query)

            # Update gym badge if battle was won
            if battle["Outcome"] == "win":
                query = f"""
                UPDATE Pokemon_Gym 
                SET Badge_Won = TRUE 
                WHERE Location = '{location}';
                """
                cur.execute(query)

        else:  # Trainer battle
            rival_trainer_id = int(input("Rival Trainer ID: "))
            location = input("Battle Location: ")

            # Validate rival trainer exists
            cur.execute(f"SELECT Trainer_No FROM Rival_Trainer WHERE Trainer_No = {rival_trainer_id}")
            if not cur.fetchone():
                raise ValueError("Rival trainer does not exist")

            # Insert into Normal_Battle table
            query = f"""
            INSERT INTO Normal_Battle (Battle_Number, Location, Rival_ID)
            VALUES ({battle["Battle_ID"]}, '{location}', {rival_trainer_id});
            """
            cur.execute(query)

            # Insert into Battling_Rival_Trainer table
            query = f"""
            INSERT INTO Battling_Rival_Trainer (Battle_Number, Pokemon_Number, Trainer_No)
            VALUES ({battle["Battle_ID"]}, {battle["Pokemon_Used"]}, {rival_trainer_id});
            """
            cur.execute(query)

        # Update Pokemon XP based on battle outcome
        updateXP(battle["Pokemon_Used"], battle["Outcome"])

        # Commit transaction
        con.commit()
        print("\nBattle added successfully!")

    except Exception as e:
        con.rollback()
        print("\nFailed to add battle.")
        print("Error:", e)
        
def readAilments():
    """
    Function to display all ailments and their cures from the Ailment_and_Cure table.
    Retrieves the table data and displays it in a tabular format.
    """
    try:
        # Query to fetch all data from Ailment_and_Cure table
        query = "SELECT Berry_Name, Item_Name, Ail_Name FROM Ailment_and_Cure;"
        cur.execute(query)
        results = cur.fetchall()
        table = [list(row.values()) for row in results]
        # Display results
        if results:
            print("\nAilments and Their Cures:")
            headers = ["Berry Name", "Item Name", "Ailment"]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo data found in the Ailment_and_Cure table.")
    except Exception as e:
        print("Failed to fetch ailments and cures.")
        print(">>>>>>>>>>>>>", e)

def checkCuresForAilments():
    """
    Function to check items (Berries and Normal Items) that cure specific ailments.
    Displays Cure, Effect, Cost, Count, and Location (if applicable).
    """
    try:
        # Take input for the ailment
        ailment = input("Enter the ailment you want a cure for: ").lower()

        # Query to find cures from both Berry and Normal_Item tables
        query = f"""
        SELECT 
            B.Berry_Name AS Cure_Name, 
            B.Effect AS Effect, 
            NULL AS Cost, 
            B.Count AS Count, 
            B.Found_At AS Location
        FROM Berries B
        WHERE LOWER(B.Effect) LIKE '%{ailment}%'
        UNION ALL
        SELECT 
            N.Item_Name AS Cure_Name, 
            N.Effect AS Effect, 
            N.Cost AS Cost, 
            N.Count AS Count, 
            NULL AS Location
        FROM Normal_Item N
        WHERE LOWER(N.Effect) LIKE '%{ailment}%';
        """
        
        # Execute the query
        cur.execute(query)
        results = cur.fetchall()
        data = [list(row.values()) for row in results]

        # Display the results
        if data:
            print(f"\nCures for '{ailment.capitalize()}':")
            headers = ["Cure Name", "Effect", "Cost", "Count", "Location"]
            print(tabulate(data, headers=headers, tablefmt="pretty"))
        else:
            print(f"\nNo cures found for '{ailment.capitalize()}'.")
    except Exception as e:
        print("Failed to fetch cures for ailments.")
        print(">>>>>>>>>>>>>", e)

def listRivalTrainers():
    """
    Function to fetch and display all rival trainers from the Rival_Trainer table.
    """
    try:
        # Query to select all rival trainers
        query = "SELECT Trainer_No, Name FROM Rival_Trainer;"
        cur.execute(query)
        results = cur.fetchall()

        # Convert the results to a list of dictionaries (if needed)
        data = [dict(row) for row in results] if isinstance(results[0], dict) else results

        # Display results
        if data:
            print("\nList of Rival Trainers:")
            headers = ["Trainer No", "Name"]
            if isinstance(data[0], dict):  # For list of dicts
                print(tabulate(data, headers="keys", tablefmt="pretty"))
            else:  # For list of tuples
                print(tabulate(data, headers=headers, tablefmt="pretty"))
        else:
            print("\nNo rival trainers found in the database.")
    except Exception as e:
        print("Failed to fetch rival trainers.")
        print(">>>>>>>>>>>>>", e)

def editRivalTrainers():
    """
    Function to edit the list of rival trainers.
    Allows the user to add or delete a rival by name or trainer number.
    """
    try:
        print("\nEdit Rival Trainers:")
        print("1. Add a Rival Trainer")
        print("2. Delete a Rival Trainer")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":  # Add a rival
            trainer_no = int(input("Enter Trainer Number: "))
            name = input("Enter Trainer Name: ")
            
            # Insert query
            query = "INSERT INTO Rival_Trainer (Trainer_No, Name) VALUES (%s, %s);"
            cur.execute(query, (trainer_no, name))
            con.commit()  # Commit changes to the database
            print(f"Successfully added Trainer '{name}' with Trainer Number {trainer_no}.")

        elif choice == "2":  # Delete a rival
            print("\nDelete by:")
            print("1. Trainer Number")
            print("2. Trainer Name")
            del_choice = input("Enter your choice (1/2): ")

            if del_choice == "1":  # Delete by Trainer Number
                trainer_no = int(input("Enter Trainer Number: "))
                query = "DELETE FROM Rival_Trainer WHERE Trainer_No = %s;"
                cur.execute(query, (trainer_no,))
                con.commit()
                if cur.rowcount > 0:
                    print(f"Successfully deleted Trainer with Trainer Number {trainer_no}.")
                else:
                    print(f"No trainer found with Trainer Number {trainer_no}.")

            elif del_choice == "2":  # Delete by Trainer Name
                name = input("Enter Trainer Name: ")
                query = "DELETE FROM Rival_Trainer WHERE Name = %s;"
                cur.execute(query, (name,))
                con.commit()
                if cur.rowcount > 0:
                    print(f"Successfully deleted Trainer '{name}'.")
                else:
                    print(f"No trainer found with the name '{name}'.")
            else:
                print("Invalid choice! Returning to main menu.")
        else:
            print("Invalid choice! Please select either 1 or 2.")
    except Exception as e:
        print("An error occurred while editing rival trainers.")
        print(">>>>>>>>>>>>>", e)

def readMoves():
    """
    Function to read about moves. The user can filter by move type, Pokémon name, or view all moves.
    """
    try:
        print("\nView Moves:")
        print("1. Filter by Move Type")
        print("2. Filter by Pokémon Name")
        print("3. View All Moves")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":  # Filter by Move Type
            move_type = input("Enter the Move Type: ")
            query = f"""
            SELECT Move_Name, Type, Category, Power, Accuracy, Contact, PP
            FROM Moves
            WHERE LOWER(Type) LIKE LOWER('%{move_type}%');
            """
            cur.execute(query)
            results = cur.fetchall()
            data = [list(row.values()) for row in results]

            # if results:
            #     print(f"\nMoves of Type '{move_type.capitalize()}':")
            #     headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
            #     print(tabulate(results, headers=headers, tablefmt="pretty"))
            # else:
            #     print(f"\nNo moves found with the type '{move_type.capitalize()}'.")
            if data:
                print(f"\nMoves of Type '{move_type.capitalize()}':")
                headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
                print(tabulate(data, headers=headers, tablefmt="pretty"))
            else:
                print(f"\nNo moves found with the type '{move_type.capitalize()}'.")
        
        elif choice == "2":  # Filter by Pokémon Name
            poke_name = input("Enter the Pokémon Name: ")
            query = f"""
            SELECT M.Move_Name, M.Type, M.Category, M.Power, M.Accuracy, M.Contact, M.PP
            FROM Moves M
            JOIN Owned_Pokemon P ON M.Pokemon_Number = P.Poke_Number
            WHERE LOWER(P.Poke_Name) = LOWER('{poke_name}');
            """
            cur.execute(query)
            results = cur.fetchall()
            data=[list(row.values()) for row in results]

            # if results:
            #     print(f"\nMoves for Pokémon '{poke_name.capitalize()}':")
            #     headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
            #     print(tabulate(results, headers=headers, tablefmt="pretty"))
            # else:
            #     print(f"\nNo moves found for Pokémon '{poke_name.capitalize()}'.")
            if data:
                print(f"\nMoves for Pokémon '{poke_name.capitalize()}':")
                headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
                print(tabulate(data, headers=headers, tablefmt="pretty"))
            else:
                print(f"\nNo moves found for Pokémon '{poke_name.capitalize()}'.")

        
        elif choice == "3":  # View All Moves
            query = """
            SELECT Move_Name, Type, Category, Power, Accuracy, Contact, PP
            FROM Moves;
            """
            cur.execute(query)
            results = cur.fetchall()
            data = [list(row.values()) for row in results]

            # if results:
            #     print("\nAll Moves:")
            #     headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
            #     print(tabulate(results, headers=headers, tablefmt="pretty"))
            # else:
            #     print("\nNo moves found in the database.")
            if data:
                print("\nAll Moves:")
                headers = ["Move Name", "Type", "Category", "Power", "Accuracy", "Contact", "PP"]
                print(tabulate(data, headers=headers, tablefmt="pretty"))
            else:
                print("\nNo moves found in the database.")

        else:
            print("Invalid choice! Please select either 1, 2, or 3.")

    except Exception as e:
        print("Failed to fetch moves details.")
        print(">>>>>>>>>>>>>", e)

def dispatch(ch, category):
    """
    Function that maps helper functions to options entered based on category.
    """
    if category == 1:  # Pokémon category
        if ch == 1:
            addNewPokemon()
        elif ch == 2:
            readAboutPokemon()
        elif ch == 3:
            releasePokemon()
        else:
            print("Error: Invalid Option")

    elif category == 2:  # Moves category
        if ch == 1:
            readMoves()
        else:
            print("Error: Invalid Option")

    elif category == 3:  # Battle category
        if ch == 1:
            viewBattleData()
        elif ch == 2:
            addNewBattle()
        else:
            print("Error: Invalid Option")

    elif category == 4:  # Bag category
        if ch == 1:
            viewItemsInBag()
        else:
            print("Error: Invalid Option")

    elif category == 5:  # Ailments category
        if ch == 1:
            readAilments()
        elif ch == 2:
            checkCuresForAilments()
        else:
            print("Error: Invalid Option")

    elif category == 6:  # Rivals category
        if ch == 1:
            listRivalTrainers()
        elif ch == 2:
            editRivalTrainers()
        else:
            print("Error: Invalid Option")

    elif category == 7:  # Gyms category
        if ch == 1:
            viewGyms()
        else:
            print("Error: Invalid Option")

    else:
        print("Error: Invalid Category")

# Main Program
while True:
    tmp = sp.call('clear', shell=True)

    try:
        # Connect to the MySQL database
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password="SABKAbaap2#",  # Replace with your MySQL root password
                              db='PokeGuide',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if con.open:
            print("Connected to the PokeGuide database.")
        else:
            print("Failed to connect.")

        with con.cursor() as cur:
            while True:
                print("1. Pokémon")
                print("2. Moves")
                print("3. Battle")
                print("4. Bag")
                print("5. Ailments")
                print("6. Rivals")
                print("7. Gyms")
                print("8. Logout")
                category = int(input("Enter category choice> "))
                
                if category == 8:
                    exit()

                # Submenu for category selection
                if category == 1:  # Pokémon category
                    print("1. Add a new Pokémon")
                    print("2. Read about Pokémon")
                    print("3. Release a Pokémon")
                    sub_choice = int(input("Enter choice> "))
                    dispatch(sub_choice, 1)
                
                elif category == 2:  # Moves category
                    # print("1. Read about Moves")
                    # sub_choice = int(input("Enter choice> "))
                    dispatch(1, 2)
                
                elif category == 3:  # Battle category
                    print("1. View battle data")
                    print("2. Add a new battle")
                    sub_choice = int(input("Enter choice> "))
                    dispatch(sub_choice,3)
               
                elif category == 4:  # Bag category
                    # print("1. View items in bag")
                    # sub_choice = int(input("Enter choice> "))
                    dispatch(1,4)

                elif category == 5:  # Ailments category
                    print("1. Read about ailments")
                    print("2. Check cures for ailments")
                    sub_choice = int(input("Enter choice> "))
                    dispatch(sub_choice,5)

                elif category == 6:  # Rivals category
                    print("1. List rival trainers")
                    print("2. Edit rival trainers")
                    sub_choice = int(input("Enter choice> "))
                    dispatch(sub_choice,6)

                elif category == 7:  # Gyms category
                    # print("1. View gyms")
                    # sub_choice = int(input("Enter choice> "))
                    dispatch(1,7)

                else:
                    print("Error: Invalid Category")

                input("Press Enter to continue...")

    except Exception as e:
        print("Connection Refused: Check your username, password, or database configuration.")
        print(">>>>>>>>>>>>>", e)
        input("Press Enter to continue...")
