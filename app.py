from flask import Flask, render_template, request, redirect

from flask_uploads import UploadSet, IMAGES, configure_uploads

from flask_wtf import FlaskForm



app = Flask(__name__)
import mysql.connector
app.config['SECRET_KEY'] = "norge123"
app.config['UPLOADED_PHOTOS_DEST'] = 'Images'

photos =  UploadSet('Photos', IMAGES)
configure_uploads(app, photos)


class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, 'Only images ')
        ]
    )



@app.route('/', methods=["GET","POST"])
def customers():
    if request.method == "POST":
        Direction = request.form['Redirect']
        if Direction == "delete":
            return redirect("/customers/delete")
        elif Direction == "add":
            return redirect("/customers/add")
        elif Direction == "update":
            return redirect("/customers/update")
    mydb = mysql.connector.connect(

        host = "10.200.14.24",
        port = 3306,
        user = "edmalemaLocal",
        password = "norge123",
        database = "flask_db"
    
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    result = mycursor.fetchall()
    return render_template('Index.html', customers = result)