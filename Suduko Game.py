import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
BUTTON_HEIGHT = 50
BUTTON_WIDTH = WIDTH // 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Default Sudoku Board (0 represents empty cells)
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Backup of the initial grid
initial_grid = [row[:] for row in grid]

# Selected cell
selected = None

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game using Backtracking")

def draw_grid():
    for i in range(GRID_SIZE + 1):
        line_width = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_SIZE * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (GRID_SIZE * CELL_SIZE, i * CELL_SIZE), line_width)

def draw_numbers():
    font = pygame.font.SysFont("comicsans", 40)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))

def draw_selected():
    if selected:
        pygame.draw.rect(screen, BLUE, (selected[1] * CELL_SIZE, selected[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

def draw_buttons():
    font = pygame.font.SysFont("comicsans", 20)
    buttons = ["Submit", "Reset", "NewGame", "Solve"]
    for i, text in enumerate(buttons):
        pygame.draw.rect(screen, GRAY, (i * BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (i * BUTTON_WIDTH + 15, HEIGHT - BUTTON_HEIGHT + 10))

def find_empty(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(GRID_SIZE):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(GRID_SIZE):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def reset_grid():
    global grid
    grid = [row[:] for row in initial_grid]

def new_game():
    # Simple new game example (reset grid)
    reset_grid()

def submit():
    print("Sudoku Submitted")

def get_clicked_cell(pos):
    if pos[1] < GRID_SIZE * CELL_SIZE:
        return (pos[1] // CELL_SIZE, pos[0] // CELL_SIZE)
    return None

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_cell = get_clicked_cell(pos)
            if clicked_cell:
                selected = clicked_cell
            else:
                button_idx = pos[0] // BUTTON_WIDTH
                if button_idx == 0:
                    submit()
                elif button_idx == 1:
                    reset_grid()
                elif button_idx == 2:
                    new_game()
                elif button_idx == 3:
                    solve_sudoku(grid)
        elif event.type == pygame.KEYDOWN:
            if selected:
                if event.key == pygame.K_1:
                    grid[selected[0]][selected[1]] = 1
                elif event.key == pygame.K_2:
                    grid[selected[0]][selected[1]] = 2
                elif event.key == pygame.K_3:
                    grid[selected[0]][selected[1]] = 3
                elif event.key == pygame.K_4:
                    grid[selected[0]][selected[1]] = 4
                elif event.key == pygame.K_5:
                    grid[selected[0]][selected[1]] = 5
                elif event.key == pygame.K_6:
                    grid[selected[0]][selected[1]] = 6
                elif event.key == pygame.K_7:
                    grid[selected[0]][selected[1]] = 7
                elif event.key == pygame.K_8:
                    grid[selected[0]][selected[1]] = 8
                elif event.key == pygame.K_9:
                    grid[selected[0]][selected[1]] = 9
                elif event.key == pygame.K_BACKSPACE:
                    grid[selected[0]][selected[1]] = 0

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    draw_selected()
    draw_buttons()
    pygame.display.flip()
