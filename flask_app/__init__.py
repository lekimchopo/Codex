from flask import Flask

app = Flask(__name__)

from flask_app import routes  # <-- importar después de crear app
