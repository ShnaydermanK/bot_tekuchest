import telebot
from handlers import StartHandler, TekuchestRoHandler, RunCodeHandler, RunUdalHandler, RunOfficelHandler

TOKEN = '6337820389:AAFBgcFXyzN8AnQOC57Enag_gykXS2OMvTo'
bot = telebot.TeleBot(TOKEN)

start_handler = StartHandler(bot)
tekuchest_ro_handler = TekuchestRoHandler(bot)
run_code_handler = RunCodeHandler(bot)
runUdal_handler = RunUdalHandler(bot)
RunOffice_handler = RunOfficelHandler(bot)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler.handle(message)

@bot.message_handler(commands=['tekuchest_ro'])
def handle_tekuchest_ro(message):
    tekuchest_ro_handler.handle(message)

@bot.message_handler(commands=['run'])
def handle_run_code(message):
    run_code_handler.handle(message)

@bot.message_handler(commands=['RunUdal'])
def handle_run_code(message):
    runUdal_handler.handle(message)

@bot.message_handler(commands=['RunOffice'])
def handle_run_code(message):
    RunOffice_handler.handle(message)

bot.polling()

