from flask import Blueprint, render_template

"""
This module acts as the controller for the application's home/dashboard view.
It defines the blueprint and handles the GET request to render the main index page.
"""

# Creates a blueprint instance for index
index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/index', methods=['GET'])
def home():
    """
    Renders and returns the main index HTML template when a user navigates to the /index route.
    """
    return render_template('index.html')