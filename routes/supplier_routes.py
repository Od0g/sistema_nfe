from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from services import supplier_service
from models import Supplier # Importe o modelo Supplier

supplier_bp = Blueprint('supplier_routes', __name__)

@supplier_bp.route('/gerenciar', methods=['GET', 'POST'])
@login_required
def manage_suppliers():
    # Lógica para exibir e adicionar fornecedores
    if request.method == 'POST':
        cnpj = request.form.get('cnpj')
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        email = request.form.get('email')

        if not cnpj or not name:
            flash('CNPJ e Nome são campos obrigatórios.', 'danger')
        else:
            success, message = supplier_service.create_supplier(cnpj, name, address, phone, email)
            if success:
                flash(message, 'success')
                return redirect(url_for('supplier_routes.manage_suppliers'))
            else:
                flash(message, 'danger')

    suppliers = supplier_service.get_all_suppliers()
    return render_template('suppliers/manage_suppliers.html', suppliers=suppliers)

# Rotas para editar e excluir fornecedores podem ser adicionadas aqui
# Exemplo:
# @supplier_bp.route('/editar/<int:supplier_id>', methods=['GET', 'POST'])
# @login_required
# def edit_supplier(supplier_id):
#     supplier = supplier_service.get_supplier_by_id(supplier_id)
#     if not supplier:
#         flash('Fornecedor não encontrado.', 'danger')
#         return redirect(url_for('supplier_routes.manage_suppliers'))
#     # Lógica de edição
#     return render_template('suppliers/edit_supplier.html', supplier=supplier)