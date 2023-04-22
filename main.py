''' Import part starts'''
from flask import Flask,render_template,request,session,redirect,url_for,flash

#importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#importing flask login for encrypted & decrypted password stored in db
from flask_login import UserMixin

#for hashed function which helps in encryption & decryption
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


# For importing json file
import json

# For using deep learnig model
import os
import numpy as np
import matplotlib.pyplot as plt
import keras
import tensorflow
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import preprocess_input
from keras.models import Model, load_model
from keras.preprocessing import image
from keras_preprocessing.image import load_img, img_to_array


'''Import part ends'''


#My database connection
local_server = True
app = Flask(__name__)
app.secret_key = ''          # add any secret_key


#This is for unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


            
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/database_name'                                             
db=SQLAlchemy(app)         




class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(1000))



class Patient(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    fname=db.Column(db.String(15))
    lname=db.Column(db.String(15))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(10))
    date=db.Column(db.String(50),nullable=False)
    id=db.Column(db.Integer)
    number=db.Column(db.String(10))



@app.route('/')                    
def index():
    return render_template('index.html')




@app.route('/patient',methods=['POST','GET'])
@login_required
def patient():
    if request.method=="POST":
        em=current_user.email
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        age=request.form.get('age')
        gender=request.form.get('gender')
        date=request.form.get('date')
        id=request.form.get('id')
        number=request.form.get('number')
        user1=Patient.query.filter_by(email=em).first()       
        user2=Patient.query.filter_by(id=id).first()

        if user1 and user2:
            flash("Passenger Already Exist","warning")
            return render_template('/patient.html')
        

        query=db.engine.execute(f"INSERT INTO `patient` (`id`,`email`,`fname`,`lname`,`age`,`gender`,`date`,`number`) VALUES ('{id}','{em}','{fname}','{lname}','{age}','{gender}','{date}','{number}')")
        
        
        flash("Registered","info")
        return redirect('/upload')
        
     
    return render_template('patient.html')

    


# For uploading the image
@app.route('/upload', methods=['POST','GET'])  
@login_required                   
def upload():
    if request.method=="POST":
        filename = request.form.get('filename')
        model_name = request.form.get('model')
        
        
        if model_name == "CNN":
            model = load_model("bestmodel.h5")

            fileacc = open ('acc_cnn.txt', 'r')
            acc = fileacc.read()
            accuracy = f"Accuracy of CNN model is {acc}%"
            
            hfile = open ('h_cnn.txt', 'r')
            hstr = hfile.read()         # reads file in string
            h = json.loads(hstr)        # reads file in dictionary format
    

            # Plotting for accuracy
            plt.plot(h['accuracy'])
            plt.plot(h['val_accuracy'], c='red')
            plt.title("Accuracy Vs Validation_Accuracy for CNN")
            plt.legend(["accuracy", "val_accuracy"], loc ="lower right")
            plt.show()



            # Plotting for loss
            plt.plot(h['loss'])
            plt.plot(h['val_loss'], c='red')
            plt.title("Loss Vs Validation_Loss for CNN")
            plt.legend(["loss", "val_loss"], loc ="upper right")
            plt.show()


            # name of image to pass plotting image for respective model in result.html file
            img1 = "cnnoutput1.png"
            img2 = "cnnoutput2.png"



        elif model_name == "MobileNet":
            model = load_model("bestmodelmobilenet.h5")
            
            fileacc = open ('acc_mn.txt', 'r')
            acc = fileacc.read()
            accuracy=f"Accuracy of MobileNet is {acc}%"

            hfile = open ('h_mn.txt', 'r')
            hstr = hfile.read()         # reads file in string
            h = json.loads(hstr)        # reads file in dictionary format
        


            # Plotting for accuracy
            plt.plot(h['accuracy'])
            plt.plot(h['val_accuracy'], c='red')
            plt.title("Accuracy Vs Val_Accuracy for MobileNet")
            plt.legend(["accuracy", "val_accuracy"], loc ="lower right")
            plt.show()


            # Plotting for loss
            plt.plot(h['loss'])
            plt.plot(h['val_loss'], c='red')
            plt.title("Loss Vs Val_Loss for MobileNet")
            plt.legend(["loss", "val_loss"], loc ="upper right")
            plt.show()


            # name of image to pass plotting image for respective model in result.html file
            img1 = "mnoutput1.png"
            img2 = "mnoutput2.png"
        




        # Model Prediction Part
        # path of the image from user to trained model for prediction
        # filename is the image name taken in the form of input in form.
        path = "give_the_absolute_url_of_dataset_folder_here" + filename
        img = load_img(path,target_size= (224,224))

        i = img_to_array(img)/255
        input_arr = np.array([i])
        input_arr.shape


        pred = (model.predict(input_arr) > 0.5).astype("int32")[0][0]

        if pred==0:
            res="The MRI image is of healthy brain"
        else:
            res="The MRI image is of Brain tumor"


        # to display the image
        plt.imshow(input_arr[0])
        plt.title("Input Image")
        plt.show()


        return render_template('result.html', filename=filename, model_name=model_name , result=res , accuracy=accuracy , img1=img1 , img2=img2)

    return render_template('image.html')






#For signup i.e signup.html
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        #used to insert values in db after signup
        new_user = db.engine(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")

        flash("Signup Successfully. Please Login","success")
        return render_template('login.html')    

    return render_template('signup.html')



#For login i.e login.html page
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
 
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Successful","primary")
            return redirect(url_for('index'))
        else:
            flash("Invalid Credentials","danger")
            return render_template('login.html')

    return render_template('login.html')



#For logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful","warning")
    return redirect(url_for('login'))


#For deleting account
@app.route('/deleteacc')
@login_required
def deleteacc():
    cid = current_user.id
    em = current_user.email
    db.engine.execute(f"DELETE FROM `user` WHERE `user`.`id`= {cid}")
    db.engine.execute(f"DELETE FROM `patient` WHERE `patient`.`email`= '{em}'")
    flash("Your Account is Deleted Successfully","warning")
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)     #For running this flask code