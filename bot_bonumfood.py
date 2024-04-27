# Подключение библиотеки для телеграм бота
import telebot
import webbrowser
from telebot import types
import random
from random import choice
import requests
from bs4 import BeautifulSoup

# подключение бота, над которым будем работать
bot = telebot.TeleBot('############################################')



# обработчик команды start со встоенными кнопками
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Узнать больше о Бонум Фуд 💁🏼‍♂️')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Продукция Бонум Фуд 🍕')
    btn3 = types.KeyboardButton('Новинки в Бонум Фуд 🔥')
    markup.row(btn2, btn3)
    markup.add(types.KeyboardButton('Запрос коммерческого предложения 📨'))
    markup.add(types.KeyboardButton('Партнерство 🤝'))
    btn4 = types.KeyboardButton('Задать свой вопрос 💚')
    btn5 = types.KeyboardButton('Перейти на сайт 🌍')
    markup.row(btn4, btn5)
    markup.add(types.KeyboardButton('Будьте в курсе важных событий 💌'))
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!💚\r\nЗдесь есть вся информация о компании Бонум Фуд 📗 \r\nБуду рад вам помочь 💬 \r\nВыберите интересующий вас раздел 📲', reply_markup=markup)
    # bot.register_next_step_handler(message, on_click)




@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    # парсинг продукции
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'qwe':
            url = "https://bonumfood.ru/product-category/долина-солнца/осетинские-пироги/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            section = soup.find_all("ul", class_="products")
            for products in section:
                product = products.find_all("li", class_="product")
                for item in product:
                    product_name = item.find("h4", class_="mfn-woo-product-title").get_text(strip=True)
                    product_link = item.find("a").get("href")
                    # print(product_name, product_link)
                    all_products = f"{product_name}\nСсылка: {product_link}\n "
                    bot.send_message(chat_id, all_products)



        if message.text == 'Узнать больше о Бонум Фуд 💁🏼‍♂️':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт компании 🌍', url='https://bonumfood.ru')
            markup.row(btn1)
            bot.send_message(message.chat.id, 'Секундочку.. Загружаю видео! 🤓 \r\nТакже вы можете: ', reply_markup=markup)
            file = open('./video.mp4', 'rb')
            bot.send_video(message.chat.id, file)

        elif message.text == 'Продукция Бонум Фуд 🍕' :
            markup = types.InlineKeyboardMarkup()
            btn2_2 = types.InlineKeyboardButton('Пицца 🍕', callback_data='something_function_2')
            btn3_3 = types.InlineKeyboardButton('Осетинские пироги 🥧', callback_data='something_function_3')
            markup.row(btn2_2)
            markup.row(btn3_3)
            bot.send_message(message.chat.id, 'Выберите категорию продукции: 🔜 ', reply_markup=markup)



        elif message.text == 'Новинки в Бонум Фуд 🔥':
            markup = types.InlineKeyboardMarkup()
            bot.send_message(message.chat.id, 'Для вас Бонум Фуд представляет новинки: 🔜 ', reply_markup=markup)

        elif message.text == 'Запрос коммерческого предложения 📨':
            markup = types.InlineKeyboardMarkup()
            btn10 = types.InlineKeyboardButton('В телеграм', callback_data='something_function_2')
            btn11 = types.InlineKeyboardButton('На почту', callback_data='something_function_3')
            markup.row(btn10)
            markup.row(btn11)
            bot.send_message(message.chat.id, 'Куда выслать коммерческое предложение? 🔜 ', reply_markup=markup)

        elif message.text == 'Партнерство 🤝':
            bot.send_message(message.chat.id, 'Что вы хотели бы предложить нам? Напишите 🔜 ')

        elif message.text == 'Задать свой вопрос 💚':
            markup = types.InlineKeyboardMarkup()
            btn12 = types.InlineKeyboardButton('Задать вопрос в телеграм ⁉️', callback_data='something_function_2')
            btn13 = types.InlineKeyboardButton('Задать вопрос по телефону 📞', callback_data='something_function_3')
            markup.row(btn12)
            markup.row(btn13)
            bot.send_message(message.chat.id, 'Выберите категорию продукции: 🔜 ', reply_markup=markup)

        elif message.text == 'Перейти на сайт 🌍':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('BonumFood.ru', url='https://bonumfood.ru')
            markup.row(btn1)
            bot.send_message(message.chat.id, 'Перейти на сайт компании 🔜',
                             reply_markup=markup)

        elif message.text == 'Будьте в курсе важных событий 💌':
            markup = types.InlineKeyboardMarkup()
            btn14 = types.InlineKeyboardButton('На почту 📩', callback_data='something_function_2')
            btn15 = types.InlineKeyboardButton('В Телеграм ', callback_data='something_function_3')
            markup.row(btn14)
            markup.row(btn15)
            bot.send_message(message.chat.id, 'Куда присылать письма? ', reply_markup=markup)



        # Команды
        elif message.text == '/site':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('BonumFood.ru', url='https://bonumfood.ru')
            markup.row(btn1)
            bot.send_message(message.chat.id, 'Перейти на сайт компании 🌍',
                             reply_markup=markup)


        elif message.text == '/about':
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт компании 🌍', url='https://bonumfood.ru')
            markup.row(btn1)
            bot.send_message(message.chat.id, 'Секундочку.. Загружаю видео! 🤓 \r\nТакже вы можете: ', reply_markup=markup)
            file = open('./video.mp4', 'rb')
            bot.send_video(message.chat.id, file)





            # Small talk
        elif message.text == 'Привет!':
            bot.send_message(message.from_user.id, 'Привет!')

        elif message.text == 'Привет':
            bot.send_message(message.from_user.id, 'Привет!')

        elif message.text == 'привет!':
            bot.send_message(message.from_user.id, 'Привет!')

        elif message.text == 'привет':
            bot.send_message(message.from_user.id, 'Привет!')

        elif message.text == 'как дела?':
            bot.send_message(message.from_user.id, 'Хорошо!')

        elif message.text == 'Как дела?':
            bot.send_message(message.from_user.id, 'Хорошо!')

        elif message.text == 'Что делаешь?':
            bot.send_message(message.from_user.id, 'Помогаю людям!')

        elif message.text == 'что делаешь?':
            bot.send_message(message.from_user.id, 'Помогаю людям!')

        elif message.text == 'что делаешь':
            bot.send_message(message.from_user.id, 'Помогаю людям!')

        elif message.text == 'че делаешь?':
            bot.send_message(message.from_user.id, 'Помогаю людям!')

        elif message.text == 'че делаешь':
            bot.send_message(message.from_user.id, 'Помогаю людям!')

        elif message.text == 'как дела':
            bot.send_message(message.from_user.id, 'Хорошо!')









