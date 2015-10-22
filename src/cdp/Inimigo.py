# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.cdp.Habilidades.Resitencia import Resistencia
from src.cdp.Personagem import Personagem
from src.util.Build.NaveJogadorBuilder import NaveJogadorBuilder
from src.util.Build.NaveJogoDirector import NaveJogoDirector

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 15:20:23$"

class Inimigo(Personagem):
    def __init__(self, naveEscolhida):
        super(Inimigo.criandoNaveInimiga(naveEscolhida))

    @staticmethod
    def criandoNaveInimiga(naveInimiga):
        naveBuilder = naveInimiga
        naveJogador = NaveJogoDirector(naveBuilder)
        naveJogador.construirNave()
        nave = naveJogador.getNave()
        return nave
