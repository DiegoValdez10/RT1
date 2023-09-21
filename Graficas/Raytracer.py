import pygame
from pygame.locals import *
from rt import Raytracer
from figures import *
from lights import *
from materials import *

width = 512
height = 1024/2

pygame.init()

screen = pygame.display.set_mode(
    (width, height), 
    pygame.DOUBLEBUF | 
    pygame.HWACCEL | 
    pygame.HWSURFACE
)
screen.set_alpha(None)


raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25, 0.25, 0.25)

brick = Material(diffuse=[1, 0.4, 0.4], spec = 8)
grass = Material(diffuse=[0.4, 1, 0.4], spec = 32)
water = Material(diffuse=[0.4, 0.4, 1], spec = 256)
snow = Material(diffuse=[1, 1, 1], spec = 64)
black = Material(diffuse=[0, 0, 0], spec = 10)
orange = Material(diffuse=[255, 128, 0], spec = 32)

raytracer.scene.append(
    Sphere(position=(0,-1.5,-10), radius=1, material=snow)
)
raytracer.scene.append(
    Sphere(position=(0,0,-10), radius=0.75, material=snow)
)
raytracer.scene.append(
    Sphere(position=(0,1.1,-10), radius=0.6, material=snow)
)
raytracer.scene.append(
    Sphere(position=(0, -1.95, -9.5), radius=0.05, material=black)
)

raytracer.scene.append(
    Sphere(position=(0, -1.2, -9.5), radius=0.05, material=black)
)

raytracer.scene.append(
    Sphere(position=(0, -0.45, -9.5), radius=0.05, material=black)
)
raytracer.scene.append(
    Sphere(position=(-0.3, 1.3, -9.5), radius=0.1, material=black)
)

raytracer.scene.append(
    Sphere(position=(0.3, 1.3, -9.5), radius=0.1, material=black)
)

raytracer.lights.append(
    AmbientLight(intensity=0.2)
) 
raytracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.5)
)
raytracer.scene.append(
    Sphere(position=(-0.1, 0.6, -9.5), radius=0.03, material=black)
)

raytracer.scene.append(
    Sphere(position=(0.1, 0.6, -9.5), radius=0.03, material=black)
)

raytracer.scene.append(
    Sphere(position=(0, 0.55, -9.5), radius=0.03, material=black)
)
orange = Material(diffuse=[1, 0.5, 0], spec=10)
raytracer.scene.append(
    Sphere(position=(0, 0.7, -9.4), radius=0.06, material=orange)
)
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    raytracer.rtClear()

    raytracer.rtRender()
    
    pygame.display.flip()

pygame.quit()