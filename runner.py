from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from flask_admin import Admin
from flask_login import login_required, logout_user, login_user, current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# text to commit
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///class-enrollment.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'keep it secret, keep it safe'
db = SQLAlchemy(app)

@login_manager.user_loader 
def load_user(user_id): 
    return Users.query.filter_by(user_id = user_id).first()

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
class Users(UserMixin, db.Model):
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

    def get_id(self):
        return self.user_id

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
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        user = Users.query.filter_by(username=data['username']).first() 
        if user is None or not user.check_password(data['password']): 
            return (url_for('login'))[1:]
        login_user(user)
        if user.acct_type == 0:
            return url_for('student_view')[1:]
        elif user.acct_type == 1:
            return url_for('teacher_view')[1:]
        else:
            return url_for('admin')[1:]
    else:   
        return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return url_for('login')[1:]

# Admin
@app.route('/admin', methods = ["GET", "POST"])
@login_required
def admin():
    if request.method == "POST":
        data = request.get_json()
        if data["post"] == "user":
            user = Users.query.filter_by(username = data["username"]).first()
            if user is None:
                user = Users(data["username"], data["name"], data["password"], int(data["acct_type"]))
                db.session.add(user)
                db.session.commit()
                return "success"
        elif data["post"] == "class":
            course = Courses.query.filter_by(class_name = data["classname"]).first()
            if course is None:
                course = Courses(data["classname"], data["teacher"], data["time"], int(data["enrollment"]), int(data["capacity"]))
                db.session.add(course)
                db.session.commit()
                return "success"
        else:
            user = Users.query.filter_by(username = data["username"]).first()
            course = Courses.query.filter_by(class_name = data["classname"]).first()
            if user is not None and course is not None and user.acct_type == 0:
                enroll = Enrollment(user.user_id, course.class_id, int(data["grade"]))
                db.session.add(enroll)
                db.session.commit()
                return "success"
    else: 
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
@app.route("/student")
@login_required
def student_view():
    listCourses = []
    enrolled_classes = Enrollment.query.filter_by(users_id = current_user.user_id)
    for course in enrolled_classes:
        listCourses.append(course.classes_id)
    classes = Courses.query.filter(Courses.class_id.in_(listCourses))
    return render_template('student-view-classes.html', courses = classes)

@app.route("/student/courses")
@login_required
def student_edit():
    return render_template('student-edit-classes.html', courses = Courses.query.all())

# Teacher
@app.route("/teacher")
@login_required
def teacher_view():
    taught_classes = Courses.query.filter_by(teacher = current_user.name)
    return render_template('teacher-view-classes.html', courses = taught_classes)

@app.route("/teacher/<class_name>")
@login_required
def teacher_edit(class_name):
    # More functionality needs to be added here...
    return class_name

# Run
if __name__ == "__main__":
    # db.create_all() # Only need this line if db not created
    app.run(debug=True)