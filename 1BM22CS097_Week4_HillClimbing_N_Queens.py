import random

# Function to calculate the number of conflicts
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:  # Same row conflict
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):  # Diagonal conflict
                conflicts += 1
    return conflicts

# Function to print the board
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("\n")

# Hill Climbing algorithm for N-Queens
def hill_climbing_n_queens(initial_state):
    n = len(initial_state)
    current_board = initial_state[:]
    current_conflicts = calculate_conflicts(current_board)

    while True:
        neighbors = []
        for col in range(n):
            for row in range(n):
                if row != current_board[col]:
                    neighbor = current_board[:]
                    neighbor[col] = row
                    neighbors.append(neighbor)

        # Find the neighbor with the least conflicts
        next_board = min(neighbors, key=calculate_conflicts)
        next_conflicts = calculate_conflicts(next_board)

        # If no neighbor has fewer conflicts, stop
        if next_conflicts >= current_conflicts:
            break

        # Move to the best neighbor
        current_board = next_board
        current_conflicts = next_conflicts

    return current_board, current_conflicts

# Main function to execute Hill Climbing for 4-Queens problem
def main():
    # Initial state as per the problem:
    initial_state = [3, 1, 2, 0]

    print("Initial board configuration:")
    print_board(initial_state)

    final_board, final_conflicts = hill_climbing_n_queens(initial_state)

    print("Final board configuration after Hill Climbing:")
    print_board(final_board)

    print(f"Number of conflicts: {final_conflicts}")

if __name__ == "__main__":
    main()
