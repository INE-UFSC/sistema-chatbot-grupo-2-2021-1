from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ('Aff, estão me perturbando de novo! Eu sou o %s >:@' % self.__nome)
    
    def executa_comando(self, cmd: str) -> str:
        return self.__comandos[cmd]

    def boas_vindas(self) -> str:
        return 'Meu deus, eu não tenho um dia de paz!!'

    def despedida(self) -> str:
        return 'ALELUIA!!! Não aguentava mais.'
