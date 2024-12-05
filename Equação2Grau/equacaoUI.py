import streamlit as st
from equacao import Equacao

class EquacaoUI:
    def main():    
        st.header("Calculo com retangulos")
        a = st.text_input("Informe a base")
        b = st.text_input("Informe a altura")
        c = st.text_input("Informe a altura")

        if st.button("Calcular"):
            eq = Equacao(float(a), float(b), float(c))
            st.write(f"Delta = {eq.delta()}")
            st.write(f"X1 = {eq.X1()}")
            st.write(f"X2 = {eq.X2()}")
            
            px = []  #coordenadas x de varios pontos
            py = [] #coordenadas y de varios pontos
            if eq.delta() > 0:
                X1 = eq.X1() #menor raiz
                X2 = eq.X1() #menor raiz
                d = X2 - X1
                xmin = X1 - d/2
                xmin = X2 + d/2
                d = (xmax - xmin) / 5
                x = min
                while x < xmax:
                        px.append(x)
                        pt.append(eq.y(x ))
                        x += d