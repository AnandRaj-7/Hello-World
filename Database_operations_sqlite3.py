import sqlite3

values = (("Jean-Baptiste Zorg", "Human", 122),("Korben Dallas", "Meat Popsicle",100),("Ak'not","Mangalore",-5))
with sqlite3.connect("New_DB.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("""CREATE TABLE Roster(
                   Name TEXT,
                   Species TEXT,
                   IQ INT);""")
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?);",values)
    cursor.execute("SELECT * FROM Roster;")
    print("The new table Roster is :\n")
    for record in cursor.fetchall():
        print(record)
    cursor.execute("UPDATE Roster SET Species = ? WHERE Name = ?;",("Human","Korben Dallas") )
    cursor.execute("SELECT Name , IQ FROM Roster WHERE Species = 'Human';")
    print("\nThe records with Species as Human are :\n")
    for record in cursor.fetchall():
        print(record)
    cursor.execute("SELECT * FROM Roster")
    print("\nThe table Roster after data updation is :\n")
    for record in cursor.fetchall():
        print(record)