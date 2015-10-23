# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.cdp.Habilidades.Resistencia import Resistencia
from src.cdp.Personagens import Personagem
#rom src.util.Build.NaveJogadorBuilder import NaveJogadorBuilder
#from src.util.Build.NaveJogoDirector import NaveJogoDirector
__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 15:20:23$"

class Jogador(Personagem):
    def __init__(self, nome, imagemID, naveEscolhida):
        super(Jogador.criandoNaveJogador(naveEscolhida))
        self.nome = nome
        self.imagemID = imagemID
        self.fase = 1
        self.pontos = 0
        self.vidas = 3

    def ganhaPontos(self, pontos):
        if (pontos > 0):
            self.pontos += pontos
    
    def compraItem(self, item):
        if (self.pontos >= item.preco):
            self.pontos -= item.preco
            item.modificacoes(self)
        
    def avancaFase(self):
        self.fase += 1
    
    def maisVida(self):
        self.vida += 1
        
    def trocaNave(self, naveEscolhida):
        self.nave = self.criandoNaveogador(naveEscolhida)
        
    def restaura(self):
        self.nave.setDano(0)
    
    def clone(self):
        self.nave.nave.resistencia = Resistencia.Resistencia(10, 20)
