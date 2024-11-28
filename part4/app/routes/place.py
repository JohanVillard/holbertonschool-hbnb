from flask import Blueprint, render_template

# Créez un blueprint
place_bp = Blueprint('place_bp', __name__)

@place_bp.route('/place.html')
def home():
    return render_template('place.html') 
