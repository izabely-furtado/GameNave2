from src.cdp.Habilidades import Resistencia
from src.cdp.Personagens import Personagem


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
