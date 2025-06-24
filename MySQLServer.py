# import pymysql
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get DB credentials from environment
# Host = os.getenv('HOST')
# User = os.getenv('USER')
# Password = os.getenv('PASSWORD')
# database_name = "alx_book_store"

# def create_database():
#     try:
#         # Connect to MySQL Server (no specific database yet)
#         connection = pymysql.connect(
#             host=Host,
#             user=User,
#             password=Password
#         )
#         cursor = connection.cursor()

#         # Create the database if it does not exist
#         cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
#         connection.commit()
#         print(f"Database '{database_name}' created successfully!")

#     except pymysql.MySQLError as e:
#         print(f"Error creating database: {e}")
    
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals():
#             connection.close()

# if __name__ == "__main__":
#     create_database()



import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

Host = os.getenv('HOST')
User = os.getenv('USER')
Password = os.getenv('PASSWORD')
database_name = "alx_book_store"

print("Starting script...")
print("Host:", Host)
print("User:", User)
print("Password:", Password)

def create_database():
    connection = None
    try:
        print("Connecting to MySQL server...")
        connection = mysql.connector.connect(
            host=Host,
            user=User,
            password=Password,
            use_pure=True
        )

        if connection.is_connected():
            print("Connected successfully.")
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            print(f"Database '{database_name}' created successfully!")
            cursor.close()
        else:
            print("[ERROR] Connection established, but is_connected() returned False.")

    except Error as e:
        print("[EXCEPTION]", e)

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_database()
