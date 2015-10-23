from src.util.FabricaNave import FabricaNave


class NaveProduct(object):
    def __init__(self):
        self.dano = 0
        self.naveFabrica = FabricaNave.FabricaNave('nome', 'figuraNave', 'figuraExplosao', 'som')            #tipo : FabricaNave
        self.imagemNave = ""        #endere�o imagem
        self.imagemExplosao = ""
        self.som = ""
        
    def getDano(self):
        return self.dano
    
    def setDano(self, dano):
        if (dano >= 0):
            self.dano = dano
    
    def getNave(self):
        return self.naveFabrica
    
    def sofreDano(self,dano):
        if (dano > 0):
            self.dano += dano
    
    def setImagemNave(self, imagem):
        self.imagemNave = imagem
