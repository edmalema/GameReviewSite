import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "10.200.14.24",
        port = 3306,
        user = "edmalemaLocal",
        password = "norge123"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE reviewdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print(mycursor.rowcount, "record(s) affected")

    mydb = mysql.connector.connect(

        host = "10.200.14.24",
        port = 3306,
        user = "edmalemaLocal",
        password = "norge123",
        database = "reviewdb"

    )

    mycursor = mydb.cursor()

    mycursor.execute("""CREATE TABLE games 
                    (id INT AUTO_INCREMENT PRIMARY KEY,
                    game VARCHAR(255),
                    info VARCHAR(255),
                     review INT NOT NULL,
                    image 
                    )""")
except:
    print("Already made")

mydb = mysql.connector.connect(

    host = "10.200.14.24",
    port = 3306,
    user = "edmalemaLocal",
    password = "norge123",
    database = "reviewdb"

)

mycursor = mydb.cursor()
sql = "INSERT INTO games (game, info, review) VALUES (%s, %s, %s)"
val = [
    ('Timmy Wong', 'Irits Row', 10),
    ('Khay Rae', 'Poptart Street')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")