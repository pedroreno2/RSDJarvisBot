import telegram
import logging

from telegram.ext import Updater, CommandHandler
from Instances    import Instances



#Token do Bot
updater    = Updater('327349585:AAHQ0IR1C4a8mzVOn7p4KdNJK8hwvsILxvk')
dispatcher = updater.dispatcher


#Loggin ( Error Report)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -\
%(message)s', level=logging.INFO)


#Main do Bot
def start(bot, update):

    welcomeMsg = "Hello I'm your RSD Jarvis Bot, what do you want, Sir?"


    #Buttons
    btnsMain = [[telegram.KeyboardButton('/Instrutores')],
                [telegram.KeyboardButton('/Ajuda')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnsMain,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text=welcomeMsg,
                     reply_markup=reply_kb_markup)







def instrutores(bot, update):

    btnsInstrutores = [[telegram.KeyboardButton('/Tyler')],
                       [telegram.KeyboardButton('/Julien')],
                       [telegram.KeyboardButton('/Max')],
                       [telegram.KeyboardButton('/Madison')],
                       [telegram.KeyboardButton('/Luke')],
                       [telegram.KeyboardButton('/Jeffy')],
                       [telegram.KeyboardButton('/Ozzye')],
                       [telegram.KeyboardButton('/Maze')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnsInstrutores,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os Instrutores RSD',
                     reply_markup=reply_kb_markup)




def Tyler(bot, update):

    btnInstrutorTyler = [[telegram.KeyboardButton('/Sobre')],
                         [telegram.KeyboardButton('/Programas')],
                         [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorTyler,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=tyler.botGetAll(),
                     reply_markup=reply_kb_markup)
)


def Julien(bot, update):

    btnInstrutorJulien = [[telegram.KeyboardButton('/Sobre')],
                          [telegram.KeyboardButton('/Programas')],
                          [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorJulien,
    resize_keyboard=True,
    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
    text=julien.botGetAll(),
    reply_markup=reply_kb_markup)


def Max(bot, update):

    btnInstrutorMax = [[telegram.KeyboardButton('/Sobre')],
                       [telegram.KeyboardButton('/Programas')],
                       [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMax,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=maximilian.botGetAll(),
                     reply_markup=reply_kb_markup)






def Madison(bot, update):

    btnInstrutorMadison = [[telegram.KeyboardButton('/Sobre')],
                           [telegram.KeyboardButton('/Programas')],
                           [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMadison,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=madison.botGetAll(),
                     reply_markup=reply_kb_markup)



def Luke(bot, update):

    btnInstrutorLuke = [[telegram.KeyboardButton('/Sobre')],
                        [telegram.KeyboardButton('/Programas')],
                        [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorLuke,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=luke.botGetAll(),
                     reply_markup=reply_kb_markup)




def Jeffy(bot, update):

    btnInstrutorJeffy = [[telegram.KeyboardButton('/Sobre')],
                         [telegram.KeyboardButton('/Programas')],
                         [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorJeffy,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=jeffy.botGetAll(),
                     reply_markup=reply_kb_markup)




def Ozzie(bot, update):

    btnInstrutorOzzie = [[telegram.KeyboardButton('/Sobre')],
                         [telegram.KeyboardButton('/Programas')],
                         [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorOzzie,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=ozzie.botGetAll(),
                     reply_markup=reply_kb_markup)





def Maze(bot, update):

    btnInstrutorMaze = [[telegram.KeyboardButton('/Sobre')],
                        [telegram.KeyboardButton('/Programas')],
                        [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMaze,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=maze.botGetAll(),
                     reply_markup=reply_kb_markup)





#Handlers
start_handler          = CommandHandler('Start', start)
instrutores_handler    = CommandHandler('Instrutores', instrutores)

instrutorTyler_handler = CommandHandler('Tyler', Tyler)
instrutorJulien_handler = CommandHandler('Julien', Julien)
instrutorMax_handler = CommandHandler('Max', Max)
instrutorMadison_handler = CommandHandler('Madison', Madison)
instrutorLuke_handler = CommandHandler('Luke', Luke)
instrutorJeffy_handler = CommandHandler('Jeffy', Jeffy)
instrutorOzzie_handler = CommandHandler('Ozzie', Ozzie)
instrutorMaze_handler = CommandHandler('Maze', Maze)




#Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(instrutores_handler)

dispatcher.add_handler(instrutorTyler_handler)
dispatcher.add_handler(instrutorJulien_handler)
dispatcher.add_handler(instrutorMax_handler)
dispatcher.add_handler(instrutorMadison_handler)
dispatcher.add_handler(instrutorLuke_handler)
dispatcher.add_handler(instrutorJeffy_handler)
dispatcher.add_handler(instrutorOzzie_handler)
dispatcher.add_handler(instrutorMaze_handler)



#Make it Alive!
updater.start_polling()
