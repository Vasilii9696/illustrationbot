from aiogram.dispatcher.filters.state import State, StatesGroup


class Admins(StatesGroup):
    admin_id = State()
    admin_username = State()


class DelAdmins(StatesGroup):
    del_admins = State()


class AddKeyword(StatesGroup):
    add_kw = State()
    add_file_kw = State()
    del_kw = State()

class AddAcKeyword(StatesGroup):
    add_kw = State()
    add_file_kw = State()
    del_kw = State()

class AddUKeyword(StatesGroup):
    add_kw = State()
    add_file_kw = State()
    del_kw = State()


class AddBf(StatesGroup):
    add_bf = State()
    add_file_kw = State()
    del_bf = State()


class Banusers(StatesGroup):
    add_bu = State()
    del_bu = State()


class AdddelChats(StatesGroup):
    add_chat_ = State()
    del_chat_ = State()


class Auto_Response(StatesGroup):
    choose_kw = State()
    add_response = State()

