from flask import Blueprint, render_template

brain_blueprint = Blueprint('brain',__name__)
@brain_blueprint.route('/brain-dead')

def brain_dead_view():
    return render_template('brain-dead.html')
