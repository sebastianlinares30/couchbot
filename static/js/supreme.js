const nextToCheckoutButton = document.getElementById('next-to-checkout');
const nextToCardButton = document.getElementById('next-to-card');
const backToItemButton = document.getElementById('back-to-item');
const backToCheckoutButton = document.getElementById('back-to-checkout');

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
