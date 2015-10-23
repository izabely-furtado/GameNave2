# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNave.FabricaNaveJogador import FabricaNaveJogador
from src.cgd import Path

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:21:32$"


class NaveJogadorBuilder(NaveBuilder):
    def __init__(self):
        super(NaveJogadorBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
 #   @override
    def buildDano(self):
        super(NaveBuilder).naveProduct.dano = 0
    
 #   @override
    def buildImagemNave(self):
        super(NaveBuilder).naveProduct.imagemNave = Path.getPath() + 'Imagem/Nave/TieFighter_archigraphs.png'
    
 #   @override
    def buildImagemExplosao(self):
        super(NaveBuilder).naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
 #   @override
    def buildSom(self):
        super(NaveBuilder).naveProduct.som = Path.getPath() + "Som/MusicNave.wav"
    
#    @override
    def buildNave(self):
        super(NaveBuilder).naveProduct.naveFabrica = FabricaNaveJogador("Vai na fé",
                                            self.naveProduct.imagemNave,
                                            self.naveProduct.imagemExplosao,
                                            self.naveProduct.som)
