# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 13:35:10$"

class NaveBuilder():
    def __init__(self):
        self.nave = None        #tipo : naveProduct
      
    def getNave(self):
        return self.nave
    
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
