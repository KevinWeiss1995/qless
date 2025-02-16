"""Command-line interface for the qless game."""
import threading
import time
from typing import List, Optional
from .board import Board
from .word_finder import load_dictionary, get_valid_words, validate_letters
import argparse

def attempt_board_generation(words: List[str], letters: str, max_attempts: int = 10) -> Optional[Board]:
    """Attempts to generate a valid game board by placing words from the given list.
    
    Makes multiple attempts to create a board where all letters are used at least once
    in the placed words. Each attempt creates a new board and tries to place words
    until either successful or all possibilities are exhausted.

    Args:
        words: List of valid words that can be placed on the board
        letters: String of 12 letters that must all be used in the placed words
        max_attempts: Maximum number of board generation attempts (default: 10)

    Returns:
        Board: A valid board object if successful
        None: If no valid board could be generated within max_attempts
    """
    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}")
        board = Board()
        if board.try_place_words(words, letters):
            return board
    return None

def main():
    import argparse
    
    print("Loading dictionary...")
    word_lookup = load_dictionary()
    print("Dictionary loaded successfully\n")

    parser = argparse.ArgumentParser(description='Generate word boards from letters')
    parser.add_argument('letters', nargs='?', help='12 letters to generate the board from')
    args = parser.parse_args()

    while True:
        if args.letters:
            letters = args.letters
            args.letters = None 
        else:
            letters = input("\nEnter 12 letters (no Q, 2-3 vowels), or 'quit' to exit: ")
            
        if letters.lower() == 'quit':
            break

        print(f"\nUsing letters: {letters}")
        print("Finding valid words...")
        valid_words = get_valid_words(letters, word_lookup)
        print(f"Found {len(valid_words)} possible words")
        print("Sample of possible words:", ", ".join(valid_words[:10]))

        print("\nAttempting to generate board...")
        print("\nAttempt 1\n")

        board = attempt_board_generation(valid_words, letters)
        if board:
            print("Success! Generated board:")
            # Print column numbers
            print("   " + "".join(f"{i:2d} " for i in range(12)))
            # Print rows with row numbers
            for i, row in enumerate(board.board):
                row_str = f"{i:2d} " + "".join(f"{cell:2s} " if cell != " " else "   " for cell in row)
                print(row_str)
            print(f"\nPlaced words: {', '.join(board.placed_words)}")
        else:
            print("Could not generate a valid board")

if __name__ == "__main__":
    main() 