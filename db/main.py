import asyncio
from bot import bot, dp
from handlers.start_handlers import start_router
from keyboards.questions_keyboard import questions_router
from handlers.questions_handler import answers_router


async def main():
    dp.include_router(start_router)
    dp.include_router(questions_router)
    dp.include_router(answers_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is disabled')