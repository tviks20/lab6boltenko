import sqlite3

conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gift TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL
)
''')

gifts_data = [
    ('Иван Иванович', 'Санки', 2000.0, 'куплен'),
    ('Ирина Сергеевна', 'Цветы', 3000.0, 'не куплен'),
    ('Петр Петрович', 'Книга', 1500.0, 'куплен'),
    ('Анна Андреевна', 'Игрушка', 1200.0, 'не куплен'),
    ('Сергей Сергеевич', 'Часы', 5000.0, 'куплен'),
    ('Ольга Владимировна', 'Косметика', 2500.0, 'не куплен'),
    ('Дмитрий Дмитриевич', 'Ноутбук', 30000.0, 'куплен'),
    ('Елена Викторовна', 'Сумка', 4000.0, 'не куплен'),
    ('Алексей Алексеевич', 'Телефон', 20000.0, 'куплен'),
    ('Мария Ивановна', 'Подарочная карта', 1000.0, 'не куплен')
]

cursor.executemany('INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)', gifts_data)
conn.commit()
conn.close()

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM gifts')
    gifts = cursor.fetchall()
    conn.close()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)



