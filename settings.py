import pygame

# Initialize pygame library
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
UI = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

# Font
FONT = pygame.font.SysFont("comicsans", 16)

# Planet properties
PLANETS = [
    {"name": "Sun", "x": 0, "y": 0, "radius": 30, "color": YELLOW, "mass": 1.98892 * 10**30, "sun": True, "y_vel": 0},
    {"name": "Earth", "x": -1 * 149.6e6 * 1000, "y": 0, "radius": 16, "color": BLUE, "mass": 5.9742 * 10**24, "y_vel": 29.783 * 1000},
    {"name": "Mars", "x": -1.524 * 149.6e6 * 1000, "y": 0, "radius": 12, "color": RED, "mass": 6.39 * 10**23, "y_vel": 24.077 * 1000},
    {"name": "Mercury", "x": 0.387 * 149.6e6 * 1000, "y": 0, "radius": 8, "color": DARK_GREY, "mass": 3.30 * 10**23, "y_vel": -47.4 * 1000},
    {"name": "Venus", "x": 0.723 * 149.6e6 * 1000, "y": 0, "radius": 14, "color": WHITE, "mass": 4.8685 * 10**24, "y_vel": -35.02 * 1000},
]