from flask import Blueprint, render_template

# Створюємо блюпринт 'products'
products_bp = Blueprint('products', __name__, template_folder='templates')

@products_bp.route("/")
def get_products():
    # Створимо простий список продуктів для прикладу
    product_list = ["iPhone 15", "MacBook Pro", "Tesla Model S"]
    return render_template("products/index.html", products=product_list)