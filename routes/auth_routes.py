from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from services import user_service # Importamos o serviço de usuário

auth_bp = Blueprint('auth_routes', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.index')) # Se já logado, vai para a página inicial

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember_me') == 'on' # Checkbox "Lembrar de mim"

        user = user_service.get_user_by_username(username)
        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash('Login bem-sucedido!', 'success')
            next_page = request.args.get('next') # Redireciona para a página que o usuário tentou acessar
            return redirect(next_page or url_for('main_routes.index'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required # Garante que apenas usuários logados podem fazer logout
def logout():
    logout_user()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('auth_routes.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
@login_required # Apenas usuários logados podem registrar novos usuários
def register():
    # Apenas 'Gestor' pode cadastrar novos usuários
    if current_user.role != 'Gestor':
        flash('Você não tem permissão para cadastrar novos usuários.', 'danger')
        return redirect(url_for('main_routes.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') # Recebe a role do formulário

        # Validação simples no front-end e reforçada no serviço
        if not username or not email or not password or not role:
            flash('Por favor, preencha todos os campos.', 'danger')
        else:
            success, message = user_service.create_user(username, email, password, role)
            if success:
                flash(message, 'success')
                return redirect(url_for('auth_routes.register')) # Ou para uma lista de usuários
            else:
                flash(message, 'danger')

    return render_template('users/register_user.html')