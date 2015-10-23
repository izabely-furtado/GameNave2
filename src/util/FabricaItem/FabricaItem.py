from src.util import FabricaObjeto


class FabricaItem(FabricaObjeto):
    def __init__(self, nome, imagemEscolhida, preco, probabilidade):
        super(FabricaItem, self).__init__(nome, imagemEscolhida)
        self.preco = preco
        self.probabilidade = probabilidade
        
    # """-----------ACOES-------------------"""
    #  @abc.abstract
    def modificacoes(self, nave):
        return 0