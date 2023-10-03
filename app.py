from flask import Flask, render_template,url_for,request,redirect
import random
from sqllite import SQLITE_UTILS
app = Flask(__name__)

sqlite = SQLITE_UTILS()
items_data = sqlite.readData()
@app.route("/",methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        item_name= request.form['todo_name']
        new_id = random.randint(1,1000)
        sqlite.insertData((item_name,new_id,0))

    items_data = sqlite.readData()
    return render_template("index.html",items=items_data)

@app.route("/clear",methods = ['POST'])
def clear():
    sqlite.clearData()
    return redirect(url_for('home'))  

@app.route("/check/<int:todo_id>",methods = ['POST'])
def check(todo_id):
    items_data = sqlite.readData()
    for item in items_data:
        if item[1]==todo_id:
            new_check = 1 - item[2]
            sqlite.updateChecked(item[0],item[1],new_check)
            break
    return redirect(url_for('home'))    

@app.route("/delete/<int:todo_id>",methods = ['POST'])
def delete(todo_id):
    items_data = sqlite.readData()
    for item in items_data:
        if item[1]==todo_id:
            sqlite.deleteData(todo_id)
            break
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)