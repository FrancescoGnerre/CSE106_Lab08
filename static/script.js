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

function loginFunc(){
    setName();
    setPassword();
    getPassword("TEST");

    consolePrint(curr_password)
    consolePrint(home_password)
    consolePrint(curr_name)
    // no username or password detected
    if (curr_name === "" || curr_password === "")
        consolePrint("PLEASE ENTER USERNAME AND PASSWORD");
    // username DNE
    else if (curr_name === "DNE")
        consolePrint("DNE");
    // username exists, password is wrong
    else if (curr_password != home_password)
        consolePrint("BAD PASSWORD");
    // there is a match
    else if (curr_password === home_password)
        consolePrint("MATCH");
}

function logoutFunc(){
    curr_name = "";
    curr_password = "";
    home_password = "";
}