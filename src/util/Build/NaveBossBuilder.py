from src.cgd import Path
from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNaveBoss


class NaveBossBuilder(NaveBuilder):
    def __init__(self):
        super(NaveBossBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    # """--------------ATRIBUTO------------------------------"""
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
        self.naveProduct.naveFabrica = FabricaNaveBoss.FabricaNaveBoss(self.naveProduct.imagemNave,
                                         self.naveProduct.imagemExplosao,
                                         self.naveProduct.som)
