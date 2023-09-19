from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("get_statistics", "Вывести статистику"),
            types.BotCommand("add_category", "Добавить свою категорию"),
            types.BotCommand("remove_category", "Удалить свою категорию"),
        ]
    )
