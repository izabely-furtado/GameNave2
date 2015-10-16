#!/usr/local/bin/python
import pygame

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
import sys

__author__ = 'Gislaine  e Izabely'

pygame.init()

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


class Municao(object):
    def __init__(self, pos):
        self.figura = self.cria_figura()
        self.posicao = self.cria_posicao(pos)
        self.velocidade = self.cria_velocidade()
        self.colisao = False
        self.ativo = True
        self.area = self.start_area()

    @staticmethod
    def cria_figura():
        figura = pygame.image.load("/home/gislaine/Dropbox/GameNave/CamadaGestaoDados/Imagem/tiro3.png").convert_alpha()

        return figura

    def cria_posicao(self, pos):
        posicao = {}
        if (pos < LIM_WIDTH - 30) and (pos < LIM_HEIGTH - 15):
            posicao = {"x": pos["x"] + 30, "y": pos["y"] + 15}
        else:
            print("Posição invalida", sys.exc_info()[0])

        return posicao

    def cria_velocidade(self):
        return {"x": 0, "y": 20}

    def start_area(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())

        return self.area

    def get_area(self):
        return self.area

    def atira(self):
        self.posicao["x"] -= self.velocidade["x"]
        self.posicao["y"] -= self.velocidade["y"]
        self.start_area()