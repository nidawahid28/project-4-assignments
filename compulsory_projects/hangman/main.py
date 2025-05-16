import random

# Hangman drawing stages
stages = [
    '''
    --------
    |      |
    |      
    |     
    |      
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     
    |      
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |      |
    |      
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|
    |      
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |      
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |     / 
    |     
    --------
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |     / \\
    |     
    --------
    '''
]

# ✅ Step 1: Fruits with Hints (dictionary)
fruits_with_hints = {
    'apple': '🍎 A red or green fruit often found in lunchboxes.',
    'banana': '🍌 A long yellow fruit that monkeys love.',
    'mango': '🥭 A sweet tropical fruit, national fruit of Pakistan.',
    'orange': '🍊 A citrus fruit with vitamin C.',
    'grape': '🍇 Small round fruit, comes in bunches.',
    'peach': '🍑 A soft fuzzy fruit with a large pit.',
    'papaya': '🍈 A tropical fruit with black seeds inside.',
    'melon': '🍈 Large round fruit, often green inside.',
    'guava': '🍐 A tropical fruit that’s pink or white inside.',
    'kiwi': '🥝 A small brown fuzzy fruit with green flesh.'
}

# ✅ Step 2: Choose a random fruit and hint
chosen_word, hint = random.choice(list(fruits_with_hints.items()))
word_length = len(chosen_word)

# ✅ Step 3: Setup game state
display = ['_' for _ in range(word_length)]
guessed_letters = []
lives = len(stages) - 1  # Total incorrect guesses allowed

# ✅ Step 4: Show intro and hint
print("🍎 Welcome to Hangman!")
print(f"💡 Hint: {hint}")
print("Word: " + " ".join(display))

# ✅ Step 5: Game loop
while lives > 0 and '_' in display:
    guess = input("\n🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter a single alphabet only.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct!")
    else:
        lives -= 1
        print(f"❌ Wrong! Lives left: {lives}")

    # ✅ Show hangman and progress
    print(stages[len(stages) - 1 - lives])
    print("Word: " + " ".join(display))
    print("Guessed: " + ", ".join(guessed_letters))

# ✅ Step 6: End game message
if '_' not in display:
    print("\n🎉 You WON! The fruit was:", chosen_word)
else:
    print(stages[-1])
    print("\n💀 Game Over! The fruit was:", chosen_word)
