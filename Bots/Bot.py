##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(nome :str):
        self.__nome = nome
        self.comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome):
        self.__nome = nome

    def mostra_comandos(self):
        return(list(self.comandos))

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass