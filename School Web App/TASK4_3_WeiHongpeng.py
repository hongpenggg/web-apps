from flask import Flask, render_template, redirect, request, url_for
import sqlite3

conn = sqlite3.connect('school.db')
data = conn.execute("SELECT * FROM People").fetchall()

app = Flask(__name__, template_folder='TASK4_3_WeiHongpeng')

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

conn.close()