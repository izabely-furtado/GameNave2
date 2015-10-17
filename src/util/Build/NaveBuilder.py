# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 13:35:10$"

class NaveBuilder(Object):
    def __init__(self):
        self.nave = null        #tipo : naveProduct
      
    def getNave(self):
        return self.nave
    
    @abc.abstractmethod
    def buildDano(self):
        return null
    
    @abc.abstractmethod
    def buildNave(self):
        return null
    
    @abc.abstractmethod
    def buildImagemNave(self):
        return null
    
    @abc.abstractmethod
    def buildImagemExplosao(self):
        return null
    
    @abc.abstractmethod
    def buildSom(self):
        return null
