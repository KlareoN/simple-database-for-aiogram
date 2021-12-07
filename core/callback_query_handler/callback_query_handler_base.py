from management import dispatcher, bot
from aiogram import types


@dispatcher.callback_query_handler(lambda c: c.data == 'keyboard_base_hi')
async def keyboard_base_hi(call: types.CallbackQuery):
    await bot.send_message(
        chat_id = call.message.chat.id,
        text = 'Вы нажали на кнопку "Привет"'
        # You clicked on the "Hi" button
    )


@dispatcher.callback_query_handler(lambda c: c.data == 'keyboard_base_bye')
async def keyboard_base_bye(call: types.CallbackQuery):
    await bot.send_message(
        chat_id = call.message.chat.id,
        text = 'Вы нажали на кнопку "Пока"'
        # You clicked on the "Bye" button
    )