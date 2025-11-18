from flask import Flask, render_template, request, redirect
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import base64
from PIL import Image
import io
from io import BytesIO

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

def convertToJpeg(image):
    with BytesIO() as f:
        image.save(f, format='JPEG')
        return f.getvalue()


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
    Y = 0
    ImgList = []
    for i in result:
        image_data = result[Y][4]
        Y += 1
        binary_data = base64.b64decode(image_data)

        image = Image.open(io.BytesIO(binary_data))

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        ImgList.append(convertToJpeg(image))
    return render_template('Index.html', Data = result, Images = ImgList, x = 0) 



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
        Img_Data = base64.b64encode(Img_Data)
        
        

        
        
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