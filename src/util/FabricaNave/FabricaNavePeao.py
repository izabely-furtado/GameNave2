# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#import pygame
from pygame.locals import *
#import sys
from CamadaDominioProblema.Habilidades import Resitencia
#from CamadaDominioProblema.Habilidades import Municao

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:22:21$"

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class FabricaNaveGrupo(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super('Nave Peão', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 10
        
    """---------------AÇOES--------------------------------------------------"""
    @abc.override
    def move(self):
        if (self.posicao["direcao"] == "DIREITA"):
            if (self.posicao["x"] < LIM_WIDTH):
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["direcao"] = "ESQUERDA"
                self.posicao["y"] += self.velocidade["y"] 
        elif (self.posicao["direcao"] == "ESQUERDA"):
            if (self.posicao["x"] > 0):
                self.posicao["x"] -= self.velocidade["x"]
            else:
                self.posicao["direcao"] = "DIREITA"
                self.posicao["y"] += self.velocidade["y"] 
        
        self.criaArea()
        
    """--------------ATRIBUTO------------------------------------------------"""
        
    @abc.override
    def criaVelocidade(self):
        return {"x": 1, "y": 1}
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia(1,1)
