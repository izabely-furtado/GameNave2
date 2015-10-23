from src.util.Build import NaveProduct


class NaveBuilder(object):
    def __init__(self):
        self.naveProduct = NaveProduct.NaveProduct()        # tipo : naveProduct

    def getNave(self):
        return self.naveProduct
    
    #   @abc.abstractmethod
    def buildDano(self):
        return None
    
    #    @abc.abstractmethod
    def buildNave(self):
        return None
    
    #   @abc.abstractmethod
    def buildImagemNave(self):
        return None
    
    #   @abc.abstractmethod
    def buildImagemExplosao(self):
        return None
    
    #   @abc.abstractmethod
    def buildSom(self):
        return None
