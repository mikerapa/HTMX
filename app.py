from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Make `enumerate` available in Jinja2 templates
app.jinja_env.globals.update(enumerate=enumerate)

# In-memory "database"
todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    if task:
        todos.append(task)
    return render_template("_todo_list.html", todos=todos)

@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return render_template("_todo_list.html", todos=todos)

@app.route("/update/<int:todo_id>", methods=["POST"])
def update_todo(todo_id):
    new_task = request.form.get("task")
    if new_task and 0 <= todo_id < len(todos):
        todos[todo_id] = new_task
    return render_template("_todo_list.html", todos=todos)

@app.route("/clear", methods=["POST"])
def clear_todos():
    todos.clear()
    return render_template("_todo_list.html", todos=todos)

if __name__ == "__main__":
    print("Running app.py")
    app.run(debug=True)
