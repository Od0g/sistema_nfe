from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import db # Importamos a instância do db

# Função para carregar o usuário pelo ID, essencial para o Flask-Login
from database import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # Nossos perfis: 'Gestor', 'Qualidade'
    role = db.Column(db.String(20), nullable=False, default='Qualidade') # 'Gestor', 'Qualidade'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False) # CNPJ sem formatação
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    nfe_items = db.relationship('NFe', backref='supplier', lazy=True) # Relação com NF-e

    def __repr__(self):
        return f"Supplier('{self.name}', '{self.cnpj}')"

class NFe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chave_acesso = db.Column(db.String(44), unique=True, nullable=False)
    numero_nota = db.Column(db.String(10), nullable=False) # Extraído da chave
    serie_nota = db.Column(db.String(5), nullable=False)    # Extraído da chave
    ano_emissao = db.Column(db.Integer, nullable=False)     # Extraído da chave
    mes_emissao = db.Column(db.Integer, nullable=False)     # Extraído da chave
    data_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # Campos de controle internos
    tipo_operacao = db.Column(db.String(10), nullable=False) # 'Recebimento' ou 'Expedicao'
    numero_processo = db.Column(db.String(50))
    responsavel_operacao = db.Column(db.String(100))
    turno = db.Column(db.String(10)) # 'Turno 1', 'Turno 2', 'Turno 3', 'Adm'
    status = db.Column(db.String(20), nullable=False, default='Pendente') # 'Pendente', 'Expedida'

    # Novos campos para controle de qualidade/rastreamento
    id_processo_qualidade = db.Column(db.String(50)) # 'ID do Processo' para rastreamento da qualidade
    responsavel_dli_pqm = db.Column(db.String(100)) # Campo para o nome do responsável DLI-PQM (caixa de marcação no front-end, nome no back-end)

    # Chave estrangeira para o Fornecedor
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

    def __repr__(self):
        return f"NFe('{self.chave_acesso}', '{self.numero_nota}', '{self.tipo_operacao}', '{self.status}')"