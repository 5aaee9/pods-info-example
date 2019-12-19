from flask import Flask
from flask_restful import Api
from route import add_route

def create_app():
    app = Flask(__name__)
    api = Api(app)

    add_route(api)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)