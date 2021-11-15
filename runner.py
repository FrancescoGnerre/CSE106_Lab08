from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class-enrollment.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# User table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    acct_type = db.Column(db.Integer, nullable = False) # 0 - Student, 1 - Teacher, 2 - Admin

    def __init__(self, username, password, acct_type):
        self.username = username
        self.password = password
        self.acct_type = acct_type

# Classes Table
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    teacher = db.Column(db.String, nullable = False)
    time = db.Column(db.String, nullable = False)
    enrolled = db.Column(db.Integer, nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

    def __init__(self, name, teacher, time, enrolled, capacity):
        self.name = name
        self.teacher = teacher
        self.time = time
        self.enrolled = enrolled
        self.capacity = capacity

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