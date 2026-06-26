from flask import Flask, render_template, request, redirect, session
from db import *
import uuid
import qrcode
import os

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return """
            <script>
                alert('Email already registered! Please Login');
                window.location='/register';
            </script>
            """

        cursor.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )
        conn.commit()

        return """
        <script>
            alert('Registration Successful!');
            window.location='/login';
        </script>
        """

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT id FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()

        if user:
            session["user_id"] = user[0]

            return """
            <script>
                alert('Login Successful!');
                window.location='/dashboard';
            </script>
            """
        else:
            return """
            <script>
                alert('Invalid Email or Password');
                window.location='/login';
            </script>
            """

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return """
        <script>
            alert('Please Login First!');
            window.location='/login';
        </script>
        """

    return render_template("dashboard.html")


@app.route("/book", methods=["GET", "POST"])
def book():

    if "user_id" not in session:
        return """
        <script>
            alert('Please Login First!');
            window.location='/login';
        </script>
        """

    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        date = request.form["date"]

        fare = 200
        ticket = str(uuid.uuid4())[:8]
        qr = qrcode.make(ticket)
        qr_path = f"static/qrcodes/{ticket}.png"
        qr.save(qr_path)

        cursor.execute(
            """
            INSERT INTO bookings
            (user_id, source, destination, journey_date, fare, ticket_number)
            VALUES(%s,%s,%s,%s,%s,%s)
            """,
            (session["user_id"], source, destination, date, fare, ticket)
        )

        conn.commit()

        return render_template(
        "success.html",
        ticket=ticket,
        qr_image=f"qrcodes/{ticket}.png"
)

    return render_template("book.html")

@app.route("/mytickets")
def mytickets():

    if "user_id" not in session:
        return redirect("/login")

    cursor.execute(
        """
        SELECT source,destination,journey_date,fare,ticket_number
        FROM bookings
        WHERE user_id=%s
        """,
        (session["user_id"],)
    )

    tickets = cursor.fetchall()

    return render_template("mytickets.html", tickets=tickets)

@app.route("/logout")
def logout():
    session.clear()

    return """
    <script>
        alert('Logged Out Successfully!');
        window.location='/login';
    </script>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)