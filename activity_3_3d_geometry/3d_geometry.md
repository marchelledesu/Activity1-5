# Activity 3: 3D Coordinate Geometry & Spatial Bounding Volumes

## 1. Technical Overview
Activity 3 develops a complete 3D coordinate geometry library in Python. It provides vector space distance metrics, 3D bounding sphere collision tests, and Axis-Aligned Bounding Box (AABB) volumetric intersection checking.

## 2. Theoretical Foundations & Mathematical Formulas
* **3D Euclidean Distance Formula:**
  $$d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

* **Sphere-Sphere Intersection Criteria:**
  $$\text{Intersects} \iff \|C_1 - C_2\| \le (r_1 + r_2)$$

* **AABB Intersection Criteria:** Two rectangular bounding volumes overlap if and only if their intervals overlap along all three Cartesian axes simultaneously:
  $$\text{Overlap} \iff (A_{\min.x} \le B_{\max.x} \land A_{\max.x} \ge B_{\min.x}) \land (A_{\min.y} \le B_{\max.y} \land A_{\max.y} \ge B_{\min.y}) \land (A_{\min.z} \le B_{\max.z} \land A_{\max.z} \ge B_{\min.z})$$

## 3. Implementation Analysis (`activity_3.py`)
* **Vector Distance Verification:** Computes distance between origin $P_1(0,0,0)$ and $P_2(3,4,12)$:
  $$d = \sqrt{3^2 + 4^2 + 12^2} = \sqrt{9 + 16 + 144} = \sqrt{169} = 13.00$$

* **Interactive Debug Visualizer:** Maps 3D spatial volumes onto a 2D viewport via axonometric projection:
  $$(x_p, y_p) = (x_{\text{center}} + x \cdot s, y_{\text{center}} - y \cdot s + z \cdot s \cdot 0.3)$$

* **Real-time Collision State:** Updates bounding volumes dynamically along a sine trajectory to visually demonstrate collision state changes (color updates) upon volumetric overlap.