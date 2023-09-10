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


def show_user(user_email):
    global users_cursor

    sql = "SELECT * FROM users WHERE UserEmail = %s"
    val = (user_email, )
    users_cursor.execute(sql, val)
    res = users_cursor.fetchall()
    # print(res)
    # print(res[0][1])
    return res

users_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shokolad2912",
    database="note_app"
)

users_cursor = users_db.cursor()
# show_user("kaloyankerr")