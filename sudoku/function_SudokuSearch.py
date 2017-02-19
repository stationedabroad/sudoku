from utils import *
from function_CP import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    # Choose one of the unfilled squares with the fewest possibilities
#    if len([box for box in values.keys() if len(values[box]) == 1]) == 81:
    if values is False:
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
        return values
    if all([len(values[box])==1 for box in boxes]):
        return values    
    # If you're stuck, see the solution.py tab!
    l, k = min([(len(v),k) for k,v in values.items() if len(v) > 1])
    
    # recursion
    for single in values[k]:
        newSearch = values.copy()
        newSearch[k] = single
        attempt = search(newSearch)
        if attempt:
            return attempt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        