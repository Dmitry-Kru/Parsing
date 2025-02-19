import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаем экземпляр переводчика
translator = Translator()


# Функция для получения английского слова и его описания
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Парсим страницу
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        english_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим английское слово и значение на русский язык
        russian_word = translator.translate(english_word, dest='ru').text
        russian_definition = translator.translate(english_definition, dest='ru').text

        # Возвращаем переведенное слово и его значение
        return {
            "english_word": english_word,
            "russian_word": russian_word,
            "russian_definition": russian_definition
        }

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Функция для самой игры
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получаем слово и его значение
        word_dict = get_english_words()
        if not word_dict:
            continue  # Если произошла ошибка, продолжаем игру

        russian_definition = word_dict["russian_definition"]
        russian_word = word_dict["russian_word"]

        # Показываем игроку определение слова
        print(f"Определение слова: {russian_definition}")
        guess = input("Какое это слово? ").lower().strip()

        # Сравниваем введенный ответ с правильным словом
        if guess == russian_word.lower():
            print("Верно! Вы молодец.")
        else:
            print(f"Неправильно. Правильное слово: {russian_word}. Попробуйте снова.")

        # Возможность завершить игру
        play_again = input("Хотите продолжить игру? y/n ").lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


# Запускаем игру
word_game()