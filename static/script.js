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

