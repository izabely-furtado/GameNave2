from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga


class FabricaNaveFuga(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super(FabricaNaveFuga, self).__init__('Nave de Fuga', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 50
        
    # """---------------ACOES-----------------"""
    # abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.posicao["x"] += self.velocidade["x"]
        self.criaArea()
        
    # """--------------ATRIBUTO---------------"""
    # abc.override
    def criaVelocidade(self):
        return {"x": 3, "y": 3}
    
    # abc.override
    def criaResistencia(self):
        return Resistencia.Resistencia(5,1)
