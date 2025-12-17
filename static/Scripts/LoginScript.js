



function ChangeLoginType() {
    if (document.getElementById("LoginTitle").textContent == "Sign Up") {

        document.getElementById("LoginTitle").textContent = "Login";

        document.getElementById("LoginInput").value = "Login";
    }
    else {
        document.getElementById("LoginTitle").textContent = "Sign Up";

        document.getElementById("LoginInput").value = "Sign Up";
    }

}