# Перенапрвление клиента на сайт по команде /site
# @bot.message_handler(commands=['startbot', 'website'])
# def startbot(message):
#     bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Здесь вы сможете найти много полезной информации')
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['about'])
# def AboutCompany(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['products'])
# def ProductsBonumFood(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['newsproducts'])
# def NewProductsBonumFood(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['offer'])
# def OfferBonumFood(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['myquestion'])
# def YourQuestion(message):
#     webbrowser.open('https://bonumfood.ru')
#
# @bot.message_handler(commands=['subscribe'])
# def Subscribe(message):
#     webbrowser.open('https://bonumfood.ru')
#








# обработка команды старт
# @bot.message_handler(commands=['start'])
# def main(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на веб-сайт компании', url='https://bonumfood.ru')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Item Button 2', callback_data='something_function_2')
#     btn3 = types.InlineKeyboardButton('Item Button 3', callback_data='something_function_3')
#     markup.row(btn2, btn3)
#     markup.add(types.InlineKeyboardButton('Item Button 4', callback_data='something_function_4'))
#     markup.add(types.InlineKeyboardButton('Item Button 5', callback_data='something_function_5'))
#     markup.add(types.InlineKeyboardButton('Item Button 6', callback_data='something_function_6'))
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Выбери то, что тебя интересует', reply_markup=markup)

 # декоратор для кнопок для обработки callback_data
#  @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#      if callback.data == 'something_function_6':
#          bot.send_message(message.chat.id, 'Здесь будет выводиться дополнительная информация')


 #    markup.add(types.InlineKeyboardButton('Item Button 1', callback_data='something_function'))
 #    markup.add(types.InlineKeyboardButton('Item Button 2', callback_data='something_function'))
 #    markup.add(types.InlineKeyboardButton('Item Button 3', callback_data='something_function'))
 #    markup.add(types.InlineKeyboardButton('Item Button 4', callback_data='something_function'))





# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Перейти на веб-сайт компании', url='https://bonumfood.ru'))

# для обработк любого текста, который пришлет пользователь
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')







#
# @bot.message_handler(commands=['help_help'])
# def main(message):
#     bot.send_message(message.chat.id, '<u>information</u>', parse_mode='html')
#
#
# @bot.message_handler(commands=['startmessage'])
# def main(message):
#     bot.send_message(message.chat.id, message)



# чтобы бот работал не прекращая, необходимо сделать так, чтобы программа не завершалась
# либо bot.infinity_poling()
bot.polling(none_stop=True)