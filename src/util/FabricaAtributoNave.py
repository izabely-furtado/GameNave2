# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:20:58$"

class FabricaAtributoNave(object):
    
    def __init__(self):
        self.esbarrar = 0
        self.danoPorTiro = 0
    
    @abc.abstractmethod
    def __criaVelocidade__(self):
        return 0
    
    @abc.abstractmethod
    def __criaMovimento__(self):
        return 0
    
    @abc.abstractmethod
    def __criaResistencia__(self):
        return 0
    
    @abc.abstractmethod
    def __criaMunicao__(self):
        return 0
    
    @abc.abstractmethod
    def __criaExplosao__(self):
        return 0;
