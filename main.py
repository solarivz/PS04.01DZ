from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Функция для ввода запроса и перехода на страницу Википедии
def search_wikipedia(query):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)



# Инициализация веб-драйвера Chrome с использованием Service
service = Service('C:/chromedriver/chromedriver.exe')
browser = webdriver.Chrome(service=service)

# Переход на главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

# Основной цикл программы
while True:
    # Спрашиваем у пользователя запрос
    query = input("Введите ваш запрос (или 'exit' для выхода): ")
    if query.lower() == 'exit':
        break

    # Выполняем поиск на Википедии
    search_wikipedia(query)

    while True:
        # Предлагаем пользователю действия
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        action = input("Введите номер действия: ")

        if action == '1':
            print_paragraphs()
        elif action == '2':
            hatnotes = print_related_links()