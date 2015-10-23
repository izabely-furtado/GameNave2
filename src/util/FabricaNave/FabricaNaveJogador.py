# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from src.cdp.Habilidades.Municao import Municao
from src.cdp.Habilidades.Resistencia import Resistencia
from src.util.FabricaNave.FabricaNave import FabricaNave

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:21:32$"

class FabricaNaveJogador(FabricaNave):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        super(FabricaNaveJogador).__init__(nome, figuraNave, figuraExplosao, som)
        self.tempoMissel = 0
        self.municao = self.criaMunicao()


    """---------------A�OES--------------------------------------------------"""
#    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
       
 #   @abc.override
    def atira(self):
        if self.criaTiro(self.posicao) != "ERRO":
            self.criaTiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()

    """--------------ATRIBUTO------------------------------------------------"""
    
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
    
    #@abc.override
    def criaVelocidade(self):
        return {"x": 0, "y": 2}
    
    #@abc.override
    def criaResistencia(self):
        return Resistencia.Resistencia(10,2)
    

