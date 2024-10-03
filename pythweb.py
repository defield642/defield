import sqlite3
from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()
conn.close()

# HTML templates
register_template = """
<!doctype html>
<title>Register</title>
<h2>Register</h2>
<form method=post>
  <input type=text name=username placeholder="Username" required>
  <input type=password name=password placeholder="Password" required>
  <input type=submit value=Register>
</form>
"""

login_template = """
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method=post>
  <input type=text name=username placeholder="Username" required>
  <input type=password name=password placeholder="Password" required>
  <input type=submit value=Login>
</form>
"""

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template_string(register_template)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('welcome'))
    return render_template_string(login_template)

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
