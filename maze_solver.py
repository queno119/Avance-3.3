import collections
import heapq

def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando el algoritmo de Búsqueda en Amplitud (BFS)."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (curr_row, curr_col), path = queue.popleft()

        if (curr_row, curr_col) == end:
            return path

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if 0 <= next_row < rows and 0 <= next_col < cols and \
               maze[next_row][next_col] == 0 and (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                new_path = list(path)
                new_path.append((next_row, next_col))
                queue.append(((next_row, next_col), new_path))

    return None # No se encontró camino

def solve_maze_dfs(maze, start, end):
    """Resuelve el laberinto usando Búsqueda en Profundidad (DFS) con pila explícita."""
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()

    while stack:
        (curr_row, curr_col), path = stack.pop()

        if (curr_row, curr_col) == end:
            return path

        if (curr_row, curr_col) in visited:
            continue

        visited.add((curr_row, curr_col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == 0:
                if (next_row, next_col) not in visited:
                    stack.append(((next_row, next_col), path + [(next_row, next_col)]))

    return None

def solve_maze_a_star(maze, start, end):
    """Resuelve el laberinto usando A* con distancia Manhattan como heurística."""
    rows, cols = len(maze), len(maze[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(heuristic(start, end), 0, start, [start])]  # (f_score, g_score, node, path)
    best_g = {start: 0}
    visited = set()

    while open_set:
        _, g_score, (curr_row, curr_col), path = heapq.heappop(open_set)

        if (curr_row, curr_col) == end:
            return path

        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row, next_col = curr_row + dr, curr_col + dc
            next_pos = (next_row, next_col)

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                continue
            if maze[next_row][next_col] == 1:
                continue

            tentative_g = g_score + 1
            if tentative_g < best_g.get(next_pos, float('inf')):
                best_g[next_pos] = tentative_g
                f_score = tentative_g + heuristic(next_pos, end)
                heapq.heappush(open_set, (f_score, tentative_g, next_pos, path + [next_pos]))

    return None

# RepresentaciÃ³n del laberinto (0: camino libre, 1: muro, 2: inicio, 3: fin)
# Un laberinto de ejemplo:

MAZE = [
        [0,1,0,0,0,0,1,0,0,0],
        [0,1,0,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [1,1,1,0,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,1,0,1,0],
        [0,1,1,1,1,0,1,0,1,0],
        [0,0,0,0,1,0,0,0,1,0],
        [0,1,1,0,0,0,1,0,0,0]
    ]

#MAZE = [
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
#    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
#    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
#    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#]

START = (0, 0)
END = (9, 9)
