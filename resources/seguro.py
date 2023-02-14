from flask_restful import Resource, reqparse


# Dentro do pacote de recursos iremos colocar todas as classe e todo o processamento da API
# para poder importa no app.py e adicionar o endpoint na API

# Criando a lista de dicionarios com os dados dos seguros para exemplificar
seguros = [
    {
        "id": 12,
        "tipo": "Auto",
        "descricao": "O seguro destinado para carros",
        "valor": 480.20
    },
    {
        "id" : 13,
        "tipo" : "Auto",
        "descricao" : "O seguro destinado para Caminhonetes",
        "valor" : 780.56
    },
    {
        "id" : 15,
        "tipo" : "Vida",
        "descricao" : "O seguro destinado para tranquilizar você e a sua família nos piores momentos",
        "valor" : 1200.85
    },
    {
        "id" : 25,
        "tipo" : "Residencial",
        "descricao" : "O seguro destinado para proteger sua casa e seu bolso",
        "valor" : 450.00
    },
]

#Criando uma classe como uma coleção
class Seguros(Resource):
    # Definindo a coleção Seguros
    def get(self):
        return {'seguros' : seguros}

class Seguro(Resource):
    #Definindo os individuos da coleção Seguros
    def get(self, seguro_id):

        for seguro in seguros:
            if seguro['id'] == seguro_id:
                return seguro, 200
        return {"message" : "Não há seguro(s) com esse identificador para serem encontrados"}, 404
    def post(self, seguro_id):
        # Necessita instanciar um objeto com a classe do parser para poder ler todos os argumentos passados na requisiçãp
        # é necessário fazer um self.addArgument("<nome_argumento>") para cada chave q se deseja ler o valor no corpo
        # da requisição. O id vem na url (Mas isso n deveria ser assim, tinha que ser auto_increment)
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('tipo')
        argumentos.add_argument('descricao')
        argumentos.add_argument('valor')

        try:
            # Com o parse args nós podemos ler todos as chaves dos add_arguments acima e salvar tudo em  um dicionario
            dados_requisicao = argumentos.parse_args()

            novo_seguro = {
                "id" : seguro_id,
                "tipo" : dados_requisicao['tipo'],
                "descricao" : dados_requisicao['descricao'],
                "valor" : dados_requisicao['valor']
            }

            seguros.append(novo_seguro)

        except:
            return {'message' : 'Falha ao inserir o novo seguro. Verifique se todos os dados necessários foram preenchidos e se os dados informados foram preenchidos corretamente'}, 406

        return {'message' : 'Novo seguro criado com sucesso'}, 200

    def put(self):
        pass

    def delete(self):
        pass