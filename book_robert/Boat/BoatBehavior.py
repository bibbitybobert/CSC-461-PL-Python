"""
Behaviors will return the distance that a boat moves each update
"""


def steady(engine_pow: int, river_flow: int):  # GRADING: STEADY_TRAVEL
    return 1


def max_dist(engine_pow: int, river_flow: int):  # GRADING: MAX_TRAVEL
    dist = engine_pow - river_flow
    return dist if dist > 1 else 1
