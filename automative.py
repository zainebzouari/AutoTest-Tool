import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'myDB')
}

def connect_db():
    return mysql.connector.connect(**db_config)

def get_vehicle_data(conn, vehicle_id):
    cursor = conn.cursor(dictionary=True)
    data = {}

    cursor.execute("SHOW TABLES")
    tables = [row['Tables_in_mydb'] for row in cursor.fetchall()]

    vehicle_found = False  

    for table in tables:
        cursor.execute(f"SELECT * FROM {table} WHERE Vehicle_ID = %s", (vehicle_id,))
        result = cursor.fetchone()
        
        if result:
            data[table] = result
            vehicle_found = True 

        while cursor.nextset():
            cursor.fetchall()

    cursor.close()

    if vehicle_found:
        return data
    else:
        return None




  
    
