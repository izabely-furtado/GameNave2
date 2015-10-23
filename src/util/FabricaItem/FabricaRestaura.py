# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.FabricaItem.FabricaItem import FabricaItem
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:15:21$"

class FabricaRestaura(FabricaItem):
    def __init__(self):
        super(FabricaRestaura, self).__init__('Restaura', Path.getPath() + "Imagem/Item/Restaura.png", 100, 30)
        
  #  @abc.abstract
    def modificacoes(self, jogador):
        jogador.restaura(jogador)