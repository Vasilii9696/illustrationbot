from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from funcs import read_file_s, write_file, read_file
from config import bot, database

async def get_job_descriptions(url, readfile=None):
    url = 'https://www.upwork.com/nx/find-work/most-recent'

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Опционально, для запуска в фоновом режиме
    driver = webdriver.Chrome(service=service, options=options)

    # Открытие страницы
    driver.get(url)

    # Небольшая задержка для загрузки страницы
    time.sleep(5)

    # Поиск всех ссылок в тегах <h3> с нужным классом
    job_titles = driver.find_elements(By.CSS_SELECTOR, 'h3.my-0.p-sm-right.job-tile-title.h5 a')

    # Извлечение ссылок и названий
    jobs = [(job_title.text, f"https://www.upwork.com{job_title.get_attribute('href')}") for job_title in job_titles]

    job_details = []

    for title, link in jobs:
        if str(link) not in read_file_s("vacupw.txt"):
            write_file("vacupw.txt", f"{read_file('vacupw.txt')} {link}")
            driver.get(link)
            time.sleep(1)
            try:
                job_description = driver.find_element(By.CSS_SELECTOR, 'p.text-body-sm').get_attribute('innerHTML')
                for i in database.get_users_en():
                    await bot.send_message(i, f"Новая вакансия с апворк!\n{title}\nhttps://www.upwork.com{link}")
            except:
                job_description = 'No description found'

    driver.quit()
