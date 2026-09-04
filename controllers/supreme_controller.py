from flask import Blueprint, render_template

supreme_blueprint = Blueprint('supreme',__name__)
@supreme_blueprint.route('/supreme')

def supreme_view():
    return render_template('supreme.html')