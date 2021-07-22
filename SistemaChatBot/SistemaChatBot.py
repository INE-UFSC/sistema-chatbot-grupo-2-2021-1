from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self,nome_empresa,lista_bots):
        self.__empresa=nome_empresa
        self.__bot = None
        self.__lista_bots = []
        for bot in lista_bots:
            if type(bot) == Bot:
                self.__lista_bots.append(bot)

    def boas_vindas(self):
        
        print("Olá, esse é o sistema de chatbots da empresa " + self.__empresa) 

    def mostra_menu(self):
        
        for index, bot in enumerate(self.__lista_bots):
            print(str(index)+" - Bot: " + bot.nome + " - Mensagem de apresentação: " 
            + bot.apresentacao())
    
    def escolhe_bot(self, numero):
        self.__bot = self.__lista_bots[numero]
        print(self.__bot.boas_vindas())
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):

        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self, comando):

        print("--> "+self.__bot.nome +" diz: " + self.__bot.comandos[comando])
        print(" --> Eu te respondo:" + self.__bot.executa_comando(comando))         
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        escolhaBot = input("Digite o número do chat bot desejado: ")
        self.escolhe_bot(escolhaBot)
        self.mostra_comandos_bot()
        while True:
            escolhaComando = input("Digite o comando desejado (ou -1 fechar o programa e sair): ")
            if escolhaComando == "-1":
                print(self.le_envia_comando("4"))
                break
            self.le_envia_comando(escolhaComando)
            self.mostra_comandos_bot()    
        
