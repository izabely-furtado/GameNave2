# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:15:03$"

class FabricaVida(FabricaItem):
    def __init__(self):
        super('Vida', "/Imagens/Vida.png", 100, 20)
        
    @abc.abstract
    def modificacoes(self, jogador):
        jogador.maisVida(jogador)