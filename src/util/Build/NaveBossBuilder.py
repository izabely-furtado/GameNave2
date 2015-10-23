from src.cgd import Path
from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNave.FabricaNaveBoss import FabricaNaveBoss

__author__ = "IzabelyFurtado e GislaineAlmeida"


class NaveBossBuilder(NaveBuilder):
    def __init__(self):
        super(NaveBossBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
    #    @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
    #   @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + 'Imagem/Nave/NaveBoss.png'
    
    #   @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + 'Imagem/Nave/NaveExplode.png'
    
    #   @override
    def buildSom(self):
        self.naveProduct.som = Path.getPath() + 'Som/MusicNave.wav'

    #    @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNaveBoss(self.naveProduct.imagemNave,
                                         self.naveProduct.imagemExplosao,
                                         self.naveProduct.som)
