import pygame
from pygame.locals import *
#import sys
from CamadaDominioProblema.Habilidades import Resitencia
from CamadaDominioProblema.Habilidades import Municao

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:20:28$"

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class FabricaNave(FabricaAtributoNave):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        #dados de qualquer objeto de tela - rever isso
        self.posicao = self.criaPosicao()
        self.som = self.criaSom(som)
        self.figura = self.criaFigura(figuraNave)
        self.area = self.criaArea()
    
        self.tipo = nome
        self.velocidade = self.criaVelocidade()
        self.resistencia = self.__criaResistencia()
        self.municao = self.criaMunicao()
        self.explosao = criaExplosao(figuraExplosao)
        self.atingido = False

    """-----------AÇOES------------------------------------------------------"""
    def get_area(self):
        return self.area

    @abc.override
    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.armamento[-1].atira()
        self.buzina()
    
    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.start_area()
    
    @abc.override
    def explode(self, figuraExplosao):
        if (self.atingido == True):
            return self.__criaExplosao__(figuraExplosao)
    
    """--------ATRIBUTOS-----------------------------------------------------"""
    
    @staticmethod
    def criaSom(som):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        return pygame.mixer.Sound(som)

    @staticmethod
    def criaFigura(figura):
        f = pygame.image.load(figura).convert_alpha()
        return f
    
    def criaPosicao(self):
        return {"x": 0, "y": 0}

    def criaArea(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())
        return Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

    @abc.override
    def criaTiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.armamento.append(m)
        return m
    
    @abc.override
    def criaVelocidade(self):
        return {"x": 0, "y": 2}
    
    @abc.override
    def criaMovimento(self):
        return Movimento.Movimento()
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia()
    
    @abc.override
    def criaMunicao(self):
        return []
    
    @abc.override
    def criaExplosao(self, figuraExplosao):
        return FabricaNave.start_figura(figuraExplosao);
