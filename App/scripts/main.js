base_url = "http://127.0.0.1:8000"

loadUser()

function loadUser() {
    user_email = localStorage.getItem("email")
    fetch(base_url + '/user?' + new URLSearchParams({
        email: user_email
    }))
    .then(async response => {
        if (response.status == 200) {
            let json = await response.json();
            render_user(json)
        }
    })
}

function render_user(user){
    console.log(user)
    document.getElementById("name").innerText = user.name
    document.getElementById("profile-picture").innerHTML = '<img src="'+ user.photo_url +'" class="card-img-top" alt="Profile Picture">'
}