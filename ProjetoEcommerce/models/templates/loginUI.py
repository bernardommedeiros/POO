import time
from view.views import View

class LoginUI:
    @staticmethod
    def main():
        print("Entrar no sistema")
        email = input("Informe e-mail: ")
        senha = input("Informe a senha: ")

        cliente = View.cliente_autenticar(email, senha)
        
        if cliente is None:
            print("E-mail ou senha inválidos")
        else:
            if email != "admin@gmail.com":
                View.venda_inserir(False, 0, cliente["id"])
            print(f"Bem-vindo(a), {cliente['nome']}!")
            time.sleep(2)
            LoginUI.main()  # Reiniciar o processo de login se desejado
