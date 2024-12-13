import mysql.connector

#MySQl Configuration Properties

HOSTNAME = "localhost"
PORT = "3306"
USERNAME = "root"
PWD = "root"
DB_NAME = "py11db"
connection = None


def get_mysqldb_connection():
    global connection
    if connection is None:
        connection = mysql.connector.connect(host=HOSTNAME, port=PORT, username=USERNAME, password=PWD,
                                             database=DB_NAME)
        print("Mysql is connected !!!")
    return connection


def close_mysqldb_connection():
    global connection
    if connection is not None:
        connection.close()
        print("Mysql is Dis-connected !!!")
        connection = None

