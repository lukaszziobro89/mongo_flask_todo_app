from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongo_db:27017/')

todos = client.todo_db.list_of_todos


@app.route('/')
def index():
    todo_item = todos.find_one()
    return str(todo_item)


@app.route('/test')
def sample():
    return render_template('index.html')


@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('add-todo')
    print(todo_item)
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/some_endpoint')
def some_endpoint():
    return "VVV"


app.run(host='0.0.0.0', port=5000, debug=True)
