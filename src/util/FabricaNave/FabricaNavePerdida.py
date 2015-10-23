import random
from src.cdp.Habilidades import Municao
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNave import FabricaNaveInimiga

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


class FabricaNavePerdida(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super(FabricaNavePerdida).__init__('Nave Perdida', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 20
        self.municao = self.criaMunicao()

    # """---------------ACOES--------------------"""
    #  @abc.override
    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < LIM_WIDTH) and (self.posicao["x"] > 0):
            if aleatorio > 5:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == LIM_WIDTH:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]
        
        self.posicao["y"] += self.velocidade["y"]    
        self.criaArea()
    
    #   @abc.override
    def atira(self):
        if self.criaTiro(self.posicao) != "ERRO":
            self.criaTiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()

    # """--------------ATRIBUTO------------------------------------------------"""
    #  @abc.override
    def criaTiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.municao.append(m)
        return m
    
    # @abc.override
    def criaMunicao(self):
        return []
    
    # @abc.override
    def criaVelocidade(self):
        return {"x": 1, "y": 1}
    
    # @abc.override
    def criaResistencia(self):
        return Resistencia.Resistencia(2,2)
