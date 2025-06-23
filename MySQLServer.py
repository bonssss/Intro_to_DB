import mysql.connector
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

Host = os.getenv('HOST')
User = os.getenv('USER')
Password = os.getenv('PASSWORD')
database_name= "alx_book_store"
try:
    mydb =mysql.connector.Connect(
        host=Host,
        user=User,
        password=Password,
        # database=database_name
    )
    
    cursor = mydb.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
    mydb.commit()
    


    print(f"Database {database_name} created successfully!")
except pymysql.MySQLError as e:
    print(f"Error creating database: {e}")
    