import math
import os

import pygame


class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    def distance_to(self, other: "Point3D") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )

    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"


class Sphere3D:
    def __init__(self, center: Point3D, radius: float):
        self.center = center
        self.radius = radius

    def contains_point(self, p: Point3D) -> bool:
        return self.center.distance_to(p) <= self.radius

    def intersects_sphere(self, other: "Sphere3D") -> bool:
        return self.center.distance_to(other.center) <= (self.radius + other.radius)


class AABB:
    def __init__(self, min_pt: Point3D, max_pt: Point3D):
        self.min_pt = min_pt
        self.max_pt = max_pt

    def intersects(self, other: "AABB") -> bool:
        return (
            self.min_pt.x <= other.max_pt.x and self.max_pt.x >= other.min_pt.x
            and self.min_pt.y <= other.max_pt.y and self.max_pt.y >= other.min_pt.y
            and self.min_pt.z <= other.max_pt.z and self.max_pt.z >= other.min_pt.z
        )


def project2d(point: Point3D, center_x: int, center_y: int, scale: float):
    return (
        center_x + int(point.x * scale),
        center_y - int(point.y * scale) + int(point.z * scale * 0.3),
    )


def draw_sphere(screen, center: Point3D, radius: float, color, label: str, scale=24, offset=(420, 260)):
    x, y = project2d(center, *offset, scale)
    pygame.draw.circle(screen, color, (x, y), int(radius * scale), 3)
    font = pygame.font.SysFont(None, 22)
    label_surface = font.render(label, True, (255, 255, 255))
    screen.blit(label_surface, (x + 18, y - 10))


def draw_box(screen, box: AABB, color, label: str, scale=24, offset=(420, 260)):
    min_x, min_y, min_z = box.min_pt.x, box.min_pt.y, box.min_pt.z
    max_x, max_y, max_z = box.max_pt.x, box.max_pt.y, box.max_pt.z
    p1 = project2d(Point3D(min_x, min_y, min_z), *offset, scale)
    p2 = project2d(Point3D(max_x, min_y, min_z), *offset, scale)
    p3 = project2d(Point3D(min_x, max_y, min_z), *offset, scale)
    p4 = project2d(Point3D(min_x, min_y, max_z), *offset, scale)
    p5 = project2d(Point3D(max_x, max_y, min_z), *offset, scale)
    p6 = project2d(Point3D(max_x, min_y, max_z), *offset, scale)
    p7 = project2d(Point3D(min_x, max_y, max_z), *offset, scale)
    p8 = project2d(Point3D(max_x, max_y, max_z), *offset, scale)

    for a, b in [(p1, p2), (p1, p3), (p1, p4), (p2, p5), (p2, p6), (p3, p5), (p3, p7), (p4, p6), (p4, p7), (p5, p8), (p6, p8), (p7, p8)]:
        pygame.draw.line(screen, color, a, b, 2)

    font = pygame.font.SysFont(None, 22)
    screen.blit(font.render(label, True, (255, 255, 255)), (p8[0] + 10, p8[1] + 10))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Activity 3: 3D Geometry & Bounding Volumes")
    clock = pygame.time.Clock()

    try:
        p1 = Point3D(0, 0, 0)
        p2 = Point3D(3, 4, 12)
        sphere_a = Sphere3D(Point3D(0, 0, 0), 5)
        sphere_b = Sphere3D(Point3D(4, 0, 0), 3)
        box_a = AABB(Point3D(0, 0, 0), Point3D(10, 10, 10))
        box_b = AABB(Point3D(8, 8, 8), Point3D(12, 12, 12))

        running = True
        t = 0.0
        frame_count = 0
        headless = os.environ.get("SDL_VIDEODRIVER", "").lower() == "dummy"

        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((16, 24, 32))

            t += 0.02
            moving_center = Point3D(4 + math.sin(t) * 2.5, 0, 0)
            moving_sphere = Sphere3D(moving_center, 3)
            sphere_intersects = sphere_a.intersects_sphere(moving_sphere)
            box_intersects = box_a.intersects(box_b)

            font = pygame.font.SysFont(None, 28)
            screen.blit(font.render("3D Geometry Demonstration", True, (220, 220, 220)), (20, 20))
            screen.blit(font.render(f"Distance P1->P2 = {p1.distance_to(p2):.2f}", True, (200, 220, 255)), (20, 55))
            screen.blit(font.render(f"Sphere overlap = {sphere_intersects}", True, (150, 255, 180) if sphere_intersects else (255, 170, 170)), (20, 90))
            screen.blit(font.render(f"AABB overlap = {box_intersects}", True, (150, 255, 180) if box_intersects else (255, 170, 170)), (20, 125))

            draw_sphere(screen, sphere_a.center, sphere_a.radius, (100, 200, 255), "Sphere A", scale=24, offset=(420, 260))
            draw_sphere(screen, moving_sphere.center, moving_sphere.radius, (255, 160, 110) if sphere_intersects else (255, 120, 120), "Moving Sphere", scale=24, offset=(420, 260))
            draw_box(screen, box_a, (110, 180, 255), "AABB A", scale=24, offset=(420, 260))
            draw_box(screen, box_b, (255, 190, 120), "AABB B", scale=24, offset=(420, 260))

            pygame.display.flip()
            frame_count += 1

            # Keep the demo from hanging in headless validation environments.
            if headless and frame_count >= 120:
                running = False
    except pygame.error:
        print("Pygame display is unavailable in this environment. Activity 3 requires a desktop display.")

    pygame.quit()
