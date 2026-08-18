import matplotlib.pyplot as plt
import os

fig, ax = plt.subplots(figsize=(10, 6))

boxes = [
    ("Crawler / Scraper\n(crawler.py)", (0.1, 0.7)),
    ("Raw SQLite DB\n(data/raw_data.db)", (0.4, 0.7)),
    ("Cleaning Pipeline\n(cleaner.py)", (0.7, 0.7)),
    ("Sentiment Model\n+ Confidence Filter\n(model.py)", (0.2, 0.3)),
    ("Keyword Extraction\n(keywords.py)", (0.5, 0.3)),
    ("Analytics Engine\n(analytics.py)", (0.8, 0.3)),
    ("FastAPI Endpoints\n(api/app.py)", (0.5, 0.05)),
]

for text, (x, y) in boxes:
    ax.text(x, y, text, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.6", fc="lightblue", ec="b", lw=1.5), fontsize=10)

arrows = [
    ((0.22, 0.7), (0.28, 0.7)),
    ((0.52, 0.7), (0.58, 0.7)),
    ((0.7, 0.62), (0.25, 0.38)),
    ((0.7, 0.62), (0.5, 0.38)),
    ((0.2, 0.22), (0.4, 0.08)),
    ((0.5, 0.22), (0.5, 0.09)),
    ((0.8, 0.22), (0.6, 0.08)),
]

for start, end in arrows:
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.85)
ax.axis('off')
plt.title("Intelligent Sentiment System Architecture", fontsize=14, fontweight='bold')

out_dir = os.path.dirname(__file__)
out_path = os.path.join(out_dir, "architecture_diagram.png")
plt.tight_layout()
plt.savefig(out_path, dpi=300)
print("System diagram created successfully at:", out_path)