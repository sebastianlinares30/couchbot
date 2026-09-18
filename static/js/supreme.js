const nextToCheckoutButton = document.getElementById('next-to-checkout');
const nextToCardButton = document.getElementById('next-to-card');
const backToItemButton = document.getElementById('back-to-item');
const backToCheckoutButton = document.getElementById('back-to-checkout');
const submitButton = document.getElementById('submit-button');

const itemForm = document.getElementById('item-form');
const checkoutForm = document.getElementById('checkout-form');
const cardForm = document.getElementById('card-form');

const cardExpiration = document.getElementById('card-expiration');

nextToCheckoutButton.addEventListener('click', () => {
    itemForm.style.display = 'none';
    checkoutForm.style.display = 'grid';
});

backToItemButton.addEventListener('click', () => {
    checkoutForm.style.display = 'none';
    itemForm.style.display = 'grid';
});

nextToCardButton.addEventListener('click', () => {
    checkoutForm.style.display = 'none';
    cardForm.style.display = 'grid';
});

backToCheckoutButton.addEventListener('click', () => {
    cardForm.style.display = 'none';
    checkoutForm.style.display = 'grid';
});

cardExpiration.addEventListener('input', (e) => {
    let value = e.target.value.replace(/\D/g, '');

    if (value.length > 4) {
        value = value.substring(0, 4);
    }

    if (value.length > 2) {
        e.target.value = `${value.substring(0, 2)}/${value.substring(2)}`;
    }
});

// Trigger the full bot execution when clicking Submit on the card form
submitButton.addEventListener('click', async () => {
    const payload = {
        // Item fields
        type: document.getElementById('type-selector').value,
        name: document.getElementById('item-name').value,
        color: document.getElementById('item-color').value,
        size: document.getElementById('size-selector').value,

        // Checkout fields
        firstName: document.getElementById('first-name').value,
        lastName: document.getElementById('last-name').value,
        address: document.getElementById('shipping-address').value,
        apt: document.getElementById('shipping-address-apartment').value,
        city: document.getElementById('city').value,
        state: document.getElementById('state').value,
        zip: document.getElementById('zip').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,

        // Card fields
        cardName: document.getElementById('billing-first-name').value,
        cardNumber: document.getElementById('card-number').value,
        cardExpiry: document.getElementById('card-expiration').value,
        cardSecurity: document.getElementById('card-security').value
    };

    await fetch('http://127.0.0.1:5000/supreme', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
});