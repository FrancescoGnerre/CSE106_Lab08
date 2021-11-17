var curr_name = "";
var curr_password = "";
var home_password = "";

// sets name to be inputted username
function setName(){
	curr_name = document.getElementById("user_name").value;
}
// sets password to be inputted password
function setPassword(){
	curr_password = document.getElementById("password").value;
}
// sets home password to be the real password
function getPassword(newPassword){
    home_password = newPassword;
}
// prints for debugging
function consolePrint(x){
	console.log(x);
}

// student view add/drop class
$("#s_edit_classes").on("click", function(){
	$.ajax({
		url: "http://127.0.0.1:5000/student",
		type: "GET",
		success: function(){
            window.location.href = "http://127.0.0.1:5000/student/courses"
        }, 
        error: function(status, error){
            alert(error)
        }
	})
});

function s_add_class_func(){
	var target_class = document.getElementById("desired_class").innerHTML;
	consolePrint(target_class)
	alert(target_class)
}

function s_drop_class_func(){
	alert("Access Denied")
}

// student edit back to view
$("#s_view_classes").on("click", function(){
	consolePrint("TEST")
	$.ajax({
		url: "http://127.0.0.1:5000/student/courses",
		type: "GET",
		success: function(){
            window.location.href = "http://127.0.0.1:5000/student"
        },  
        error: function(status, error){
            alert(error)
        }
	})
});

// When login button is clicked...
$("#loginbutton").on("click", function(){
    let username = $("#user_name").val();
    let password = $("#password").val()
    if (username !== "" && password !== "") {
        $.ajax({
            url: "http://127.0.0.1:5000/",
            type: "POST",
            data: JSON.stringify({"username" : username, "password" : password}),
            contentType: "application/JSON",
            success: function(response){
                window.location.href = "http://127.0.0.1:5000/" + response
            }, 
            error: function(status, error){
                alert(error)
            }
        });
    }
    else{
        document.getElementById('xyz').play();
        alert('haha') 
    }
});

// When logout button on Admin is clicked...
$("#logoutAdmin").on("click", function(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When logout button on Student View classes is clicked...
$("#logoutStudentView").on("click", function(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When logout button on Student Edit classes is clicked...
$("#logoutStudentEdit").on("click", function(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When logout button on Teacher Details is clicked...
$("#logoutTeacherDetails").on("click", function(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When logout button on Teacher View is clicked...
$("#logoutTeacherView").on("click", function(){
    $.ajax({
        url: "http://127.0.0.1:5000/logout",
        type: "GET",
        success: function(response){
            window.location.href = "http://127.0.0.1:5000/" + response
        }, 
        error: function(status, error){
            alert(error)
        }
    });
});

// When Admin uploads new user
$("#admin_newuser").on("click", function(){
    let username = $("#add_username").val();
    let name = $("#add_name").val();
    let password = $("#add_password").val();
    let acct_type = $("#add_acct_type").val()
    if (username !== "" && name !== "" && password !== "" && acct_type !== ""){
        $.ajax({
            url: "http://127.0.0.1:5000/admin",
            type: "POST",
            data: JSON.stringify({"username" : username, "name" : name, "password" : password, "acct_type" : acct_type, "post" : "user"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Successfully Added User!")
            },
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When Admin uploads new class
$("#admin_newclass").on("click", function(){
    let classname = $("#add_class_name").val();
    let time = $("#add_time").val();
    let capacity = $("#add_capacity").val();
    let enrollment = $("#add_current_enrollment").val();
    let teacher = $("#add_teacher").val();
    if (classname !== "" && time !== "" && capacity !== "" && enrollment !== "" && teacher !== ""){
        $.ajax({
            url: "http://127.0.0.1:5000/admin",
            type: "POST",
            data: JSON.stringify({"classname" : classname, "time" : time, "capacity" : capacity, "enrollment" : enrollment, "teacher" : teacher, "post" : "class"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Successfully Added Class!")
            },
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When Admin enrolls student in class
$("#admin_enroll").on("click", function(){
    let classname = $("#enroll_classname").val();
    let username = $("#enroll_user_name").val()
    let grade = $("#enroll_grade").val()
    if (classname !== "" && username !== "" && grade !== ""){
        $.ajax({
            url: "http://127.0.0.1:5000/admin",
            type: "POST",
            data: JSON.stringify({"classname" : classname, "username" : username, "grade" : grade, "post" : "enroll"}),
            contentType: "application/JSON",
            success: function(response){
                alert("Successfully Enrolled User in Class!")
            },
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// Teacher editing grades
$("#grade_change").on("click", function(){
    let grade = $("#edit_grade").val()
    let student = $("#student_name").val()
    let course_name = document.getElementById("course_name").innerHTML
    if (student !== "" && grade !== ""){
        $.ajax({
            url: "http://127.0.0.1:5000/teacher/" + course_name,
            type: "PUT",
            data: JSON.stringify({"name" : student, "grade" : grade}),
            contentType: "application/JSON",
            success: function(response){
                alert("Successfully Changed Student Grade!")
                window.location.href = "http://127.0.0.1:5000/teacher/" + course_name
            },
            error: function(status, error){
                alert(error)
            }
        });
    }
});

// When Admin edits a user
$("#update_user").on("click", function(){
    let orig_username = $("#update_original_user").val()
    let new_username = $("#update_new_user").val()
    let new_name = $("#update_new_name").val()
    let new_password = $("#update_new_password").val()
    let new_acct = $("#update_new_type").val()
    $.ajax({
        url: "http://127.0.0.1:5000/admin",
        type: "PUT",
        data: JSON.stringify({"original_name" : orig_username, "new_username" : new_username, "new_name" : new_name, "new_password" : new_password, "new_acct" : new_acct, "put" : "user"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Successfully Edited User!")
        },
        error: function(status, error){
            alert(error)
        }
        });
    });

// When Admin edits a class
$("#update_class").on("click", function(){
    let orig_class = $("#original_class_name").val()
    let new_class = $("#new_class_name").val()
    let new_teacher = $("#new_teacher").val()
    let new_time = $("#new_time").val()
    let new_enrolled = $("#new_enrolled").val()
    let new_capacity = $("#new_capacity").val()
    $.ajax({
        url: "http://127.0.0.1:5000/admin",
        type: "PUT",
        data: JSON.stringify({"original_class" : orig_class, "new_class" : new_class, "new_teacher" : new_teacher, "new_time" : new_time, "new_enrolled" : new_enrolled, "new_capacity" : new_capacity, "put" : "class"}),
        contentType: "application/JSON",
        success: function(response){
            alert("Successfully Edited Class!")
        },
        error: function(status, error){
            alert(error)
        }
        });
    });