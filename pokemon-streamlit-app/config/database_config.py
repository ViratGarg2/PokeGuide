import pymysql

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'SABKAbaap2#',  # Replace with your MySQL root password
    'db': 'PokeGuide',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    connection = pymysql.connect(**DB_CONFIG)
    return connection