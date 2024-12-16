import time
from view.views import View

class ManterClienteUI:
    @staticmethod
    def main():
        print("Cadastro de Clientes")
        print("1 - Listar Clientes")
        print("2 - Inserir Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("9 - Finalizar programa")
        
        op = int(input("Escolha uma opção: "))
        if op == 1: 
            ManterClienteUI.cliente_listar()
        elif op == 2: 
            ManterClienteUI.cliente_inserir()
        elif op == 3: 
            ManterClienteUI.cliente_atualizar()
        elif op == 4: 
            ManterClienteUI.cliente_excluir()
        elif op == 9:
            print("Programa finalizado.")
            return
        else:
            print("Opção inválida")
            time.sleep(2)
            ManterClienteUI.main()

    @staticmethod 
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        senha = input("Informe a senha: ")

        confirmar = input("Confirmar cadastro? (s/n): ")
        if confirmar.lower() == "s":
            View.cliente_inserir(nome, email, fone, senha)
            print("Cliente adicionado com sucesso!")
        else:
            print("Cadastro cancelado.")
        time.sleep(2)
        ManterClienteUI.main()

    @staticmethod 
    def cliente_listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(f"ID: {cliente.get_id()} | Nome: {cliente.get_nome()} | E-mail: {cliente.get_email()} | Fone: {cliente.get_fone()} | Senha: {cliente.get_senha()}")
        time.sleep(2)
        ManterClienteUI.main()

    @staticmethod 
    def cliente_atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i} - {cliente.get_nome()}")
            selecao = int(input("Escolha o número do cliente para atualizar: ")) - 1
            selecionado = clientes[selecao]

            nome = input(f"Informe o novo nome ({selecionado.get_nome()}): ")
            email = input(f"Informe o novo e-mail ({selecionado.get_email()}): ")
            fone = input(f"Informe o novo fone ({selecionado.get_fone()}): ")
            senha = input(f"Informe a nova senha ({selecionado.get_senha()}): ")

            confirmar = input("Confirmar atualização? (s/n): ")
            if confirmar.lower() == "s":
                View.cliente_atualizar(selecionado.get_id(), nome, email, fone, senha)
                print("Cliente atualizado com sucesso!")
            else:
                print("Atualização cancelada.")
        time.sleep(2)
        ManterClienteUI.main()

    @staticmethod 
    def cliente_excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i} - {cliente.get_nome()}")
            selecao = int(input("Escolha o número do cliente para excluir: ")) - 1
            selecionado = clientes[selecao]

            confirmar = input(f"Tem certeza que deseja excluir {selecionado.get_nome()}? (s/n): ")
            if confirmar.lower() == "s":
                View.cliente_excluir(selecionado.get_id())
                print("Cliente excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
        time.sleep(2)
        ManterClienteUI.main()

# Inicia a execução
ManterClienteUI.main()
