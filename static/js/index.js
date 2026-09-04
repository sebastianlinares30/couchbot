const startButton = document.getElementById('start-button');

startButton.addEventListener('click', () => {
    const selectedStore = document.getElementById('store-selector').value;

    if (selectedStore) {
        window.location.href = selectedStore;
    }
});