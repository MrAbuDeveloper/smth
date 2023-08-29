from data.loader import bot
from telebot.types import Message
from keyboards.default import get_choose_lang


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.send_message(chat_id, f'Salom, {first_name}',
                     reply_markup=get_choose_lang())
    
