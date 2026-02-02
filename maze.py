from collections import deque
import random

def generate_maze(rows, cols, wall_prob):
    wall = wall_prob / 100
    maze = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('#' if random.random() < wall else '.')
        maze.append(row)

    while True:
        start = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        end = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        if start != end and maze[start[0]][start[1]] != '#' and maze[end[0]][end[1]] != '#':
            break

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    bfs(maze, start, end)
    return maze

def bfs(maze, start, end):
    visited = set()
    queue = deque([start])
    parent = {start: None}
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        current = queue.popleft()
        x, y = current
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            c = (nx, ny)

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '#' or c in visited:
                    continue
                parent[c] = current
                if c == end:
                    draw_path(start, end, parent, maze)
                    return
                visited.add(c)
                queue.append(c)

def draw_path(start, end, parent, maze):
    k = end
    while k != start:
        k = parent[k]
        if k == start:
            break
        maze[k[0]][k[1]] = '*'
