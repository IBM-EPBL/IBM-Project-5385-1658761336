# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'root',
							host = 'localhost',
							database = 'user')

print(conn)

# Disconnecting from the server
conn.close()
