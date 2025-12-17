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


LikeList = []



def OpenMysql():
    mydb = mysql.connector.connect(

        host = env_Host,
        port = 3306,
        user = env_User,
        password = env_Password,
        database = "reviewdb"

    )

    mycursor = mydb.cursor()

    return mydb, mycursor



def Like(Post):
    for i in LikeList:
        print(i)
        if i == Post: return
    LikeList.append(Post)

    mydb, mycursor = OpenMysql()


    sql = f"UPDATE games SET likes = likes + 1 WHERE id = '{int(Post)}'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    mycursor.close()
    mydb.close()


def ImageLoader():
    mydb, mycursor = OpenMysql()

    mycursor.execute("SELECT * FROM games")
    result = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    Y = 0
    ImgList = []
    for i in result:
        image_data = result[Y][4]
        Y += 1
        binary_data = base64.b64decode(image_data)

        image = Image.open(io.BytesIO(binary_data))

        if image.mode == 'RGBA':
            image = image.convert('RGB')

        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        jpeg_bytes = buffer.getvalue()
        jpeg_b64 = base64.b64encode(jpeg_bytes).decode("utf-8")

        ImgList.append(jpeg_b64)

    return [result, ImgList]



@app.route('/', methods=["GET","POST"])
def Index():
    if request.method == "POST":
        SubmitInfo = request.form.get('submit')
        if SubmitInfo == "upload":
            return redirect("/upload")
        elif SubmitInfo == "login":
            return redirect("/login?ErrorType = None")
        
        LikeInfo = request.form.get('Like')
        print(LikeInfo)
        Like(LikeInfo)
        if LikeInfo != None:
            return render_template('Index.html', SQLData = ImageLoader()[0], Images = ImageLoader()[1])
            


    
    return render_template('Index.html', SQLData = ImageLoader()[0], Images = ImageLoader()[1]) 





@app.route('/upload', methods=["GET","POST"])
def UploadImage():
    if request.method == "POST":

        pic = request.files['pic']
        if not pic:
            return "no img"
        
        print(pic)
        GameName = request.form['name']
        Description = request.form['description']
        Rating = int(request.form['review'])
        Img_Data = pic.read()
        Img_Data = base64.b64encode(Img_Data)
                
        
        #try:
        mydb, mycursor = OpenMysql()


        sql = "INSERT INTO games (game, info, review, image, likes) VALUES (%s, %s, %s, %s, %s)"
        val = (GameName, Description, Rating, Img_Data, 0)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        mydb.close()
        return redirect("/")
        #except:
        #    return "Something went wrong"
    return render_template("UploadSite.html")



@app.route('/login', methods=["GET","POST"])
def LoginSite():
    if request.method == "POST":
        
        Username = request.form['username']
        Password = request.form['password']
        
        LoginSignUp = request.form['type']

        if LoginSignUp == 'Login':
            mydb, mycursor = OpenMysql()

            mycursor.execute("SELECT * FROM users")
            result = mycursor.fetchall()
            mycursor.close()
            mydb.close()

            LoggedIn = False
            Y = 0
            for i in result:
                if Username == result[Y][1] and Password == result[Y][2]:
                    LoggedIn = True
                    break
                Y += 1
            if LoggedIn:
                return redirect("/")
            else:
                return render_template("Login.html", ErrorType = "Login")           

        else:

            mydb, mycursor = OpenMysql()


            mycursor.execute("SELECT * FROM users")
            result = mycursor.fetchall()
            mycursor.close()
            mydb.close()
            Eksists = False
            Y = 0
            for i in result:
                if Username == result[Y][1]:
                    Eksists = True
                    break
                Y += 1
            
            if not Eksists:
                mydb, mycursor = OpenMysql()

                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                val = (Username, Password)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                mycursor.close()
                mydb.close()
                return redirect("/")

            else:
                return render_template("Login.html", ErrorType = "SignUp")
        


    return render_template("Login.html", ErrorType = "None")