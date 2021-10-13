from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://mongo_db:27017/')

todos = client.todo_db.list_of_todos


@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('add-todo')
    todos.insert_one({'description': todo_item, 'complete': False})
    return redirect(url_for('home'))


@app.route('/complete_todo/<oid>')
def complete_todo(oid):
    todo_item = todos.find_one({'_id': ObjectId(oid)})
    todo_item['complete'] = True
    todos.save(todo_item)
    return redirect(url_for('home'))


@app.route('/delete_completed')
def delete_completed():
    todos.delete_many({'complete': True})
    return redirect(url_for('home'))


@app.route('/delete_all')
def delete_all():
    todos.remove()
    return redirect(url_for('home'))


@app.route('/home')
def home():
    todos_list = todos.find()
    return render_template('home.html', todos_list=todos_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
