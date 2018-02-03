from flask import Flask, request, render_template, redirect, session, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'string'

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


    else:
        filename = None
    print(filename)
    filename = session.get('filename')
    return render_template('test.html', filename=filename)


app.run(debug=True)