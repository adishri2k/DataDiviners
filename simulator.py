from behaviors import update_behavior
import pandas as pd

def run_simulation(vehicles, assets, duration, dt, highway_y):
    traj = []
    steps = int(duration/dt)+1
    for step in range(steps):
        t = step*dt
        for v in vehicles:
            traj.append({"time":t, **v})
            v["speed"] = update_behavior(v, vehicles, assets, dt, highway_y)
            v["x"] += v["speed"] * dt
    return pd.DataFrame(traj)