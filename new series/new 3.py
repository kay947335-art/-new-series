import random

def play_game():
    words = ["python", "variable", "function", "coding", "software"]
    secret_word = random.choice(words)
    jumbled = "".join(random.sample(secret_word, len(secret_word)))

    print(f"Unscramble this word: {jumbled}")
    
    guess = input("Your guess: ").lower()
    if guess == secret_word:
        print("Correct! You nailed it.")
    else:
        print(f"Incorrect. The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
    input("\nPress Enter to exit...")