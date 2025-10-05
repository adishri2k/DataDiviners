import random

def find_vehicle_ahead(v, vehicles, lane_filter=None):
    ahead = [u for u in vehicles if u["id"] != v["id"] and (lane_filter is None or u["lane"]==lane_filter) and u["x"] > v["x"]]
    return min(ahead, key=lambda u: u["x"] - v["x"]) if ahead else None

def update_behavior(veh, vehicles, assets, dt, highway_y):
    desired_speed = veh["speed"]
    if veh["behavior"] == "slow":
        desired_speed = min(desired_speed, 10.0)
    elif veh["behavior"] == "erratic" and random.random() < 0.04:
        desired_speed = max(0.0, veh["speed"] - random.uniform(5, 12))
    for a in assets:
        dx, dy = abs(veh["x"]-a["x"]), abs(veh["y"]-a["y"])
        if dx < 6.0 and dy < 1.2:
            if a["type"] == "pothole":
                desired_speed = max(desired_speed - 6.0, 2.0)
            elif a["type"] == "barricade":
                desired_speed = 0.0
            elif a["type"] == "animal" and random.random() < 0.25:
                desired_speed = 0.0
            elif a["type"] == "unpaved_patch":
                desired_speed = max(desired_speed - 4.0, 3.0)
    return max(desired_speed, 0.0)