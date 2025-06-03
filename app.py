from flask import Flask
from config import Config
from database import db, login_manager, init_db
from models import User, Supplier, NFe# Importe User para que Flask-Login possa usá-lo
from datetime import datetime # Adicione esta importação
from flask_moment import Moment

# Importa os blueprints de rotas
from routes.auth_routes import auth_bp
from routes.supplier_routes import supplier_bp
from routes.nfe_routes import nfe_bp
from routes.main_routes import main_bp
# from routes.user_routes import user_bp # Será adicionado depois

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    moment = Moment(app) # Inicialize o Flask-Moment aqui

    init_db(app) # Inicializa o DB e o LoginManager

    # Registro dos blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(supplier_bp, url_prefix='/fornecedores')
    app.register_blueprint(nfe_bp, url_prefix='/nfe')
    app.register_blueprint(main_bp, url_prefix='/') # Rotas da homepage

    # Opcional: Adicionar um contexto de shell para fácil acesso ao DB
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Supplier': Supplier, 'NFe': NFe} # Importar models aqui
    
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()} # Ou datetime.now() se quiser a hora local do servidor

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) # Em produção, debug=False