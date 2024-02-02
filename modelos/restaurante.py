from modelos.avaliacao import Avaliacao

class Restaurante():
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacoes = []
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status\n")
        for rest in cls.restaurantes:
            print(f'{rest._nome.ljust(25)} | {rest._categoria.ljust(25)} | {str(rest.calcula_media_avaliacoes).ljust(25)} | {rest.ativo}')
    
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, nome, nota):
        self._avaliacoes.append(Avaliacao(nome, nota))

    @property
    def calcula_media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        
        soma = sum(av._nota if av._nota <= 5 else 5 for av in self._avaliacoes) 
        qtd = len(self._avaliacoes)
        resultado = round(soma/qtd, 1)
        return resultado

# restaurante_praca = Restaurante('praça três', 'Gourmet')
# restaurante_pizza = Restaurante('pizza', 'Italiana')

# restaurante_praca.alterar_estado()

# Restaurante.listar()


# mostrar todos atributos e métodos do objeto
# print(dir(restaurante_praca))

# mostrar um dicionário com os atributos e valores do objeto
# print(vars(restaurante_praca))

# acessando um atributo
# print(restaurante_praca.ativo)

# mostrando objeto para imprimir o que foi definido na função __str__
# print(restaurante_praca)