from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Инициализация веб-драйвера Chrome
browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")

# Переход на главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")