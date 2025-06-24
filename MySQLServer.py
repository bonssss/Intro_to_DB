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
# database_name = "alx_book_store"

print("Starting script...")
print("Host:", Host)
print("User:", User)
print("Password:", Password)

try:
    # Connect to MySQL Server (no specific database yet)
    connection = mysql.connector.connect(
        host=Host,
        user=User,
        password=Password,
        database="alx_book_store" , # Specify the database name here
        use_pure=True
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create the database if it does not exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store")
        connection.commit()
        print(f"Database alx_book_store created successfully!")
    else:
        print("Failed to connect to the database server.")
except Error as e:
    print(f"Error creating database: {e}")