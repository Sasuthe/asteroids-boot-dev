import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

        # Required by pygame.sprite.Sprite
        diameter = self.radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)  # transparent surface
        self.rect = self.image.get_rect(center=self.position)

    def triangle(self):
        # Unit vectors
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # -1 to make "0" point up
        right = forward.rotate(90) * self.radius / 1.5

        tip = self.position + forward * self.radius
        left = self.position - forward * self.radius - right
        right_corner = self.position - forward * self.radius + right

        return [tip, left, right_corner]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", [v.xy for v in self.triangle()], width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(-dt)

        if keys[pygame.K_s]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shoot()

        self.rect.center = self.position

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.shot_cooldown = SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, -1)
        shot.velocity = shot.velocity.rotate(self.rotation) * PLAYER_SHOT_SPEED
