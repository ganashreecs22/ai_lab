
from collections import deque

def print_puzzle(state):
    for i in range(0, len(state), 3):
        print(state[i:i+3])
    print("\n")

def find_blank(state):
    return state.index(0)


def is_goal(state, goal):
    return state == goal


def get_neighbors(state):
    neighbors = []
    blank_pos = find_blank(state)
    
    
    moves = {
        'up': -3,
        'down': 3,
        'left': -1,
        'right': 1
    }
    
    for direction, move in moves.items():
        new_pos = blank_pos + move
    
        if direction == 'left' and blank_pos % 3 == 0:
            continue
        if direction == 'right' and blank_pos % 3 == 2:
            continue
        if 0 <= new_pos < len(state):
            new_state = state[:]
            new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
            neighbors.append(new_state)
    
    return neighbors


def non_recursive_dfs(start, goal):
    stack = [start]  
    visited = set()  
    parent = {tuple(start): None}  
    while stack:
        current = stack.pop()
        
        print("Current State:")
        print_puzzle(current)


        if is_goal(current, goal):
            print("Goal reached!")
            return reconstruct_path(parent, current)
        
        visited.add(tuple(current))  


        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                stack.append(neighbor)  
                parent[tuple(neighbor)] = current  

    return None  


def reconstruct_path(parent, current):
    path = []
    while current:
        path.append(current)
        current = parent[tuple(current)]
    path.reverse()
    return path


start_state = [1, 2, 3, 4, 5, 6, 0,7, 8]  
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]   


path_dfs = non_recursive_dfs(start_state, goal_state)


print("Non-Recursive DFS Path to Solution:")
if path_dfs:
    for step in path_dfs:
        print_puzzle(step)
