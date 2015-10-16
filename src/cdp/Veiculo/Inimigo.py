#!/usr/local/bin/python
from CamadaDominioProblema.Veiculo import Nave

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine e Izabely'


class Inimigo(Nave):
    def __init__(self, nome, figura):
        super(nome, figura)
        self.pontuacao_por_derrotar = 0
        self.estrategia = None

    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.start_area()
