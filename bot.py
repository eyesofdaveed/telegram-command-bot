# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import threading

""" Error catcher """
import logging

""" Bot is linked to a local variable """
updater = Updater(token='1826674897:AAGj09HwS9c6sdtn6ExWgEODwjjN7D3Z2Gg', use_context=True)
dispatcher = updater.dispatcher

""" Basic info on status of the bot """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

""" New User Handler """
def new_member(update, context):
    if update.message.new_chat_members:
        user = update.message.new_chat_members[0]
        context.bot.send_message(chat_id=update.effective_chat.id, text="""Добро пожаловать {}, 
        \nв группу для начинающих веб разработчиков. 
        \nТебя здесь ждет исключительно актуальная и полезная информация про сферу фронтенд программирования. \nА кстати я чат бот этой группы, и имею следующие команды:
        \n/demo - ссылка на пробные уроки
        \n/full - полный курс по вебке
        \n/contact - связь с нами""".format(user['username']))

""" /start """
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот SMAVY. Снизу ты можешь найти список команд:\n/demo - Доступ к пробным урокам\n/full - Запрос на полный курс\n/contact - Способы связаться с нами")

""" /demo """
def demo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пробные уроки можно пройти по ссылке внизу: \nhttps://www.smavy.kz/courses/trial")

""" /full """
def full(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Заполните заявку на нашем веб-сайте на полный доступ к нашим курсам и материалом:\nhttps://smavy.kz/apply/")

""" /contact """
def contact(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Помимо нашего канала здесь, с нами можно связаться через:\nhttps://www.instagram.com/smavyschool/")


""" /stop """
def stop(update, context):
    updater.dispatcher.add_handler(CommandHandler('stop', stop))


""" Shutdown the bot """
def shutdown():
    updater.stop()
    updater.is_idle = False

def stop(bot, update):
    threading.Thread(target=shutdown).start()

""" Echo out message"""
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

""" Unrecognized message/command """
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я к сожалению простой бот и не распознаю команду, попробуйте выбрать один из списка.")


""" Handle /start """
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

""" Handle /demo """
start_handler = CommandHandler('demo', demo)
dispatcher.add_handler(start_handler)

""" Handle /full """
start_handler = CommandHandler('full', full)
dispatcher.add_handler(start_handler)

""" Handle /contact """
start_handler = CommandHandler('contact', contact)
dispatcher.add_handler(start_handler)

""" Handle all non command messages """
""" echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler) """

""" Handle unknown messages """
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

""" Handle new users """
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))

""" Stops the bot """
updater.dispatcher.add_handler(CommandHandler('stop', stop))

""" Start the bot """
updater.start_polling()

print("Done...")



