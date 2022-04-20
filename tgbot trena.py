import json
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='')
dp = Dispatcher(bot)


# @dp.message_handler(commands="start")
# async def start(message: types.Message):
#     await message.reply('Хей!')


@dp.message_handler(commands="all_news")
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in news_dict.items():
        news = f"{v['article_date']}\n" \
            f"{v['article_url']}"

        await message.answer(news)


if __name__ == '__main__':
    executor.start_polling(dp)
