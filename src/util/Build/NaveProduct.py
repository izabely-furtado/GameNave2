# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 13:34:34$"

class NaveProduct(Object):
    def __init__(self):
        self.dano = 0
        self.nave = null            #tipo : naveProduct
        self.imagemNave = ""        #endereço imagem
        self.imagemExplosao = ""
        self.som = ""
        
    def getDano(self):
        return self.dano
    
    def setDano(self, dano):
        if (dano >= 0):
            self.dano = dano
    
    def getNave(self):
        return self.nave
    
    def perdeVida(self):
        if (self.nave.vidas > 0):
            self.nave.vidas -=1
    
    def sofreDano(self,dano):
        if (dano > 0):
            self.dano += dano
    
    def setImagemNave(self, imagem):
        self.imagemNave = imagem
