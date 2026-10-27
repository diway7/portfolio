import random


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def determine_winner(player, computer):
    if player == computer:
        return "ничья"

    if (
        (player == "камень" and computer == "ножницы")
        or (player == "ножницы" and computer == "бумага")
        or (player == "бумага" and computer == "камень")
    ):
        return "игрок"
    else:
        return "компьютер"


def main():
    player_score = 0
    computer_score = 0
    print("Здравствуйте! это игра камень ножницы бумага, давайте начнем игру")
    while player_score < 3 and computer_score < 3:

        print("\nВведите ваш выбор (камень, ножницы, бумага):")
        player_choice = input().strip().lower()

        if player_choice in ["камень", "ножницы", "бумага"]:
            computer_choice = get_computer_choice()
            print(f"Компьютер выбрал: {computer_choice}")

            result = determine_winner(player_choice, computer_choice)

            if result == "игрок":
                player_score += 1
                print("Вы выиграли раунд!")
            elif result == "компьютер":
                computer_score += 1
                print("Компьютер выиграл раунд!")
            else:
                print("Ничья в раунде!")

            print(f"Текущий счет -> Вы: {player_score} | Компьютер: {computer_score}")
        else:
            print("Неправильный ввод, попробуйте еще раз.")

    print("\n--- ИГРА ОКОНЧЕНА ---")
    print(f"Финальный счет: Вы {player_score} : {computer_score} Компьютер")

    if player_score == 3:
        print("Поздравляем! Вы победили в игре!")
    else:
        print("Компьютер победил в игре.")


if __name__ == "__main__":
    main()