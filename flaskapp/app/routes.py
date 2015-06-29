from flask import Flask, render_template
from forms import ContactForm
import requests

app = Flask(__name__)


app.secret_key = 'development key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form Posted'

    elif request.method == 'GET' :
        return render_template('contact.html',form=form)

if __name__ == '__main__' :
    app.run(debug=True)
