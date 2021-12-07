from aiogram import types
from management import dispatcher, bot

from core.database_management.database_core import database_users
from core.keyboard_management.keyboard_base import for_commands_start


@dispatcher.message_handler(commands = ['start'])
async def message_handler_start(
    message: types.Message,
    chat_type=types.ChatType.PRIVATE
):
    if not database_users().exists_account(
        user_id = message.from_user.id
    ):
        database_users().create_account(
            user_id = message.from_user.id
        )
    
    # en
    await message.answer(
        text = 'Hi!\nYou\'ve <b>successfully</b> created an account!',
        reply_markup = for_commands_start()
    )

    
    # ru
    await message.answer(
        text = 'Привет!\nТы <b>успешно</b> создал аккаунт!',
        reply_markup = for_commands_start()
    )
