from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram import F
from aiogram import Router


questions_router = Router()


page_1_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Какие способы доставки доступны?',
                          callback_data='delivery_method')],
    [InlineKeyboardButton(text='Сколько времени занимает доставка?',
                         callback_data='delivery_time')],
    [InlineKeyboardButton(text='Какие способы оплаты принимаются?',
                          callback_data='payment_methods')],
    [InlineKeyboardButton(text='Можно ли оплатить заказ при получении?',
                         callback_data='payment_get_possibility')],
    [InlineKeyboardButton(text='Вперед➡️',
                          callback_data='to_page_2')]
])


page_2_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Есть ли доставка за границу?',
                          callback_data='delivery_abroad')],
    [InlineKeyboardButton(text='Как вернуть товар?',
                         callback_data='return_product')],
    [InlineKeyboardButton(text='Какие срок и возврата?',
                          callback_data='return_term')],
    [InlineKeyboardButton(text='Можно ли обменять товар?',
                          callback_data='product_exchange')],
    [InlineKeyboardButton(text='⬅️Назад',
                         callback_data='to_page_1'),
    InlineKeyboardButton(text='Вперед➡️',
                          callback_data='to_page_3')]
])


page_3_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нужно ли платить за возврат?',
                          callback_data='payment_return')],
    [InlineKeyboardButton(text='Как получить деньги за возврат?',
                          callback_data='getting_money_return')],
    [InlineKeyboardButton(text='Есть ли размеры для моего типа фигуры?',
                          callback_data='clothes_size')],
    [InlineKeyboardButton(text='Как подобрать размер?',
                          callback_data='get_size_method')],
    [InlineKeyboardButton(text='⬅️Назад',
                         callback_data='to_page_2'),
    InlineKeyboardButton(text='Вперед➡️',
                          callback_data='to_page_4')]
])


page_4_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Какие материалы используются для одежды?',
                          callback_data='clothes_materials')],
    [InlineKeyboardButton(text='Когда появится новый ассортимент?',
                          callback_data='new_assortment_time')],
    [InlineKeyboardButton(text='Могу ли я отменить заказ?',
                          callback_data='cancel_order')],
    [InlineKeyboardButton(text='Как изменить адрес доставки в заказе?',
                          callback_data='change_address')],
    [InlineKeyboardButton(text='⬅️Назад',
                         callback_data='to_page_3'),
    InlineKeyboardButton(text='Вперед➡️',
                          callback_data='to_page_5')]
])


page_5_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Можно ли объединить два заказа в один?',
                          callback_data='unite_orders')],
    [InlineKeyboardButton(text='Как связаться с оператором?',
                          callback_data='operator_connection')],
    [InlineKeyboardButton(text='Какие скидки и акции доступны сейчас?',
                          callback_data='discounts')],
    [InlineKeyboardButton(text='Есть ли программа лояльности?',
                          callback_data='loyalty_program')],
    [InlineKeyboardButton(text='⬅️Назад',
                         callback_data='to_page_4')]
])


@questions_router.callback_query(F.data == 'to_page_1')
async def page_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите из пунктов',
                                     reply_markup=page_1_kb)


@questions_router.callback_query(F.data == 'to_page_2')
async def page_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите из пунктов',
                                     reply_markup=page_2_kb)
    

@questions_router.callback_query(F.data == 'to_page_3')
async def page_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите из пунктов',
                                     reply_markup=page_3_kb)
    

@questions_router.callback_query(F.data == 'to_page_4')
async def page_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите из пунктов',
                                     reply_markup=page_4_kb)
    

@questions_router.callback_query(F.data == 'to_page_5')
async def page_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите из пунктов',
                                     reply_markup=page_5_kb)