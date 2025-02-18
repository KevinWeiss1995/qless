# Q-less
Q-Less is a crossword solitaire game that offers a unique twist on traditional crossword puzzles. Instead of using a standard crossword grid, players roll twelve dice, each featuring a different letter on each face. The objective is to arrange these dice to form interconnected words, creating a crossword-like structure. Notably, the letter 'Q' is excluded from the dice to streamline gameplay, which is reflected in the game's name.

## How to Play:

Roll the Dice: Begin by rolling all twelve dice.

Form Words: Use the letters on the dice to create words that intersect, similar to a traditional crossword puzzle.

Complete the Puzzle: Aim to use all the dice to form a complete crossword.

Q-Less is designed for solo play, making it ideal for individual puzzle enthusiasts. It challenges players to think strategically about word placement and letter distribution. The game is available in both physical and digital formats, including an app version for mobile devices. 

For more information you can visit the official Q-Less website.

## Overview

Given 12 letters, Qless finds all possible valid words and arranges them in a crossword pattern where:
- All letters must be used at least once
- Words must intersect like a crossword puzzle
- Each word must be at least 3 letters long
- Input must contain 2-3 vowels (no Q allowed)

## Setup

Run 
```
pip install -e .
```

Then 

```
qless
```

## Example Output

```
Using letters: jumpingtrst
Finding valid words...
Found 416 possible words
Sample of possible words: trumpings, trumping, smutting, jumpings, spurting, stumping, trusting, turnspit, sturting, ruttings

Attempting to generate board...

Attempt 1


Attempt 1
Success! Generated board:
    0  1  2  3  4  5  6  7  8  9 10 11
 0
 1
 2
 3
 4
 5          j
 6    t  r  u  m  p  i  n  g  s
 7          t
 8
 9
10
11

Placed words: trumpings, jut
```




## Details

- Uses backtracking algorithm for word placement
- Efficient dictionary lookup using sorted letter keys
- Type-hinted Python implementation
- Modular design with separate board, word finding, and CLI components

## Requirements
- Python 3.7+
- words_alpha.txt dictionary file
