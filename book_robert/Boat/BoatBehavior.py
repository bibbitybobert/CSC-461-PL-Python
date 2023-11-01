"""
Behaviors will return the distance that a boat moves each update
"""


def steady(engine_pow: int, river_flow: int):  # GRADING: STEADY_TRAVEL
    """
    steady function that always returns 1 distance
    :param engine_pow: boat engine power
    :param river_flow: flow of the section that the boat is in
    :return: 1
    """
    return 1


def max_dist(engine_pow: int, river_flow: int):  # GRADING: MAX_TRAVEL
    """
    function to calculate the max distance a boat will move dependent on the engine power of the boat and the flow
    of the river that the boat is in. Min distance the boat can move is 1. (boat cannot have zero optimal distance and
    cannot move backwards)
    :param engine_pow: power of the engine
    :param river_flow: flow of the river that the boat is in
    :return: the max distance the boat can move
    """
    dist = engine_pow - river_flow
    return dist if dist > 1 else 1
