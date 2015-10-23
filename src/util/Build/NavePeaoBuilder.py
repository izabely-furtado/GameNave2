from src.util.Build import NaveBuilder
from src.util.FabricaNave import FabricaNavePeao
from src.cgd import Path


class NavePeaoBuilder(NaveBuilder):
    def __init__(self):
        super(NavePeaoBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    # """--------------ATRIBUTO------------------"""
    #  @override
    def buildDano(self):
        self.naveProduct.dano = 0
    
    #   @override
    def buildImagemNave(self):
        self.naveProduct.imagemNave = Path.getPath() + "Imagem/Nave/NavePeao.png"
    
    #  @override
    def buildImagemExplosao(self):
        self.naveProduct.imagemExplosao = Path.getPath() + "Imagem/Nave/NaveExplode.png"
    
    #   @override
    def buildSom(self):
        self.naveProduct.som = "Som/MusicNave.wav"
    
    #   @override
    def buildNave(self):
        self.naveProduct.naveFabrica = FabricaNavePeao.FabricaNavePeao(self.naveProduct.imagemNave,
                                         self.naveProduct.imagemExplosao,
                                         self.naveProduct.som)
