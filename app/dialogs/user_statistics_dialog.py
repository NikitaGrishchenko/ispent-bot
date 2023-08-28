import datetime

from aiogram.types import CallbackQuery
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
from aiogram_dialog.widgets.kbd import Back, Button, Group, Row, Select, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format, Multi
from utils.states import UserStatisticsState


async def get_data(dialog_manager: DialogManager, **kwargs):
    return {
        "current_date": dialog_manager.current_context().dialog_data.get(
            "current_date", datetime.datetime.now()
        )
    }


async def go_previous_month(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Going on!")


async def go_next_month(c: CallbackQuery, button: Button, manager: DialogManager):
    await c.message.answer("Running!")


user_statistics_dialog = Dialog(
    Window(
        Format("{current_date}"),
        Group(
            Row(
                Button(Const("prev"), id="go", on_click=go_previous_month),
                Button(Const("next"), id="run", on_click=go_next_month),
            )
        ),
        getter=get_data,
        state=UserStatisticsState.current_date,
    ),
)
