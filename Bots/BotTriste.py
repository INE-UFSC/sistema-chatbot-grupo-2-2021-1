from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ('Ola... Eu sou o %s... não que isso importe... >:@' % self.__nome)
    
    def executa_comando(self, cmd: str) -> str:
        return self.__comandos[cmd]

    def boas_vindas(self) -> str:
        return 'Oi... Você esta bem? Pois eu nao estou...'

    def despedida(self) -> str:
        return 'Tchau... ve se você se cuida...'
