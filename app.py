from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça três', 'Gourmet')
restaurante_pizza = Restaurante('pizza', 'Italiana')

restaurante_praca.alterar_estado()

restaurante_pizza.receber_avaliacao('Vinicius', 10)
restaurante_pizza.receber_avaliacao('Zezinho', 0)

def main():
    Restaurante.listar()

if __name__ == '__main__':
    main()