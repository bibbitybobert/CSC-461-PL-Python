"""
Behaviors will return the distance that a boat moves each update
"""


def steady(engine_pow: int, river_flow: int):
    return 1


def max_dist(engine_pow: int, river_flow: int):
    dist = engine_pow - river_flow
    return dist if dist > 1 else 1
