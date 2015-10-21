# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:23:00$"

class FabricaNaveFuga(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super('Nave de Fuga', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 50
        
    """---------------AÇOES--------------------------------------------------"""
    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.posicao["x"] += self.velocidade["x"]
        self.criaArea()
        
    """--------------ATRIBUTO------------------------------------------------"""
        
    @abc.override
    def criaVelocidade(self):
        return {"x": 3, "y": 3}
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia(5,1)

