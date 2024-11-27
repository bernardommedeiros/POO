from random import randint

class Pessoa():
    ano_atual = 2019
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self): 
        # relacionado com as instancias (self)
        print(self.ano_atual - self.idade) 
        
    @classmethod 
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        # se refere a classe (cls)
        
    @staticmethod
    # não utiliza classe nem instância 
    # independente
    def gera_id():
        rand = randint (100, 999)
        return rand
        
# instancias
#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print (p1)
p1.get_ano_nascimento()
print(p1.nome, p1.idade)
print (Pessoa.gera_id())
