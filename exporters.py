import json
import matplotlib.pyplot as plt

def save_json(scenario, filename):
    with open(filename, "w") as f:
        json.dump(scenario, f, indent=2)

def plot_trajectories(df, assets, filename):
    plt.figure(figsize=(10,6))
    for vid, g in df.groupby("id"):
        plt.plot(g["x"], g["y"], label=vid)
    for a in assets:
        plt.scatter(a["x"], a["y"], label=a["type"], s=50)
    plt.legend()
    plt.savefig(filename)