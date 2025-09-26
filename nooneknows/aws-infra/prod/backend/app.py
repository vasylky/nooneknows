from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# ініціалізація БД
def init_db():
    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    text TEXT
                )""")
    conn.commit()
    conn.close()

init_db()

# API для додавання повідомлення
@app.route("/api/messages", methods=["POST"])
def add_message():
    data = request.get_json()
    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (name, text) VALUES (?, ?)", 
              (data["name"], data["text"]))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"}), 201

# API для отримання всіх повідомлень
@app.route("/api/messages", methods=["GET"])
def get_messages():
    conn = sqlite3.connect("site.db")
    c = conn.cursor()
    c.execute("SELECT id, name, text FROM messages")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "text": r[2]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
