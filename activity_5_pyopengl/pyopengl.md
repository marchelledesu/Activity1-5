# Activity 5: Hardware Graphics Pipeline & Shading with PyOpenGL

## 1. Technical Overview
Activity 5 transitions graphics execution to hardware acceleration using PyOpenGL and Pygame (`OPENGL | DOUBLEBUF`). It demonstrates GPU transformation pipelines, $Z$-buffer depth testing, alpha transparency blending, and coordinate axis primitives.

## 2. Pipeline Configuration & OpenGL Architecture
* **Frustum & Viewing Matrix:** Configures a perspective viewing frustum using `gluPerspective(45, aspect_ratio, 0.1, 50.0)` and translates the eye origin along the Z-axis via `glTranslatef(0.0, 0.0, -5)`.
* **Depth Testing ($Z$-Buffer):** Enables `GL_DEPTH_TEST` so the GPU automatically performs hidden-surface removal based on fragment depth values.
* **Alpha Blending:** Enables `GL_BLEND` using `glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)` to calculate transparency compositing:
  $$I_{\text{out}} = \alpha \cdot I_{\text{src}} + (1 - \alpha) \cdot I_{\text{dst}}$$

## 3. Implementation Analysis (`activity_5.py`)
* **Buffer Clearing:** Executes `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)` at the start of every frame to reset render targets and prevent temporal artifacts.
* **Matrix Stack Operations:** Encapsulates mesh rotation using `glPushMatrix()` and `glPopMatrix()` to maintain localized transformation state.
* **Primitive Specification:** Renders 6 quad surfaces (`GL_QUADS`) with per-face RGBA colors (`glColor4f`) and builds world-space coordinate axes (`GL_LINES`) to visualize spatial orientation.