import telegram
import logging

from telegram.ext import Updater, CommandHandler
from Instrutor    import Instrutor
from Canal        import Canal
from Programa     import Programa



#Instânciando Canais
canalTyler   = Canal('Owen Cook', 'RSD Tyler',
                     'https://www.youtube.com/RSDTyler',
                     '20/11/2010', 149)

canalJulien  = Canal('Julien Blanc', 'JulienHimSelf',
                     'https://www.youtube.com/channel/UCaN4Pe5JEsWzAByY2WfxxjQ',
                     '17/05/2015', 178)

canalMax     = Canal('Maximilian Berger', 'RSDMax',
                     'https://www.youtube.com/RSDMaximilian',
                     '28/03/2014', 297)

canalMadison = Canal('Madison', 'RSD Madison',
                     'https://www.youtube.com/MontrealRSDCrew',
                     '04/09/2010', 122)

canalLuke    = Canal('Luke', 'RSD Luke',
                     'https://www.youtube.com/channel/UC2XMvfBq5w2P4_ZYOsMlxVg',
                     '08/10/2015', 64)

canalJeffy   = Canal('Jeffy', 'jlaix',
                     'https://www.youtube.com/RSDJeffy',
                     '25/11/2010', 171)

canalOzzie   = Canal('Ozzie', 'RSD Ozzie',
                     'https://www.youtube.com/RSDOzzie',
                     '28/11/2010', 37)

canalMaze    = Canal('Maze', 'RSD Maze',
                     'https://www.youtube.com/channel/UC1MWQJGBSIGXvL7Gld5PKBw',
                     '04/03/2017', 9)

#Instâncias Programas

HotSeatAtHome                  = Programa('Owen Cook', 'Hot Seat At Home', '?', 'R$297,00')

HotSeatAtHomeMastermindEdition = Programa('Owen Cook', 'Hot Seat At Home Mastermind Edition', '?', 'R$397,00')

TheBlueprintDecoded            = Programa('Owen Cook', 'The Blueprint Decoded', '?', 'R$397,00')

TransformationMastery          = Programa('Julien Blanc', 'Transformation Mastery', '?', 'R$297,00')

Pimp                           = Programa('Julien Blanc', 'PIMP', '?', 'R$197,00')

Shift                          = Programa('Julien Blanc', 'SHIFT', '?', 'R$297,00')

TenGame                        = Programa('Julien Blanc', 'Ten Game', '?', 'R$297,00')

Fearless                       = Programa('Maximilian Berger', 'Fearless', '?', 'R$397,00')

TheNatural                     = Programa('Maximilian Berger', 'The Natural', '?', 'R$497,00')

MadisonBootcampAtHome          = Programa('Madison', 'Madison Bootcamp At Home', '?', 'R$297,00')

Boss                           = Programa('Madison', 'Boss', '?', 'R$297,00')

SocialCircleBlueprint          = Programa('Luke', 'Social Circle Blueprint', '?', 'R$297,00')

SocialCircleBlueprint2         = Programa('Luke', 'Social Circle Blueprint 2.0', '?', '?')

Resonator                      = Programa('Jeffy', 'Resonator', '?', 'R$197,00')

ExecuteTheProgram2             = Programa('Jeffy', 'Execute The Program 2.0', '?', 'R$197,00')

TheJeffyShow                   = Programa('Jeffy', 'The Jeffy Show', '?', 'R$269,00')

NineBall                       = Programa('Jeffy', 'Nine Ball', '?', 'R$39,95')

ThePhysicalBook                = Programa('Ozzie', 'The Physical Book', '?', 'R$29,95')


#Instânciando Instrutores

tyler      = Instrutor('Owen Cook', '01/10/1979', canalTyler, ['Hot Seat at Home Mastermind Edition', 'Hot Seat at Home', 'The Blueprint Decoded'], 'Tyler is the Co-Founder and Executive Producer for Real Social Dynamics. He has been the creative mastermind and main public speaker at hundreds of RSD seminars worldwide. The foundational principles, concepts, and lessons of Real Social Dynamics centers around advanced content Tyler created while traveling the world and analyzing male-and-female interactions.')

