#print("Hello World!")
from flask import Flask, render_template, request, redirect, url_for, flash

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField
from werkzeug.utils import secure_filename
import os

# For NLP
from textblob import TextBlob

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

#from flask_uploads import ALL, UploadSet, configure_uploads
#from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class NLPForm(FlaskForm):
    query = TextAreaField("Enter your query")
    document = FileField("Upload a document")
    submit = SubmitField("Ask")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Process the document here
            return redirect(url_for('results', filename=filename))
    return render_template('index.html')

@app.route('/results/<filename>')
def results(filename):
    # You can use TextBlob or other NLP libraries to process the file here
    # and show the results.
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        content = f.read()
        blob = TextBlob(content)
        # Do more with the content, analyze, etc.
    return render_template('results.html', content=content, analysis=blob.sentences)
  
if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host='0.0.0.0', debug=True)