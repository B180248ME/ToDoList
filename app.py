from flask import Flask, render_template,url_for,request,redirect
import random
app = Flask(__name__)

listed_items = [
    {
        'name':'first-item',
        'id':1,
        'checked':False
    },
    {
        'name':'second-item',
        'id':2,
        'checked':True
    }
]
@app.route("/",methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        item_name= request.form['todo_name']
        new_id = random.randint(1,1000)
        new_item = {
            'name':item_name,
            'id':new_id,
            'checked':False
        }
        listed_items.append(new_item)
    return render_template("index.html",items=listed_items)

@app.route("/check/<int:todo_id>",methods = ['POST'])
def reverse_check(todo_id):
    for item in listed_items:
        if item['id']==todo_id:
            item['checked']=not item['checked']
            break
    return redirect(url_for('home'))    

@app.route("/delete/<int:todo_id>",methods = ['POST'])
def delete_item(todo_id):
    for item in listed_items:
        if item['id']==todo_id:
            listed_items.remove(item)
            break
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)