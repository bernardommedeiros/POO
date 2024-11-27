class Vendedor():
    # construtor  
    # atribui os atributos do vendedor
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas
    # vendas do vendedor

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print ("bateu a meta")
        else:
            print ("não bateu a meta")

vendedor1 = Vendedor("lira")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor("bd")
vendedor2.vendeu(1000)
vendedor2.bateu_meta(6000)
