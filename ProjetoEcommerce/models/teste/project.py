import streamlit as st
import time
from view.views import View

# Função para autenticação
def autenticar_usuario():
    st.header("Entrar no sistema")
    email = st.text_input("Informe seu e-mail")
    senha = st.text_input("Informe sua senha", type="password")
    
    if st.button("Entrar"):
        cliente = View.cliente_autenticar(email, senha)
        if cliente:
            st.session_state["cliente_id"] = cliente["id"]
            st.session_state["cliente_nome"] = cliente["nome"]
            st.session_state["cliente_email"] = email
            st.session_state["perfil"] = "cliente" if email != "admin" else "admin"
            st.success(f"Bem-vindo {cliente['nome']}!")
            time.sleep(2)
            st.rerun()
        else:
            st.error("E-mail ou senha inválidos!")

# Função para abrir conta de cliente
def abrir_conta():
    st.header("Criar nova conta")
    nome = st.text_input("Informe seu nome")
    email = st.text_input("Informe seu e-mail")
    fone = st.text_input("Informe seu telefone")
    senha = st.text_input("Informe sua senha", type="password")
    
    if st.button("Cadastrar"):
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Conta criada com sucesso!")
        time.sleep(2)
        st.rerun()

# Função para o cliente acessar funcionalidades
def cliente_dashboard():
    st.header(f"Olá, {st.session_state['cliente_nome']}!")
    
    menu = ["Listar Produtos", "Carrinho", "Visualizar Pedidos"]
    
    escolha = st.selectbox("Escolha uma opção", menu)
    
    if escolha == "Listar Produtos":
        produtos = View.produto_listar()
        for produto in produtos:
            st.write(f"{produto.descricao} - R$ {produto.preco}")
        if st.button("Adicionar ao Carrinho"):
            # Adicionar produto ao carrinho (lógica a ser implementada)
            pass
    
    elif escolha == "Carrinho":
        # Visualizar carrinho e finalizar compra
        st.write("Carrinho de compras")
        # Exibir produtos no carrinho (lógica a ser implementada)
    
    elif escolha == "Visualizar Pedidos":
        pedidos = View.pedido_listar_cliente(st.session_state["cliente_id"])
        for pedido in pedidos:
            st.write(f"Pedido #{pedido.id} - Status: {pedido.status}")

# Função para o admin acessar funcionalidades
def admin_dashboard():
    st.header(f"Admin - Bem-vindo, {st.session_state['cliente_nome']}!")
    
    menu = ["Gerenciar Clientes", "Gerenciar Categorias", "Gerenciar Produtos", "Reajustar Preços", "Visualizar Pedidos"]
    
    escolha = st.selectbox("Escolha uma opção", menu)
    
    if escolha == "Gerenciar Clientes":
        # Listar, inserir, excluir e atualizar clientes
        pass
    elif escolha == "Gerenciar Categorias":
        # Gerenciar categorias
        pass
    elif escolha == "Gerenciar Produtos":
        # Gerenciar produtos
        pass
    elif escolha == "Reajustar Preços":
        # Reajustar preços
        pass
    elif escolha == "Visualizar Pedidos":
        # Visualizar pedidos de clientes
        pass

# Função principal para controle de acesso e navegação
def main():
    st.sidebar.title("Menu de Navegação")
    
    if "perfil" not in st.session_state:
        st.sidebar.write("Você não está logado.")
        st.sidebar.write("1. Entrar")
        st.sidebar.write("2. Criar conta")
        
        escolha = st.sidebar.selectbox("Escolha uma opção", ["Entrar", "Criar conta"])
        
        if escolha == "Entrar":
            autenticar_usuario()
        elif escolha == "Criar conta":
            abrir_conta()
    else:
        perfil = st.session_state["perfil"]
        if perfil == "cliente":
            cliente_dashboard()
        elif perfil == "admin":
            admin_dashboard()

if __name__ == "__main__":
    main()
