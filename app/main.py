from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="company",
        user="postgres",
        password="admin123"
    )
    return conn

@app.route("/")
def home():
    return "Flask + Postgres Connected"

@app.route("/init")
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Table created!"

@app.route("/add/<name>")
def add(name):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO employees (name) VALUES (%s)", (name,))

    conn.commit()
    cur.close()
    conn.close()

    return f"Added {name}"

@app.route("/employees")
def employees():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
