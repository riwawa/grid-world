# Grid World, Ray Casting, and Occupancy Grid

Probabilistic robotics fundamentals mini-project, implemented from scratch in pure Python (no external dependencies). Goal: understand, cell by cell, how a robot represents the space around it, "sees" obstacles with a range sensor, and builds a map from uncertain readings — before any of these pieces come bundled inside a ready-made library (like ROS2's `slam_toolbox`).

## What was implemented

```
Grid World             → represent a 2D environment as a discrete grid,
                          with conversion between cells (row, column) and
                          real-world coordinates (x, y) in meters

Ray Casting (DDA)       → simulate a single sensor ray: from a position
                          and an angle, find the distance to the nearest
                          obstacle by walking cell by cell efficiently
                          (Digital Differential Analyzer)

LiDAR simulation         → fire several evenly spaced rays around a
                          position, simulating a full scan from a
                          rotating sensor

Occupancy Grid           → accumulate multiple LiDAR scans into a
                          probability map (one value per cell), using a
                          log-odds update -- the same core logic (Bayes
                          filter) used in real SLAM
```

## File structure

| File | What it contains |
|---|---|
| `grid.py` | Map definition (`mapa_bruto`), parsing into `grid` (list of lists of booleans), cell↔world conversion, `celula_esta_livre`, and the Occupancy Grid functions (`criar_occupancy_grid`, `atualizar_occupancy_grid`, `log_odds_para_probabilidade`) |
| `ray_casting.py` | `lancar_raio` (distance to the nearest obstacle in a direction) and `lancar_raio_com_caminho` (same thing, also returning every free cell traversed — used by the Occupancy Grid) |
| `simular_lidar.py` | `simular_lidar`, which fires multiple uniformly spaced rays, reusing `ray_casting.py` |

*(Adjust the names above if your local file organization differs — some blocks may have been consolidated into the same file during development.)*

## How to run

No dependencies to install — just standard Python:

```bash
python grid.py           # tests Grid World and Occupancy Grid on their own
python ray_casting.py    # tests a single ray
python simular_lidar.py  # tests a full multi-ray scan
```

## References used

- Grid World / cell↔coordinate conversion: technique adapted from grid-maze tutorials (e.g., the "Pac-Man in Python" series, @TheWannabeCoder)
- Ray Casting (DDA): javidx9 (OneLoneCoder), *"Super Fast Ray Casting in Tiled Worlds using DDA"* — https://youtu.be/NbSee-XM7WA (algorithm in C++, adapted to Python for this project)
- Occupancy Grid Mapping (log-odds representation, binary Bayes filter): *Probabilistic Robotics* (Thrun, Burgard, Fox) — check the specific chapter on Occupancy Grid Mapping in the reference PDF before citing an exact number
- *Introduction to Autonomous Mobile Robots* (Siegwart, Nourbakhsh) — complementary mobile robotics reference