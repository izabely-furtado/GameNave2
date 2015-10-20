# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "IzabelyFurtado"
__date__ = "$20/10/2015 09:17:54$"

class FabricaObjeto(Object):
    def __init__(self, nome, imagemEscolhida):
        self.nome = nome
        self.imagemObjeto = criaFigura(imagemEscolhida)
        self.posicao = self.criaPosicao()
        self.area = self.criaArea()
        self.velocidade = self.criaVelocidade()
        self.atingido = False
        
    """-----------AÇOES------------------------------------------------------"""
    def get_area(self):
        return self.area
    
    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
    
    """--------ATRIBUTOS-----------------------------------------------------"""
    @staticmethod
    def criaFigura(figura):
        f = pygame.image.load(figura).convert_alpha()
        return f
    
    def criaPosicao(self):
        return {"x": 0, "y": 0, "direcao": "DIREITA"}

    def criaArea(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())
        return Rect(self.posicao["x"], self.posicao["y"], self.figura.get_width(), self.figura.get_height())
    
    def criaVelocidade(self):
        return {"x": 0, "y": 2}
