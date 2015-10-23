from src.util.FabricaNave import FabricaNave
from src.cgd import Path


class NaveProduct(object):
    def __init__(self):
        self.dano = 0
        self.naveFabrica = FabricaNave.FabricaNave('nome', Path.getPath()+'/Imagem/X Wing.png',
                                                   Path.getPath()+'/Imagem/Item/Clone0.png',
                                                   Path.getPath()+'/Som/MusicNave.wav')    # tipo : FabricaNave
        self.imagemNave = Path.getPath()+'/Imagem/X Wing.png'                              # endereco imagem
        self.imagemExplosao = Path.getPath()+'/Imagem/Item/Clone0.png'
        self.som = Path.getPath()+'/Som/MusicNave.wav'
        
    def getDano(self):
        return self.dano
    
    def setDano(self, dano):
        if dano >= 0:
            self.dano = dano
    
    def getNave(self):
        return self.naveFabrica
    
    def sofreDano(self,dano):
        if dano > 0:
            self.dano += dano
    
    def setImagemNave(self, imagem):
        self.imagemNave = imagem
