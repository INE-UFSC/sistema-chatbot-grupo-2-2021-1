from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome: str):
        super().__init__(nome)

    def apresentacao(self) -> str:
        return ('Ola... Eu sou o %s... não que isso importe... >:@' % self.nome)
    
    def executa_comando(self, cmd: str) -> str:
        respostas = {"1": "Bom dia? Se for pra você beleza, pra mim é só tristeza.",
                     "2": ("É ...%s, um nome triste eu sei." % self.nome),
                     "3": "Vida é dor e sofrimento, mas as vezes é só dor e outras só sofrimento.",
                     "4": "Se existe felicidade, diria que foi um prazer..."}
        return respostas[cmd]
        

    def boas_vindas(self) -> str:
        return 'Oi... Você esta bem? Pois eu nao estou...'

    def despedida(self) -> str:
        return 'Tchau... ve se você se cuida...'
