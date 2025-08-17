import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"  
    )

    cursor = connection.cursor()

    
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

    
    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
