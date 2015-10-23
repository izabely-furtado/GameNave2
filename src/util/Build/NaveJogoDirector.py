

class NaveJogoDirector(object):
    def __init__(self, naveBuilder):
        self.montadora = naveBuilder
        
    def construirNave(self):
        self.montadora.buildDano()
        self.montadora.buildImagemNave()
        self.montadora.buildImagemExplode()
        self.montadora.buildSom()
        self.montadora.buildNave()

    def getNave(self):
        return self.montadora.nave

