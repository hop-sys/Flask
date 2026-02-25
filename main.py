import os

from flask import *
import pymysql
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route("/api/add_novels", methods=["POST"])
def add_novels():
    if request.method == "POST":
        name=request.form["name"]
        author=request.form["author"]
        publisher=request.form["publisher"]
        publicationyear=request.form["publicationyear"]
        price=request.form["price"]
        stock=request.form["stock"]
        photo=request.files["photo"]
        
        # extract the file name of the product photo
        filename = photo.filename
        # by use of the os module we can extract the file path where the image is currently saved
        # by use of an os module we can extract the file path where the image is currently saved.
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # save the product photo image into the new location
        photo.save(photo_path)

        # print them out to test whether you are receiving the details sent with the request.
        # print(name, author, publisher, publicationyear, price, stock, photo)

        # establish a connection to the db
        connection=pymysql.connect(host="localhost", user="root", password="", database="online")

        # create a cursor
        cursor=connection.cursor()

        # structure an sql query to insert the product details to the database
        sql = "INSERT INTO novels(name, author, publisher, publicationyear, price, stock, photo) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # create the tuple that will hold the data from the form which are currently being held on different variables declaired.
        data = (name, author, publisher, publicationyear, price, stock, filename)
        # use the cursor to execute the sql as you replace the placeholders with actual data.
        cursor.execute(sql, data)

        # commit the changes to the database
        connection.commit()


        return jsonify({"message" : "Novel added successfully"})
    


# below is a route for adding consoles
@app.route("/api/add_consoles", methods=["POST"])
def add_consoles():
    if request.method=="POST":
        name=request.form["name"]
        brand=request.form["brand"]
        storage=request.form["storage"]
        warranty=request.form["warranty"]
        price=request.form["price"]
        stock=request.form["stock"]
        photo=request.files["photo"]

        # extract the file name of the console photo
        filename = photo.filename
        # by use of the os module we can extract the file path where the image is currently saved
        # by use of an os module we can extract the file path where the image is currently saved.
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # save the product photo image into the new location
        photo.save(photo_path)

        # print them out to test whether you are receiving the details sent with the request.
        print(name, brand, storage, warranty, price, stock, photo)

        # establish a connection to the db
        connection=pymysql.connect(host="localhost", user="root", password="", database="online")

        # create a cursor
        cursor=connection.cursor()

        # structure an sql query to insert the product details to the database
        sql = "INSERT INTO consoles(name,brand, storage, warranty, price, stock, photo) VALUES ( %s, %s,%s, %s, %s, %s, %s)"

        # create the tuple that will hold the data from the form which are currently being held on different variables declaired.
        data = (name, brand, storage, warranty, price, stock, filename)
        # use the cursor to execute the sql as you replace the placeholders with actual data.
        cursor.execute(sql, data)

        # commit the changes to the database
        connection.commit()


        return jsonify({"message" : "Console added successfully"})
    



# run the application
app.run(debug=True)