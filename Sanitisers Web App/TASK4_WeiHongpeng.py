from flask import Flask, render_template, redirect, request, url_for
import sqlite3

conn = sqlite3.connect('sanitisers.db')
rows = conn.execute("SELECT * FROM Sanitisers").fetchall()

app = Flask(__name__)
active_ingredient = ''
new_rows = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        active_ingredient = request.form['ing']
        new_rows = [i for i in rows if i[1] == active_ingredient]
        return render_template('active.html', rows=new_rows)
    
    return render_template('index.html', rows=rows)

@app.route('/active', methods=['GET', 'POST'])
def active():
    new_rows = [i for i in rows if i[1] == active_ingredient]
    return render_template('active.html', rows=new_rows)

if __name__ == '__main__':
    app.run(debug=True)

conn.close()