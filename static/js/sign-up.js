const registerButton = document.getElementById('register-button');

registerButton.addEventListener('click', async(e) => {
    e.preventDefault();

    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const email = document.getElementById('email').value;

    const response = await fetch('http://127.0.0.1:5000/sign-up', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email
        })
    });

    const result = await response.json();
    
    if (result.success) {
        alert("Account created successfully.");
        window.location.href = '/login'
    } else {
        alert("Unable to create account.");
    }
});