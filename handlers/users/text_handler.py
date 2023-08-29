from data.loader import bot
from telebot.types import Message, ReplyKeyboardRemove


@bot.message_handler(func=lambda message: message.text in ['🇷🇺 Русский язык', '🇺🇿 O\'zbek tili'])
def reaction_to_langs(message: Message):
    chat_id = message.chat.id
    lang = message.text
    if lang == '🇷🇺 Русский язык':
        msg = 'Вы выбрали русский язык'
    else:
        msg = "Siz o'zbek tilini tanladingiz"
    bot.send_message(chat_id, msg)
