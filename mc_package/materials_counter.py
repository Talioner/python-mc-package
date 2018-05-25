def count_tiles(x, y, s):
    """Returns amount of tiles needed for the specified room size."""
    result = float(x) * float(y) / float(s)
    return result


def count_time(s, v):
    """Returns time needed to reach the destination,
    having distance and speed from input.
    """
    time = float(s) / float(v)
    return time
