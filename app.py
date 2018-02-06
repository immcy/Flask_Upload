import os
from flask import Flask, request, render_template, redirect,\
    session, flash, abort
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config.from_pyfile('settings.py', silent=False)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'apk'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    # user_agent = request.headers.get('User_Agent')
    if request.method == 'POST':

        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            session['filename'] = filename
            return redirect('/')
        elif not file:
            return redirect('/')
        elif not allowed_file(file.filename):
            flash('file type not support')
            return redirect('/')

    filename = session.get('filename')
    print(filename)
    return render_template('test.html', filename=filename)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username is None or password is None:
            abort(400)  # 用户名或者密码为空
        elif username != "wt" or password != "123":
            return render_template('login.html')
        else:
            return redirect('/')
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
