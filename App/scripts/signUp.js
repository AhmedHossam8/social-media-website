base_url = "http://127.0.0.1:8000"

function signUp() {
    var valid = true;

    formLabels = document.getElementsByTagName("label");

    var firstName = document.myForm.firstName.value;
    if (firstName == "") {
        formLabels[0].innerHTML = "Required";
        formLabels[0].style = "color: red";
        valid = false;
    }
    else if (!isNaN(firstName)) {
        formLabels[0].innerHTML = "Text Only";
        formLabels[0].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[0].innerHTML = "";
    }

    var lastName = document.myForm.lastName.value;
    if (lastName == "") {
        formLabels[1].innerHTML = "Required";
        formLabels[1].style = "color: red";
        valid = false;
    }
    else if (!isNaN(lastName)) {
        formLabels[1].innerHTML = "Text Only";
        formLabels[1].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[1].innerHTML = "";
    }

    var email = document.myForm.email.value;
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (email == "") {
        formLabels[2].innerHTML = "Required";
        formLabels[2].style = "color: red";
        valid = false;
    }
    else if (!re.test(email)) {
        formLabels[2].innerHTML = "Incorrect Email";
        formLabels[2].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[2].innerHTML = "";
    }

    var password = document.myForm.password.value;
    if (password == "") {
        formLabels[3].innerHTML = "Required";
        formLabels[3].style = "color: red";
        valid = false;
    }
    else if (password.length < 8) {
        formLabels[3].innerHTML = "Must be greater than 8 characters";
        formLabels[3].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[3].innerHTML = "";
    }

    var passwordII = document.myForm.passwordII.value;
    if (passwordII == "") {
        formLabels[4].innerHTML = "Required";
        formLabels[4].style = "color: red";
        valid = false;
    }
    else if (passwordII.length < 8 || passwordII != password) {
        formLabels[4].innerHTML = "The Two Passwords are not the same";
        formLabels[4].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[4].innerHTML = "";
    }

    var mobile = document.myForm.mobile.value;
    if (isNaN(mobile)) {
        formLabels[5].innerHTML = "Numbers Only";
        formLabels[5].style = "color: red";
        valid = false;
    }
    else if (mobile == "") {
        formLabels[5].innerHTML = "Required";
        formLabels[5].style = "color: red";
        valid = false;
    }
    else if (mobile.length < 11 || mobile.length > 11) {
        formLabels[5].innerHTML = "Enter valid number";
        formLabels[5].style = "color: red";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[5].innerHTML = "";
    }

    if (valid) {
        fetch(base_url + '/auth/sign-up', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                "name": firstName + "-" + lastName,
                "email": email,
                "password": password
            })
        }).then(response => {
            if (response.status == 200) {
                window.location.href = "../html/Main.html"
            }
            formLabels[5].innerHTML = "Email exists";
            formLabels[5].style = "color: orange";
        })
    }
}