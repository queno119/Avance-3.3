# maze_solver.py
import heapq
from collections import deque

# ============================
# CONFIGURACIÓN DEL LABERINTO
# ============================

# 0 = camino
# 1 = muro
MAZE = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0]
]

START = (0, 0)
END = (4, 5)

# Movimientos: arriba, abajo, izquierda, derecha
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# ============================
# BFS
# ============================
def solve_maze_bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parents = {start: None}

    while queue:
        node = queue.popleft()

        if node == end:
            return reconstruct_path(parents, start, end)

        for move in MOVES:
            nr, nc = node[0] + move[0], node[1] + move[1]
            if valid_cell(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parents[(nr, nc)] = node
                queue.append((nr, nc))

    return None


# ============================
# DFS
# ============================
def solve_maze_dfs(maze, start, end):
    stack = [start]
    visited = set([start])
    parents = {start: None}

    while stack:
        node = stack.pop()

        if node == end:
            return reconstruct_path(parents, start, end)

        for move in MOVES:
            nr, nc = node[0] + move[0], node[1] + move[1]
            if valid_cell(maze, nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                parents[(nr, nc)] = node
                stack.append((nr, nc))

    return None


# ============================
# A*
# ============================
def solve_maze_a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}
    parents = {start: None}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            return reconstruct_path(parents, start, end)

        for move in MOVES:
            nr, nc = current[0] + move[0], current[1] + move[1]
            neighbor = (nr, nc)

            if not valid_cell(maze, nr, nc):
                continue

            new_cost = g_cost[current] + 1

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor, end)
                parents[neighbor] = current
                heapq.heappush(open_set, (f_cost, neighbor))

    return None


# ============================
# FUNCIONES AUXILIARES
# ============================

def heuristic(a, b):
    """Heurística Manhattan."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def valid_cell(maze, r, c):
    """Verifica si la celda está dentro de límites y es transitable."""
    return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0


def reconstruct_path(parents, start, end):
    """Reconstruye el camino desde el final hasta el inicio."""
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = parents.get(node, None)

    path.reverse()
    return path
