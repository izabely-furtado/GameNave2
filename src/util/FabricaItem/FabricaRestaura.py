# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 08:15:21$"

class FabricaRestaura(FabricaItem):
    def __init__(self, nome, imagemEscolhida, preco, probabilidade):
        super('Restaura', imagemEscolhida, 100, 30)
        
    @abc.abstract
    def modificacoes(self, jogador):
        jogador.restaura(jogador)