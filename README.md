# couchbot
couchbot is a full-stack web application designed to streamline multi-checkout workflows using Selenium browser automation.

## Installation
Clone the repository and install the required Python dependencies:
```bash
git clone https://github.com/sebastianlinares30/couchbot
```
```bash
pip install selenium
```
```bash
pip install Flask
```

## Usage
Start the Flask application:
```bash
python app.py
```

Once the server is running, open your browser and go to:
```bash
http://127.0.0.1:5000
```

## Tech Stack
**Backend**
* Python, Flask, Selenium, SQLite

**Frontend**
* HTML, CSS, JavaScript

## Architecture
This project is built using a Model-View-Controller (MVC) architectural pattern to cleanly separate data handling, user interfaces, and application control. To ensure high maintainability and long-term scalability, the following design principles and patterns were incorporated:
* N-Tier Architecture: Clearly defines boundaries between the presentation layer, business logic, and data access.
* Service Layer Pattern: Handles complex business rules and browser automation workflows keeping controllers thin.
* Repository Pattern: Acts as an intermediary for database interactions and data persistence operations.

## Supported Stores
* Supreme

## Recommended Steps for Demo
If you prefer not to register a new account, you can log in using the test credentials below:
```bash
test@mail.com
```
Supreme is the current active store. Due to dynamic inventory and catalog availability, use the following verified parameters for your demo test:
* **Type**: accessories

* **Item Name**: Supreme®/Hanes® Tagless Tees (3 Pack)

* **Color**: Black

* **Size**: XLarge

* **State**: Utah (Note: Must be fully typed out with the first letter capitalized)

Feel free to use mock/dummy data for any remaining fields.

## Disclaimer
This automation workflow will not submit any card information for purchase. couchbot is intended for demonstration purposes and does not guarantee successful purchases of limited stock items.

