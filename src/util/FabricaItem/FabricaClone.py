from src.util.FabricaItem import FabricaItem


class FabricaClone(FabricaItem):
    def __init__(self, imagem):
        super(FabricaClone, self).__init__('Clone', imagem, 100, 6)
        
    #  @abstractmethod
    def modificacoes(self, jogador):
        jogador.clone(jogador)
