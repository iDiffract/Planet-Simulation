import pygame
from planet import Planet
from settings import UI, WIDTH, HEIGHT, PLANETS

class PlanetSimulation:
    def __init__(self):
        self.planets = self.initialize_planets()
        self.clock = pygame.time.Clock()
        self.run = True

    def initialize_planets(self):
        planets = []
        for planet_info in PLANETS:
            planet = Planet(
                name = planet_info["name"],
                x = planet_info["x"],
                y = planet_info["y"],
                radius = planet_info["radius"],
                color = planet_info["color"],
                mass = planet_info["mass"]
            )
            if planet_info.get("sun"):
                planet.sun = True
            planet.y_vel = planet_info["y_vel"]
            planets.append(planet)
        return planets

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):
        for planet in self.planets:
            planet.update_position(self.planets)
    
    def draw(self):
        UI.fill((0, 0, 0))
        for planet in self.planets:
            planet.draw(UI)
        pygame.display.update()

    def run_simulation(self):
        while self.run:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    simulation = PlanetSimulation()
    simulation.run_simulation()
