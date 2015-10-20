import pygame
from pygame.locals import *
#import sys
from CamadaDominioProblema.Habilidades import Resitencia
#from CamadaDominioProblema.Habilidades import Municao

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:20:28$"

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class FabricaNave(FabricaObjeto):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        #dados de qualquer objeto de tela - rever isso
        super(nome, fuguraNave)
        self.som = self.criaSom(som)
        self.resistencia = self.criaResistencia()
        self.explosao = criaExplosao(figuraExplosao)
        self.atingido = False

    """-----------AÇOES------------------------------------------------------"""
    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
    
    @abc.override
    def explode(self, figuraExplosao):
        if (self.atingido == True):
            return self.__criaExplosao__(figuraExplosao)
    
    """--------ATRIBUTOS-----------------------------------------------------"""
    
    @staticmethod
    def criaSom(som):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        return pygame.mixer.Sound(som)

    @abc.override
    def criaVelocidade(self):
        return {"x": 0, "y": 2}
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia()
    
    @abc.override
    def criaExplosao(self, figuraExplosao):
        return FabricaNave.start_figura(figuraExplosao);
