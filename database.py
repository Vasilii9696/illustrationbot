import sqlite3  # Импортируем модуль sqlite3 для работы с базой данных SQLite


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)  # Устанавливаем соединение с базой данных
        self.cursor = self.connection.cursor()  # Создаем курсор для выполнения SQL-запросов

    def add_us(self, id, katn, katd, lanr, lana, time):
        with self.connection:  # Открываем контекстный менеджер для автоматической фиксации транзакций
            self.cursor.execute("INSERT INTO `users` VALUES (?, ?, ?, ?, ?, ?)",
                                (id, katn, katd, lanr, lana, time))  # Выполняем SQL-запрос на добавление данных в таблицу `users`
            self.connection.commit()  # Фиксируем изменения в базе данных

    def user_exist(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))  # Выполняем SQL-запрос на выборку пользователя по id
        user = self.cursor.fetchone()  # Получаем первую строку результата запроса

        if user:  # Проверяем, существует ли пользователь
            return True  # Если пользователь существует, возвращаем True
        else:
            return False  # Если пользователя нет, возвращаем False

    def get_users(self):
        self.cursor.execute("SELECT id FROM users")  # Выполняем SQL-запрос на выборку всех id из таблицы `users`
        result = self.cursor.fetchall()  # Получаем все строки результата запроса

        c = []

        for value in result:  # Итерируемся по результатам запроса
            c.append(value[0])  # Добавляем id каждого пользователя в список c
        return c  # Возвращаем список id пользователей

    def select_ints(self, user_id, inter):
        self.cursor.execute("SELECT " + str(inter) + " FROM users WHERE id = " + str(user_id))  # Выполняем SQL-запрос на выборку указанного поля для данного пользователя
        result0 = self.cursor.fetchone()  # Получаем первую строку результата запроса
        return result0[0]  # Возвращаем значение выбранного поля

    def updateint(self, intg, n, user_id):
        self.cursor.execute("UPDATE users SET " + intg + " = ? WHERE id = ?", (n, user_id))  # Выполняем SQL-запрос на обновление указанного поля для данного пользователя
        self.connection.commit()  # Фиксируем изменения в базе данных

    def select_kats(self, user_id):
        new_list = []
        kategorieslist = ["neiro", "design"]  # Список категорий для выборки
        for i in kategorieslist:
            self.cursor.execute("SELECT " + i + " FROM users WHERE id = " + str(user_id))  # Выполняем SQL-запрос на выборку значений категорий для данного пользователя
            result0 = self.cursor.fetchone()[0]  # Получаем первую строку результата запроса
            if result0 == "✅":  # Проверяем, если значение категории равно "✅"
                new_list.append(i)  # Добавляем категорию в список new_list
        return new_list  # Возвращаем список категорий

    # Добавление ключевого слова
    def add_keyword(self, category, word):
        self.cursor.execute('INSERT INTO keywords (category, word) VALUES (?, ?)', (category, word))  # Выполняем SQL-запрос на добавление ключевого слова в таблицу `keywords`
        self.connection.commit()  # Фиксируем изменения в базе данных

    # Удаление ключевого слова
    def delete_keyword(self, word):
        self.cursor.execute('DELETE FROM keywords WHERE word = ?', (word,))  # Выполняем SQL-запрос на удаление ключевого слова из таблицы `keywords`
        self.connection.commit()  # Фиксируем изменения в базе данных

    # Получение списка ключевых слов
    def get_keywords(self, category):
        self.cursor.execute('SELECT word FROM keywords WHERE category = ?', (category,))  # Выполняем SQL-запрос на выборку всех ключевых слов для данной категории
        return [row[0] for row in self.cursor.fetchall()]  # Возвращаем список ключевых слов

    def get_all_keywords(self):
        self.cursor.execute('SELECT category, word FROM keywords')  # Выполняем SQL-запрос на выборку всех категорий и ключевых слов из таблицы `keywords`
        return self.cursor.fetchall()  # Возвращаем все строки результата запроса

    def get_users_ru(self):
        self.cursor.execute("SELECT id FROM users WHERE russian = ?", ("✅",))  # Выполняем SQL-запрос на выборку всех пользователей, у которых значение поля `russian` равно "✅"
        result = self.cursor.fetchall()  # Получаем все строки результата запроса

        c = []

        for value in result:  # Итерируемся по результатам запроса
            c.append(value[0])  # Добавляем id каждого пользователя в список c
        return c  # Возвращаем список id пользователей

    def get_users_en(self):
        self.cursor.execute("SELECT id FROM users WHERE american = ?", ("✅",))  # Выполняем SQL-запрос на выборку всех пользователей, у которых значение поля `american` равно "✅"
        result = self.cursor.fetchall()  # Получаем все строки результата запроса

        c = []

        for value in result:  # Итерируемся по результатам запроса
            c.append(value[0])  # Добавляем id каждого пользователя в список c
        return c  # Возвращаем список id пользователей