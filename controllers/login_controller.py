from flask import Blueprint, render_template, request, jsonify
from models.user import User
from services.login_service import LoginService

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        data = request.get_json()
        user = User(email=data.get('email'))
        service = LoginService()
        result = service.login(user)
        return jsonify(result)

    return render_template('login.html')