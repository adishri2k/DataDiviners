import random
from config import VILLAGE_APPROACH_LENGTH, ASSET_TYPES

def generate_assets(seed=42):
    random.seed(seed)
    assets = []
    for i in range(8):
        t = random.random()
        x = -VILLAGE_APPROACH_LENGTH * (0.05 + 0.9 * t)
        y = random.gauss(0.0, 1.2)
        kind = random.choices(ASSET_TYPES, weights=[0.4,0.2,0.25,0.15])[0]
        assets.append({"id":f"A{i+1}","type":kind,"x":x,"y":y})
    assets.append({"id":"A9","type":"barricade","x":-15.0,"y":0.8})
    assets.append({"id":"A10","type":"animal","x":-120.0,"y":-0.6})
    return assets