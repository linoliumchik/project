import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from src import TOKEN
from Triangle import Triangle
import json


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


tr = Triangle()
tr.counter()

swich = {
	"1": tr.rawb,
	"2": tr.raw
}

print(swich.get(str(tr.cout), tr.raz)())

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Привет, я больная фантазия Андрея!\n"
    					"Он захотел усложнить задание на Stepik..\n"
    					"Поэтому ВСЕ, что я могу - так это определять треугольник по длинам его сторон)\n")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
	await message.reply("Все, что тебе нужно - это отправить мне длины сторон\n(В одном сообщении;) )")

@dp.message()
async def math(message: types.Message):
	print(message.text)
	nums = message.text
	parse = json.loads(nums)
	print(parse)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# ты собирался проверить json и сделать так,
# чтоб через сообщение можно было сохранять длины стророн!