#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste

###construa a lista de bots disponíveis aqui

botTriste = BotTriste("Neymar")
botFeliz = BotFeliz("Guga")
botZangado = BotZangado("Yoda")

lista_bots = [botZangado, botFeliz, botTriste]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
