from fileinput import filename
import json
import os.path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify

app = Flask(__name__)
app.secret_key = 'hjhaueraisdkm23jfalskjdf'


def get_json_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        note_title = request.form['note_title']
        note = request.form['note']
        res = {note_title: note}
        with open('data.json', 'r') as f:
            data = json.load(f)

        data.update(res)
        with open('data.json', 'w') as f:
            json.dump(data, f)

        return render_template('index.html', data=get_json_data())
    else:
        return render_template('index.html', data=get_json_data())


if __name__ == '__main__':
    app.run(debug=True)
