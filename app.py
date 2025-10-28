from flask import Flask, render_template, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://clickuser:clickpass@localhost:5432/clickdb")


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


def get_click_count():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT count FROM clicks WHERE id = 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result["count"] if result else 0


def increment_click_count():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "UPDATE clicks SET count = count + 1, updated_at = CURRENT_TIMESTAMP WHERE id = 1 RETURNING count"
    )
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result["count"]


@app.route("/")
def index():
    count = get_click_count()
    return render_template("index.html", clicks=count)


@app.route("/click", methods=["POST"])
def click():
    count = increment_click_count()
    return jsonify({"clicks": count})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

