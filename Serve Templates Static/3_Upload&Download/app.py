from io import BytesIO
import psycopg2
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:08012002@localhost/postgres'  # Replace with your actual username, password, and database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress a warning

# Create a SQLAlchemy instance
db = SQLAlchemy(app)


class Gambar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    data = db.Column(db.LargeBinary)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		upload = Gambar(filename=file.filename, data=file.read())
		db.session.add(upload)
		db.session.commit()
		return f'Uploaded: {file.filename}'
	return render_template('index.html')


@app.route('/download/<upload_id>')
def download(upload_id):
	upload = Gambar.query.filter_by(id=upload_id).first()
	return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True )

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)