from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Функция для ввода запроса и перехода на страницу результатов поиска Википедии
def search_wikipedia(query):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)


# Функция для вывода текста параграфов текущей статьи
def print_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Paragraph {i + 1}:\n{paragraph.text}\n")
        if i >= 4:  # Показываем первые 5 параграфов, потом спрашиваем пользователя
            break


# Функция для получения ссылок на связанные статьи из результатов поиска
def print_related_links():
    elements = browser.find_elements(By.CLASS_NAME, "mw-search-result")
    links = []

    print(f"Found {len(elements)} search results")  # Отладочный вывод

    for i, element in enumerate(elements):
        a_tag = element.find_element(By.TAG_NAME, "a")
        link_text = a_tag.text
        link_href = a_tag.get_attribute("href")
        if link_href:  # Проверяем, что ссылка не пустая
            print(f"Link {i + 1}: {link_text} - {link_href}")  # Отладочный вывод
            links.append((i, link_href))

    return links


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
            links = print_related_links()
            if links:
                for index, (i, link_href) in enumerate(links):
                    print(f"{index + 1}. {link_href}")
                link_choice = input("Введите номер ссылки для перехода: ")
                try:
                    link_index = int(link_choice) - 1
                    link = links[link_index][1]
                    browser.get(link)
                except (ValueError, IndexError):
                    print("Неправильный формат или номер ссылки. Попробуйте еще раз.")
            else:
                print("Связанные статьи не найдены.")
        elif action == '3':
            browser.quit()
            exit()
        else:
            print("Неправильный номер действия. Попробуйте еще раз.")
