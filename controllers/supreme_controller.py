from flask import Blueprint, render_template, request
from services.supreme_services import SupremeService

"""
This module defines the supreme blueprint and handles GET requests to serve the interface.
It also processes POST requests containing configuration payloads to trigger automated actions.
"""

# Creates a blueprint instance for supreme
supreme_blueprint = Blueprint('supreme', __name__)

@supreme_blueprint.route('/supreme', methods=['GET', 'POST'])
def supreme_view():
    """
    Handles both rendering the automation control interface (GET).
    Receives data to trigger the backend automation workflow (POST).
    """
    if request.method == 'POST':
        # Extracts the incoming JSON payload containing user details and automation parameters
        data = request.get_json()
        # Instantiates the automation service layer with the configuration data
        service = SupremeService(data)
        # Triggers the automation execution workflow
        service.run_checkout()

    # If it's a GET request (or after processing the POST logic), render the control template
    return render_template('supreme.html')