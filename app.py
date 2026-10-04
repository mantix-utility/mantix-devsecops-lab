from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Secure query using parameterized SQL
    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )

    user = cursor.fetchone()
    connection.close()

    return str(user)


if __name__ == "__main__":
    app.run()
