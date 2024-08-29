# Импортируем классы InlineKeyboardMarkup и InlineKeyboardButton из модуля aiogram.types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Функция для создания клавиатуры категорий
def kategories(user_id, database):
    # Создаем объект InlineKeyboardMarkup с шириной строки 1
    kategory = InlineKeyboardMarkup(row_width=1)
    # Добавляем кнопки с текстом и callback_data
    kategory.add(
        InlineKeyboardButton(text=f'🎯Иллюстрация и нейросети {database.select_ints(user_id, "neiro")}', callback_data='kat0'),
        InlineKeyboardButton(text=f'📝Дизайн {database.select_ints(user_id, "design")}', callback_data='kat1'),
        InlineKeyboardButton(text=f'Оба варианта', callback_data='kat2')
    )
    # Возвращаем объект клавиатуры
    return kategory

# Функция для создания клавиатуры с оригиналами
def originals(user_id, database):
    # Создаем объект InlineKeyboardMarkup с шириной строки 1
    kategory = InlineKeyboardMarkup(row_width=1)
    # Добавляем кнопки с текстом и callback_data
    kategory.add(
        InlineKeyboardButton(text=f'🎯Рынок РФ {database.select_ints(user_id, "russian")}', callback_data='ori0'),
        InlineKeyboardButton(text=f'📝Иностранный рынок {database.select_ints(user_id, "american")}', callback_data='ori1'),
        InlineKeyboardButton(text=f'Оба варианта', callback_data='ori2')
    )
    # Возвращаем объект клавиатуры
    return kategory

# Создаем объект InlineKeyboardMarkup с шириной строки 1 для категорий
kategoryk = InlineKeyboardMarkup(row_width=1)
# Добавляем кнопки для категорий с текстом и callback_data
kategoryk.add(
        InlineKeyboardButton(text=f'🎯Иллюстрация и нейросети', callback_data='mkat0'),
        InlineKeyboardButton(text=f'📝Дизайн', callback_data='mkat1'),
        InlineKeyboardButton(text=f'И то и другое', callback_data='mkat2')
    )

# Создаем объект InlineKeyboardMarkup с шириной строки 1 для оригиналов
kategoryo = InlineKeyboardMarkup(row_width=1)
# Добавляем кнопки для оригиналов с текстом и callback_data
kategoryo.add(
        InlineKeyboardButton(text=f'🎯Рынок РФ', callback_data='mori0'),
        InlineKeyboardButton(text=f'📝Иностранный рынок', callback_data='mori1'),
        InlineKeyboardButton(text=f'И то и другое', callback_data='mori2')
    )

# Создаем объект InlineKeyboardMarkup с шириной строки 1 для главного меню
home_buttons = InlineKeyboardMarkup(row_width=1)
# Добавляем кнопки для главного меню с текстом и callback_data
home_buttons.add(
    InlineKeyboardButton(text=f'ВЫБОР КАТЕГОРИИ ЗАКАЗОВ', callback_data='choose_kats'),
    InlineKeyboardButton(text=f'ВЫБОР ИСТОЧНИКОВ ЗАКАЗОВ', callback_data='choose_origins'),
    InlineKeyboardButton(text=f'ВЫБОР РАБОЧЕГО ВРЕМЕНИ', callback_data='choose_time'),
    InlineKeyboardButton(text=f'РУКОВОДСТВО', callback_data='rukvo'),
    InlineKeyboardButton(text=f'МЕНЮ', callback_data='menu')
)

# Создаем объект InlineKeyboardMarkup с шириной строки 1 для меню
menu_buttons = InlineKeyboardMarkup(row_width=1)
# Добавляем кнопки для меню с текстом и callback_data
menu_buttons.add(
    InlineKeyboardButton(text=f'О боте ', callback_data='about_b'),
    InlineKeyboardButton(text=f'Настройки', callback_data='nalash'),
    InlineKeyboardButton(text=f'Тарифы', callback_data='tarifs'),
    InlineKeyboardButton(text=f'Памятка', callback_data='pam'),
    InlineKeyboardButton(text=f'О проекте ', callback_data='about_p'),
    InlineKeyboardButton(text=f'Назад', callback_data='backb'),
)

