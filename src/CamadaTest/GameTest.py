from CamadaDominioProblema.Habilidades import Municao
from CamadaDominioProblema.Veiculo import Nave
__author__ = 'IzabelyFurtado e GislaineJessica'

import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def cria_posicao_valido(self):
        val = 100
        resultado = {"x": val["x"] + 30, "y": val["y"] + 15}
        self.assertEqual(resultado, Municao.cria_posicao(val))

    def cria_posicao_invalid0(self):
        val = 100000
        resultado = {}
        self.assertEqual(resultado, Municao.cria_posicao(val))

    def cria_tiro_valido(self):
        val = 100
        resultado = Municao.Municao(val)
        self.assertEqual(resultado, Nave.cria_tiro(val))

    def cria_tiro_invalid0(self):
        val = 100000
        resultado = "ERRO"
        self.assertEqual(resultado, Nave.cria_tiro(val))




if __name__ == '__main__':
    unittest.main()
