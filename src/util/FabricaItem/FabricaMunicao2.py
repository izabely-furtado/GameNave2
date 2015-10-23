from src.util.FabricaItem import FabricaMunicao
from src.cgd import Path


class FabricaMunicao2(FabricaMunicao):
    def __init__(self):
        super(FabricaMunicao2, self).__init__(Path.getPath() + "Imagem/Item/Municao2.png", 200, 5)
