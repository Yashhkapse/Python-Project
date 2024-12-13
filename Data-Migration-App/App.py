import config.mysqldb
import config.mongodb
from config.mongodb.configuration import close_mongodb_connection
from config.mysqldb.configuration import close_mysqldb_connection

print("Welcome to Data Migration App")
print("byeee")
close_mysqldb_connection()
close_mongodb_connection()