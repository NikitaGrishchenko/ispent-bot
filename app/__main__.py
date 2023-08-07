import handlers
from aiogram import executor
from loader import dp

# async def on_startup(dispatcher: Dispatcher):
#     await utils.setup_default_commands(dispatcher)
#     await utils.notify_admins(config.SUPERUSER_IDS)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
