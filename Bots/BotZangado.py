from Bots.Bot import Bot

class BotZangado(Bot):
    comandos = {"1": "Bom dia", 
                "2": "Qual o seu nome?",
                "3": "Quero um conselho",
                "4": "Adeus"}
    
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ("Aff, estão me perturbando de novo! Eu sou o %s >:@" % self.nome)
    
    def executa_comando(self, cmd: str) -> str:
        respostas = {"1": "Bom dia? Bom dia pra quem??!!",
                     "2": ("É %s!!! Você tem uma memória péssima assim sempre?" % self.nome),
                     "3": "Hmmm... que tal parar de incomodar os outros? Esse é o meu conselho.",
                     "4": "Poderia dizer que foi um prazer, mas estaria mentindo."}
        return respostas[cmd]

    def boas_vindas(self) -> str:
        return "Meu deus, eu não tenho um dia de paz!!"

    def despedida(self) -> str:
        return "ALELUIA!!! Não aguentava mais."
