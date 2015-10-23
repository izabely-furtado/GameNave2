
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
from src.cdp.Veiculo.Inimigo import Inimigo

__author__ = 'Gislaine e Izabely'


class General(Inimigo):
    def __init__(self, nome, figura):
        super.__init__(nome, figura)
