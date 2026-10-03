# Activity 4: Software 3D Wireframe Projection Engine

## 1. Technical Overview
Activity 4 constructs a software-based wireframe projection pipeline in Pygame. It applies 3D spatial rotation matrices to a cube mesh centered at the origin and projects vertices onto a 2D view plane across three distinct parallel and perspective projection modes.

## 2. Mathematical Pipeline Equations
1. **3D Rotation Transformations:** Vertices undergo Euler angle rotations around X and Y axes prior to projection:
   $$R_x(\theta): \begin{bmatrix} y' \\ z' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} y \\ z \end{bmatrix}$$
   $$R_y(\theta): \begin{bmatrix} x' \\ z' \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ z \end{bmatrix}$$

2. **Orthographic Projection:** Directly projects coordinates onto the view plane while discarding depth:
   $$x_p = x, \quad y_p = y$$

3. **Oblique (Cavalier) Projection:** Projects receding depth along angle $\phi = 45^\circ$ without foreshortening ($L_1 = 1.0$):
   $$x_p = x + z \cdot \cos(\phi), \quad y_p = y + z \cdot \sin(\phi)$$

4. **Perspective Projection:** Scales coordinates inversely relative to distance $D$, causing parallel lines to converge toward a center vanishing point:
   $$x_p = \frac{x \cdot D}{z + D}, \quad y_p = \frac{y \cdot D}{z + D} \quad (D = 400)$$

## 3. Implementation Analysis (`activity_4.py`)
* **Multi-Viewport Architecture:** Renders three distinct side-by-side display panels ("Orthographic", "Cavalier", and "Perspective") simultaneously within a single window.
* **Rasterization Engine:** Maps edge connectivity using index topology array `cube_edges` and rasterizes lines between projected 2D coordinates using `pygame.draw.line()`.