julien     = Instrutor('Julien Blanc', '24/08/1988', canalJulien, ['Transformation Mastery', 'PIMP',  'SHIFT', 'Ten Game'], 'Julien Blanc is a Swiss-born, U.S.-based self-help speaker, entrepreneur and dating coach. He has been an executive coach for the Los Angeles-based company Real Social Dynamics since 2010, and has personally coached tens of thousands of clients face to face around the World, empowering them to create massive success in their lives! The company itself runs over one thousand events a year, in 70 countries and 270 cities. In 2015, Julien Blanc started his own company: JulienHimself and has shifted his teachings toward personal development and life-enrichment.')

maximilian = Instrutor('Maximilian Berger', '26/06/1990', canalMax, ['Fearless', 'The Natural'], 'RSD Max, executive coach for Real Social Dynamics, the international leader in dating advice. Dating advice, personal development, health, freedom.')

madison    = Instrutor('Madison', 'segredo', canalMadison, ['Madison Bootcamp at Home', 'Boss'], 'In 10 years, Madison has built a reputation as one of the worlds leading experts in self-confidence and cold-approach techniques. Having toured with every RSD instructor to assist on live programs and seminars all over North America, he has come a long way from his early days. To overcome his extreme introversion as a youth, he embarked on a journey of self discovery. He traveled the world, read over 500 personal development books, and aligned himself with world-renowned mentors, and worked daily to achieve a highly specific character and behavior-based road map to improvement. This all culminated in deep identity level change at the cellular level. His background includes working in the fashion, advertising, and music industry. He teaches confidence, originality, and razor sharp communication skills that will transform anyones approach to social interactions. With his inside expertise, Madison will fully prepare his clients to embark on or reach new heights in their personal journey.')

luke       = Instrutor('Luke', 'segredo', canalLuke, ['Social Circle Blueprint 2.0', 'Social Circle Blueprint', ], 'RSD’s First Ever LONG TERM EXPERIENTIAL PROGRAM Designed To Condense A Decade Of Gaming Experience In Record Breaking Time! Surrounded by like hard-core like-minded peers, in the most conducive environment for learning pick up known to man, Las Vegas, Nevada you will take your game to levels youve never known existed.')

jeffy      = Instrutor('Jeffy', 'segredo', canalJeffy, ['Resonator', 'Execute The Program 2.0', 'The Jeffy Show', 'Nine Ball'], 'Jeff Allen has been an Executive Coach with Real Social Dynamics since 2003 and is the author of "Get Laid or Die Trying." His channel features in depth information about dating, self-actualization and success in life.')

ozzie      = Instrutor('Ozzie', 'segredo', canalOzzie, ['The Physical Book'],'Ozzie was born and raised in Havana, Cuba. From a very young age, he realized that he was meant to travel the world and get an education that would allow him to achieve great things. He studied English at the University of Havana, and through hard work, he was eventually awarded a government scholarship to study in Europe. This provided him with the opportunity to leave Cuba, and move to Austria, where he learned business management.Over the years, he traveled throughout Europe, eventually settling in Spain, where he went on to play semi-professional baseball, and, also form his own successful business teaching English to locals. Still not content, Ozzie decided to learn as much as he could about male-female dynamics so he could have the fulfilling relationships that had always eluded him. He traveled the world, learning seduction and dating secrets from the best of the best.')

maze       = Instrutor('Maze', 'segredo', canalMaze, [], 'Ele é novo')







#-  -  -  -  -  -  -  -  -  -  -  - Respostas do Usuário -  -  -  -  -  -  -
#usu_oi = ['oi', 'oii', 'ola', 'olá', 'ooi', 'hello', 'hi', 'hii', 'hey']

#usu_tyler   = ['rsd tyler', 'tyler', 'rsdtyler', 'tylerrsd']

#usu_julien  = ['rsd julien', 'julien', 'rsdjulien', 'julienrsd']

#usu_max     = ['rsd max', 'max', 'rsdmax', 'maxrsd']

#usu_madison = ['', '', 'rsdmadison', 'madisonrsd']
#-  -  -  -  -  -  -  -  -  -  -  - ---------------- -  -  -  -  -  -  -  -  -



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
                       [telegram.KeyboardButton('/Ozzie')],
                       [telegram.KeyboardButton('/Maze')],]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnsInstrutores,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os Instrutores do RSD',
                     reply_markup=reply_kb_markup)












