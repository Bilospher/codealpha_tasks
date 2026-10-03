import random

WORDS = ["python", "computer", "program", "keyboard", "developer"]
MAX_ATTEMPTS = 6


def play_hangman():
    word = random.choice(WORDS)
    revealed = ["_"] * len(word)
    guessed_letters = set()
    attempts = 0

    while attempts < MAX_ATTEMPTS and "_" in revealed:
        print(" ".join(revealed))
        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    revealed[index] = letter
        else:
            attempts += 1
            print(f"Incorrect. Attempts: {attempts}/{MAX_ATTEMPTS}")

    if "_" not in revealed:
        print(f"{word}\nYOU WON")
    else:
        print(f"The word was: {word}\nSorry, you lose.")


if __name__ == "__main__":
    play_hangman()