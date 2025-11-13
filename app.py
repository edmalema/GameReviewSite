from flask import Flask, render_template, request, redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


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
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File should not be empty')
        ]
    )
    submit = SubmitField('Upload')



@app.route('/', methods=["GET","POST"])
def Index():
    mydb = mysql.connector.connect(

        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password,
        database = "reviewdb"
    
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM games")
    result = mycursor.fetchall()
    return render_template('Index.html', Data = result)



@app.route('/upload', methods=["GET","POST"])
def UploadImage():
    if request.method == "POST":
        print("balz")
        pic = request.files['pic']
        if not pic:
            return "no img"
        print("img")
        
        print(pic)
        GameName = request.form['name']
        Description = request.form['description']
        Rating = int(request.form['review'])
        Img_Data = pic.read()

        #try:
        mydb = mysql.connector.connect(

            host = env_Host,
            port = 3306,
            user = env_User,
            password = env_Password,
            database = "reviewdb"

        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO games (game, info, review, image) VALUES (%s, %s, %s, %s)"
        val = (GameName, Description, Rating, Img_Data)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        mydb.close()
        return redirect("/")
        #except:
        #    return "Something went wrong"
    return render_template("UploadSite.html")