import math
import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Activity 1: 2D Animation, Tweening & Morphing")
clock = pygame.time.Clock()


def lerp_point(p1, p2, t):
    return (
        p1[0] + (p2[0] - p1[0]) * t,
        p1[1] + (p2[1] - p1[1]) * t,
    )


def ease_in_out(t):
    return t * t * (3 - 2 * t)


triangle_start = [(200, 100), (300, 300), (100, 300)]
quad_end = [(200, 100), (350, 150), (300, 350), (100, 300)]

ball = {
    "x": 120.0,
    "y": 100.0,
    "vx": 0.0,
    "vy": 0.0,
    "radius": 20,
    "gravity": 0.35,
    "restitution": 0.75,
    "ground_y": SCREEN_HEIGHT - 80,
}

# Track the morphing polygon by pairing vertices based on corresponding positions.
def morph_polygon(t):
    start = triangle_start[:]
    end = quad_end[:]
    if len(start) == len(end):
        return [lerp_point(start[i], end[i], t) for i in range(len(start))]

    if len(start) < len(end):
        # Duplicate the first edge point in the source shape to match the target count.
        adjusted = start[:]
        adjusted.insert(1, ((start[0][0] + start[1][0]) / 2, (start[0][1] + start[1][1]) / 2))
        return [lerp_point(adjusted[i], end[i], t) for i in range(len(end))]

    return [lerp_point(start[i], end[i], t) for i in range(len(start))]


def draw_polygon(points, color):
    if len(points) > 2:
        pygame.draw.polygon(screen, color, points, 3)


def draw_ball():
    pygame.draw.circle(screen, (255, 165, 0), (int(ball["x"]), int(ball["y"])), ball["radius"])


running = True
elapsed = 0.0
while running:
    dt = clock.tick(60) / 1000.0
    elapsed += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bouncing ball dynamics: position + velocity, gravity, floor collision.
    ball["vy"] += ball["gravity"]
    ball["x"] += ball["vx"] * 60 * dt
    ball["y"] += ball["vy"] * 60 * dt

    if ball["y"] + ball["radius"] >= ball["ground_y"]:
        ball["y"] = ball["ground_y"] - ball["radius"]
        ball["vy"] = -ball["vy"] * ball["restitution"]
        if abs(ball["vy"]) < 0.4:
            ball["vy"] = 0.0

    if ball["x"] < ball["radius"]:
        ball["x"] = ball["radius"]
    if ball["x"] > SCREEN_WIDTH - ball["radius"]:
        ball["x"] = SCREEN_WIDTH - ball["radius"]

    t = 0.5 + 0.5 * math.sin(elapsed * 1.5)
    eased = ease_in_out(t)
    morph_points = morph_polygon(eased)

    screen.fill((15, 18, 30))

    # Ground plane for bouncing ball.
    pygame.draw.rect(screen, (60, 90, 70), (0, ball["ground_y"], SCREEN_WIDTH, SCREEN_HEIGHT - ball["ground_y"]))

    # Draw morphing shape.
    draw_polygon(morph_points, (120, 200, 255))

    # Draw a dynamic connecting line over the ball to show movement.
    line_end = (ball["x"], ball["ground_y"] - 20)
    pygame.draw.line(screen, (200, 220, 255), (100, ball["ground_y"] - 20), line_end, 2)

    draw_ball()

    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    pass
