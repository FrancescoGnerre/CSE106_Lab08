from flask import Flask, request, render_template
from flask_admin import Admin
from flask_login import Login, login_required, logout_user, login_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class-enrollment.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)

# Many to many relationship table with Users and Classes
enrollment = db.Table('enrollment',
            db.Column("user_id", db.Integer, db.ForeignKey("users.user_id")),
            db.Column("class_id", db.Integer, db.ForeignKey("classes.class_id")),
            db.Column("grade", db.Integer) # This line may need fixing...
            )

# User table
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    acct_type = db.Column(db.Integer, nullable = False) # 0 - Student, 1 - Teacher, 2 - Admin
    enrollment = db.Relationship("Classes", secondary = enrollment, backref = db.backref("enrolled", lazy = "dynamic"))

    def __init__(self, username, password, acct_type):
        self.username = username
        self.password = password
        self.acct_type = acct_type

# Classes Table
class Classes(db.Model):
    class_id = db.Column(db.Integer, primary_key = True)
    class_name = db.Column(db.String, nullable = False)
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

# Login
@app.route("/")
def login():
    return render_template('login.html')

# Admin
@app.route('/admin')
def admin():
    return 0

@app.route('/admin/C', methods =['GET', 'POST'])
def admin():
    return 0

@app.route('/admin/R', methods =['GET'])
def admin():
    return 0

@app.route('/admin/U', methods =['GET', 'PUT'])
def admin():
    return 0

@app.route('/admin/D', methods =['DELETE'])
def admin():
    return 0

# Student
@app.route("/student/view")
def student_view():
    return render_template('student-view-classes.html')

@app.route("/student/edit")
def student_edit():
    return render_template('student-edit-classes.html')

# Teacher
@app.route("/teacher/view")
def teacher_view():
    return render_template('teacher-view-classes.html')

@app.route("/teacher/view/<class_name>")
def teacher_edit(class_name):
    return render_template('teacher-view-class-details.html')

# run
if __name__ == "__main__":
    app.run(debug=True)