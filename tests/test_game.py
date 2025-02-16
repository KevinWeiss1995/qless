import os
import sys
from pathlib import Path

# Get the absolute path to the src directory
root_dir = Path(__file__).parent.parent
src_dir = os.path.join(root_dir, "src")

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from qless.word_finder import load_dictionary, get_valid_words, validate_letters
from qless.board import Board
from qless.cli import attempt_board_generation

def test_basic_gameplay():
    print("Loading dictionary...")
    dictionary_path = os.path.join(root_dir, "words_alpha.txt")
    print(f"Looking for dictionary at: {dictionary_path}")
    
    try:
        word_lookup = load_dictionary(dictionary_path)
        print("Dictionary loaded successfully")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nPlease ensure words_alpha.txt is in the project root directory")
        return

    while True:
        user_input = input("\nEnter 12 letters (no Q, 2-3 vowels), or 'quit' to exit: ").strip().lower()
        if user_input == 'quit':
            break
            
        letters = ''.join(c for c in user_input if c.isalpha())
        
        if len(letters) != 12:
            print(f"Please enter exactly 12 letters (you entered {len(letters)}).")
            continue
            
        if not validate_letters(letters):
            print("Input must have 2-3 vowels and no Q.")
            continue
        
        print(f"\nUsing letters: {letters}")
        print("Finding valid words...")
        words = get_valid_words(letters, word_lookup)
        
        if not words:
            print("No valid words found. Try different letters.")
            continue
            
        print(f"Found {len(words)} possible words")
        print("Sample of possible words:", ", ".join(words[:10]))
        
        print("\nAttempting to generate board...")
        board = attempt_board_generation(words, letters)
        
        if board:
            print("\nSuccess! Generated board:")
            board.print_board()
            print("\nPlaced words:", ", ".join(board.placed_words))
        else:
            print("Failed to generate board")
            print("This can happen sometimes - try different letters")
        
        retry = input("\nTry another set of letters? (y/n): ").strip().lower()
        if retry != 'y':
            break

if __name__ == "__main__":
    test_basic_gameplay()