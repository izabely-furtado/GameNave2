# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "20121bsi0040"
__date__ = "$14/10/2015 08:20:58$"

class FabricaAtributoNave(object):
    
    """-----AÇOES-------"""
    @abc.abstractmethod
    def __move__(self):
        return 0
        
    """"----ATRIBUTOS-----"""
    @abc.abstractmethod
    def __criaFigura__(self, figura):
        return 0
    
    @abc.abstractmethod
    def __criaPosicao__(self):
        return 0
    
    @abc.abstractmethod
    def __criaArea__(self):
        return 0
    
    @abc.abstractmethod
    def __criaVelocidade__(self):
        return 0
    