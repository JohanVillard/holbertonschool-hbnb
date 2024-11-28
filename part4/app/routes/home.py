from flask import Blueprint, render_template

# Créez un blueprint
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/index.html')
def home():
    return render_template('index.html') 
