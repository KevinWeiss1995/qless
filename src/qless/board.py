"""Board management and word placement logic."""
from collections import defaultdict
import random
from typing import List, Set, Tuple, Dict, Optional

class Board:
    def __init__(self, size: int = 12):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.placed_positions = set()
        self.placed_words = []
        self.used_letters = defaultdict(int)
        self.total_letters = defaultdict(int)

    def initialize_letters(self, letters: str) -> None:
        for letter in letters:
            self.total_letters[letter] += 1

    def remove_word(self, word: str, start_x: int, start_y: int, direction: str) -> None:
        dx, dy = (1, 0) if direction == "H" else (0, 1)
        for i, letter in enumerate(word):
            x, y = start_x + i*dx, start_y + i*dy
            if self.board[y][x] == letter:
                self.board[y][x] = " "
                self.used_letters[letter] -= 1
                self.placed_positions.remove((x, y))
        self.placed_words.remove(word)

    def check_ends(self, x: int, y: int, direction: str, word_length: int) -> bool:
        dx, dy = (1, 0) if direction == "H" else (0, 1)
        # Check before start
        start_x, start_y = x - dx, y - dy
        if (0 <= start_x < self.size and 0 <= start_y < self.size and 
            self.board[start_y][start_x] != " "):
            return False
        # Check after end
        end_x = x + dx * word_length
        end_y = y + dy * word_length
        if (0 <= end_x < self.size and 0 <= end_y < self.size and 
            self.board[end_y][end_x] != " "):
            return False
        return True

    def find_intersection(self, word: str) -> List[Tuple[int, int, str]]:
        intersections = []
        if not self.placed_words:
            middle = self.size // 2
            if len(word) <= self.size:
                start = (self.size - len(word)) // 2
                intersections.append((start, middle, "H"))
                intersections.append((middle, start, "V"))
            return intersections

        for y in range(self.size):
            for x in range(self.size):
                if self.board[y][x] != " ":
                    # Check horizontal placement
                    for i, letter in enumerate(word):
                        if letter == self.board[y][x]:
                            start_x = x - i
                            if (start_x >= 0 and 
                                start_x + len(word) <= self.size and 
                                self.check_ends(start_x, y, "H", len(word))):
                                intersections.append((start_x, y, "H"))
                    
                    # Check vertical placement
                    for i, letter in enumerate(word):
                        if letter == self.board[y][x]:
                            start_y = y - i
                            if (start_y >= 0 and 
                                start_y + len(word) <= self.size and 
                                self.check_ends(x, start_y, "V", len(word))):
                                intersections.append((x, start_y, "V"))
        
        random.shuffle(intersections)
        return intersections

    def can_use_letters(self, word: str, start_x: int, start_y: int, direction: str) -> bool:
        dx, dy = (1, 0) if direction == "H" else (0, 1)
        temp_used = defaultdict(int)
        
        for i, letter in enumerate(word):
            x, y = start_x + i*dx, start_y + i*dy
            if self.board[y][x] == " ":
                temp_used[letter] += 1
        
        return all(self.used_letters[letter] + count <= self.total_letters[letter] 
                  for letter, count in temp_used.items())

    def is_connected(self) -> bool:
        if not self.placed_positions:
            return True
            
        visited = set()
        start = next(iter(self.placed_positions))
        stack = [start]
        
        while stack:
            pos = stack.pop()
            visited.add(pos)
            x, y = pos
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < self.size and 0 <= new_y < self.size and 
                    self.board[new_y][new_x] != " " and 
                    (new_x, new_y) not in visited):
                    stack.append((new_x, new_y))
        
        return visited == self.placed_positions

    def place_word(self, word: str, start_x: int, start_y: int, direction: str, valid_words: Set[str]) -> bool:
        if not self.can_use_letters(word, start_x, start_y, direction):
            return False
            
        dx, dy = (1, 0) if direction == "H" else (0, 1)
        positions = [(start_x + i*dx, start_y + i*dy) for i in range(len(word))]
        
        # Check bounds
        if any(x >= self.size or y >= self.size or x < 0 or y < 0 for x, y in positions):
            return False

        # Check ends
        if not self.check_ends(start_x, start_y, direction, len(word)):
            return False

        # Create temporary board state
        temp_board = [row[:] for row in self.board]
        for i, (x, y) in enumerate(positions):
            if temp_board[y][x] != " " and temp_board[y][x] != word[i]:
                return False
            temp_board[y][x] = word[i]

        # Validate all words formed
        for i, (x, y) in enumerate(positions):
            if temp_board[y][x] != self.board[y][x]:
                # Check horizontal word
                horiz_word = ""
                start_x = x
                while start_x > 0 and temp_board[y][start_x-1] != " ":
                    start_x -= 1
                curr_x = start_x
                while curr_x < self.size and temp_board[y][curr_x] != " ":
                    horiz_word += temp_board[y][curr_x]
                    curr_x += 1
                if len(horiz_word) > 1 and horiz_word not in valid_words:
                    return False

                # Check vertical word
                vert_word = ""
                start_y = y
                while start_y > 0 and temp_board[start_y-1][x] != " ":
                    start_y -= 1
                curr_y = start_y
                while curr_y < self.size and temp_board[curr_y][x] != " ":
                    vert_word += temp_board[curr_y][x]
                    curr_y += 1
                if len(vert_word) > 1 and vert_word not in valid_words:
                    return False

        # Update board state
        for i, (x, y) in enumerate(positions):
            if self.board[y][x] == " ":
                self.used_letters[word[i]] += 1
            self.board[y][x] = word[i]
            self.placed_positions.add((x, y))
        self.placed_words.append(word)
        
        return self.is_connected()

    def try_place_words(self, words: List[str], letters: str) -> bool:
        self.initialize_letters(letters)
        
        def recursive_place(depth: int = 0) -> bool:
            if depth > 10:
                return False
                
            if all(self.used_letters[letter] == count 
                   for letter, count in self.total_letters.items()):
                return True
                
            for word in words:
                if word in self.placed_words:
                    continue
                    
                intersections = self.find_intersection(word)
                for start_x, start_y, direction in intersections:
                    if self.place_word(word, start_x, start_y, direction, set(words)):
                        if recursive_place(depth + 1):
                            return True
                        self.remove_word(word, start_x, start_y, direction)
            return False
        
        return recursive_place()

    def print_board(self) -> None:
        print("  " + " ".join(str(i).rjust(2) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{str(i).rjust(2)} {' '.join(cell.ljust(2) for cell in row)}") 