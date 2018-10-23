from telegram.ext import Updater
import logging
from telegram.ext import MessageHandler, Filters
import threading
from telegram.ext import CommandHandler
import config


updater = Updater(token=config.BOT_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sinkata si gaze!")

def shutdown():
    updater.stop()
    updater.is_idle = False

def stop(bot, update):
    threading.Thread(target=shutdown).start()

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.dispatcher.add_handler(CommandHandler('stop', stop))

justin_trigger = {
    "sine:":"neka pushat kur!",
    "kako si":"Prijatno be brat.",
    "sinka od kaj si?":"Sine doagjam od Bajro",
    "apo mnogu jak":"Takov e be brat.",
    "apo nogu jak":"Takov e be brat!",
    "kaj sum sine":"Proveri na shanko\'",
    "nastinat":"https://www.youtube.com/watch?v=g88KrE9smHc",
    "brat": "(brat)",
    "tri":"Pod kuro mi se skri!",
    "3":"Pod kuro mi se skri!",
    "zdr":"Bomboklat!",
    "jat":"(jat - jat - jat)",
    "keva brat":"kuro da mi jat!"
    }

def echo(bot, update):
    msg_txt = update.message.text
    msg_txt = msg_txt.lower()
    msg_list = msg_txt.split(" ")
    last = msg_list[-1]
    if last in justin_trigger.keys():
        bot.send_message(chat_id=update.message.chat_id, text=justin_trigger[last])
    elif "bev na orevche na trap" in msg_txt:
        bot.send_message(chat_id=update.message.chat_id, text="(trap)")
        bot.send_message(chat_id=update.message.chat_id, text="manav sine ap")
        bot.send_message(chat_id=update.message.chat_id, text="(ap)")
        bot.send_message(chat_id=update.message.chat_id, text="apo nogu jak")
        bot.send_message(chat_id=update.message.chat_id, text="(jak)")
        bot.send_message(chat_id=update.message.chat_id, text="takov e be brat...")
    elif last == "sto":
        bot.send_message(chat_id=update.message.chat_id, text="dvesta")
        bot.send_message(chat_id=update.message.chat_id, text="trista, sine")
        bot.send_message(chat_id=update.message.chat_id, text="500")
    else:
        for key in justin_trigger.keys():
            if key in msg_txt:
                bot.send_message(chat_id=update.message.chat_id, text=justin_trigger[key])

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()