#Def Instrutores

def instrutorTyler(bot, update):

    btnInstrutorTyler = [[telegram.KeyboardButton('/SobreTyler')],
                         [telegram.KeyboardButton('/ProgramasTyler')],
                         [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorTyler,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=tyler.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorJulien(bot, update):

    btnInstrutorJulien = [[telegram.KeyboardButton('/SobreJulien')],
                          [telegram.KeyboardButton('/ProgramasJulien')],
                          [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorJulien,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=julien.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorMax(bot, update):

    btnInstrutorMax = [[telegram.KeyboardButton('/SobreMax')],
                       [telegram.KeyboardButton('/ProgramasMax')],
                       [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMax,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=maximilian.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorMadison(bot, update):

    btnInstrutorMadison = [[telegram.KeyboardButton('/SobreMadison')],
                           [telegram.KeyboardButton('/ProgramasMadison')],
                           [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMadison,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=madison.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorLuke(bot, update):

    btnInstrutorLuke = [[telegram.KeyboardButton('/SobreLuke')],
                        [telegram.KeyboardButton('/ProgramasLuke')],
                        [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorLuke,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=luke.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorOzzie(bot, update):

    btnInstrutorOzzie = [[telegram.KeyboardButton('/SobreOzzie')],
                         [telegram.KeyboardButton('/ProgramasOzzie')],
                         [telegram.KeyboardButton('/Instrutores')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorOzzie,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=ozzie.botGetAll(),
                     reply_markup=reply_kb_markup)



def instrutorMaze(bot, update):

    btnInstrutorMaze = [[telegram.KeyboardButton('/SobreMaze')],
                        [telegram.KeyboardButton('/Programas')],
                        [telegram.KeyboardButton('/Voltar')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnInstrutorMaze,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)



    bot.send_message(chat_id=update.message.chat_id,
                     text=maze.botGetAll(),
                     reply_markup=reply_kb_markup)




#Defs Sobres

def sobreTyler(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Tyler')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = tyler.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreJulien(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Julien')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = julien.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreMax(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Max')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = maximilian.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreMadison(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Madison')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = madison.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreLuke(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Luke')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = luke.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreJeffy(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Jeffy')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = jeffy.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreOzzie(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Ozzie')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = ozzie.getSobre(),
                     reply_markup = reply_kb_markup)




def sobreMaze(bot, update):

    btnSobre = [[telegram.KeyboardButton('/Maze')],
                [telegram.KeyboardButton('/Instrutores')]]


    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSobre,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = maze.getSobre(),
                     reply_markup = reply_kb_markup)




#Defs Apresentar Programas

def programasTyler(bot, update):

    btnProgramasTyler = [[telegram.KeyboardButton('/HotSeatAtHomeMastermindEdition')],
                         [telegram.KeyboardButton('/HotSeatAtHome')],
                         [telegram.KeyboardButton('/TheBlueprintDecoded')],
                         [telegram.KeyboardButton('/Tyler')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasTyler,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Tyler',
                     reply_markup=reply_kb_markup)




def programasJulien(bot, update):

    btnProgramasJulien = [[telegram.KeyboardButton('/TransformationMastery')],
                          [telegram.KeyboardButton('/PIMP')],
                          [telegram.KeyboardButton('/SHIFT')],
                          [telegram.KeyboardButton('/TenGame')],
                          [telegram.KeyboardButton('/Julien')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasJulien,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Julien',
                     reply_markup=reply_kb_markup)





def programasMax(bot, update):

    btnProgramasMax = [[telegram.KeyboardButton('/Fearless')],
                       [telegram.KeyboardButton('/TheNatural')],
                       [telegram.KeyboardButton('/Maximilian')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasMax,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Max',
                     reply_markup=reply_kb_markup)





def programasMadison(bot, update):

    btnProgramasMadison = [[telegram.KeyboardButton('/MadisonBootcampAtHome')],
                           [telegram.KeyboardButton('/Boss')],
                           [telegram.KeyboardButton('/Madison')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasMadison,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Madison',
                     reply_markup=reply_kb_markup)




def programasLuke(bot, update):

    btnProgramasLuke = [[telegram.KeyboardButton('/SocialCircleBlueprint2')],
                        [telegram.KeyboardButton('/SocialCircleBlueprint')],
                        [telegram.KeyboardButton('/Luke')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasLuke,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Luke',
                     reply_markup=reply_kb_markup)




def programasJeffy(bot, update):

    btnProgramasJeffy = [[telegram.KeyboardButton('/Resonator')],
                         [telegram.KeyboardButton('/ExecuteTheProgram2')],
                         [telegram.KeyboardButton('/TheJeffyShow')],
                         [telegram.KeyboardButton('/NineBall')],
                         [telegram.KeyboardButton('/Jeffy')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasJeffy,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Jeffy',
                     reply_markup=reply_kb_markup)




def programasOzzie(bot, update):

    btnProgramasOzzie = [[telegram.KeyboardButton('/ThePhysicalBook')],
                         [telegram.KeyboardButton('/Ozzie')]]



    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnProgramasOzzie,
                                                    resize_keyboard=True,
                                                    one_time_keyboard=True)


    bot.send_message(chat_id=update.message.chat_id,
                     text='Estes são os programs do Ozzie',
                     reply_markup=reply_kb_markup)


#Defs Programas

def hotSeatAtHome(bot, update):

    btnHotSeatAtHome = [[telegram.KeyboardButton('/Tyler')],
           [telegram.KeyboardButton('/ProgramasTyler')],
           [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnHotSeatAtHome,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = HotSeatAtHome.botGetAll(),
                     reply_markup = reply_kb_markup)




def hotSeatAtHomeMastermindEdition(bot, update):

    btnHotSeatAtHomeMastermindEdition = [[telegram.KeyboardButton('/Tyler')],
                                        [telegram.KeyboardButton('/ProgramasTyler')],
                                        [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnHotSeatAtHomeMastermindEdition,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = HotSeatAtHomeMastermindEdition.botGetAll(),
                     reply_markup = reply_kb_markup)




def theBlueprintDecoded(bot, update):

    btnTheBlueprintDecoded = [[telegram.KeyboardButton('/Tyler')],
                              [telegram.KeyboardButton('/ProgramasTyler')],
                                [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnTheBlueprintDecoded,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = TheBlueprintDecoded.botGetAll(),
                     reply_markup = reply_kb_markup)




def transformationMastery(bot, update):

    btnTransformationMastery = [[telegram.KeyboardButton('/Julien')],
                                [telegram.KeyboardButton('/ProgramasJulien')],
                                [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnTransformationMastery,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = TransformationMastery.botGetAll(),
                     reply_markup = reply_kb_markup)




def pimp(bot, update):

    btnPimp = [[telegram.KeyboardButton('/Julien')],
               [telegram.KeyboardButton('/ProgramasJulien')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnPimp,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = Pimp.botGetAll(),
                     reply_markup = reply_kb_markup)




def shift(bot, update):

    btnShift = [[telegram.KeyboardButton('/Julien')],
                [telegram.KeyboardButton('/ProgramasJulien')],
                [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnShift,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = Shift.botGetAll(),
                     reply_markup = reply_kb_markup)




def tenGame(bot, update):

    btnTenGame = [[telegram.KeyboardButton('/Julien')],
                    [telegram.KeyboardButton('/ProgramasJulien')],
                    [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnTenGame,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = TenGame.botGetAll(),
                     reply_markup = reply_kb_markup)




def fearless(bot, update):

    btnFearless = [[telegram.KeyboardButton('/Maximilian')],
               [telegram.KeyboardButton('/ProgramasMax')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnFearless,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = Fearless.botGetAll(),
                     reply_markup = reply_kb_markup)




def theNatural(bot, update):

    btnTheNatural = [[telegram.KeyboardButton('/Maximilian')],
               [telegram.KeyboardButton('/ProgramasMax')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnTheNatural,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = TheNatural.botGetAll(),
                     reply_markup = reply_kb_markup)




def madisonBootcampAtHome(bot, update):

    btnMadisonBootcampAtHome = [[telegram.KeyboardButton('/Madison')],
               [telegram.KeyboardButton('/ProgramasMadison')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnMadisonBootcampAtHome,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = MadisonBootcampAtHome.botGetAll(),
                     reply_markup = reply_kb_markup)




def boss(bot, update):

    btnBoss = [[telegram.KeyboardButton('/Madison')],
               [telegram.KeyboardButton('/ProgramasMadison')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnBoss,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = Boss.botGetAll(),
                     reply_markup = reply_kb_markup)




def socialCircleBlueprint(bot, update):

    btnSocialCircleBlueprint = [[telegram.KeyboardButton('/Luke')],
               [telegram.KeyboardButton('/ProgramasLuke')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSocialCircleBlueprint,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = SocialCircleBlueprint.botGetAll(),
                     reply_markup = reply_kb_markup)




def socialCircleBlueprint2(bot, update):

    btnSocialCircleBlueprint2 = [[telegram.KeyboardButton('/Luke')],
               [telegram.KeyboardButton('/ProgramasLuke')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnSocialCircleBlueprint2,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = SocialCircleBlueprint2.botGetAll(),
                     reply_markup = reply_kb_markup)




def resonator(bot, update):

    btnResonator = [[telegram.KeyboardButton('/Jeffy')],
               [telegram.KeyboardButton('/ProgramasJeffy')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnResonator,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = Resonator.botGetAll(),
                     reply_markup = reply_kb_markup)




def executeTheProgram2(bot, update):

    btnExecuteTheProgram2 = [[telegram.KeyboardButton('/Jeffy')],
               [telegram.KeyboardButton('/ProgramasJeffy')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnExecuteTheProgram2,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = ExecuteTheProgram2.botGetAll(),
                     reply_markup = reply_kb_markup)




def theJeffyShow(bot, update):

    btnTheJeffyShow = [[telegram.KeyboardButton('/Jeffy')],
               [telegram.KeyboardButton('/ProgramasJeffy')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnTheJeffyShow,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = TheJeffyShow.botGetAll(),
                     reply_markup = reply_kb_markup)




def nineBall(bot, update):

    btnNineBall = [[telegram.KeyboardButton('/Jeffy')],
               [telegram.KeyboardButton('/ProgramasJeffy')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnNineBall,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = NineBall.botGetAll(),
                     reply_markup = reply_kb_markup)




def thePhysicalBook(bot, update):

    btnThePhysicalBook = [[telegram.KeyboardButton('/Ozzie')],
               [telegram.KeyboardButton('/ProgramasOzzie')],
               [telegram.KeyboardButton('/Instrutores')]]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(btnThePhysicalBook,
                                                   resize_keyboard = True,
                                                   one_time_keyboard = True)

    bot.send_message(chat_id = update.message.chat_id,
                     text = ThePhysicalBook.botGetAll(),
                     reply_markup = reply_kb_markup)



#Handlers
start_handler       = CommandHandler('Start', start)
instrutores_handler = CommandHandler('Instrutores', instrutores)

instrutorTyler_handler   = CommandHandler('Tyler', instrutorTyler)
instrutorJulien_handler  = CommandHandler('Julien', instrutorJulien)
instrutorMax_handler     = CommandHandler('Max', instrutorMax)
instrutorMadison_handler = CommandHandler('Madison', instrutorMadison)
instrutorLuke_handler    = CommandHandler('Luke', instrutorLuke)
instrutorOzzie_handler   = CommandHandler('Ozzie', instrutorOzzie)
instrutorMaze_handler    = CommandHandler('Maze', instrutorMaze)

sobreTyler_handler   = CommandHandler('SobreTyler', sobreTyler)
sobreJulien_handler  = CommandHandler('SobreJulien', sobreJulien)
sobreMax_handler     = CommandHandler('SobreMax', sobreMax)
sobreMadison_handler = CommandHandler('SobreMadison', sobreMadison)
sobreLuke_handler    = CommandHandler('SobreLuke', sobreLuke)
sobreJeffy_handler   = CommandHandler('SobreJeffy', sobreJeffy)
sobreOzzie_handler   = CommandHandler('SobreOzzie', sobreOzzie)
sobreMaze_handler    = CommandHandler('SobreMaze', sobreMaze)

programasTyler_handler   = CommandHandler('ProgramasTyler', programasTyler)
programasJulien_handler  = CommandHandler('ProgramasJulien', programasJulien)
programasMax_handler     = CommandHandler('ProgramasMax', programasMax)
programasMadison_handler = CommandHandler('ProgramasMadison', programasMadison)
programasLuke_handler    = CommandHandler('ProgramasLuke', programasLuke)
programasJeffy_handler   = CommandHandler('ProgramasJeffy', programasJeffy)
programasOzzie_handler   = CommandHandler('ProgramasOzzie', programasOzzie)

hotSeatAtHome_handler                  = CommandHandler('HotSeatAtHome', hotSeatAtHome)
hotSeatAtHomeMastermindEdition_handler = CommandHandler('HotSeatAtHomeMastermindEdition', hotSeatAtHomeMastermindEdition)
theBlueprintDecoded_handler            = CommandHandler('TheBlueprintDecoded', theBlueprintDecoded)
transformationMastery_handler          = CommandHandler('TransformationMastery', transformationMastery)
pimp_handler                           = CommandHandler('PIMP', pimp)
shift_handler                          = CommandHandler('SHIFT', shift)
tenGame_handler                        = CommandHandler('TenGame', tenGame)
fearless_handler                       = CommandHandler('Fearless', fearless)
theNatural_handler                     = CommandHandler('TheNatural', theNatural)
madisonBootcampAtHome_handler          = CommandHandler('MadisonBootcampAtHome', madisonBootcampAtHome)
boss_handler                           = CommandHandler('Boss', boss)
socialCircleBlueprint_handler          = CommandHandler('SocialCircleBlueprint', socialCircleBlueprint)
socialCircleBlueprint2_handler         = CommandHandler('SocialCircleBlueprint2', socialCircleBlueprint2)
resonator_handler                      = CommandHandler('Resonator', resonator)
executeTheProgram2_handler             = CommandHandler('ExecuteTheProgram2', executeTheProgram2)
theJeffyShow_handler                   = CommandHandler('TheJeffyShow', theJeffyShow)
nineBall_handler                       = CommandHandler('NineBall', nineBall)
thePhysicalBook_handler                = CommandHandler('ThePhysicalBook', thePhysicalBook)



#Dispatchers
dispatcher.add_handler(start_handler)

dispatcher.add_handler(instrutores_handler)
dispatcher.add_handler(instrutorTyler_handler)
dispatcher.add_handler(instrutorJulien_handler)
dispatcher.add_handler(instrutorMax_handler)
dispatcher.add_handler(instrutorMadison_handler)
dispatcher.add_handler(instrutorLuke_handler)
dispatcher.add_handler(instrutorOzzie_handler)
dispatcher.add_handler(instrutorMaze_handler)

dispatcher.add_handler(sobreTyler_handler)
dispatcher.add_handler(sobreJulien_handler)
dispatcher.add_handler(sobreMax_handler)
dispatcher.add_handler(sobreMadison_handler)
dispatcher.add_handler(sobreLuke_handler)
dispatcher.add_handler(sobreJeffy_handler)
dispatcher.add_handler(sobreOzzie_handler)
dispatcher.add_handler(sobreMaze_handler)

dispatcher.add_handler(programasTyler_handler)
dispatcher.add_handler(programasJulien_handler)
dispatcher.add_handler(programasMax_handler)
dispatcher.add_handler(programasMadison_handler)
dispatcher.add_handler(programasLuke_handler)
dispatcher.add_handler(programasJeffy_handler)
dispatcher.add_handler(programasOzzie_handler)

dispatcher.add_handler(hotSeatAtHome_handler)
dispatcher.add_handler(hotSeatAtHomeMastermindEdition_handler)
dispatcher.add_handler(theBlueprintDecoded_handler)
dispatcher.add_handler(transformationMastery_handler)
dispatcher.add_handler(pimp_handler)
dispatcher.add_handler(shift_handler)
dispatcher.add_handler(tenGame_handler)
dispatcher.add_handler(fearless_handler)
dispatcher.add_handler(theNatural_handler)
dispatcher.add_handler(madisonBootcampAtHome_handler)
dispatcher.add_handler(boss_handler)
dispatcher.add_handler(socialCircleBlueprint_handler)
dispatcher.add_handler(socialCircleBlueprint2_handler)
dispatcher.add_handler(resonator_handler)
dispatcher.add_handler(executeTheProgram2_handler)
dispatcher.add_handler(theJeffyShow_handler)
dispatcher.add_handler(nineBall_handler)
dispatcher.add_handler(thePhysicalBook_handler)



#Make it Alive!
updater.start_polling()
