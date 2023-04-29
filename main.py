import telebot

from additional import markup as i,parcer as FilesInDir
from database_package import database as db,db_get_interface as dgi,db_set_interface as dsi
from user import text_react as text_react,video_react as videoreact

token = '6067752322:AAHu_wi5U227pk4s7K1FjJTZzA_7ZzTaoLA'
bot = telebot.TeleBot(token)
print("Bot is working")


@bot.message_handler(content_types=['text'])
def getText(message):
    text_react.send_message(message, bot)


@bot.message_handler(content_types=['video'])
def getVideo(message):
    if (dgi.get_approved(message.chat.id)):
        videoreact.video_checker(message, bot)
@bot.callback_query_handlers(func=lambda callback: callback.data)
def react(callback):
    if callback.data == "gibbenzumir":
        bot.send_message(callback.message.chat.id,"",reply_markup=i.menu_markup())

@bot.message_handler(content_types=['contact'])
def contact(message):
    print(message)
    if message.contact is not None:
        k = db.CreateNewUser(str(message.chat.id), str(message.contact.phone_number))
        if k == "User is already registered":
            bot.send_message(
                message.from_user.id,
                "Здравствуйте, " + message.contact.first_name + " Рад Вас видеть снова\n",
                reply_markup=i.menu_markup()
            )
            dsi.set_lasttext("mobilenumb", message.chat.id)
        if k == "User Created":
            bot.send_message(
                message.from_user.id,
                "Здравствуйте, " + message.contact.first_name + ". Ожидайте одобрения администратором!",
                #reply_markup=i.menu_markup()
            )
            dsi.set_lasttext("mobilenumb", message.chat.id)
        if k == "User is already added":
            bot.send_message(
                message.chat.id,
                "Здравствуйте, " + message.contact.first_name + ". Ваш номер уже зарегестрирован в боте",
                #reply_markup=i.menu_markup()
            )

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        print("перезапуск")

