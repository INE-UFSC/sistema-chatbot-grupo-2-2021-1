from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        
        return "Olá, esse é o sistema de chatbots da empresa " + self.__empresa 

    def mostra_menu(self):
       
        return self.__lista_bots
    
    def escolhe_bot(self, numero):
        self.__bot = self.__lista_bots[numero]
        return self.__bot.boas_vindas()
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self, comando):

        return self.__bot.executa_comando(comando)         
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        sistema = SistemaChatBot()
        sistema.boas_vindas()
        sistema.mostra_menu()
        sistema.escolhe_bot("Digite o número do chat bot desejado: ")
        sistema.mostra_comandos_bot()
        while True:
            sistema.mostra_comandos_bot()
            sistema.le_envia_comando("Digite o comando desejado (ou -1 fechar o programa e sair): ")
            sistema.boas_vindas()
            sistema.mostra_menu()
            sistema.escolhe_bot("Digite o número do chat bot desejado: ")
            sistema.mostra_comandos_bot()    
        