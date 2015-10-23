# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.FabricaItem.FabricaClone import FabricaClone
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:14:09$"

class FabricaClone2(FabricaClone):
    def __init__(self):
        super(FabricaClone2, self).__init__(Path.getPath() + "Imagem/Item/Clone2.png")
        
    