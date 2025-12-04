import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv





dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

env_User = os.getenv("user")
env_Password = os.getenv("password")
env_Host = os.getenv("host")

try:
    mydb = mysql.connector.connect(
        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE reviewdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print(mycursor.rowcount, "record(s) affected")
except:
    print("Database already created")

try:
    mydb = mysql.connector.connect(

        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password,
        database = "reviewdb"

    )

    mycursor = mydb.cursor()

    mycursor.execute("""CREATE TABLE games 
                    (id INT AUTO_INCREMENT PRIMARY KEY,
                    game VARCHAR(255),
                    info VARCHAR(255),
                    review INT NOT NULL,
                    image LONGBLOB NOT NULL,
                    likes INT NOT NULL
                    )""")
except:
    print("Table already made")


question = input("Delete table? y/n: ")

if (question == "y"):
    mydb = mysql.connector.connect(

        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password,
        database = "reviewdb"

    )

    mycursor = mydb.cursor()

    mycursor.execute("""DROP TABLE games;""")
    print(mycursor.rowcount, "record(s) affected")


# mydb = mysql.connector.connect(

#     host = env_Host,
#     port = 3306,
#     user = env_User,
#     password = env_Password,
#     database = "reviewdb"

# )

# mycursor = mydb.cursor()
# sql = "INSERT INTO games (game, info, review) VALUES (%s, %s, %s)"
# val = [
#     ('Timmy Wong', 'Irits Row', 10),
#     ('Khay Rae', 'Poptart Street')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")