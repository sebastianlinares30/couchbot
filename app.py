from flask import Flask
from core.router import register_routes

"""
This module initializes the Flask web application.
Configures directory paths for templates and static assets.
Registers blueprints/routes and starts the local development server.
"""

# Initializes Flask app and points to 'views' and 'static' directories.
app = Flask(__name__,template_folder="views",static_folder="static") 

# Registers application routes
register_routes(app)

if __name__ == "__main__":
  #app.run(debug=True)
  app.run()

