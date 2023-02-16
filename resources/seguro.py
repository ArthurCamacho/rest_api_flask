from flask_restful import Resource, reqparse
from models.seguro import SeguroModel


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
    # Necessita instanciar um objeto com a classe do parser para poder ler todos os argumentos passados na requisiçãp
    # é necessário fazer um self.addArgument("<nome_argumento>") para cada chave q se deseja ler o valor no corpo
    # da requisição
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('tipo')
    argumentos.add_argument('descricao')
    argumentos.add_argument('valor')

    # Definindo a coleção Seguros toda sem filtro
    def get(self):
        return {'seguros' : seguros}

    def post(self):

        try:
            # Com o parse args nós podemos ler todos as chaves dos add_arguments acima e salvar tudo em  um dicionario
            dados_requisicao = Seguros.argumentos.parse_args()

            # novo_seguro = {
            #     "id" : seguros[-1]['id'] + 1,
            #     "tipo" : dados_requisicao['tipo'],
            #     "descricao" : dados_requisicao['descricao'],
            #     "valor" : dados_requisicao['valor']
            # }

            # Cria uma instancia do objeto com os dados provenientes da requisição
            seguro_objeto = SeguroModel(seguros[-1]['id'] + 1, **dados_requisicao)

            # Estruturando os dados em formato de dicionario/json
            novo_seguro = seguro_objeto.json()

            # Inseri o novo seguro
            seguros.append(novo_seguro)

        except:
            return {'message' : 'Falha ao inserir o novo seguro. Verifique se todos os dados necessários foram preenchidos e se os dados informados foram preenchidos corretamente'}, 406

        return {'message' : 'Novo seguro criado com sucesso',
                'dados_seguro' : novo_seguro}, 201

class Seguro(Resource):
    # Define os argumentos que são possíveis de serem recebidos para manipulação dos individuos
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('tipo')
    argumentos.add_argument('descricao')
    argumentos.add_argument('valor')

    @staticmethod
    def buscar_seguro_id(seguro_id):
        """Recebe um id e busca entre os seguros esse determinado id /
           Retorna tambem o indice dentro do array que se encontra o seguro"""
        for i, seguro in enumerate(seguros):
            if seguro['id'] == seguro_id:
                return seguro, i

    #Definindo os individuos da coleção Seguros
    def get(self, seguro_id):
        """Busca um seguro especifico"""
        seguro = Seguro.buscar_seguro_id(seguro_id)
        if seguro:
            return seguro[0], 200
        return {"message" : "Não há seguro(s) com esse identificador para serem encontrados"}, 404


    def put(self, seguro_id):
        """Atualiza os dados de um seguro existente"""
        seguro = Seguro.buscar_seguro_id(seguro_id)

        if seguro:
            dados_requisicao = Seguro.argumentos.parse_args()
            # ATUALIZAÇÃO
            # Cria um novo dicionario que irá receber todas as chaves e valores dentro de dados_requisicao
            # Alem do id do seguro passado na url. Importante lembrar que não serão recebidos argumentos
            # Não mapeados dentro da variavel "argumentos" pertencente a essa classe (uma especie
            # construtor sem __init__)
            # NOVIDADE
            # Ao invés de criar um novo dicionario, faz somente as atualizações nos valores das chaves que foram
            # Informadas na requisição. Dessa forma, não há mais a possibilidade de setar um dado como nulo
            # Caso sua chave não seja informada
            for chave in dados_requisicao.keys():
                # Caso a chave do argumento for vazia, mantem o valor atual que esta no dicionario
                seguro[0][chave] = dados_requisicao[chave] if dados_requisicao[chave] is not None else seguro[0][chave]

            return {'message' : 'Seguro atualizado com sucesso',
                    'dados_seguro' : seguro[0]}, 200

        return {'message' : 'Nenhum seguro encontrado'}, 404

    def delete(self, seguro_id):
        indice, seguro = Seguro.buscar_seguro_id(seguro_id)
        if seguro:
            seguros.remove(indice)
            return {'message' : 'Seguro deletado com sucesso'}, 200
        return {'message' : 'Nenhum seguro encontrado'}, 404