from flask import Flask
from .pages import pages

app = Flask(__name__)
app.register_blueprint(pages)
