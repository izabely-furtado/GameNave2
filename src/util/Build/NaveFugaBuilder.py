from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNaveFuga
from src.cgd import Path


class NaveFugaBuilder(NaveBuilder):
    def __init__(self):
        super(NaveFugaBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    # """--------------ATRIBUTO---------------------"""
    #    @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
    #   @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + "Imagem/Nave/NaveFuga.png"
    
    #   @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
    #  @override
    def buildSom(self):
        self.naveProduct.som = Path.getPath() + "Som/MusicNave.wav"
    
    #    @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNaveFuga.FabricaNaveFuga(self.naveProduct.imagemNave,
                                                                       self.naveProduct.imagemExplosao,
                                                                       self.naveProduct.som)