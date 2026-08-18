import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


steps = [
    "1. CRAWLER\nCollects reviews and raw data",
    "2. RAW DATABASE\nStores collected raw reviews",
    "3. CLEANING PIPELINE\nCleans and preprocesses text",
    "4. SENTIMENT MODEL\nPredicts Positive / Negative / Neutral",
    "5. CONFIDENCE FILTERING\nFilters low confidence predictions",
    "6. KEYWORD EXTRACTION\nKeyword Trends",
    "7. ANALYTICS\nSentiment Distribution + Report",
    "8. FASTAPI WEB SERVICE\n/predict + Swagger"
]

fig, ax = plt.subplots(figsize=(10, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 18)
ax.axis("off")

ax.text(
    5, 17.3,
    "INTELLIGENT SENTIMENT SYSTEM",
    ha="center",
    va="center",
    fontsize=18,
    fontweight="bold"
)

y_positions = [15.5, 13.5, 11.5, 9.5, 7.5, 5.5, 3.5, 1.5]

for i, (step, y) in enumerate(zip(steps, y_positions)):

    box = FancyBboxPatch(
        (1.5, y - 0.7),
        7,
        1.3,
        boxstyle="round,pad=0.05",
        edgecolor="black",
        facecolor="lightblue"
    )

    ax.add_patch(box)

    ax.text(
        5,
        y,
        step,
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

    if i < len(steps) - 1:
        ax.annotate(
            "",
            xy=(5, y_positions[i + 1] + 0.7),
            xytext=(5, y - 0.7),
            arrowprops=dict(arrowstyle="->", lw=2)
        )

plt.savefig(
    "diagrams/system_diagram.png",
    dpi=300,
    bbox_inches="tight"
)

print("System diagram created successfully!")