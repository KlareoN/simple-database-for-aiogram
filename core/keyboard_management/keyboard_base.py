from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def for_commands_start():
    """Создание Inline клавиш""" 
    """Creating Inline Keys"""
    
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        InlineKeyboardButton(
            text = 'Привет', # Hi
            callback_data = 'keyboard_base_hi'
        ),
        InlineKeyboardButton(
            text = 'Пока', # Bye
            callback_data = 'keyboard_base_bye'
        )
    )
    return keyboard
