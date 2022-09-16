import json
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

app = Flask(__name__)
app.secret_key = 'hjhaueraisdkm23jfalskjdf'


def get_json_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def update_json_data(json_key, json_value):
    data = get_json_data()
    data[json_key] = json_value

    with open('data.json', 'w') as f:
        json.dump(data, f)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        note_title = request.form['note_title']
        note = request.form['note']
        res = {note_title: note}
        # with open('data.json', 'r') as f:
        #     data = json.load(f)
        data = get_json_data()
        data.update(res)

        with open('data.json', 'w') as f:
            json.dump(data, f)

        return render_template('index.html', data=get_json_data())
    else:
        return render_template('index.html', data=get_json_data())


@app.route('/update/<note>', methods=['POST', 'GET'])
def update_note(note):
    # data = get_json_data()
    description = request.form['description'].value

    if request.method == 'POST':
        # new_note_title = request.form['note_title']
        new_note = request.form['note']
        update_json_data(json_key=note, json_value=new_note)
        
        # data[note] = new_note
        # with open('data.json', 'w') as f:
        #     json.dump(data, f)

        return redirect('/')
    else:
        return render_template("update.html", note=note, description=description)


if __name__ == '__main__':
    app.run(debug=True)
