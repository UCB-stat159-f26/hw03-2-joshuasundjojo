"""Plot a player's career matches."""
import matplotlib.pyplot as plt

COLORS = {"W": "#1f77b4", "L": "#d62728"}
LABELS = {"W": "Win", "L": "Loss"}


def plot_player_career(matches):
    fig, ax = plt.subplots(figsize=(10, 6))
    for result in ("W", "L"):
        subset = matches[matches["result"] == result]
        ax.scatter(subset["age"], subset["age_diff"], s=20, alpha=0.6,
                   color=COLORS[result], label=LABELS[result])
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_xlabel("Player's age")
    ax.set_ylabel("Player's age minus opponent's age (years)")
    ax.legend()
    return ax