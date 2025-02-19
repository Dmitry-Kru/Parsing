from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import sys


def clear_screen():
    """Очищаем экран"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def open_browser_and_search(query):
    """
    Открывает браузер и ищет информацию на Википедии.
    Возвращает объект драйвера для дальнейшего использования.
    """
    driver = webdriver.Chrome()  # Используйте нужный вам драйвер
    driver.get("https://ru.wikipedia.org/wiki/")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(query + Keys.ENTER)

    return driver


def list_paragraphs(driver):
    """
    Получение текста всех параграфов на странице.
    Вывод первых десяти параграфов.
    """
    content_div = driver.find_elements(By.XPATH, "//div[@class='mw-parser-output']//p")[:10]
    paragraphs = [paragraph.text for paragraph in content_div]
    for paragraph in paragraphs:
        print(paragraph)


def find_related_links(driver):
    """
    Поиск ссылок на связанные страницы внутри текущей статьи.
    """
    links = driver.find_elements(By.XPATH, "//a[starts-with(@href,'/wiki/')]")[:10]
    link_texts = []
    for i, link in enumerate(links):
        link_text = link.text
        href = link.get_attribute('href')
        link_texts.append((i + 1, link_text, href))
    return link_texts


def select_link(link_texts):
    """
    Интерфейс выбора связанной страницы.
    """
    for index, text, _ in link_texts:
        print(f"{index}. {text}")
    choice = int(input("Выберите номер связанной страницы: "))
    return link_texts[choice - 1][2]


def main():
    while True:
        query = input("\nВведите ваш запрос: ").strip()
        if not query:
            break

        driver = open_browser_and_search(query)
        list_paragraphs(driver)

        action_choice = input(
            "\nЧто вы хотите сделать дальше?\n1. Листать параграфы этой статьи.\n2. Перейти на одну из связанных страниц.\n3. Выйти из программы.\nВаш выбор: ")

        if action_choice == '1':
            continue
        elif action_choice == '2':
            related_links = find_related_links(driver)
            if len(related_links) > 0:
                selected_href = select_link(related_links)
                driver.get(selected_href)
                list_paragraphs(driver)
            else:
                print("На этой странице нет связанных ссылок.")
        elif action_choice == '3':
            driver.quit()
            sys.exit()
        else:
            print("Неправильный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()