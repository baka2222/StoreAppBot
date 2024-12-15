from aiogram import types
from aiogram import F
from aiogram import Router
from aiogram.filters import Command
from keyboards.start_keyboards import start_keyboard
from keyboards.questions_keyboard import page_1_kb
from keyboards.assortment_keyboard import assortment_keyboard


start_router = Router()


@start_router.message(Command('start'))
async def start_command_handler(message: types.Message):
    await message.answer(text=f'''
Привет, {message.from_user.first_name}, это магазин одежды StoreApp.
Здесь Вы можете рассмотреть широкий ассортимент из наших товаров, который включает одежду на любой вкус и цвет!😋😋
''')
    await message.answer(text='Чтобы начать, нажмите на раздел в меню.', reply_markup=start_keyboard)


@start_router.message(F.text == 'Ассортимент')
async def assortment(message: types.Message):
    await message.answer(text='Выберите категорию', reply_markup=assortment_keyboard)


@start_router.message(F.text == 'Часто задаваемые вопросы')
async def questions(message: types.Message):
    await message.answer(text='Выберите из пунктов', reply_markup=page_1_kb)


@start_router.message(F.text == 'Служба поддержки')
async def support(message: types.Message):
    await message.answer(text='Вы можете написать нам через бота или позвонить на номер менеджера: +996 990 478 119.')