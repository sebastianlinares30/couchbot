from flask import Blueprint, render_template, request, jsonify
from models.user import User
from services.login_service import LoginService

"""
This module acts as the controller for user authentication.
It defines the blueprint, handles incoming GET and POST requests for the login page.
It also parses JSON payloads and communicates with the service layer to process logins.
"""
# Creates a blueprint instance for index
login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login_view():
    """
    Handles both rendering the login page (GET) and processing the login credentials submission (POST).
    """
    if request.method == 'POST':
        # Extracts incoming JSON data payload from the frontend request
        data = request.get_json()
        # Instantiates the User model and populates it with the email
        user = User(email=data.get('email'))
        # Instantiates the login service that will validate user login
        service = LoginService()
        # Passes the User object to the service to query the database
        result = service.login(user)
        # Returns the result back as a JSON HTTP response
        return jsonify(result)

    # If it's a GET request, render and return the HTML template
    return render_template('login.html')