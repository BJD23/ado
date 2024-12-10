from flask import Blueprint, render_template

module2 = Blueprint('module2', __name__, template_folder="../templates")

@module2.route('/module2')
def index():
    return render_template('module2.html')
