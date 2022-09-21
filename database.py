import mysql.connector


def show_table():
    global users_cursor

    users_cursor.execute("SHOW TABLES")
    res = users_cursor.fetchall()
    for x in res:
        print(x)

    return res


def show_users():
    global users_cursor

    users_cursor.execute("SELECT * FROM Users")
    res = users_cursor.fetchall()
    for x in res:
        print(x)

    return res


users_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berkely_3106_@",
    database="note_app"
)

users_cursor = users_db.cursor()
