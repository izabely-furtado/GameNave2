# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:21:32$"

class NaveGrupoBuilder(NaveBuilder):
    def __init__(self, naveEscolhida):
        super()
        self.buildDano()
        self.buildImagemNave(naveEscolhida)
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
    @override
    def buildDano(self):
        self.nave.dano = 0
    
    @override    
    def buildImagemNave(self, naveExcolhida):
        self.nave.imagemNave = naveExcolhida
    
    @override    
    def buildImagemExplosao(self):
        self.nave.imagemExplosao = "/Imagens/NaveExplode.png"
    
    @override    
    def buildSom(self):
        self.nave.som = "/Som/MusicNave.wav"
    
    @override    
    def buildNave(self):
        self.nave.nave = FabricaNaveJogador(self.nave.imagemNave, 
                                            self.nave.imagemExplosao,
                                            self.nave.som)
