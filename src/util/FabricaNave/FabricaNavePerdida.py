# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
#import pygame
from pygame.locals import *
#import sys
from CamadaDominioProblema.Habilidades import Resitencia
#from CamadaDominioProblema.Habilidades import Municao
import random
__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:21:41$"

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class FabricaNavePerdida(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super('Nave Perdida', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 20
        self.municao = self.criaMunicao()

    """---------------AÇOES--------------------------------------------------"""
    @abc.override
    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < LIM_WIDTH and self.posicao["x"] > 0):
            if (aleatorio > 5):
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["x"] -= self.velocidade["x"]
        elif (self.posicao["x"] == LIM_WIDTH):
            self.posicao["x"] -= self.velocidade["x"]
        elif (self.posicao["x"] == 0):
            self.posicao["x"] += self.velocidade["x"]
        
        self.posicao["y"] += self.velocidade["y"]    
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
        return Resitencia.Resistencia(2,2)
