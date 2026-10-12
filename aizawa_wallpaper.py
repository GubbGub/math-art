import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap
from scipy.integrate import solve_ivp

# Rebuild font cache
fm.fontManager.__init__()

# Find Inter SemiBold automatically
inter_path = None
for f in fm.findSystemFonts():
    if 'Inter' in f and 'SemiBold' in f:
        inter_path = f
        break

if inter_path is None:
    raise FileNotFoundError("Couldn't find Inter SemiBold automatically.")

inter_semibold = fm.FontProperties(fname=inter_path)

# 1. Math System (Untouched accuracy)


def aizawa(t, state, a, b, c, d, e, f):
    x, y, z = state
    dx = (z - b) * x - d * y
    dy = d * x + (z - b) * y
    dz = c + a * z - (z**3) / 3 - (x**2 + y**2) * (1 + e * z) + f * z * (x**3)
    return [dx, dy, dz]


a, b, c, d, e, f = 0.95, 0.7, 0.6, 3.5, 0.25, 0.1
initial_state = [0.1, 0.0, 0.0]
t_span = (0, 150)
t_eval = np.linspace(t_span[0], t_span[1], 150000)

solution = solve_ivp(
    aizawa, t_span, initial_state, args=(a, b, c, d, e, f), t_eval=t_eval,
    method='RK45', rtol=1e-9, atol=1e-9
)
x, y, z = solution.y

# Colors
custom_colors = ["#0A1A2F", "#1D4E89", "#4DA4EA", "#8FD3F4", "#DFF6FF"]
custom_cmap = LinearSegmentedColormap.from_list("blue_glow", custom_colors)
bg_top, bg_bottom = "#1A1A1C", "#0A0A0C"
bg_cmap = LinearSegmentedColormap.from_list(
    "warm_grey_bg", [bg_bottom, bg_top])

# 2. Double-Density Resolution Strategy (5120 x 3328 px)
# This forces macOS to render it perfectly sharp without compressing it to mush.
fig = plt.figure(figsize=(16, 10.4), dpi=320)

bg_ax = fig.add_axes([0, 0, 1, 1])
gradient = np.linspace(0, 1, 512).reshape(-1, 1)
bg_ax.imshow(gradient, aspect='auto', cmap=bg_cmap,
             extent=[0, 1, 0, 1], origin='lower')
bg_ax.set_axis_off()

ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.patch.set_alpha(0)
ax.set_facecolor((0, 0, 0, 0))

# Increased line-width slightly (to 1.2) so it remains bold at higher density
colors = custom_cmap(np.linspace(0, 1, len(x)))
for i in range(len(x) - 1):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=colors[i], alpha=0.7, lw=1.2)

ax.set_axis_off()


def padded_limits(arr, pad_fraction=0.25):
    lo, hi = min(arr), max(arr)
    span = hi - lo
    pad = span * pad_fraction
    return [lo - pad, hi + pad]


ax.set_xlim(padded_limits(x))
ax.set_ylim(padded_limits(y))
ax.set_zlim(padded_limits(z))
ax.view_init(elev=20, azim=45)

# 3. Dock-Safe Typography Bounds
# Shifted upward to y=0.10 and y=0.07 so it sits completely clear of the Dock frame
label_color = "#FFFFFF"
label_alpha = 0.55

fig.text(0.06, 0.11, "AIZAWA ATTRACTOR", fontsize=14, color=label_color,
         alpha=label_alpha, fontproperties=inter_semibold)
fig.text(0.06, 0.08, "Chaotic dynamical system — studied by Aizawa, 1990s",
         fontsize=10, color=label_color, alpha=label_alpha - 0.1, fontproperties=inter_semibold)

eq_text = r"$\dot{z} = c + az - \frac{z^3}{3} - (x^2+y^2)(1+ez) + fzx^3$"
fig.text(0.94, 0.08, eq_text, fontsize=12, color=label_color,
         alpha=label_alpha, ha='right', va='bottom')

# 4. Save with absolute pixel limits
plt.savefig('aizawa_wallpaper_retina.png', dpi=320, pad_inches=0)
print("Ultra-sharp wallpaper generated safely!")
