import os

from flask import Flask, request

from helpers.django_app_request_client import DjangoAppRequestClient

app = Flask(__name__)


@app.route('/categories', methods=['POST'])
def save_category():
    """
    Guardar una categoría en el proyecto de Django vía HTTP, Circuit Breaker.

    Returns:
        tuple: (response, status_code)
            response (dict): JSON con las categorías o el mensaje de error.
            status_code (int): Código de estado HTTP de la respuesta.
    """
    data = request.get_json()
    response, status = DjangoAppRequestClient().save_category(data)
    return response, status


if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
