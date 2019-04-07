import telebot
from telebot import types

token = '811308820:AAEzmkKYLiLc45RrI58wTXx_7jfRhBBJzQM'
bot = telebot.TeleBot(token)
txt = ['''MasterPechBot позволит вам ознакомиться с нашим видом деятельности.

Выберите интересующий пункт меню:
    /services - Услуги
    /contacts - Контакты
    /menu - Меню
''', '''Строительство, проэктирование каминов, печей, барбекю.
Монтаж дымоходов, саун.
Строим гибридные камины с тепловым щитком из кирпича.
Авторские камины.
Продажа печных материалов, изоляции, дымоходов из нержавеющей стали.
Заказ элементов из нержавеющей стали индивидуально, и многое другое.''',
'''Номер телефона: 
067 378 43 64
066 220 93 72
Сайт: https://www.master-pech.com/
Телеграм: @MasterPech
Также вы можете посетить наш магазин, по адресу с. Стоянка 21 км. Житомирское шоссе 1а''']

@bot.message_handler(commands=['start', 'menu'])
def handle_start(message):
    user_m = telebot.types.ReplyKeyboardMarkup(True, False)
    user_m.row('Меню')
    user_m.row('Услуги', 'Контакты')
    bot.send_message(message.from_user.id, 'Привет, %s!' % (message.from_user.first_name) + '\n' + txt[0], reply_markup=user_m)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == '/services' or message.text == 'Услуги':
        bot.send_message(message.from_user.id, txt[1])

    elif message.text == '/contacts' or message.text == 'Контакты':
        bot.send_message(message.from_user.id, txt[2])
        bot.send_location(message.from_user.id, 50.445503, 30.226001)

    elif message.text == 'Меню':
        bot.send_message(message.from_user.id, 'Привет, %s!' % (message.from_user.first_name) + '\n' + txt[0])

bot.polling()