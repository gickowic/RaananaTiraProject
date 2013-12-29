from twisted.internet import reactor
from twisted.internet import task
from components import Matrix

author = 'gickowic'
import pygame, sys


class RacingGamingClient():

    def __init__(self, client):
        self.client = client
        self.init_pygame_resources()
        # TODO: construct objects (matrix + car)
        ## create car

        matrix = Matrix.Matrix()
        self.add_component(matrix)

        self.init()
        self.looper = task.LoopingCall(self.tick)
        frame_delay = 1 / config.frame_rate
        self.looper.start(frame_delay)

    def init_pygame_resources(self):
        pygame.init()
        self.size = 640, 480
        self.bg_color = 0, 0, 0
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        for component in self.components:
            if hasattr(component, 'update'):
                component.update()

    def draw(self, screen):
        screen.fill(self.bg_color)
        for component in self.components:
            if hasattr(component, 'draw'):
                component.draw(screen)
        pygame.display.flip()

    def init(self):
        for component in self.components:
            if hasattr(component, 'init'):
                    component.init()

    def tick(self):
        screen = pygame.display.set_mode(self.size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.update()
        self.draw(screen)

    # Client events

    def client_connected(self):
        print 'client connected'

    def client_disconnected(self):
        print 'client disconnected'

    def client_failed(self):
        print 'client failed'

    def client_update(self, info):
        print 'client_update', info

    def client_welcome(self):
        print 'client_welcome'
