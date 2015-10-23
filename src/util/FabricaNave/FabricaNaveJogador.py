from src.cdp.Habilidades import Municao
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNave import FabricaNave


class FabricaNaveJogador(FabricaNave):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        super(FabricaNaveJogador).__init__(nome, figuraNave, figuraExplosao, som)
        self.tempoMissel = 0
        self.municao = self.criaMunicao()

    # """---------------ACOES----------------------"""
    #  @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
       
    #  @abc.override
    def atira(self):
        if self.criaTiro(self.posicao) != "ERRO":
            self.criaTiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()

    # """--------------ATRIBUTO------------------"""
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
        return {"x": 0, "y": 2}
    
    # @abc.override
    def criaResistencia(self):
        return Resistencia.Resistencia(10,2)
    

