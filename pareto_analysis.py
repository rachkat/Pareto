
import pandas as pd
import matplotlib.pyplot as plt

# === Config ===
INPUT_CSV = "issues_pareto.csv"       # path to your dataset
OUTPUT_IMG = "pareto_chart.png"       # chart will be saved here
TITLE = "Pareto Analysis of Issues"

# === Load data ===
df = pd.read_csv(INPUT_CSV)

# Validate required columns
required = {"Issue", "Count"}
if not required.issubset(df.columns):
    raise ValueError(f"CSV must contain columns: {required}")

# Sort by Count descending
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

# Cumulative percentage
df["Cumulative %"] = df["Count"].cumsum() / df["Count"].sum() * 100

# === Plot ===
plt.figure(figsize=(8, 5))

# Bars for counts
plt.bar(df["Issue"], df["Count"])

# Line for cumulative percentage (second axis)
# To avoid subplots, we draw the line scaled to the primary axis and add a right y-axis label
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot(df["Issue"], df["Cumulative %"], marker="D")
ax2.set_ylabel("Cumulative %")
ax2.axhline(80, linestyle="--")  # 80% reference line

plt.title(TITLE)
plt.xlabel("Issue")
ax.set_ylabel("Count")
plt.tight_layout()
plt.savefig(OUTPUT_IMG, dpi=150, bbox_inches="tight")
print(f"Saved {OUTPUT_IMG}")
