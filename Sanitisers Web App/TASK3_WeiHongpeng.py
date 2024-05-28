from flask import Flask, render_template, redirect, request, url_for
import sqlite3

conn = sqlite3.connect('sanitisers.db')
rows = conn.execute("SELECT * FROM Sanitisers").fetchall()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('TASK3_WeiHongpeng.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

conn.close()