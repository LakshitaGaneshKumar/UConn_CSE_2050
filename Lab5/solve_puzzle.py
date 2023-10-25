def solve_puzzle(board, curr_index=0, visited=None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution? Returns true if we have landed on the last index.
    if curr_index == len(board) - 1: return True

    # Checks if we have already solved the current index. If we have, then that must mean that this board is 
    # unsolvable since we returned to a previously solved spot, so return False
    if visited != None:
        if curr_index in visited: return False
        
    # Else, create a new set of visited indices and append the current index to that list
    else: visited = set()
    visited.add(curr_index)

    # 2) Find all valid next-steps
    next_index_CW = (curr_index + board[curr_index]) % len(board)
    next_index_CCW = (curr_index - board[curr_index]) % len(board)

    # 3) Recursively explore next-steps, returning True if any valid solution is found
    cw_solved = solve_puzzle(board, next_index_CW, visited)
    ccw_solved = solve_puzzle(board, next_index_CCW, visited)

    if cw_solved or ccw_solved:
        return True
    return False
