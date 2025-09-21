import matplotlib.pyplot as plt
import matplotlib.animation as animation
import binary_search_cpp

# Example array
arr = [3, 7, 12, 18, 23, 31, 42, 56, 67, 89]
target = 42

# Get steps from C++
steps = binary_search_cpp.binary_search(arr, target)

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(range(len(arr)), arr, color="lightgray", edgecolor="black")

# Put indices on x-axis
ax.set_xticks(range(len(arr)))
ax.set_xticklabels([str(i) for i in range(len(arr))], fontsize=10)
ax.set_xlabel("Index", fontsize=12)

# Show values above bars
value_labels = []
for i, val in enumerate(arr):
    txt = ax.text(i, arr[i] + 1, str(val), ha="center", fontsize=10, weight="bold")
    value_labels.append(txt)

# Target displayed at top
target_text = ax.text(0.02, 1.05, f"Target = {target}",
                      transform=ax.transAxes,
                      fontsize=12, color="darkred", weight="bold")

# Arrow annotations
arrow_low = ax.annotate("low", xy=(0, 0), xytext=(0, -20),
                        textcoords="offset points",
                        arrowprops=dict(facecolor="blue", shrink=0.05),
                        ha="center", fontsize=9, color="blue")

arrow_mid = ax.annotate("mid", xy=(0, 0), xytext=(0, -35),
                        textcoords="offset points",
                        arrowprops=dict(facecolor="orange", shrink=0.05),
                        ha="center", fontsize=9, color="orange")

arrow_high = ax.annotate("high", xy=(0, 0), xytext=(0, -50),
                         textcoords="offset points",
                         arrowprops=dict(facecolor="red", shrink=0.05),
                         ha="center", fontsize=9, color="red")


def init():
    ax.set_ylim(0, max(arr) + 20)
    ax.set_title("Binary Search Visualization", fontsize=14, weight="bold")
    return list(bars) + value_labels + [arrow_low, arrow_mid, arrow_high, target_text]


def update(frame):
    # Reset all bars to gray
    for bar in bars:
        bar.set_color("lightgray")

    step = steps[frame]
    low, mid, high, val, found = (
        step["low"], step["mid"], step["high"], step["value"], step["found"]
    )

    # Highlight search range (blue)
    for i in range(low, high + 1):
        bars[i].set_color("skyblue")

    # Highlight mid (orange, or green if found)
    bars[mid].set_color("orange")
    if found:
        bars[mid].set_color("green")

    # Move arrows
    arrow_low.xy = (low, arr[low])
    arrow_mid.xy = (mid, arr[mid])
    arrow_high.xy = (high, arr[high])

    # Update step description
    ax.set_xlabel(
        f"Step {frame+1}: low={low}, mid={mid} (val={val}), high={high}, found={bool(found)}",
        fontsize=11
    )

    # Return updated artists
    return list(bars) + value_labels + [arrow_low, arrow_mid, arrow_high, target_text]


# Animation
anim = animation.FuncAnimation(
    fig, update, frames=len(steps), init_func=init,
    blit=False, repeat=False, interval=1500  # slower for clarity
)

# Save as GIF
anim.save("binary_search_demo.gif", writer="pillow", fps=1)

plt.show()