from aiogram import Router, F, types


answers_router = Router()


@answers_router.callback_query(F.data == 'delivery_method')
async def delivery_method(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Наш магазин предлагает следующие варианты доставки:
 • Курьерская доставка на дом.
 • Самовывоз из пункта выдачи.
 • Почтовая доставка.
Введите ваш город, чтобы узнать доступные способы доставки.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'delivery_time')
async def delivery_time(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Срок доставки зависит от вашего региона:
 • По городу: 1–3 рабочих дня.
 • По стране: 3–7 рабочих дней.
Введите ваш город для уточнения.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'payment_methods')
async def payment_methods(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Вы можете оплатить заказ:
 • Банковской картой (Visa, Mastercard).
 • Через электронные кошельки (Mbank, Optima, O!Деньги, Bakai Bank).
 • Наличными (только по предоплате 50%).
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'payment_get_possibility')
async def payment_get_possibility(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Да, оплата при получении доступна в большинстве регионов. Укажите ваш город, чтобы узнать точную информацию.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'delivery_abroad')
async def delivery_abroad(callback: types.CallbackQuery):
    await callback.message.answer(text='''
К сожалению, доставка за границу не осуществляется.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'return_product')
async def return_product(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Чтобы вернуть товар, заполните форму возврата на нашем сайте или свяжитесь с оператором. Мы предоставим инструкции по возврату. Возврат принимается в течение 14 дней с момента получения заказа.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'return_term')
async def return_term(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Срок возврата зависит от способа возврата:
 • Через почту: 5–10 рабочих дней.
 • При возврате через курьера: 3–5 рабочих дней.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'product_exchange')
async def product_exchange(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Да, вы можете обменять товар в течение 14 дней с момента получения. Если нужного размера/цвета нет в наличии, мы предложим аналогичный товар.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'payment_return')
async def payment_return(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Возврат бесплатный, если товар оказался бракованным. В остальных случаях стоимость возврата оплачивает клиент.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'getting_money_return')
async def getting_money_return(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Деньги возвращаются тем же способом, которым вы оплачивали заказ. Срок возврата — 3–7 рабочих дней после обработки заявки.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'clothes_size')
async def clothes_size(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Воспользуйтесь нашим онлайн-гидом по выбору размеров https://hmonline.ru/blog/kak-vybrat-razmer-odezhdy-tablica-dlya-zhenshchin?srsltid=AfmBOoq2DwjT7rRsJDgXTVL1l9-gKT3o75CvzNPKXZAIT7ZAvbgXYCNK. Если сомневаетесь, напишите свои параметры, и оператор подберёт подходящий размер.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'get_size_method')
async def get_size_method(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Измерьте грудь, талию и бёдра, затем сопоставьте данные с таблицей размеров https://hmonline.ru/blog/kak-vybrat-razmer-odezhdy-tablica-dlya-zhenshchin?srsltid=AfmBOoq2DwjT7rRsJDgXTVL1l9-gKT3o75CvzNPKXZAIT7ZAvbgXYCNK. Если нужен совет, напишите оператору.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'clothes_materials')
async def clothes_materials(callback: types.CallbackQuery):
    await callback.message.answer(text='''
На странице каждого товара указан материал. Если вам нужен совет, какой материал выбрать, напишите, для какого случая вы покупаете одежду.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'new_assortment_time')
async def new_assortment_time(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Новый ассортимент обновляется каждые 2 недели.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'cancel_order')
async def cancel_order(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Заказ можно отменить, если он ещё не отправлен. Напишите оператору или укажите номер телефона, с которого был сделан заказ, для отмены.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'change_address')
async def change_address(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Введите номер телефона, с которого был сделан заказ, и новый адрес. Мы изменим его, если заказ ещё не передан в службу доставки.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'unite_orders')
async def unite_orders(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Да, если оба заказа ещё не отправлены. Укажите номера телефонов, с которых были сделаны заказы, и мы объединим их.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'operator_connection')
async def operator_connection(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Вы можете написать нам через бота или позвонить на номер менеджера: +996 990 478 119.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'discounts')
async def discounts(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Вот текущие акции:
 • Скидка 10% на весь ассортимент (действует до 01.09.2025).
 • Бесплатная доставка при заказе от 5000 сомов.
''')
    await callback.answer()
    

@answers_router.callback_query(F.data == 'loyalty_program')
async def loyalty_program(callback: types.CallbackQuery):
    await callback.message.answer(text='''
Да, вы можете узнать подробности у нашего менеджера: +996 990 478 119.
''')
    await callback.answer()