"""Utility functions for board operations."""
from typing import List, Tuple

def get_adjacent_positions(x: int, y: int) -> List[Tuple[int, int]]:
    """Get adjacent positions for a given coordinate.
    
    Args:
        x (int): X coordinate
        y (int): Y coordinate
        
    Returns:
        List[Tuple[int, int]]: List of adjacent (x,y) coordinates
    """
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def get_word_at_position(board: List[List[str]], x: int, y: int, 
                        direction: str, size: int) -> str:
    """Get the word at a given position in specified direction.
    
    Args:
        board (List[List[str]]): Game board
        x (int): Starting x coordinate
        y (int): Starting y coordinate
        direction (str): 'H' for horizontal or 'V' for vertical
        size (int): Board size
        
    Returns:
        str: Word found at position
    """
    word = ""
    if direction == "H":
        # Find start of word
        start_x = x
        while start_x > 0 and board[y][start_x-1] != " ":
            start_x -= 1
        # Read word
        curr_x = start_x
        while curr_x < size and board[y][curr_x] != " ":
            word += board[y][curr_x]
            curr_x += 1
    else:  # direction == "V"
        # Find start of word
        start_y = y
        while start_y > 0 and board[start_y-1][x] != " ":
            start_y -= 1
        # Read word
        curr_y = start_y
        while curr_y < size and board[curr_y][x] != " ":
            word += board[curr_y][x]
            curr_y += 1
    
    return word