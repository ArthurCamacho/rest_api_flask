from flask_restful import Resource


# Dentro do pacote de recursos iremos colocar todas as classe e todo o processamento da API
# para poder importa no app.py e adicionar o endpoint na API

# Criando a lista de dicionarios com os dados dos seguros para exemplificar
lista_seguros = [
    {
        "ID": 12,
        "Tipo": "Auto",
        "Descricao": "O seguro destinado para carros",
        "Valor": 480.20
    },
    {
        "ID" : 13,
        "Tipo" : "Auto",
        "Descricao" : "O seguro destinado para Caminhonetes",
        "Valor" : 780.56
    },
    {
        "ID" : 15,
        "Tipo" : "Vida",
        "Descricao" : "O seguro destinado para tranquilizar você e a sua família nos piores momentos",
        "Valor" : 1200.85
    },
    {
        "ID" : 25,
        "Tipo" : "Residencial",
        "Descricao" : "O seguro destinado para proteger sua casa e seu bolso",
        "Valor" : 450.00
    },
]

#Criando uma classe como uma coleção
class Seguros(Resource):
    # Definindo metodo get
    def get(self):
        return {'Seguros' : lista_seguros}
