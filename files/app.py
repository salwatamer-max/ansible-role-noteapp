from flask import Flask, request, render_template
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

DB_PATH = '/opt/noteapp/notes.db'

# DB setup
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE notes (content TEXT, created_at TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute("INSERT INTO notes VALUES (?, ?)", (note, timestamp))
        conn.commit()
    c.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
