# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.FabricaItem.FabricaMunicao import FabricaMunicao
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:14:36$"

class FabricaMunicao1(FabricaMunicao):
    def __init__(self):
        super(FabricaMunicao1, self).__init__(Path.getPath() + "Imagem/Item/Municao1.png", 200, 5)
        