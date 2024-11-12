import random
import math

def calculate_conflicts(state):
    """Calculate the number of conflicts in the board state."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def n_queens_simulated_annealing(n, max_iterations=1000, initial_temp=100, cooling_rate=0.99):
    # Step 1: Initialize a random configuration
    # We represent each queen's position as a list where the index is the row, and the value is the column.
    state = [random.randint(0, n - 1) for _ in range(n)]
    
    # Helper function to get a neighbor by moving a queen to another column in the same row
    def get_neighbor(state):
        neighbor = state[:]
        row = random.randint(0, n - 1)
        new_col = random.randint(0, n - 1)
        while new_col == neighbor[row]:  # Ensure the queen actually moves
            new_col = random.randint(0, n - 1)
        neighbor[row] = new_col
        return neighbor

    # Step 2: Initialize parameters
    current_conflicts = calculate_conflicts(state)
    temperature = initial_temp
    
    for iteration in range(max_iterations):
        # Step 3: If solution is found, return the state
        if current_conflicts == 0:
            return state, iteration  # Solution found
        
        # Step 4: Generate a neighbor and calculate its conflicts
        neighbor = get_neighbor(state)
        neighbor_conflicts = calculate_conflicts(neighbor)
        
        # Step 5: Calculate delta (change in conflicts)
        delta = neighbor_conflicts - current_conflicts
        
        # Step 6: Decide whether to accept the neighbor
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            state = neighbor
            current_conflicts = neighbor_conflicts
        
        # Step 7: Decrease temperature
        temperature *= cooling_rate
    
    # Return the best state found if no solution was found within the max_iterations
    return state, max_iterations

# Example usage
n = 8
solution, iterations = n_queens_simulated_annealing(n)
if calculate_conflicts(solution) == 0:
    print(f"Solution found in {iterations} iterations: {solution}")
else:
    print(f"No solution found after {iterations} iterations. Best state: {solution}")
