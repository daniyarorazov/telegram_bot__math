import telebot

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = telebot.types.KeyboardButton("Помоги Даня")

    markup.add(item)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}', reply_markup=markup)

num1 = 0
num2 = 0

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "Помоги Даня":
        bot.send_message(message.from_user.id, "Напиши первое число знаменателя")
        bot.register_next_step_handler(message, get_second_number)

def get_second_number(message):
    global num1
    try:
        num1 = int(message.text)
        bot.send_message(message.from_user.id, "Напиши второе число знаменателя")
        bot.register_next_step_handler(message, find_common)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, get_second_number)

def findCommonValue(a, b):
    lengthVal = int(a * b)
    for i in range(1, lengthVal + 4):
        if (b * i) % a == 0:
            return i

def find_common(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = telebot.types.KeyboardButton("Помоги Даня")

    markup.add(item)
    global num2
    try:
        num2 = int(message.text)
        bot.send_message(message.from_user.id, f"Первое число: {num1}, Второе число: {num2}")
        bot.send_message(message.from_user.id, f"<b>Первое число</b> нужно умножить на: {(findCommonValue(num1, num2) * num2) / num1}", parse_mode="html")
        bot.send_message(message.from_user.id, f"<b>Второе число</b> нужно умножить на: {findCommonValue(num1, num2)}", parse_mode="html")
        bot.send_message(message.from_user.id, f"<b>Общий знаменатель:</b> {findCommonValue(num1, num2) * num2}", parse_mode="html", reply_markup=markup)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, find_common)


bot.polling(none_stop=True)
