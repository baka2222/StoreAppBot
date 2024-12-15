from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db_tools.fetch_clothes import fetch_category


buttons = []
categories = fetch_category()


for i in categories:
    buttons.append([InlineKeyboardButton(text=f'{i[1]}',
                                         callback_data=f'cat_{i[0]}')])


assortment_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)