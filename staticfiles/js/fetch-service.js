import { environment } from "./environment";


const isResponseOk = (response) =>  {
    if (response.status >= 200 && response.status <= 299) {
        console.log(response);
        return response.json();
    } else {
        throw Error(response.statusText);
    }
};

console.log("123")
  
//add to cart
function addToCart(productId) {
    console.log(cookies.get("csrftoken"))
    return fetch(environment.base_url + `add-to-cart/${productId}` , {
        method: "GET",
        headers: {
        "X-Csrftoken": cookies.get("csrftoken"),
        },
        credentials: "include",
    })
    .then(isResponseOk)
    .then((data) => {
        console.log(data);
        return data;
    })
    .catch((err) => {
        console.log(err);
    });
}