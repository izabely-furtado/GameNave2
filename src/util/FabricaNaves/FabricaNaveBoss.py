import random
from src.cdp.Habilidades import Municao
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


class FabricaNaveBoss(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super(FabricaNaveBoss, self).__init__('BOSS!!', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 200
        self.municao = self.criaMunicao()

    # """---------------ACOES----------------------"""
    #    @abc.override
    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < LIM_WIDTH - aleatorio) and (self.posicao["x"] > 0 + aleatorio):
            if aleatorio < 5:
                self.posicao["x"] += self.velocidade["x"] + aleatorio
            else:
                self.posicao["x"] -= self.velocidade["x"] - aleatorio
        elif self.posicao["x"] == LIM_WIDTH:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]
        
        if (self.posicao["y"] < LIM_HEIGTH - aleatorio) and (self.posicao["y"] > 0 + aleatorio):
            if aleatorio < 5:
                if self.posicao["direcao"] != "ABAIXO":
                    self.posicao["y"] += self.velocidade["y"] + aleatorio
                    self.posicao["direcao"] = "ABAIXO"
                else:
                    self.posicao["y"] -= self.velocidade["y"] - aleatorio
                    self.posicao["direcao"] = "ACIMA"

        self.criaArea()
    """
    #  @abc.override
    def atira(self):
        if self.criaTiro(self.posicao) != "ERRO":
            self.criaTiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()
    """
    # """--------------ATRIBUTO----------------------"""

    # @abc.override
    def criaVelocidade(self):
        return {"x": 1, "y": 1}
    
    # @abc.override
    def criaResistencia(self):
        return Resistencia.Resistencia(10,4)