import random
import sqlite3


def add_excuse():
    connection = sqlite3.connect("excuses.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS excuses (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT NOT_NULL)"
    )
    new_sorry = input("Introdu o noua scuza: ")
    cursor.execute("INSERT INTO excuses (text) VALUES (?)", (new_sorry,))
    connection.commit()
    print("Scuza a fost adaugata!")
    connection.close()


def show_random_excuse():
    connection = sqlite3.connect("excuses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT text from excuses")
    excuses = cursor.fetchall()
    print(f"Scuza random: {random.choice(excuses)[0]}")
    connection.close()


def delete_random_excuse():
    connection = sqlite3.connect("excuses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM excuses")
    excuses = cursor.fetchall()
    cursor.execute("DELETE FROM excuses WHERE id = ?", random.choice(excuses))
    connection.commit()
    print("Scuza a fost stearsa cu succes !")
    connection.close()


# add_excuse()
# add_excuse()
show_random_excuse()
delete_random_excuse()
