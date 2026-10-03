import math
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Activity 4: 3D Projection Pipeline")
clock = pygame.time.Clock()

cube_vertices = [
    [-100, -100, -100], [100, -100, -100], [100, 100, -100], [-100, 100, -100],
    [-100, -100, 100], [100, -100, 100], [100, 100, 100], [-100, 100, 100],
]

cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]


def rotate_x(point, angle_deg):
    angle = math.radians(angle_deg)
    x, y, z = point
    return [x, y * math.cos(angle) - z * math.sin(angle), y * math.sin(angle) + z * math.cos(angle)]


def rotate_y(point, angle_deg):
    angle = math.radians(angle_deg)
    x, y, z = point
    return [x * math.cos(angle) + z * math.sin(angle), y, -x * math.sin(angle) + z * math.cos(angle)]


def transform_point(point, rx, ry):
    p = rotate_x(point, rx)
    p = rotate_y(p, ry)
    return p


def project_orthographic(x, y, z):
    return int(x + 400), int(y + 260)


def project_oblique(x, y, z, phi_deg=45, depth_scale=1.0):
    phi = math.radians(phi_deg)
    x_p = x + z * depth_scale * math.cos(phi)
    y_p = y + z * depth_scale * math.sin(phi)
    return int(x_p + 400), int(y_p + 260)


def project_perspective(x, y, z, distance=400):
    x_p = (x * distance) / (z + distance)
    y_p = (y * distance) / (z + distance)
    return int(x_p + 400), int(y_p + 260)


def draw_cube(view_func, offset_x, angle_x, angle_y, color=(200, 220, 255)):
    projected = []
    for vertex in cube_vertices:
        p = transform_point(vertex, angle_x, angle_y)
        projected.append(view_func(*p))

    # Shift the projected cube to the requested panel column.
    shifted = [(x + offset_x, y) for x, y in projected]
    for a, b in cube_edges:
        p1 = shifted[a]
        p2 = shifted[b]
        pygame.draw.line(screen, color, p1, p2, 2)


def draw_panel_label(x, y, title):
    text = pygame.font.SysFont(None, 24).render(title, True, (255, 255, 255))
    screen.blit(text, (x, y))


running = True
angle = 0.0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += 1.0
    screen.fill((10, 12, 20))

    draw_panel_label(90, 20, "Orthographic")
    draw_panel_label(420, 20, "Cavalier")
    draw_panel_label(730, 20, "Perspective")

    draw_cube(project_orthographic, 40, angle, angle * 1.2, color=(120, 190, 255))
    draw_cube(lambda x, y, z: project_oblique(x, y, z, 45, 1.0), 360, angle, angle * 1.2, color=(145, 255, 180))
    draw_cube(lambda x, y, z: project_perspective(x, y, z, distance=400), 700, angle, angle * 1.2, color=(255, 185, 120))

    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    pass
