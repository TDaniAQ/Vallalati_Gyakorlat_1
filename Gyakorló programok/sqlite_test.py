import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute(
            '''
            CREATE TABLE TERMEKEK
         (
         ID INT PRIMARY KEY     NOT NULL,
         NAME           CHAR(50)    NOT NULL,
         PRICE            INT     NOT NULL,
         STOCK        INT,
         SOLD         INT
         );
         '''
)

print("Table created successfully")

conn.execute("INSERT INTO TERMEKEK (ID,NAME,PRICE,STOCK,SOLD) \
      VALUES (1, 'Toll', 200, 1568, 259 )")

conn.commit()

print("Insert successful")

conn.close()

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT ID,NAME,PRICE,STOCK,SOLD from TERMEKEK")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("PRICE = ", row[2])
    print("STOCK = ", row[3])
    print("SOLD = ", row[4], "\n")

print("Operation done successfully")
conn.close()
