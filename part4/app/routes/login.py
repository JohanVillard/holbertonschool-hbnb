from flask import Blueprint, render_template

# Créez un blueprint
login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login.html')
def home():
    return render_template('login.html') 
