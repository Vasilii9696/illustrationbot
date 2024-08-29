from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup


from config import database, bot
from funcs import read_file, write_file, checker, timee
# Настройка драйвера с использованием webdriver-manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def read_urls(url):
    # Настройка драйвера с использованием webdriver-manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
   # options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    # Даем странице время на загрузку контента
    time.sleep(1)  # Можно увеличить время, если контент загружается дольше

    # Получаем HTML код страницы после загрузки
    html = driver.page_source

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Находим div, содержащий текст вакансии
    job_description_div = soup.find('div', class_='JobDetailContent-jobContent-Nga')

    if job_description_div:
        # Получаем весь текст из div
        description = job_description_div.get_text(separator='\n', strip=True)
    else:
        description = 'Не удалось найти описание вакансии.'

    driver.quit()  # Закрываем браузер
    return description


# Функция для получения списка ссылок на вакансии
def get_urls():
    url = 'https://www.behance.net/joblist'

    # Настройка драйвера с использованием webdriver-manager
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Открываем страницу
    driver.get(url)

    # Прокручиваем страницу до конца
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Прокручиваем до низа страницы
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Ждем загрузки новой части страницы
        time.sleep(4)
        # Вычисляем новую высоту страницы
        new_height = driver.execute_script("return document.body.scrollHeight")
        # Если высота страницы не изменилась, выходим из цикла
        if new_height == last_height:
            break
        last_height = new_height

    # Получаем HTML код страницы после прокрутки
    html = driver.page_source

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Ищем все ссылки на вакансии
    job_links = soup.find_all('a', class_='JobCard-jobCardLink-Ywm')

    driver.quit()  # Закрываем браузер
    return job_links

async def send_message_withv():
    # Получаем список ссылок на вакансии из файла
    links = read_file("urlsb.txt")
    done_list = []
    # Получаем список ссылок на вакансии
    job_links = get_urls()
    #print(len(job_links))
    #print(job_links)
    # Цикл для обработки каждой ссылки
    for link in job_links:
        href = link['href']
        print(href)
        # Проверяем, есть ли уже такая ссылка в нашем списке
        if href not in links:
            # Добавляем ссылку в список ссылок
            write_file("urlsb.txt", f"{read_file('urlsb.txt')} {href}")
            # print(href)
            # Получаем текст описания вакансии
            description = read_urls(f"https://www.behance.net{href}")
            #print(description)
            # Проверяем текст описания
            if checker(description.lower()):
                users: list = database.get_users_en()
                text = f"{link['aria-label']}\n\nhttps://www.behance.net{href}"
                for i in users:
                    print(users)
                    try:
                        if timee(i):
                            await bot.send_message(i, text)
                    except Exception as e:
                        print(e)

   # return done_list

