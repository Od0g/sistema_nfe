from models import db, User
from werkzeug.security import generate_password_hash

def create_user(username, email, password, role):
    """
    Cria um novo usuário no banco de dados.
    Verifica se o usuário ou e-mail já existem antes de criar.
    """
    if User.query.filter_by(username=username).first():
        return False, "Nome de usuário já existe."
    if User.query.filter_by(email=email).first():
        return False, "Email já cadastrado."

    # Validar a role para garantir que é 'Gestor' ou 'Qualidade'
    if role not in ['Gestor', 'Qualidade']:
        return False, "Perfil de usuário inválido. Apenas 'Gestor' ou 'Qualidade' são permitidos."

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return True, "Usuário cadastrado com sucesso!"

def get_user_by_username(username):
    """Retorna um usuário pelo nome de usuário."""
    return User.query.filter_by(username=username).first()

def get_user_by_id(user_id):
    """Retorna um usuário pelo ID."""
    return User.query.get(int(user_id))

# Outras funções de serviço para usuários podem ser adicionadas aqui (ex: update_user, delete_user)