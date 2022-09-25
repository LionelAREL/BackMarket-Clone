base_url = "http://127.0.0.1:8000";

function load(url, element){
    fetch(url)
    .then((res) => {
        return res.text()
    })
    .then((res) => {
        console.log(res)
        element.innerHTML = res; 
    });
}

function update_cart() {
    load(base_url + "/shop/update-header",document.querySelector('header'));
}
function update_all() {
    location.reload();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const isResponseOk = (response) =>  {
    if (response.status >= 200 && response.status <= 299) {
        console.log(response);
        return response.json();
    } else {
        throw Error(response.statusText);
    }
};

  
function fetchUpdateCart(url) {
    let url_complete = 'http://127.0.0.1:8000' + url;
    console.log(url)
    fetch( url_complete, {
        method: "GET",
        headers: {
        "X-Csrftoken": getCookie('csrftoken'),
        },
        credentials: "include",
    })
    .then(isResponseOk)
    .then((data) => {
        console.log(data);
        update_cart();
        return data;
    })
    .catch((err) => {
        console.log(err);
    });
}
function fetchUpdateAll(url) {
    let url_complete = 'http://127.0.0.1:8000' + url;
    console.log(url)
    fetch( url_complete, {
        method: "GET",
        headers: {
        "X-Csrftoken": getCookie('csrftoken'),
        },
        credentials: "include",
    })
    .then(isResponseOk)
    .then((data) => {
        console.log(data);
        update_all();
        return data;
    })
    .catch((err) => {
        console.log(err);
    });
}
