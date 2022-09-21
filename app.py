import json
from database import users_db, users_cursor
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

app = Flask(__name__)
app.secret_key = 'hjhaueraisdkm23jfalskjdf'


def get_json_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def dump_json_data(new_data):
    with open('data.json', 'w') as f:
        json.dump(new_data, f)


def update_json_data(json_key, json_value):
    data = get_json_data()
    data[json_key] = json_value
    dump_json_data(new_data=data)
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)


def delete_json_data(json_key):
    data = get_json_data()
    del data[json_key]
    dump_json_data(new_data=data)


def is_valid_str(note_title: str, note: str):
    if note_title != "" and note != "":
        return True
    return False


def is_correct(users_data, email, password):
    for user in users_data:
        if email == user[2] and password == user[3]:
            return True
    return False


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        users_cursor.execute("SELECT * FROM users")
        users = users_cursor.fetchall()

        if is_correct(users_data=users, email=email, password=password):
            return redirect(url_for('home'))
        else:
            flash("Data incorrect!")
            return redirect(url_for('login'))
    else:
        return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstName']
        last_name = request.form['lastName']

        users_cursor.execute("SELECT * FROM users")
        res = users_cursor.fetchall()
        is_valid = [True if email in x[1] else False for x in res][0]

        if not is_valid:
            sql = ("INSERT INTO users (Username, UserEmail, UserPass, FirstName, LastName) VALUES (%s, %s, %s, %s, %s)")
            val = (username, email, password, first_name, last_name)
            users_cursor.execute(sql, val)
            users_db.commit()

            flash("You successfully created an account!")
            return redirect(url_for('login'))
        else:
            flash("You've an account already")
            return redirect(url_for('login'))
    else:
        return render_template('register.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        note_title = request.form['note_title']
        note = request.form['note']

        if not is_valid_str(note_title=note_title, note=note):
            flash("You typed the note incorrectly")
            return redirect(url_for('home'))

        res = {note_title: note}
        data = get_json_data()
        data.update(res)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        return render_template('home.html', data=get_json_data())
    else:
        return render_template('home.html', data=get_json_data())


@app.route('/update/<note>', methods=['POST', 'GET'])
def update_note(note):
    data = get_json_data()
    # description = request.form['description']
    description = data[note]

    if request.method == 'POST':
        # new_note_title = request.form['note_title']
        delete_json_data(json_key=note)
        new_title = request.form['note_title']
        new_note = request.form['note']
        update_json_data(json_key=new_title, json_value=new_note)

        return redirect('/home')
    else:
        return render_template("update.html", note=note, description=description)


@app.route('/delete/<note>', methods=['POST', 'GET'])
def delete_note(note):
    delete_json_data(json_key=note)
    return redirect('/home')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
