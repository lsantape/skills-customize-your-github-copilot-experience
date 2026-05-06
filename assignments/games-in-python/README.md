# 📘 Assignment: Games in Python - Hangman Game Challenge

## 🎯 Objective

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Build the Game Core

#### Description
Implement the main game logic that manages the game state, word selection, and game flow.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Track the current word state with underscores for unrevealed letters
- Track incorrect guesses remaining
- Validate letter input from the player

### 🛠️ Handle Player Input and Feedback

#### Description
Create the system that accepts player guesses, validates them, and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Display current progress in `_ _ _` format
- Show a list of previously guessed letters
- Provide clear feedback for correct and incorrect guesses

### 🛠️ Implement Win/Lose Conditions

#### Description
Add logic to determine when the game ends and display appropriate messages.

#### Requirements
Completed program should:

- End game when the word is completely guessed
- End game when attempts are exhausted
- Display clear win/lose messages with the final word
- Offer the player an option to play again
