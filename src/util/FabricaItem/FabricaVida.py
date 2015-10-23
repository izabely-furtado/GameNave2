from src.util.FabricaItem import FabricaItem
from src.cgd import Path


class FabricaVida(FabricaItem):
    def __init__(self):
        super(FabricaVida, self).__init__('Vida', Path.getPath() + "Imagem/Item/Vida.png", 100, 20)
        
    #  @abc.abstract
    def modificacoes(self, jogador):
        jogador.maisVida(jogador)