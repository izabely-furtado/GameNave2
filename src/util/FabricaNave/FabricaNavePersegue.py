# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$15/10/2015 20:22:42$"

class FabricaNavePersegue(FabricaNaveInimiga):
    def __init__(self, figuraNave, figuraExplosao, som):
        super('Nave Perseguidora', figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 40
        self.municao = self.criaMunicao()

    """---------------AÇOES--------------------------------------------------"""
    @abc.override
    def move(self, posicaoJogador):
        if (posicaoJogador["x"] > self.posicao["x"]):
            self.posicao["x"] += self.velocidade["x"]
        elif (posicaoJogador["x"] < self.posicao["x"]):
            self.posicao["x"] -= self.velocidade["x"]
        
        if (posicaoJogador["y"] > self.posicao["y"]):
            self.posicao["y"] += self.velocidade["y"]
        elif (posicaoJogador["y"] < self.posicao["y"]):
            self.posicao["y"] -= self.velocidade["y"]
        
        self.criaArea()
        
    @abc.override
    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()

    """--------------ATRIBUTO------------------------------------------------"""
    
    @abc.override
    def criaTiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.municao.append(m)
        return m
    
    @abc.override
    def criaMunicao(self):
        return []
    
    @abc.override
    def criaVelocidade(self):
        return {"x": 0, "y": 1}
    
    @abc.override
    def criaResistencia(self):
        return Resitencia.Resistencia(4,2)

