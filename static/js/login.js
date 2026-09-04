const loginButton = document.getElementById('login-button');

loginButton.addEventListener('click', async(e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;

    const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email
        })
    });

    const result = await response.json()

    if (result.success) {
        window.location.href = '/index'
    }
})