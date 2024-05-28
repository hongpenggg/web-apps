# Task 4.4

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, template_folder='TASK4_4')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # return render_template('warranty.html')
        serial = request.form['serial']
        return redirect(url_for('warranty', serial=serial))

@app.route('/warranty', methods=['GET', 'POST'])
def warranty():

    # return render_template('warranty.html')

    serial = request.args.get('serial')
    import sqlite3

    conn = sqlite3.connect('spectrum.db')
    
    serial_model = conn.execute(f"SELECT * FROM ProductInfo WHERE SerialNo = '{serial}'").fetchall()
    monitor = serial_model[0][1]
    specs = conn.execute(f"SELECT * FROM MonitorInfo WHERE ModelNo = '{monitor}'").fetchall()
    order_email = conn.execute(f"SELECT * FROM SalesRecord WHERE SerialNo = '{serial}'").fetchall()

    conn.close()
    
    return render_template('warranty.html', serial_model=serial_model, specs=specs, order_email=order_email)

if __name__ == '__main__':
    app.run(debug=True)