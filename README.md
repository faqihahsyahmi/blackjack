# Blackjack Game (Python CLI Project)

## A functional simple project fully written in Python

A simple text-based Python Blackjack game.

This program is created as a beginner-friendly learning exercise focused on Python fundamentals like loops, conditionals, lists, and input handling.

This is a basic command-line version of the classic casino game **Blackjack**, where the user plays against the computer.

Let's get started!

### 🎯 Game Objective

The goal is to get a hand of cards with a value **as close to 21 as possible** without going over (bust). 
Whoever has the higher score at the end—without going over—wins.

### 🧠 Basic Blackjack Rules & Logic

- Number cards count as their number (2–10)
- Face cards (Jack, Queen, King) count as 10
- Aces can be **11 or 1**, depending on situation
- Blackjack is an **automatic win** with an Ace + 10/Face card (score = 21 with 2 cards)
- If either player **goes over 21**, they automatically lose
- If both have the **same score**, it's a draw



## How it works
* The game is played between a **player** and the **computer**.
* At the start:
  - Both player and the computer are dealt **two random cards**
  - Player can **see both of their own cards** and **only one of the computer’s cards** (the other remains hidden)
* Player can choose to:
  - **Draw another card**
  - **Remains** not drawing another card 
* The computer follows a simple rule:
  - It will **automatically draw** cards until it reaches a score more than **17**
* Once both parties are done drawing cards, the scores are revealed and the winner is determined.

### 🧮 Winner Logic
1. If both have the **same score** → It's a **draw**
2. If the **computer has a Blackjack** → You lose
3. If the **player has a Blackjack** → You win
4. If the **player goes over 21** → You lose
5. If the **computer goes over 21** → You win
6. Otherwise, the one with the **higher score** wins


## Concept:
* `while` loops
* `if/elif/else` conditionals
* Random module
* Functions
* User input handling
* Basic scoring logic


## It has the following features:
* Deals random cards to both player and computer
* Hides the computer's second card until the end
* Allows player to draw or hold based on input
* Auto-draws for the computer
* Declares win/lose/draw results based on Blackjack logic
* Shows final hands and scores for both players


## Weakness/To improve:
* To have error handling for invalid inputs
* Card deck is unlimited (not removed after being drawn)


## Versioning
* 1.0: original program
* 1.1: fix the opening yes/no promt asking the player. Add symbols/emojis