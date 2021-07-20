##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(self, nome :str):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def mostra_comandos(self):
        a = list(self.__comandos)
        for i in range(len(self.__comandos)):
            print( str(i + 1) + " - " + str(a[i]))

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass