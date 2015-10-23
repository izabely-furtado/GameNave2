# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNave.FabricaNavePerdida import FabricaNavePerdida
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:21:41$"

class NavePerdidaBuilder(NaveBuilder):
    def __init__(self):
        super(NavePerdidaBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
   # @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
  #  @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + "Imagem/Nave/NavePerdida.png"
    
 #   @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
  #  @override
    def buildSom(self):
        self.naveProduct.som = Path.getPath() + "Som/MusicNave.wav"
    
   # @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNavePerdida(self.naveProduct.imagemNave,
                                            self.naveProduct.imagemExplosao,
                                            self.naveProduct.som)
