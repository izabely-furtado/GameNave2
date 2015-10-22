__author__ = 'IzabelyFurtado'
__date__ = "$17/10/2015 15:20:23$"

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Personagem():
    def __init__(self, nave):
        self.veiculo = nave

    def get_area(self):
        return self.veiculo.nave.getArea()

    def armamento(self):
        return self.veiculo.nave.municao

    def removeTiro(self, tiro):
        assert isinstance(self.veiculo, object)
        self.veiculo.nave.municao.remove(tiro)

    def getPosicaoY(self):
        return self.veiculo.nave.posicao["y"]

    def getPosicaoX(self):
        return self.veiculo.nave.posicao["x"]

    def setPosicaoY(self, valor):
        self.veiculo.nave.posicao["y"] = valor

    def setPosicaoX(self, valor):
        self.veiculo.nave.posicao["x"] = valor

    def start_area(self):
        return self.veiculo.nave.criaArea()

    def atira(self):
        self.veiculo.nave.atira()

    def figura(self):
        return self.veiculo.imagemNave

    def atingido(self):
        return self.veiculo.nave.atingido

    def foiAtingido(self):
        self.veiculo.nave.atingido = True

    def move(self):
        self.veiculo.nave.move()