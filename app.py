from flask import Flask, render_template
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
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",items=listed_items)

if __name__ == "__main__":
    app.run(debug=True)