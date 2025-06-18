from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('stock.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        barcode = request.form['barcode']
        action = request.form['action']
        quantity = int(request.form['quantity'])

        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM stock WHERE barcode = ?', (barcode,))
        item = c.fetchone()

        if item:
            new_qty = item['quantity'] + quantity if action == 'in' else item['quantity'] - quantity
            new_qty = max(0, new_qty)  # Prevent negative stock
            c.execute('UPDATE stock SET quantity = ? WHERE barcode = ?', (new_qty, barcode))
            conn.commit()
            message = f"{item['name']} updated to quantity: {new_qty}"
        else:
            message = "⚠️ Barcode not found in database."

        conn.close()

        # ✅ Redirect to avoid resubmission
        return redirect(f"/?message={message}")

    # Handle GET request
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM stock')
    stock = c.fetchall()
    conn.close()

    # Get message from redirected GET
    message = request.args.get('message', '')

    return render_template('index.html', stock=stock, message=message)

if __name__ == '__main__':
    app.run(debug=True)
