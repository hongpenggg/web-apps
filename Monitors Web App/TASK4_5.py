# Task 4.5

from flask import Flask, render_template, request, redirect, url_for

def valid(serial):
    d = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 1,
        "K": 2,
        "L": 3,
        "M": 4,
        "N": 5,
        "O": 6,
        "P": 7,
        "Q": 8,
        "R": 9,
        "S": 2,
        "T": 3,
        "U": 4,
        "V": 5,
        "W": 6,
        "X": 7,
        "Y": 8,
        "Z": 9,
    }

    weights = {
        1: 8,
        2: 7,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 9,
        9: 4,
    }

    digits = {
        0: "S",
        1: "P",
        2: "E",
        3: "C",
        4: "T",
        5: "R",
        6: "U",
        7: "M",
        8: "X",
        9: "Y",
        10: "Z",
    }

    if len(serial) == 0:
        return "Presence check failed. Please enter the serial number of the product."
    
    elif len(serial) != 14:
        return "Length check failed. Please make sure the serial no. has 14 characters."
    
    elif serial[:4:] != "SPEC" or serial[:4:].lower() != "spec":
        return "Format check failed. Please make sure the serial no. starts with 'SPEC'."
    
    for i in set(serial):
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890":
            return "Format check failed. Please make sure the serial no. contains only alphanumeric characters."
    
    check_digit = serial[-1]
    check_serial = serial[4:-1:]

    check_sum = 0

    for i in range(len(check_serial)):
        if check_serial[i].isalpha():
            digit = d[check_serial[i].upper()]
            w = weights[i+1]
            check_sum += digit*w

        else:
            check_sum += int(check_serial[i])*weights[i+1]
    
    # check_sum = sum([d[check_serial[i].upper()]*weights[i+1] for i in range(len(check_serial))])
    
    if check_digit != digits[check_sum % 11]:
        return "Check digit failed. Please make sure the serial no. is valid."
    
    return True



app = Flask(__name__, template_folder='TASK4_5')
serial = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    serial = request.form['serial']
    msg = valid(serial)

    if msg == True:
        serial = request.form['serial']
        return redirect(url_for('warranty', serial=serial))
    
    else:
        return render_template('error.html', msg=msg)


@app.route('/warranty', methods=['GET', 'POST'])
def warranty():

    serial = request.args.get('serial')

    if request.method == 'GET':

        # return render_template('warranty.html')

        import sqlite3

        conn = sqlite3.connect('spectrum.db')
        
        serial_model = conn.execute(f"SELECT * FROM ProductInfo WHERE SerialNo = '{serial}'").fetchall()
        monitor = serial_model[0][1]
        specs = conn.execute(f"SELECT * FROM MonitorInfo WHERE ModelNo = '{monitor}'").fetchall()
        order_email = conn.execute(f"SELECT * FROM SalesRecord WHERE SerialNo = '{serial}'").fetchall()

        conn.close()
        
        return render_template('warranty.html', serial_model=serial_model, specs=specs, order_email=order_email)
    
    yap = request.form['yap']
    return redirect(url_for('ack', yap=yap, serial=serial))


@app.route('/ack', methods=['GET', 'POST'])
def ack():
    yap = request.args.get('yap')
    serial = request.args.get('serial')

    import sqlite3
    from datetime import date

    conn = sqlite3.connect('spectrum.db')

    conn.execute(f"""
CREATE TABLE IF NOT EXISTS `CustomerRequest` (
	`SerialNo`	TEXT NOT NULL,
	`RequestMessage`	TEXT NOT NULL,
	`RequestDate`	TEXT NOT NULL,
	PRIMARY KEY(`SerialNo`)
);
                 """)
    
    d = str(date.today())

    conn.execute(f"INSERT OR IGNORE INTO CustomerRequest (SerialNo, RequestMessage, RequestDate) VALUES ('{serial}', '{yap}', '{d}')")
    conn.commit()

    conn.close()

    return render_template("yap.html", serial=serial, yap=yap, d=d)


if __name__ == '__main__':
    app.run(debug=True)