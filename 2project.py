import random
import re
import time

users = {}
user_cards = {}
current_user = None

def register():
    username = input("Введите логин: ")
    if username in users: 
        print("Такой пользователь уже существует.")
        return

    password = input("Введите пароль: ")

    if len(password) < 5:
        print("Пароль должен быть не меньше 5 символов.")
        return

    if not re.fullmatch(r"[A-Za-z0-9]+", password):
        print("Пароль должен содержать только латинские буквы и цифры.")
        return

    users[username] = password
    user_cards[username] = []
    print("Вы зарегистрировались.")

def login():
    global current_user
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if users.get(username) == password:
        current_user = username
        print(f"Добро пожаловать, {username}!")
        return True
    else:
        print("Неверный логин или пароль.")
        return False

def add_card():
    question = input("Введите вопрос: ")
    answer = input("Введите ответ: ")
    user_cards[current_user].append((question, answer))
    print("Карточка добавлена.")

def show_random_card():
    cards = user_cards[current_user]
    if not cards:
        print("У вас пока нет карточек.")
        return
    question, answer = random.choice(cards)
    print(f"Вопрос: {question}")
    input("Нажмите Enter, чтобы увидеть ответ...")
    print(f"Ответ: {answer}")

def quiz():
    cards = user_cards[current_user]
    if not cards:
        print("У вас пока нет карточек для викторины.")
        return

    questions = cards.copy()
    random.shuffle(questions)

    correct = 0
    total = len(questions)

    for question, answer in questions:
        print(f"\nВопрос: {question}")
        start_time = time.time()
        user_answer = input("Ваш ответ (30 секунд): ")
        elapsed = time.time() - start_time

        if elapsed > 30:
            print("Время вышло! Переход к следующему вопросу.")
            continue

        if user_answer.strip().lower() == answer.strip().lower():
            print("Правильно!")
            correct += 1
        else:
            print(f"Неправильно. Правильный ответ: {answer}")

    print(f"\nВикторина завершена. Правильных ответов: {correct}/{total}")

def main_menu():
    while True:
        print("\nВыберите функцию:")
        print("1. Добавить карточку.")
        print("2. Показать рандомную карточку.")
        print("3. Викторина из карточек.")
        print("4. Выход.")
        choose = input("> ")
        if choose == "1":
            add_card()
        elif choose == "2":
            show_random_card()
        elif choose == "3":
            quiz()
        elif choose == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

def start():
    while current_user is None:
        print("1. Регистрация")
        print("2. Вход")
        choice = input("> ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break
        else:
            print("Некорректный выбор.")

    main_menu()

start()