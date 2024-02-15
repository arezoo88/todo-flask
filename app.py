from flask import Flask,render_template

app = Flask(__name__)


@app.route('/home')
def home():
    # return 'Hello World...'
    return render_template('home.html',name='arezoo')


@app.route('/about')
def about():
    return render_template('about.html')