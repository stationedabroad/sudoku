from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    # Choose one of the unfilled squares with the fewest possibilities
    if len([box for box in values.keys() if len(values[box]) == 1]) == 81:
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
        return values
    # If you're stuck, see the solution.py tab!
    else:
        sortedSearch = [(len(v),k) for k,v in values.items() if len(v) > 1]
        sortedSearch.sort()
        #print(sortedSearch)
        for ex in sortedSearch:
            for v in values[ex[1]]:
                values[ex[1]] = v
                return search(values)    
