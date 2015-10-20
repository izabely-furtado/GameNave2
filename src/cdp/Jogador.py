# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$17/10/2015 15:20:23$"

class NaveJogoDirector(Object):
    def __init__(self, nome, imagemEscolhida, naveEscolhida):
        self.nome = nome
        self.imagemID = imagemEscolhida
        self.fase = 1
        self.pontos = 0
        self.vidas = 3
        self.nave = self.criandoNaveJogador(naveEscolhida)
    
    def criandoNaveJogador(self, naveImagemEscolhida):
        naveBuilder = NaveJogadorBuilder(naveImagemEscolhida)
        naveJogador = NaveJogoDirector(naveBuilder)
        naveJogador.construirNave()
        nave = naveJogador.getNave()
        return nave
        
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
        self.nave.nave.resistencia = Resitencia.Resistencia(10,20)