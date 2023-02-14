from flask import Flask
from flask_restful import Api, Resource
from resources.seguro import Seguros, Seguro


# Instancia o aplicativo
app = Flask(__name__)
# Instancia a API (deve receber uma instancia de aplicativo)
api = Api(app)


# Disponibilizandoa classe como coleção e criando seu endpoint
api.add_resource(Seguros, '/seguros')
api.add_resource(Seguro, '/seguros/<int:seguro_id>')

if __name__ == "__main__":
    app.run(debug=True)