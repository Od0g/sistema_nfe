from models import db, Supplier

def create_supplier(cnpj, name, address=None, phone=None, email=None):
    """
    Cria um novo fornecedor no banco de dados.
    Verifica se o CNPJ já existe.
    """
    if Supplier.query.filter_by(cnpj=cnpj).first():
        return False, "Fornecedor com este CNPJ já cadastrado."

    new_supplier = Supplier(cnpj=cnpj, name=name, address=address, phone=phone, email=email)
    db.session.add(new_supplier)
    db.session.commit()
    return True, "Fornecedor cadastrado com sucesso!"

def get_all_suppliers():
    """Retorna todos os fornecedores cadastrados."""
    return Supplier.query.all()

def get_supplier_by_cnpj(cnpj):
    """Retorna um fornecedor pelo CNPJ."""
    return Supplier.query.filter_by(cnpj=cnpj).first()

def get_supplier_by_id(supplier_id):
    """Retorna um fornecedor pelo ID."""
    return Supplier.query.get(int(supplier_id))

# Funções para atualização e exclusão podem ser adicionadas aqui
def update_supplier(supplier_id, name, address, phone, email):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        supplier.name = name
        supplier.address = address
        supplier.phone = phone
        supplier.email = email
        db.session.commit()
        return True, "Fornecedor atualizado com sucesso!"
    return False, "Fornecedor não encontrado."

def delete_supplier(supplier_id):
    supplier = get_supplier_by_id(supplier_id)
    if supplier:
        db.session.delete(supplier)
        db.session.commit()
        return True, "Fornecedor excluído com sucesso!"
    return False, "Fornecedor não encontrado."