from flask import Flask
from flask_restful import Api
from resources.seguro import Seguros, Seguro


# Instancia o aplicativo
app = Flask(__name__)
# Adiciona as configurações na aplicação
app.config.from_object('config')
# Instancia a API (deve receber uma instancia de aplicativo)
api = Api(app)


# Disponibilizandoa classe como coleção e criando seu endpoint
api.add_resource(Seguros, '/seguros')
api.add_resource(Seguro, '/seguros/<int:seguro_id>')

if __name__ == "__main__":
    # Importa o banco somente se estiver sendo executado diretamente de app
    from sql_alchemy import banco
    with app.app_context():
        # ATENÇÃO
        # Antes de criar o banco deve referencia-lo na aplicação
        # Associa o banco à aplicação
        banco.init_app(app)
        # Cria o banco de dados
        banco.create_all()
        # Executa a API
        app.run(debug=True)
