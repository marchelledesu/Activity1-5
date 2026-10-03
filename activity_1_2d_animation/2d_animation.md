# Activity 1: 2D Animation Principles & Kinematics Engine

## 1. Technical Overview
Activity 1 implements core 2D computer animation algorithms using Pygame, focusing on keyframing via linear interpolation (LERP), shape morphing with smooth easing curves, and Newtonian bouncing dynamics. The software system executes within a continuous Pygame event loop capped at 60 FPS using delta time (`dt`) for frame-rate independence.

## 2. Theoretical Foundations & Mathematical Formulas
* **Linear Interpolation (LERP):** Interpolates 2D coordinates between keyframe positions parameterized by normalized time $t \in [0.0, 1.0]$:
  $$P(t) = P_{\text{start}} + (P_{\text{end}} - P_{\text{start}}) \cdot t$$

* **Ease-In-Out Smoothing:** Applies a smoothstep Hermite polynomial to convert linear time into natural acceleration and deceleration:
  $$f(t) = t^2 \cdot (3 - 2t)$$

* **Polygon Edge Subdivision (Vertex Correspondence):** To morph a 3-vertex triangle into a 4-vertex quadrilateral without structural tearing, an intermediate midpoint vertex is inserted along the first edge of the triangle:
  $$V_{\text{mid}} = \left(\frac{x_0 + x_1}{2}, \frac{y_0 + y_1}{2}\right)$$

* **Newtonian Bouncing Dynamics:** Models gravitational acceleration $g$ and kinetic energy loss upon ground impact using a coefficient of restitution $e$:
  $$v_{y,(i+1)} = v_{y,i} + g$$
  $$y_{i+1} = y_i + v_{y,i} \cdot (60 \cdot dt)$$
  $$v_{\text{rebound}} = -e \cdot v_{\text{impact}} \quad (\text{when } y + r \ge y_{\text{ground}})$$

## 3. Implementation Analysis (`activity_1.py`)
* **Interpolation Routines:** `lerp_point()` performs 2D linear interpolation, while `ease_in_out()` shapes the progression parameter $t$.
* **Dynamic Morphing Engine:** `morph_polygon(t)` dynamically evaluates shape vertex counts, subdivides simpler geometries on the fly, and interpolates matching control points.
* **Harmonic Time Driver:** Uses a trigonometric wave `0.5 + 0.5 * math.sin(elapsed * 1.5)` to drive continuous ping-pong morphing cycles.
* **Collision & Resting Thresholds:** Clamps ball position to `ground_y - radius` upon impact and zeroes out tiny residual velocity ($|v_y| < 0.4$) to eliminate infinite micro-bouncing jitter.