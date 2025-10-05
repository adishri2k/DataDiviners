from config import SCENARIO_NAME, DURATION, DT, HIGHWAY_Y
from assets import generate_assets
from vehicles import initialize_vehicles
from simulator import run_simulation
from exporters import save_json, plot_trajectories

# Generate scenario
assets = generate_assets()
vehicles = initialize_vehicles()
df = run_simulation(vehicles, assets, DURATION, DT, HIGHWAY_Y)

# Save outputs
scenario = {"name": SCENARIO_NAME, "vehicles": vehicles, "assets": assets}
save_json(scenario, "scenario.json")
plot_trajectories(df, assets, "trajectories.png")
df.to_csv("trajectories.csv", index=False)
print("Simulation complete.")