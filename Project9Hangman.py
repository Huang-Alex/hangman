# Hangman
# By Alex Huang
# Project #9
import random


def hangman_image(lives):
    hangman_pic = {
        0: ("   _______\n"
            "  |/      |\n"
            "  |      (xx)\n"
            "  |      \|/\n"
            "  |       |\n"
            "  |      / \\\n"
            "  |\n"
            "__|___\n"),

        1: ("   _______\n"
            "  |/      |\n"
            "  |      (_)\n"
            "  |      \|/\n"
            "  |       |\n"
            "  |      / \\\n"
            "  |\n"
            "__|___\n"),

        2: ("   _______\n"
            "  |/      |\n"
            "  |      (_)\n"
            "  |      \|\n"
            "  |       |\n"
            "  |      / \\\n"
            "  |\n"
            "__|___\n"),

        3: ("   _______\n"
            "  |/      |\n"
            "  |      (_)\n"
            "  |       |\n"
            "  |       |\n"
            "  |      / \\\n"
            "  |\n"
            "__|___\n"),

        4: ("   _______\n"
            "  |/      |\n"
            "  |      (_)\n"
            "  |       |\n"
            "  |       |\n"
            "  |        \\\n"
            "  |\n"
            "__|___\n"),

        5: ("   _______\n"
            "  |/      |\n"
            "  |      (_)\n"
            "  |       |\n"
            "  |       |\n"
            "  |       \n"
            "  |\n"
            "__|___\n"),

        6: ("   _______\n"
            "  |/      |\n"
            "  |\n"
            "  |\n"
            "  |\n"
            "  |\n"
            "  |\n"
            "__|___\n"),
    }
    return hangman_pic.get(lives)

all_words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle " \
        "ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda " \
        "parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork " \
        "swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()


letters_guessed = ""


def get_random_word(list_of_words):
    random_number_generated = random.randrange(0, len(list_of_words))
    random_word = list_of_words[random_number_generated]
    return random_word


def get_unknown_word(answer):
    answer_length = len(answer)
    unknown_string = "*" * answer_length
    return unknown_string


def check_guess(all, guess):
    all_length = len(all)
    for i in range(0, all_length):
        if guess == all[i]:
            return True
    return False


def handle_user_input(answer_word, hangman_lives):
    underscores = get_unknown_word(answer_word)
    temp_underscores_answer = underscores
    answer_length = len(answer_word)
    while hangman_lives != 0:
        user_guess = already_guessed()
        if len(user_guess) == 1:
            if user_guess not in answer_word:
                hangman_lives -= 1
                print("You have", hangman_lives, "lives left")
                if hangman_lives == 0:
                    game_over(answer_word)
                else:
                    print(hangman_image(hangman_lives))
                    print(temp_underscores_answer)
            else:
                for i in range(0, answer_length):
                    if user_guess == answer_word[i]:
                        temp_underscores_answer = temp_underscores_answer[:i] + user_guess + temp_underscores_answer[i+1:]
                        if temp_underscores_answer == answer_word:
                            game_win(answer_word, hangman_lives)
                            return
                print("You have", hangman_lives, "lives left")
                print(hangman_image(hangman_lives))
                print(temp_underscores_answer)
        else:
            if user_guess == answer_word:
                game_win(answer_word, hangman_lives)
                return
            else:
                hangman_lives -= 1
                print("You have", hangman_lives, "lives left")
                if hangman_lives == 0:
                    game_over(answer_word)
                else:
                    print(hangman_image(hangman_lives))
                    print(temp_underscores_answer)


def already_guessed():
    global letters_guessed
    while True:
        user_guess = input("Guess the word or a letter: ")
        if user_guess in letters_guessed:
            print("Guess a different string, you already guessed that one!")
        else:
            letters_guessed += user_guess
            return user_guess


def game_over(answer_word):
    print(hangman_image(0))
    print("You lose, the answer was:", answer_word)
    replay()


def game_win(answer_word, hangman_lives):
    print("You still had", hangman_lives, "lives left!")
    print(hangman_image(hangman_lives))
    print("YOU WON!!! the answer was:", answer_word)
    replay()


def replay():
    choice = str(input("Do you want to play again? (y/n): "))
    if choice.startswith("y"):
        global letters_guessed
        letters_guessed = ""
        main()
    else:
        print("Goodbye, thank you for playing.")


def main():
    hangman_initial_lives = 6
    print(hangman_image(hangman_initial_lives))
    answer_word = get_random_word(all_words)
    # print(answer_word)
    print(get_unknown_word(answer_word))
    handle_user_input(answer_word, hangman_initial_lives)


main()
