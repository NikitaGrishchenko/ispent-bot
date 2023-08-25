from typing import Any

import services
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram_dialog import (
    ChatEvent,
    Dialog,
    DialogManager,
    DialogRegistry,
    StartMode,
    Window,
)
from aiogram_dialog.manager.protocols import ManagedDialogAdapterProto
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Back, Button, Row, Select, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format, Multi
from loader import dp
from utils.filters import IsAuth
from utils.states import MySG


async def get_data(dialog_manager: DialogManager, **kwargs):
    age = dialog_manager.current_context().dialog_data.get("age", None)
    return {
        "name": dialog_manager.current_context().dialog_data.get("name", ""),
        "age": age,
        "can_smoke": age in ("18-25", "25-40", "40+"),
    }


async def name_handler(
    m: types.Message, dialog: ManagedDialogAdapterProto, manager: DialogManager
):
    if manager.is_preview():
        await dialog.next()
        return
    manager.current_context().dialog_data["name"] = m.text
    await m.answer(f"Nice to meet you, {m.text}")
    await dialog.next()


async def on_finish(c: types.CallbackQuery, button: Button, manager: DialogManager):
    if manager.is_preview():
        await manager.done()
        return
    await c.message.answer("Thank you. To start again click /start")
    await manager.done()


async def on_age_changed(
    c: ChatEvent, select: Any, manager: DialogManager, item_id: str
):
    manager.current_context().dialog_data["age"] = item_id
    await manager.dialog().next()


dialog = Dialog(
    Window(
        Const("Greetings! Please, introduce yourself:"),
        MessageInput(name_handler),
        state=MySG.greeting,
    ),
    Window(
        Format("{name}! How old are you?"),
        Select(
            Format("{item}"),
            items=["0-12", "12-18", "18-25", "25-40", "40+"],
            item_id_getter=lambda x: x,
            id="w_age",
            on_click=on_age_changed,
        ),
        state=MySG.age,
        getter=get_data,
        preview_data={"name": "Tishka17"},
    ),
    Window(
        Multi(
            Format("{name}! Thank you for your answers."),
            Const("Hope you are not smoking", when="can_smoke"),
            sep="\n\n",
        ),
        Row(
            Back(),
            SwitchTo(Const("Restart"), id="restart", state=MySG.greeting),
            Button(Const("Finish"), on_click=on_finish, id="finish"),
        ),
        getter=get_data,
        state=MySG.finish,
    ),
)

registry = DialogRegistry(dp)
registry.register(dialog)


@dp.message_handler(commands="test")
async def test_command(message: types.Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.greeting, mode=StartMode.RESET_STACK)


# @dp.message_handler(commands="test")
# async def test_command(message: types.Message, state: FSMContext):
#     await state.finish()
