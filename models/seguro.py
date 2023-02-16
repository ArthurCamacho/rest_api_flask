# O objetivo da classe é facilitar a estruturação do json que será retornado pela api
class SeguroModel:
    def __init__(self, id, tipo, descricao, valor):
        self.id = id
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor

    # A função formata os dados recebidos e retorna um json
    # Isso é necessário pois não é possível retornar um objeto como response de uma requisição
    def json(self):
        return  {
                    "id": self.id,
                    "tipo": self.tipo,
                    "descricao": self.descricao,
                    "valor": self.valor
                }
