from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main_routes', __name__)

@main_bp.route('/')
@login_required # Garante que apenas usuários logados acessam a página inicial
def index():
    return render_template('index.html', user=current_user)

@main_bp.route('/protocolo')
@login_required
def protocolo():
    # Lógica para a página de protocolo
    return render_template('nfe/protocolo.html')