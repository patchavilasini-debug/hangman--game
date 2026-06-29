 import random

categories = {
    "Programming": {
        "python": "Popular programming language",
        "java": "Runs on JVM",
        "developer": "Person who writes code"
    },
    "Animals": {
        "lion": "King of the jungle",
        "tiger": "Big striped cat",
        "elephant": "Largest land animal"
    },
    "Countries": {
        "india": "Country in South Asia",
        "japan": "Land of the rising sun",
        "canada": "Country with maple leaf flag"
    }
}

stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

print("=" * 50)
print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("=" * 50)

while True:

    score = 0

    print("\nCategories:")
    category_names = list(categories.keys())

    for i, category in enumerate(category_names, start=1):
        print(f"{i}. {category}")

    choice = int(input("\nChoose Category (1-3): "))
    selected_category = category_names[choice - 1]

    words = categories[selected_category]
    word = random.choice(list(words.keys()))
    hint = words[word]

    print("\nDifficulty Levels")
    print("1. Easy (8 lives)")
    print("2. Medium (6 lives)")
    print("3. Hard (4 lives)")

    diff = int(input("Select Difficulty: "))

    if diff == 1:
        lives = 8
    elif diff == 2:
        lives = 6
    else:
        lives = 4

    max_lives = lives

    display = ["_" for _ in word]
    guessed_letters = []
    hint_used = False
    game_over = False

    while not game_over:

        print("\nWord:", " ".join(display))
        print("Lives:", lives)
        print("Score:", score)

        print("\nOptions:")
        print("1. Guess Letter")
        print("2. Use Hint")

        option = input("Choose Option: ")

        if option == "2":

            if not hint_used:
                print("\n💡 Hint:", hint)
                hint_used = True
                score -= 5
            else:
                print("Hint already used!")

            continue

        guess = input("Enter Letter: ").lower()

        if len(guess) != 1:
            print("Enter only one letter!")
            continue

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:

            for pos in range(len(word)):
                if word[pos] == guess:
                    display[pos] = guess

            score += 10
            print("✅ Correct!")

        else:
            lives -= 1
            print("❌ Wrong!")

            wrong_guesses = max_lives - lives

            stage_index = int((wrong_guesses / max_lives) * 6)

            if stage_index > 6:
                stage_index = 6

            print(stages[stage_index])

        if "_" not in display:
            print("\n🎉 YOU WIN!")
            print("Word:", word)
            print("Final Score:", score + 50)
            game_over = True

        if lives <= 0:
            print(stages[6])
            print("\n💀 GAME OVER!")
            print("Correct Word:", word)
            game_over = True

    replay = input("\nPlay Again? (y/n): ").lower()

    if replay != "y":
        print("\nThank you for playing! 👋")
        break