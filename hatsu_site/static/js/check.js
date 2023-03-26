const listBtnIcon = document.querySelectorAll('#btn-icon');
const modal = document.querySelector('#loginModal');

async function sendRequest(method, url, headers, body = "") {
    await fetch(url, {
        method: method,
        headers: headers,
        credentials: 'same-origin',
        body: body,

    }).then(response => {
        console.log(response.json());
    }).then(data => {
        console.log(data);
    }).catch(error => {
        console.error(error);
    });
}

listBtnIcon.forEach(btnIcon => {
    btnIcon.addEventListener('click', async (event) => {
        const cookie = document.cookie.split(';')
        let csrf_token = "";
        cookie.forEach(value => {
            const key = value.split("=");
            if (key[0] === "csrftoken") {
                csrf_token = key[1];
            }
        })
        if (csrf_token === "") {
            return
        }

        const cardId = event.target.closest('.card').id
        let element_count_like = event.target.parentNode.querySelector('p')
        if (event.target.classList.contains("no-like")) {

            await sendRequest("POST", "http://127.0.0.1:8000/api/v1/like/",
                {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token
                }, JSON.stringify({
                    "post": cardId,
                    "author": 1
                }))
            element_count_like.innerText = (parseInt(element_count_like.innerText) + 1).toString();
        } else {
            await sendRequest("DELETE", 'http://127.0.0.1:8000/api/v1/like/delete/' + cardId.toString() + '/',
                {
                    'X-CSRFToken': csrf_token
                })
            element_count_like.innerText = (parseInt(element_count_like.innerText) - 1).toString();
        }
        event.target.classList.toggle('like')
        event.target.classList.toggle('no-like')

    });
});