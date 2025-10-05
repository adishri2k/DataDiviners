from config import INITIAL_VEHICLES

def initialize_vehicles():
    vehicles = []
    for i, v in enumerate(INITIAL_VEHICLES, start=1):
        v = v.copy()
        v["id"] = f"V{i}"
        vehicles.append(v)
    return vehicles