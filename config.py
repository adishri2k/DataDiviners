# Scenario configuration parameters
SCENARIO_NAME = "village_to_highway_merge_demo"
DURATION = 60.0
DT = 0.5
HIGHWAY_LENGTH = 800.0
VILLAGE_APPROACH_LENGTH = 200.0
HIGHWAY_Y = [3.0, -3.0]
MERGE_X = 0.0

ASSET_TYPES = ["pothole", "barricade", "animal", "unpaved_patch"]

# Vehicle definitions
INITIAL_VEHICLES = [
    {"type":"tractor","x":-180,"y":0.5,"speed":6,"lane":"village","behavior":"slow"},
    {"type":"two_wheeler","x":-140,"y":-0.5,"speed":18,"lane":"village","behavior":"erratic"},
    {"type":"car","x":-160,"y":0,"speed":22,"lane":"village","behavior":"normal"},
    {"type":"truck","x":-220,"y":0.3,"speed":20,"lane":"village","behavior":"normal"},
    {"type":"car","x":-60,"y":-0.2,"speed":24,"lane":"village","behavior":"normal"},
    {"type":"car","x":50,"y":3,"speed":26,"lane":"highway_north","behavior":"normal"},
    {"type":"bus","x":30,"y":-3,"speed":22,"lane":"highway_south","behavior":"normal"},
    {"type":"car","x":10,"y":3.4,"speed":24,"lane":"highway_north","behavior":"normal"},
]