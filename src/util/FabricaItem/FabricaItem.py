from src.util.FabricaObjeto import FabricaObjeto

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:01:52$"

class FabricaItem(FabricaObjeto):
    def __init__(self, nome, imagemEscolhida, preco, probabilidade):
        super(nome, imagemEscolhida)
        self.preco = preco
        self.probabilidade = probabilidade
        
    """-----------A�OES------------------------------------------------------"""
  #  @abc.abstract
    def modificacoes(self, nave):
        return 0
            