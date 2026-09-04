from flask import Blueprint, render_template, request, jsonify
from models.user import User
from services.sign_up_service import SignUpService

sign_up_blueprint = Blueprint('sign_up', __name__)

@sign_up_blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up_view():
    if request.method == 'POST':
        data = request.get_json()
        user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email')
        )
        service = SignUpService()
        result = service.create_user(user)
        return jsonify(result)

    return render_template('sign-up.html')