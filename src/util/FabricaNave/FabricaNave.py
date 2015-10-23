import pygame
from src.cdp.Habilidades import Resistencia
from src.util import FabricaObjeto

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


class FabricaNave(FabricaObjeto):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        super(FabricaNave, self).__init__(nome, figuraNave)
        self.som = self.criaSom(som)
        self.resistencia = self.criaResistencia()
        self.explosao = FabricaNave.criaExplosao(figuraExplosao)
        
    # """-----------ACOES-----------------------"""
    # @override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
    
    # @abc.override
    def explode(self, figuraExplosao):
        if (self.atingido == True):
            return self.criaExplosao(figuraExplosao)
    
    # """--------ATRIBUTOS----------------------"""
    
    @staticmethod
    def criaSom(som):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        return pygame.mixer.Sound(som)

    def buzina(self):
        self.som.set_volume(0.1)
        self.som.play()

    # @abc.override
    def criaVelocidade(self):
        return {"x": 0, "y": 2}
    
    # @abc.override
    def criaResistencia(self):
        resiste = Resistencia.Resistencia(0, 0)
        return resiste
    
    # @abc.override
    @staticmethod
    def criaExplosao(figuraExplosao):
        return FabricaNave.criaFigura(figuraExplosao)
