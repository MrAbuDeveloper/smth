from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def get_choose_lang():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ru = KeyboardButton('🇷🇺 Русский язык')
    uz = KeyboardButton('🇺🇿 O\'zbek tili')
    markup.add(ru, uz)
    return markup
