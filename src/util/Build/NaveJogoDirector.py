# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 13:35:32$"

class NaveJogoDirector(object):
    def __init__(self, naveBuilder):
        self.montadora = naveBuilder
        
    def construirNave(self):
        self.montadora.buildDano()
        self.montadora.buildImagemNave()
        self.montadora.buildImagemExplode()
        self.montadora.buildSom()
        self.montadora.buildNave()

    def getNave(self):
        return self.montadora.nave
        
    
