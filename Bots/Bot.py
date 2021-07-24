##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r


class Bot(ABC):
    def __init__(self, nome :str):
        self.__nome = nome
        self.__comandos = {"1" : "Bom dia","2" : "Qual o seu nome?", "3" : "Quero um conselho", "4" : "Adeus"}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def mostra_comandos(self):
        for i in self.__comandos:
            print(i + " - " + self.__comandos[i])

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
