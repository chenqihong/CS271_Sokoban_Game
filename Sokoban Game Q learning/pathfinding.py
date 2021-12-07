def get_neighbors(board, position, goal):
    """
    :param board: current board state
    :param position: coordinate on grid
    :return: neighbors: a list of neighboring coordinates for given position
    """
    possible_neighbors = [(position[0] + 1, position[1]), (position[0] - 1, position[1]),
                          (position[0], position[1] + 1), (position[0], position[1] - 1)]
    valid_neighbors = []

    box = board.boxes.copy()
    box.remove(goal)

    # ignore walls when getting neighbors because cannot move to wall
    # make sure found neighbor is inside the bounds of the game board
    for neighbor in possible_neighbors:
        if neighbor not in board.walls and neighbor not in box and \
                not (neighbor[0] > board.rows or neighbor[1] > board.columns):
            valid_neighbors.append(neighbor)

    return valid_neighbors


def get_direction(cord1, cord2):
    if cord1[0] - cord2[0] == 1: return 'U'
    if cord1[0] - cord2[0] == -1: return 'D'
    if cord1[1] - cord2[1] == 1: return 'L'
    if cord1[1] - cord2[1] == -1: return 'R'


def bfs(board):
    """
    Returns all possible paths to location from player position
    :param board: Current game board state
    :return: all possible paths avoiding walls and other boxes
                to box location
    """
    global box_state_value_table
    final_paths = []
    for box in board.boxes:
        # Use Nodes to trace path

        queue = [[board.get_player()]]
        while queue:
            cur_path = queue.pop()
            cur_pos = cur_path[-1]

            if cur_pos == box:
                final_paths.append(cur_path)
                continue
            for neighbor in get_neighbors(board, cur_pos, box):
                if neighbor not in cur_path:
                    new_path = list(cur_path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    results = dict()
    for path in final_paths:
        if path[-2][0] - path[-1][0] == 1:
            next = (path[-1][0] - 1, path[-1][1])
        elif path[-2][0] - path[-1][0] == -1:
            next = (path[-1][0] + 1, path[-1][1])
        elif path[-2][1] - path[-1][1] == 1:
            next = (path[-1][0], path[-1][1] - 1)
        elif path[-2][1] - path[-1][1] == -1:
            next = (path[-1][0], path[-1][1] + 1)
        if not (next in board.walls or next in board.boxes or next in board.state_value_table):
            results[(path[-1], get_direction(path[-2], path[-1]))] = path
    return results
