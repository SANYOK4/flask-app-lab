from flask import Flask

from .users.views import users_bp
from .products.views import products_bp

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')