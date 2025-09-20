import matplotlib.pyplot as plt
import matplotlib.animation as animation
import binary_search_cpp

# Example array
arr = [3, 7, 12, 18, 23, 31, 42, 56, 67, 89]
target = 42

# Get steps from C++
steps = binary_search_cpp.binary_search(arr, target)

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(range(len(arr)), arr, color="lightblue")

def init():
    ax.set_ylim(0, max(arr) + 10)
    ax.set_title("Binary Search Visualization")
    return bars

def update(frame):
    for bar in bars:
        bar.set_color("lightblue")

    step = steps[frame]
    low, mid, high, val, found = step["low"], step["mid"], step["high"], step["value"], step["found"]

    bars[low].set_color("green")
    bars[high].set_color("green")
    bars[mid].set_color("orange" if not found else "red")

    ax.set_xlabel(f"Step {frame+1}: low={low}, mid={mid} (val={val}), high={high}, found={bool(found)}")
    return bars

# ---------------------------
# Keep reference to the animation
# ---------------------------
anim = animation.FuncAnimation(fig, update, frames=len(steps),
                               init_func=init, blit=False, repeat=False)

# Option 2: Save as GIF or MP4
anim.save("binary_search_demo.gif", writer='pillow', fps=1)