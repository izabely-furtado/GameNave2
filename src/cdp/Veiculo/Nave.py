#!/usr/local/bin/python
import pygame
from pygame.locals import *
import sys
from CamadaDominioProblema.Habilidades import Resitencia
from CamadaDominioProblema.Habilidades import Municao
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine e Izabely'

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50

class Nave(object):

    def __init__(self, nome, figura):
        self.posicao = self.cria_posicao()
        self.velocidade = self.cria_posicao()
        self.som = self.start_controles()
        self.tipo = nome
        self.figura = self.start_figura(figura)
        self.area = self.start_area()
        self.armamento = []
        self.resistencia = Resitencia.Resistencia()
        self.atingido = False

    @staticmethod
    def start_controles():

        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

        return pygame.mixer.Sound("/home/gislaine/Dropbox/GameNave/CamadaGestaoDados/Som/MusicNave.wav")

    def cria_posicao(self):
        return {"x": 0, "y": 0}

    def cria_velocidade(self):
        return {"x": 0, "y": 2}

    def get_area(self):

        return self.area

    def cria_tiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.armamento.append(m)
        return m

    @staticmethod
    def start_figura(figura):
        f = pygame.image.load(figura).convert_alpha()
        return f

    def start_area(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())
        return Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

    def buzina(self):
        self.som.set_volume(0.1)
        self.som.play()

    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.armamento[-1].atira()
        self.buzina()

    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.start_area()
