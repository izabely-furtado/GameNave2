# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.FabricaItem.FabricaItem import FabricaItem

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:14:09$"

class FabricaClone(FabricaItem):
    def __init__(self, imagem):
        super('Clone', imagem, 100, 6)
        
#    @abstractmethod
    def modificacoes(self, jogador):
            jogador.clone(jogador)
        