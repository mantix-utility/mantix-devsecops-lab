from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Intentionally vulnerable for SAST gate test
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    user = cursor.fetchone()
    connection.close()

    return str(user)


if __name__ == "__main__":
    app.run()
