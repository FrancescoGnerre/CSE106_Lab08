from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class-enrollment.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/hello/<name>') 
def hello_name(name):
    return 'Hello %s!' % name 

@app.route("/")
def login():
    return render_template('login.html')

@app.route('/admin', methods =['GET'])
def admin():
    return render_template('admin.html')

@app.route("/student/view")
def student_view():
    return render_template('student-view-classes.html')

@app.route("/student/edit")
def student_edit():
    return render_template('student-edit-classes.html')

@app.route("/teacher/view")
def teacher_view():

    return render_template('teacher-view-classes.html')

@app.route("/teacher/view/<class_name>")
def teacher_edit(class_name):
    return render_template('teacher-view-class-details.html')

if __name__ == "__main__":
    app.run(debug=True)