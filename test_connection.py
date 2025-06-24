import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Test@123',
        use_pure=True
        #  database="mysql"
    )

    print("Connection object:", connection)
    print("Is connected:", connection.is_connected())

except Error as e:
    print("Connection failed:", e)
