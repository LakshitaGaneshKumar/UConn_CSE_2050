def solve_puzzle(board):
    """Finds the optimal path to solve the puzzle"""

    def _sp(curr_index, path, path_len):
        """Recursively finds the paths to solve the puzzle"""

        #BASE CASE: reached the last index, so return the path and increment the path length by 1
        if curr_index == len(board) - 1:
            path.append(curr_index)
            return path, path_len + 1
        
        # Return None, None is curr_index is in path because this means we have already explored this index and it does not lead to a solution
        if curr_index in path: return (None, None)
        
        # Add the current index to the path
        path.append(curr_index)

        # Find the next clockwise (cw) and counterclockwise (ccw) moves
        next_cw_move = curr_index + board[curr_index]
        next_ccw_move = curr_index - board[curr_index]

        # Initialize the tuple that will be returned with an empty list and an initial value of infinity for the path length
        cw_path, cw_path_len = [], float('inf')
        ccw_path, ccw_path_len = [], float('inf')

        # Recursively send the next moves into the _sp function
        if next_cw_move < len(board): cw_path, cw_path_len = _sp(next_cw_move, path[:], path_len + 1)
        if next_ccw_move >= 0: ccw_path, ccw_path_len = _sp(next_ccw_move, path[:], path_len + 1)

        # If cw_path_len or ccw_path_len are None, set them equal to infinity for ease in comparison in the next code block
        if cw_path_len == None: cw_path_len = float('inf')
        if ccw_path_len == None: ccw_path_len = float('inf')

        # Compare the lengths of each possible path and return the shortest (most optimal) path
        if cw_path_len < ccw_path_len:
            return (cw_path, cw_path_len)
        else:
            return (ccw_path, ccw_path_len)
        
    # Find the optimal path
    opt_path, opt_path_len = _sp(0, [], 0)

    # Return (None, None) if there is no optimal path
    if opt_path == None:
        return (None, None)
    
    return opt_path, opt_path_len - 1