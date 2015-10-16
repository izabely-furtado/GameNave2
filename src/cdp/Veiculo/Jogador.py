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


class Jogador(Nave):

    def __init__(self, nome, figura):
        super(nome, figura)
        self.fase = 0
        self.pontuacao = 0
        self.tempoMissel = 0
