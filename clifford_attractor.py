import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Clifford attractor system
# dx/dt = sin(a * y) + c * cos(a * x)
# dy/dt = sin(b * x) + d * cos(b * y)


def clifford_step(x, y, a, b, c, d):
    x_new = np.sin(a * y) + c * np.cos(a * x)
    y_new = np.sin(b * x) + d * np.cos(b * y)
    return x_new, y_new


def generate_clifford_points(a, b, c, d, n_steps=300000, burn_in=30000):
    x = np.empty(n_steps)
    y = np.empty(n_steps)
    x[0], y[0] = 0.1, 0.1

    for i in range(1, n_steps):
        x[i], y[i] = clifford_step(x[i - 1], y[i - 1], a, b, c, d)

    return x[burn_in:], y[burn_in:]


def main():
    a, b, c, d = 1.7, 1.3, 1.5, 0.2
    x, y = generate_clifford_points(a, b, c, d)

    bg_top, bg_bottom = "#0B1020", "#121828"
    bg_cmap = LinearSegmentedColormap.from_list(
        "night_bg", [bg_bottom, bg_top]
    )
    art_cmap = LinearSegmentedColormap.from_list(
        "clifford_palette",
        ["#12071D", "#3D1B5F", "#8A2BE2", "#FF5C8A", "#FFC857", "#F2F7FF"],
    )

    fig = plt.figure(figsize=(16, 10.4), dpi=320)

    bg_ax = fig.add_axes([0, 0, 1, 1])
    gradient = np.linspace(0, 1, 1024).reshape(-1, 1)
    bg_ax.imshow(gradient, aspect='auto', cmap=bg_cmap,
                 extent=[0, 1, 0, 1], origin='lower')
    bg_ax.set_axis_off()

    ax = fig.add_axes([0, 0, 1, 1], facecolor='none')
    ax.set_axis_off()

    sample = np.arange(0, len(x), 3)
    colors = art_cmap(np.linspace(0, 1, len(sample)))

    ax.scatter(
        x[sample],
        y[sample],
        s=10,
        c=colors,
        cmap=art_cmap,
        alpha=0.9,
        linewidths=0,
        rasterized=True,
    )

    pad_x = 0.18
    pad_y = 0.18
    ax.set_xlim(np.min(x) - pad_x, np.max(x) + pad_x)
    ax.set_ylim(np.min(y) - pad_y, np.max(y) + pad_y)

    fig.text(
        0.06,
        0.11,
        "CLIFFORD ATTRACTOR",
        fontsize=14,
        color="#F5F7FA",
        alpha=0.7,
        fontweight='bold',
    )
    fig.text(
        0.06,
        0.08,
        "Chaotic flow in a nonlinear oscillator system",
        fontsize=10,
        color="#F5F7FA",
        alpha=0.5,
    )

    plt.savefig("clifford_wallpaper.png", dpi=320, pad_inches=0)
    plt.savefig("clifford_wallpaper_retina.png", dpi=640, pad_inches=0)
    print("Clifford attractor wallpaper generated successfully.")


if __name__ == "__main__":
    main()
