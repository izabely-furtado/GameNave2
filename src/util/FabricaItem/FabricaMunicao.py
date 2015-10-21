# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.FabricaItem.FabricaItem import FabricaItem

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:14:36$"

class FabricaMunicao(FabricaItem):
    def __init__(self, imagem, preco, probabilidade):
        super('Municao', imagem, preco, probabilidade)
        
  #  @abc.abstract
    def modificacoes(self, jogador):
        return 0