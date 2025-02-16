"""Word finding and validation logic."""
import itertools
from collections import defaultdict
from typing import Dict, Set, List

def load_dictionary(filename: str = "words_alpha.txt") -> Dict[str, Set[str]]:
    word_lookup = defaultdict(set)
    with open(filename, "r") as f:
        for word in f:
            word = word.strip().lower()
            if len(word) >= 3:
                word_lookup[''.join(sorted(word))].add(word)
    return word_lookup

def get_valid_words(letters: str, word_lookup: Dict[str, Set[str]]) -> List[str]:
    """Finds all valid words that can be formed from the given letters.
    
    A word is considered valid if:
    1. It can be formed using only the provided letters
    2. It uses each letter no more times than it appears in the input
    3. It exists in the word lookup dictionary
    4. It is at least 3 letters long

    Args:
        letters: String of available letters to form words from
        word_lookup: Dictionary mapping sorted letters to valid words
                    (as created by load_dictionary)

    Returns:
        List[str]: List of valid words sorted by length (longest first)
    """
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    valid_words = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            sorted_combo = ''.join(sorted(combo))
            for word in word_lookup[sorted_combo]:
                word_letter_count = {}
                for letter in word:
                    word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
                if all(word_letter_count[letter] <= letter_count.get(letter, 0) 
                      for letter in word_letter_count):
                    valid_words.add(word)
    return sorted(valid_words, key=len, reverse=True)

def validate_letters(letters: str) -> bool:
    if 'q' in letters:
        return False
    vowels = sum(1 for c in letters if c in 'aeiou')
    return 2 <= vowels <= 3 