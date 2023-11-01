
def pass_through(dir_str: str):
    """
    Pass_though behavior for the lock where it acts like a section
    :param dir_str: 'Fill' or 'Drain' (not used, need for strategy pattern)
    :return: always returns 0
    """
    return 0


def basic(dir_str: str):  # GRADING: BASIC_FILL
    """
    Basic fill behavior for the Lock where it will fill and drain at speed 1
    :param dir_str: 'Fill' or 'Drain' (not used, need for strategy pattern)
    :return: always returns 1
    """
    return 1


def fast(dir_str: str):  # GRADING: FAST_EMPTY
    """
    Fast empty behavior for the lock where it will fill at speed 1 and drain at speed 2
    :param dir_str: 'Fill' or 'Drain' to determine what speed to return
    :return: 1 if filling, 2 if draining
    """
    return 1 if dir_str == 'Fill' else 2
