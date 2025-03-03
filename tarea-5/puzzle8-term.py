import heapq
import time

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_position(state, tile):
    for i, row in enumerate(state):
        if tile in row:
            return (i, row.index(tile))
    return None

def heuristic(state):
    cost = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                goal_i, goal_j = find_position(goal_state, state[i][j])
                cost += abs(i - goal_i) + abs(j - goal_j)
    return cost

def generate_moves(state):
    moves = []
    x, y = find_position(state, 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(state) and 0 <= ny < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def solve_puzzle(initial_state):
    start_time = time.time()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(initial_state), 0, initial_state, []))
    visited = set()
    
    while priority_queue:
        _, moves, current_state, path = heapq.heappop(priority_queue)
        
        if current_state == goal_state:
            end_time = time.time()
            return path + [current_state], len(path), end_time - start_time
        
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        for next_state in generate_moves(current_state):
            new_path = path + [current_state]
            heapq.heappush(
                priority_queue,
                (heuristic(next_state) + len(new_path), len(new_path), next_state, new_path),
            )
    
    return None, 0, 0

def print_solution(solution, moves, time_taken):
    if solution:
        print(f"Solución encontrada en {moves} movimientos | Tiempo: {time_taken:.4f} segundos")
        for step, state in enumerate(solution):
            print(f"Paso {step}:")
            for row in state:
                print(" ".join(str(num) if num != 0 else " " for num in row))
            print("-")
    else:
        print("No se encontró solución.")

def main():
    initial_state = [[2, 5, 4], [3, 8, 6], [7, 1, 0]]
    solution, moves, time_taken = solve_puzzle(initial_state)
    print_solution(solution, moves, time_taken)

if __name__ == "__main__":
    main()

