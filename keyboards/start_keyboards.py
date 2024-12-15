from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ассортимент')],
    [KeyboardButton(text='Часто задаваемые вопросы')],
    [KeyboardButton(text='Служба поддержки')]
], resize_keyboard=True)