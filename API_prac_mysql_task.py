# 1. Write a program to insert a record in sql table via api database.
# 2. Write a program to update a record via api.
# 3. Write a program to delete a record via api.
# 4. Write a program to fetch a record via api.


from flask import Flask , request , jsonify
import mysql.connector as conn


app = Flask(__name__)

mydb = conn.connect(host="localhost", user = "root", password = "root")
cursor = mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mysqltable(name varchar(30), number int)")

# insert the data
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s,%s)", (name, number))
        mydb.commit()
        return jsonify(str('successfully inserted'))

# update the data
@app.route("/update" , methods= ['POST'])
def update():
    if request.method=='POST':
         get_name = request.json['get_name']
         cursor.execute("update tasksql.mysqltable set number = number + 500 where name = %s ",(get_name,))
         mydb.commit()
         return jsonify(str("updated successfully"))

# delete the data
@app.route("/delete" , methods= ['POST'])
def delete():
    name_del = request.json['name_del']
    cursor.execute("delete from tasksql.mysqltable where name = %s", (name_del,))
    mydb.commit()
    return jsonify(str("deleted successfully"))


# fetch the data
@app.route("/fetch" , methods= ['POST','GET'])
def fetch_data():
    cursor.execute("select * from tasksql.mysqltable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__ == "__main__":
    app.run()



