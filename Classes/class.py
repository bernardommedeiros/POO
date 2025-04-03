# conjunto que considera: atributos -> características e metodos -> ações.

class MinhaClasse:
    # self -> se refere a classe, indica que o metodo é englobado pela classe
    def metodo_01(self):
        print("minha primeira ação:")
        return ("Hello, World!")
    # objeto -> é instanciado a partir de uma classe
minha_classe = MinhaClasse()


print (minha_classe.metodo_01())