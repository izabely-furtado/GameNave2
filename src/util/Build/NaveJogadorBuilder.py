from src.util.Build import NaveBuilder
from src.util.FabricaNave import FabricaNaveJogador
from src.cgd import Path


class NaveJogadorBuilder(NaveBuilder):
    def __init__(self):
        super(NaveJogadorBuilder, self).__init__()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    # """--------------ATRIBUTO---------------------"""
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
        super(NaveBuilder).naveProduct.naveFabrica = FabricaNaveJogador.FabricaNaveJogador("Vai na fé",
                                                                        self.naveProduct.imagemNave,
                                                                        self.naveProduct.imagemExplosao,
                                                                        self.naveProduct.som)
