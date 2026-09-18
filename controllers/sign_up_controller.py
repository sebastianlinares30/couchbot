from flask import Blueprint, render_template, request, jsonify
from models.user import User
from services.sign_up_service import SignUpService

"""
This module defines the sign-up blueprint and manages GET and POST requests for account creation.
It also parses incoming JSON payloads, populates the User model, and communicates with the service layer.
"""

# Creates a blueprint instance for sign_up
sign_up_blueprint = Blueprint('sign_up', __name__)

@sign_up_blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up_view():
    """
    Handles both rendering the registration page (GET) and processing new user account creation data submission (POST).
    """
    if request.method == 'POST':
        # Extracts incoming JSON data payload from the frontend request
        data = request.get_json()
        # Instantiates User and populates it with full user details
        user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email')
        )
        # Instantiates the sign up service that will persist new user record
        service = SignUpService()
        # Passes the User object to the service to persist data
        result = service.create_user(user)
        # Returns the result back as a JSON HTTP response
        return jsonify(result)

    # If it's a GET request, render and return the HTML registration template
    return render_template('sign-up.html')