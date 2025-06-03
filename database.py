from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth_routes.login' # Define a rota para login caso não esteja autenticado
login_manager.login_message_category = 'info' # Categoria da mensagem flash

def init_db(app):
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all() # Cria as tabelas do banco de dados se não existirem
        # db.session.commit() # Não é necessário commit aqui, create_all já gerencia isso