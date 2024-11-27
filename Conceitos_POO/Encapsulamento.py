#public - dentro e fora da classe
#private - disponível apenas dentro da classe

class BaseDeDados():
    def __init__(self):
        # se alterarem o construtor, interfere todo o programa, assim, é interessante deixa-la privada
        # classse com __ de maneira convencional é privada
        self.dados = {} #dicionario vazio 
        
        
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            # cria chave no dicionario
            self.__dados['clientes'] = {id: nome}
        else:
            # verifica se a chave foi criada, e apenas a atualiza, uma vez que ela de fato ja existe no dicionario
            self.__dados['clientes'].update({'id': nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print (id, nome)
    
    def apaga_clientes (self, id):
        del self.__dados['clientes'] [id]
            
            
bd = BaseDeDados()
print (bd.__dados)  
