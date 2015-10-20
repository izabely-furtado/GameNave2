# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from pygame.locals import *
#import sys
from CamadaDominioProblema.Habilidades import Resitencia
#from CamadaDominioProblema.Habilidades import Municao
__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:29:33$"

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class FabricaNaveBoss(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super('BOSS!!', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 200
        self.municao = self.criaMunicao()

    """---------------AÇOES--------------------------------------------------"""
    @abc.override
    def move(self):
        aleatorio = randint(0, 10)
        if (self.posicao["x"] < LIM_WIDTH - aleatorio and self.posicao["x"] > 0 + aleatorio):
            if (aleatorio < 5):
                self.posicao["x"] += self.velocidade["x"] + aleatorio
            else:
                self.posicao["x"] -= self.velocidade["x"] - aleatorio
        elif (self.posicao["x"] == LIM_WIDTH):
            self.posicao["x"] -= self.velocidade["x"]
        elif (self.posicao["x"] == 0):
            self.posicao["x"] += self.velocidade["x"]
        
        if (self.posicao["y"] < LIM_HEIGTH - aleatorio and self.posicao["y"] > 0 + aleatorio):
            if (aleatorio < 5):
                if (self.posicao["direcao"] != "ABAIXO"):
                    self.posicao["y"] += self.velocidade["y"] + aleatorio
                    self.posicao["direcao"] = "ABAIXO"
                else:
                    self.posicao["y"] -= self.velocidade["y"] - aleatorio
                    self.posicao["direcao"] = "ACIMA"

        self.criaArea()
    
    @abc.override
    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()

    """--------------ATRIBUTO------------------------------------------------"""
    
    @abc.override
    def criaTiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.municao.append(m)
        return m
    
    @abc.override
    def criaMunicao(self):
        return []
    
    @abc.override
    def criaVelocidade(self):
        return {"x": 1, "y": 1}
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia(10,4)