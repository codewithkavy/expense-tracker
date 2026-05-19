from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount INTEGER,
            type TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
    expense = cursor.fetchone()[0] or 0

    balance = income - expense

    conn.close()

    return render_template(
        'index.html',
        transactions=transactions,
        income=income,
        expense=expense,
        balance=balance
    )

@app.route('/add', methods=['POST'])
def add_transaction():

    title = request.form['title']
    amount = request.form['amount']
    t_type = request.form['type']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions(title, amount, type) VALUES(?,?,?)",
        (title, amount, t_type)
    )

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)