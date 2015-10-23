# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNave.FabricaNavePersegue import FabricaNavePersegue
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:22:42$"

class NavePersegueBuilder(NaveBuilder):
    def __init__(self):
        super(NavePersegueBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
 #   @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
  #  @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + "Imagem/Nave/NavePersegue.png"
    
  #  @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
#    @override
    def buildSom(self):
        self.naveProduct.som = Path.getPath() + "Som/MusicNave.wav"
    
 #   @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNavePersegue(self.naveProduct.imagemNave,
                                             self.naveProduct.imagemExplosao,
                                             self.naveProduct.som)
