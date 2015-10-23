# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNave.FabricaNaveGrupo import FabricaNaveGrupo
from src.cgd import Path

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:22:21$"


class NaveGrupoBuilder(NaveBuilder):
    def __init__(self):
        super(NaveGrupoBuilder, self).__init__()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        self.buildDano()
        
    """--------------ATRIBUTO------------------------------------------------"""
 #   @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
#    @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + "Imagem/Nave/NaveGrupo.png"
    
 #   @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
  #  @override
    def buildSom(self):
        self.naveProduct.som = Path.getPath() + "Som/MusicNave.wav"
    
  #  @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNaveGrupo(self.naveProduct.imagemNave,
                                         self.naveProduct.imagemExplosao,
                                         self.naveProduct.som)
