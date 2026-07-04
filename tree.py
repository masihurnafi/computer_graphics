import matplotlib.pyplot as plt
import random

def draw_branch(ax, x, y, angle, length, depth):
    if depth == 0 or length < 2:
        return

    x2 = x + length * 0.6 * __import__("math").cos(__import__("math").radians(angle))
    y2 = y + length * 0.6 * __import__("math").sin(__import__("math").radians(angle))

    width = max(0.5, depth * 0.6)
    color = "#8B5A2B" if depth > 2 else "#2E8B57"
    ax.plot([x, x2], [y, y2], color=color, linewidth=width, solid_capstyle="round")

    if depth <= 2:
        for _ in range(3):
            leaf_x = x2 + random.uniform(-3, 3)
            leaf_y = y2 + random.uniform(-1, 3)
            ax.plot(leaf_x, leaf_y, "o", color="#3CB043", markersize=random.uniform(3, 6), alpha=0.8)

    new_length = length * 0.75
    angle_variation = random.uniform(15, 25)

    draw_branch(ax, x2, y2, angle + angle_variation, new_length, depth - 1)
    draw_branch(ax, x2, y2, angle - angle_variation, new_length, depth - 1)

    if random.random() < 0.3:
        draw_branch(ax, x2, y2, angle + random.uniform(-8, 8), new_length * 0.8, depth - 1)


def main():
    random.seed(7)
    fig, ax = plt.subplots(figsize=(8, 10))

    draw_branch(ax, x=0, y=0, angle=90, length=18, depth=9)

    ax.set_xlim(-25, 25)
    ax.set_ylim(-2, 40)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("#E8F4F8")
    fig.patch.set_facecolor("#E8F4F8")
    ax.set_title("Fractal Tree", fontsize=16, color="#333333")

    plt.tight_layout()
    plt.savefig("tree.png", dpi=150, facecolor=fig.get_facecolor())
    plt.show()


if __name__ == "__main__":
    main()
