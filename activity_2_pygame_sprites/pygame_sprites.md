# Activity 2: Interactive Game Architecture & Sprites

## 1. Technical Overview
Activity 2 demonstrates an object-oriented interactive graphics system using Pygame's `pygame.sprite.Sprite` encapsulation, sprite groups, real-time collision detection, dynamic enemy spawning, and HUD text blitting.

## 2. Architecture & Design Principles
* **Game Loop Lifecycle:** Strictly segregates execution into distinct stages:
  $$\text{Process Input} \longrightarrow \text{Update Game State} \longrightarrow \text{Resolve Collisions} \longrightarrow \text{Render Surface} \longrightarrow \text{Regulate FPS}$$

* **Class Encapsulation:**
  * `Player`: Controllable entity directed via arrow keys (`pygame.key.get_pressed()`) with strict screen boundary clamping.
  * `Enemy`: Autonomous obstacles moving horizontally across the viewport, reversing velocity vectors upon boundary collision.

## 3. Implementation Analysis (`activity_2.py`)
* **Alpha Transparency:** Initializes 32-bit drawing surfaces using `pygame.SRCALPHA` and `pygame.draw.circle()` to render crisp, anti-aliased circular graphics.
* **Collision Engine:** Invokes `pygame.sprite.spritecollide(player, enemies, True)` to process rectangular bounding box intersections and consume target entities upon contact.
* **Dynamic Lifecycle Management:** Tracks active player score and continuously spawns replacement enemy sprites into the `all_sprites` and `enemies` groups up to designated capacity limits.