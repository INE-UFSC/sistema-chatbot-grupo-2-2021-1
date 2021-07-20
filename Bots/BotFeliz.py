from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ('Oiii! Prazer em conhecê-lo(a), eu sou o %s. :)' % self.__nome)
    
    def executa_comando(self, cmd: str) -> str:
        return self.__comandos[cmd]

    def boas_vindas(self) -> str:
        return 'Bem vindo(a)! Que felicidade poder atendê-lo(a)!!!'

    def despedida(self) -> str:
        return 'Adorei conversar com você! Espero que tenha um dia maravilhoso! :D'
