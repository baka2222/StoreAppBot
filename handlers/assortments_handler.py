from aiogram import Router, F, types
from db_tools.fetch_clothes_by_cat import fetch_all_clothes


assortments_router = Router()


@assortments_router.callback_query(F.data.startswith('cat_'))
async def assortment_handler(callback: types.CallbackQuery):
    category_id = callback.data.split('_')[-1]
    clothes = fetch_all_clothes(cat=category_id)
    imgs = ['StoreApp/media/' + i[1] for i in clothes]
    for i in imgs:
        await callback.message.answer_photo(types.FSInputFile(f'{i}'))