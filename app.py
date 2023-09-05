#print("Hello World!")
from flask import Flask, render_template, request, redirect, url_for, flash

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField
from werkzeug.utils import secure_filename
#import os

# For NLP
from textblob import TextBlob

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

#from flask_uploads import ALL, UploadSet, configure_uploads
#from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'uploads'
#app.secret_key = 'some_secret_key'
app.config['SECRET_KEY'] = 'YourSecretKey'
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class NLPForm(FlaskForm):
    query = TextAreaField("Enter your query")
    document = FileField("Upload a document")
    submit = SubmitField("Ask")

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0', debug=True)