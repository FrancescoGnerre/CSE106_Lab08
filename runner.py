from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from flask_admin import Admin
from flask_login import login_required, logout_user, login_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class-enrollment.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)

# Many to many relationship table with Users and Classes
class Enrollment(db.Model):
    __tablename__ = "Enrollment"
    users_id = db.Column(db.ForeignKey("Users.user_id"), primary_key = True)
    classes_id = db.Column(db.ForeignKey("Courses.class_id"), primary_key = True)
    grade = db.Column(db.Integer, nullable = False)

    def __init__(self, user_id, classes_id, grade):
        self.users_id = user_id
        self.classes_id = classes_id
        self.grade = grade

# User table
class Users(db.Model):
    __tablename__ = "Users"
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    acct_type = db.Column(db.Integer, nullable = False) # 0 - Student, 1 - Teacher, 2 - Admin

    def __init__(self, username, name, password, acct_type):
        self.username = username
        self.name = name
        self.password = password
        self.acct_type = acct_type

    def check_password(self, password):
        return self.password == password

# Classes Table
class Courses(db.Model):
    __tablename__ = "Courses"
    class_id = db.Column(db.Integer, primary_key = True)
    class_name = db.Column(db.String, nullable = False)
    teacher = db.Column(db.String, nullable = False)
    time = db.Column(db.String, nullable = False)
    enrolled = db.Column(db.Integer, nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

    def __init__(self, class_name, teacher, time, enrolled, capacity):
        self.class_name = class_name
        self.teacher = teacher
        self.time = time
        self.enrolled = enrolled
        self.capacity = capacity

# Login
@app.route("/")
def login():
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Admin
@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/admin/C', methods =['GET', 'POST'])
@login_required
def admin_create():
    return 0

@app.route('/admin/R', methods =['GET'])
@login_required
def admin_read():
    return 0

@app.route('/admin/U', methods =['GET', 'PUT'])
@login_required
def admin_update():
    return 0

@app.route('/admin/D', methods =['DELETE'])
@login_required
def admin_delete():
    return 0

# Student
@app.route("/student/view")
@login_required
def student_view():
    return render_template('student-view-classes.html')

@app.route("/student/edit")
@login_required
def student_edit():
    return render_template('student-edit-classes.html')

# Teacher
@app.route("/teacher/view")
@login_required
def teacher_view():
    return render_template('teacher-view-classes.html')

@app.route("/teacher/view/<class_name>")
@login_required
def teacher_edit(class_name):
    return render_template('teacher-view-class-details.html')

# Run
if __name__ == "__main__":
    # db.create_all() # Only need this line if db not created
    app.run(debug=True)