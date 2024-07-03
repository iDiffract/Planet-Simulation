# Planet Simulation

This project is a Python implementation of a planet simulation using the Pygame library. It simulates the gravitational interactions between planets and their orbits around the Sun, providing a visual representation of their movement.

## Features

- Realistic simulation of planetary orbits based on Newton's laws of motion and universal gravitation.
- Visualization of planets and their orbits on a canvas.
- Customizable planet properties, including name, position, radius, color, mass, and initial velocity.
- Display of the distance between each planet and the Sun.

## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Python 3.x
- Pygame

You can install the Pygame library using pip:

```
pip install pygame
```

## Usage

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the `main.py` file:

```
python main.py
```

4. The planet simulation will start, and you should see the planets and their orbits displayed on the canvas.
5. You can observe the planets moving in their respective orbits around the Sun.
6. The distance between each planet and the Sun is displayed near the corresponding planet.
7. To exit the simulation, close the window or press the appropriate key combination (e.g., Ctrl+C in the terminal).

## Customization

You can customize the planet properties by modifying the `PLANETS` list in the `settings.py` file. Each planet is represented as a dictionary with the following keys:

- `"name"`: The name of the planet.
- `"x"`: The initial x-coordinate of the planet.
- `"y"`: The initial y-coordinate of the planet.
- `"radius"`: The radius of the planet (in pixels).
- `"color"`: The color of the planet (RGB tuple).
- `"mass"`: The mass of the planet (in kg).
- `"sun"` (optional): Set to `True` if the planet is the Sun.
- `"y_vel"`: The initial y-velocity of the planet (in m/s).

You can add, remove, or modify the planet dictionaries in the `PLANETS` list to customize the simulation.

## Code Structure

The project consists of the following files:

- `main.py`: The entry point of the application, which initializes and runs the planet simulation.
- `planet.py`: Contains the `Planet` class, which represents a planet and handles its position updates and gravitational interactions.
- `settings.py`: Stores the global settings and configurations, such as screen dimensions, colors, font, and planet properties.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
