<img src="PokeGuide.jpeg" alt="PokeGuide Logo" width="350" height="350">

# Team 37
<span style="font-size: 20px; color: turquoise;">
Arnav Sharma 2023111033<br>
Hardik Chadha 2023111031<br>
Hiten Garg 2023101116<br>
Virat Garg 2023101081
</span>
<br><br><br>


# Pokémon Database Management Application

## Overview

PokéGuide is a comprehensive Python+SQL application for managing a Pokémon database using PyMySQL, providing various functionalities for tracking Pokémon, battles, items, and more.

## Link to Presentation Video
[Link to 1x Speed, 1080p Presentation Video](https://youtu.be/xz5PQb0MNc8 "Link to Presentation Video")


## Database Functions

### Pokémon Management
- `readAboutPokemon()`:
  - Provides flexible search for Pokémon by name or type.
  - Retrieves comprehensive Pokémon details including stats, type information.
  - Displays results in a tabular format using tabulate library.

- `addNewPokemon()`: 
  - Allows adding a new Pokémon to the database.
  - Collects detailed information including Pokémon number, name, stats, moves, and type.
  - Inserts data into multiple tables: Owned_Pokemon, Moves, and Poke_Type.
  - Handles database transactions with commit and rollback.

- `releasePokemon()`:
  - Enables deleting a Pokémon from the database.
  - Supports deletion by Pokémon name or number.
  - Provides feedback on successful deletion or if no Pokémon is found.
 
### Moves
- `readMoves()`:
  - Provides comprehensive move information.
  - Can filter moves by type or Pokémon.
  - Shows move details like power, accuracy, category.

### Battle System
- `viewBattleData()`:
  - Provides flexible filtering for battle history.
  - Can filter by battle type, outcome, date range, Pokémon.
  - Displays battle information in a detailed table using tabulate library.

- `addNewBattle()`:
  - Supports adding both Gym and Trainer battles.
  - Tracks battle details like Pokémon used, outcome, date.
  - Updates gym badges for won battles.
  - Automatically updates Pokémon XP after battles.

- `updateXP()`:
  - Automatically manages Pokémon experience points.
  - Increases XP based on battle outcomes.
  - Levels up Pokémon when XP reaches certain thresholds.

### Item and Inventory Management
- `viewItemsInBag()`:
  - Allows viewing different types of items (Pokéballs, Berries, Normal Items).
  - Displays item details like quantity, cost, effects.

### Ailments and Cures Information
- `readAilments()`:
  - Lists all ailments and their potential cures.
  - Helps players understand status conditions and treatments.

- `checkCuresForAilments()`:
  - Searches for items that can cure specific ailments.
  - Checks both Berries and Normal Items.
  - Provides details about potential cures.

### Rival and Gym Tracking
- `listRivalTrainers()`:
  - Displays all registered rival trainers.
  - Shows trainer numbers and names.

- `editRivalTrainers()`:
  - Allows adding or deleting rival trainers.
  - Supports modification by trainer number or name.

- `viewGyms()`:
  - Shows detailed information about Pokémon gyms.
  - Displays gym locations, badges, types, and leaders.



## Database Connection
- Uses PyMySQL for database connectivity.
- Connects to a local MySQL database named 'PokeGuide'.
- Implements error handling for database operations.

## Usage
1. Ensure MySQL is installed and running.
2. Create the 'PokeGuide' database with required tables.
3. Update database connection parameters in the script.
4. Run the script and navigate through menu options.

## Dependencies
- Python 3.x
- PyMySQL
- tabulate

## Note
Requires a MySQL database setup with the specific schema used in this application.

