import requests  # Импортируем модуль для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # Импортируем библиотеку для парсинга HTML и XML документов
from config import database, bot  # Импортируем базу данных и бота из файла конфигурации
from funcs import read_file, write_file, checker, timee  # Импортируем функции из модуля funcs

# URL страницы с вакансиями
url = 'https://dribbble.com/jobs'

# Заголовки для HTTP-запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Функция для получения описания вакансии
def get_descr(link):
    full_link = f'https://dribbble.com{link}'  # Формируем полный URL вакансии

    job_response = requests.get(full_link, headers=headers)  # Выполняем GET-запрос к странице вакансии

    if job_response.status_code == 200:  # Проверяем, успешно ли выполнен запрос
        job_soup = BeautifulSoup(job_response.text, 'html.parser')  # Парсим HTML-ответ

        description = job_soup.find('div', class_='job-details-description')  # Ищем блок с описанием вакансии
        if description:  # Если описание найдено
            return description.get_text(separator='\n', strip=True)  # Возвращаем текст описания с разделителем и без лишних пробелов

# Асинхронная функция для парсинга вакансий с dribbble.com
async def dribble():
    response = requests.get(url, headers=headers)  # Выполняем GET-запрос к странице с вакансиями

    if response.status_code == 200:  # Проверяем, успешно ли выполнен запрос
        soup = BeautifulSoup(response.text, 'html.parser')  # Парсим HTML-ответ

        jobs = soup.find_all('a', class_='job-link')  # Ищем все ссылки на вакансии
        for job in jobs:  # Перебираем все найденные вакансии
            links = read_file("vacsd.txt")  # Читаем список уже обработанных вакансий из файла
            if job['href'] not in links:  # Проверяем, не была ли вакансия уже обработана
                write_file("vacsd.txt", f"{read_file('vacsd.txt')} {job['href'] }")  # Записываем новую вакансию в файл

                description = get_descr(f"{job['href']}")  # Получаем описание вакансии
                print(description[0:10])  # Печатаем первые 10 символов описания для отладки
                if checker(description.lower()):  # Проверяем описание вакансии на соответствие критериям
                    users: list = database.get_users_en()  # Получаем список пользователей из базы данных
                    text = f"Вакансия с dribbble.com!\n\nhttps://dribbble.com{job['href']}"  # Формируем текст сообщения
                    for i in users:  # Перебираем всех пользователей
                        print(users)  # Печатаем список пользователей для отладки
                        try:
                            if timee(i):  # Проверяем, можно ли отправлять сообщение пользователю
                                await bot.send_message(i, text)  # Отправляем сообщение пользователю
                        except Exception as e:  # Обрабатываем исключения
                            print(e)  # Печатаем исключение для отладки
                else:
                    print('не судьба')  # Печатаем сообщение, если вакансия не прошла проверку