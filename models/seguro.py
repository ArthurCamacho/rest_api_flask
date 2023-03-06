from sql_alchemy import banco


# A classe representa uma tabela do banco de dados
class SeguroModel(banco.Model):
    # Definindo nome da tabela
    __tablename__ = 'seguros'

    # Cada objeto representa uma coluna da tabela, a qual a classe representa
    id = banco.Column(banco.Integer, primary_key=True)
    tipo = banco.Column(banco.String(50))
    descricao = banco.Column(banco.String(300))
    valor = banco.Column(banco.Float(precision=2))

    def __init__(self, tipo, descricao, valor):
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

    def inserir_seguro(self):
        banco.session.add(self)
        banco.session.commit()