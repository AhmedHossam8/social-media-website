base_url = "http://127.0.0.1:8000"

function login() {
    var valid = true;
    formLabels = document.getElementsByTagName("label");

    var email = document.myForm.email.value;
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (email == "") {
        formLabels[0].innerHTML = "*Required";
        formLabels[0].style = "color: orange";
        valid = false;
    }
    else if (!re.test(email)) {
        formLabels[0].innerHTML = "Incorrect Email";
        formLabels[0].style = "color: orange";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[0].innerHTML = "";
    }

    var password = document.myForm.password.value;
    if (password == "") {
        formLabels[1].innerHTML = "*Required";
        formLabels[1].style = "color: orange";
        valid = false;
    }
    else {
        valid = (valid) ? true : false;
        formLabels[1].innerHTML = "";
    }

    if (valid) {
        fetch(base_url + '/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin' : '*'
            },
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        })
        .then(response => {
            if(response.status == 200){
                window.location.href = "../html/Main.html"
            }
            formLabels[1].innerHTML = "Wrong Credentials";
        })
    }
    
}