from flask import Blueprint

v1 = Blueprint('v1', __name__)


@v1.route('/hello')
def hello_world():
    return 'Hello, World!'