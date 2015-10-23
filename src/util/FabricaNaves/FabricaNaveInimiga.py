from src.util.FabricaNaves import FabricaNave


class FabricaNaveInimiga(FabricaNave):
    def __init__(self, nome, figuraNave, figuraExplosao, som):
        super(FabricaNaveInimiga, self).__init__(nome, figuraNave, figuraExplosao, som)
        self.pontuacaoDerrotar = 0

    #  @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.criaArea()
