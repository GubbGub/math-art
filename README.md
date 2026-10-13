# Math Art

A collection of generative artworks built from mathematical systems, dynamical equations, and computational visualization.

This project explores the beauty of chaos, flow fields, attractors, and emergent structure through code. Each piece starts from a mathematical model and is rendered into an image or animation that feels both scientific and artistic.

## Featured works

### Aizawa attractor wallpaper

The current piece in the repository is an Aizawa attractor rendered as a dark blue, high-contrast wallpaper.

- `aizawa_wallpaper.py` — generates the visualization
- `aizawa_wallpaper.png` — standard export
- `aizawa_wallpaper_retina.png` — higher-resolution export

The system is defined by a set of chaotic differential equations and plotted in 3D, creating a dense ribbon-like structure that resembles a glowing orbital sketch.

### Clifford attractor wallpaper

A second piece in the collection uses the Clifford attractor system, producing a denser and more floral, neon-like structure with a darker palette and vividly saturated tones.

- `clifford_attractor.py` — generates the visualization
- `clifford_wallpaper.png` — standard export
- `clifford_wallpaper_retina.png` — higher-resolution export

The Clifford attractor is governed by a nonlinear pair of equations that create intricate looping patterns and a rich sense of motion even in a static render.

## Why this project exists

These artworks sit at the intersection of:

- nonlinear dynamics
- chaotic systems
- geometry
- computational aesthetics
- visual experimentation

The goal is not just to produce pretty outputs, but to study how mathematical rules create forms, motion, and texture that feel alive.

## Project structure

```text
math-art/
├── README.md
├── .gitignore
├── aizawa_wallpaper.py
├── aizawa_wallpaper.png
├── aizawa_wallpaper_retina.png
├── clifford_attractor.py
├── clifford_wallpaper.png
├── clifford_wallpaper_retina.png
└── future pieces...
```

## Setup

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

Generate the current image:

```bash
python aizawa_wallpaper.py
```

Generate the Clifford attractor image:

```bash
python clifford_attractor.py
```

## Can we make these animated?

Yes — absolutely.

These kinds of systems are especially well-suited to animation because they evolve over time. The most natural approach is to render a sequence of frames while the system or camera moves through the attractor, then combine them into a video.

A few ideas:

- rotate the 3D camera slowly around the attractor
- increase the number of plotted points over time
- fade the trail length in and out
- animate parameter changes to morph between shapes
- accumulate multiple passes for a glowing, cinematic effect

For example, a script could:

1. simulate the system over a time window
2. plot a subset of the trajectory for each frame
3. save each frame as an image
4. stitch them together with `ffmpeg` or Python video tools

This would turn a static wallpaper into a looping generative motion study.

## Future direction

This repo is intended to grow into a small collection of different systems and visual styles, including:

- Lorenz and Rossler attractors
- strange attractors with different color palettes
- animated loops
- wallpaper exports
- abstract parameter studies

## License

This project is intended for personal, artistic, and educational exploration. If you reuse any of the visuals, please credit the project and original author.
