from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# def get_wikipedia_button():
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     btn = KeyboardButton('🌎 Wikipedia')
#     btn_2 = KeyboardButton('🔍 Page')
#     markup.add(btn, btn_2)
#     return markup

def wikipedia_buttons():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('🌎 Wikipedia', callback_data='wiki')
    btn_2 = InlineKeyboardButton('🔍 Page', callback_data='page')
    markup.add(btn, btn_2)
    return markup