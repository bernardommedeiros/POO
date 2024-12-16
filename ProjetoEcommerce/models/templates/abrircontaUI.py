import time
from view.views import View

class AbrirContaUI:
    @staticmethod
    def main():
        print("Abrir conta no sistema")
        AbrirContaUI.inserir()
    
    @staticmethod
    def inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")
        
        confirmar = input("Confirmar cadastro? (s/n): ")
        if confirmar.lower() == "s":
            View.cliente_inserir(nome, email, fone, senha)
            print("Conta criada com sucesso!")
            time.sleep(2)
            AbrirContaUI.main()  # Para reiniciar o processo, caso desejado
        else:
            print("Cadastro cancelado.")
