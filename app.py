from flask import Flask, render_template, request, redirect

from flask_uploads import UploadSet, IMAGES, configure_uploads

from flask_wtf import FlaskForm
import mysql.connector

import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

env_User = os.getenv("user")
env_Password = os.getenv("password")
env_Host = os.getenv("host")



app = Flask(__name__)
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

        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password,
        database = "flask_db"
    
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    result = mycursor.fetchall()
    return render_template('Index.html', customers = result)