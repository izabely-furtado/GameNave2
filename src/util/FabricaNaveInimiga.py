# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:21:43$"

class FabricaNaveInimiga(FabricaNave):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        super(nome, figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 0

    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.start_area()

