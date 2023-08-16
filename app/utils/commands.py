from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Регистрация"),
            types.BotCommand("get_statistics", "Вывести статистику"),
            types.BotCommand("test", "Тестовая команда"),
            types.BotCommand("add_category", "Добавить свою категорию"),
        ]
    )
