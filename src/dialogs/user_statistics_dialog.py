import datetime

import monthdelta
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
from services import GetUserStatistics
from utils.states import UserStatisticsState


async def get_data(dialog_manager: DialogManager, **kwargs):
    current_date = dialog_manager.current_context().dialog_data.get("current_date")
    if current_date is None:
        current_date = datetime.datetime.now()
        dialog_manager.current_context().dialog_data.update(
            {
                "current_date": current_date,
            }
        )

    user_telegram_id = dialog_manager.event.from_user.id
    return {
        "output_data": await GetUserStatistics.execute(user_telegram_id, current_date),
    }


async def go_previous_month(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    current_date = dialog_manager.current_context().dialog_data.get("current_date")
    await dialog_manager.update(
        {
            "current_date": current_date + monthdelta.monthdelta(-1),
        }
    )


async def go_next_month(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    current_date = dialog_manager.current_context().dialog_data.get("current_date")
    await dialog_manager.update(
        {
            "current_date": current_date + monthdelta.monthdelta(1),
        }
    )


user_statistics_dialog = Dialog(
    Window(
        Format("{output_data}"),
        Group(
            Row(
                Button(Const("<<"), id="go_previous_month", on_click=go_previous_month),
                Button(Const(">>"), id="go_next_month", on_click=go_next_month),
            )
        ),
        getter=get_data,
        state=UserStatisticsState.main,
    ),
)
