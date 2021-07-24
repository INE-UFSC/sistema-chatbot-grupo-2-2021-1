from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ('Oiii! Prazer em conhecê-lo(a), eu sou o %s. :)' % self.nome)
    
    def executa_comando(self, cmd: str) -> str:
        respostas = {"1": "Hoje é o dia mais feliz da vida, porque hoje é único.",
                     "2": ("É %s, um belo nome não?" % self.nome),
                     "3": "Faça dos seus momentos, instantes de vida que valem a pena serem vividos",
                     "4": "Seja Feliz! Boa sorte no teu caminho!"}
        return respostas[cmd]

    def boas_vindas(self) -> str:
        return 'Bem vindo(a)! Que felicidade poder atendê-lo(a)!!!'

    def despedida(self) -> str:
        return 'Adorei conversar com você! Espero que tenha um dia maravilhoso! :D'
