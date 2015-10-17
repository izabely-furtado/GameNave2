# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:22:21$"

class NaveGrupoBuilder(NaveBuilder):
    def __init__(self):
        super()
        self.buildDano()
        self.buildImagemNave()
        self.buildImagemExplosao()
        self.buildSom()
        self.buildNave()
        
    """--------------ATRIBUTO------------------------------------------------"""
    @override
    def buildDano(self):
        self.nave.dano = 0
    
    @override    
    def buildImagemNave(self):
        self.nave.imagemNave = "/Imagens/NaveGrupo.png"
    
    @override    
    def buildImagemExplosao(self):
        self.nave.imagemExplosao = "/Imagens/NaveExplode.png"
    
    @override    
    def buildSom(self):
        self.nave.som = "/Som/MusicNave.wav"
    
    @override    
    def buildNave(self):
        self.nave.nave = FabricaNaveGrupo(self.nave.imagemNave, 
                                         self.nave.imagemExplosao,
                                         self.nave.som)
