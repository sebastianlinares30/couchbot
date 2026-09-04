from flask import Flask
from core.router import register_routes

app = Flask(__name__,template_folder="views",static_folder="static")

app.secret_key = "couchbot-key"

register_routes(app)

if __name__ == "__main__":
  app.run(debug=True)

