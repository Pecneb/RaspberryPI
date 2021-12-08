from flask import Flask, request, render_template, url_for, redirect
from db_operations import add_user, get_events
app = Flask(__name__)

HOST = '127.0.0.1'
PORT = 5000

@app.route('/')
def index():
    events = get_events()
    return render_template('index.html', events = events)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        ret = add_user(username, email, password, 0)
        if ret != False:
            return f'<p>Regisration successful!</p><p>Username: {username} Email: {email}</p>'
        return '<p>This should not happen.'
    return render_template('email.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
