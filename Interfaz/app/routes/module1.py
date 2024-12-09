from flask import Blueprint, render_template

module1 = Blueprint('module1', __name__, template_folder="../templates")

@module1.route('/module1')
def index():
    return render_template('module1.html', title="Módulo 1")
