import random

# List of predefined words
words = ["python", "apple", "computer", "banana", "school"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("====== HANGMAN GAME ======")
print("Guess the word one letter at a time!")

while incorrect_guesses > 0:

    # Display the word with underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses -= 1
        print("❌ Wrong Guess!")
        print("Remaining Incorrect Guesses:", incorrect_guesses)

# If player loses
if incorrect_guesses == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)