def draw_road(length=0, orientation="horizontal"):
    """
    Prints a road of a given length

    Args:
        length: integer defining the length of a road
        orientation: string defining orientation of a road
                     values in [vertical, horizontal]
    """
    ALLOWED_ORIENTATIONS = ["vertical", "horizontal"]

    # Sanitizing parameter
    if length < 0:
        raise ValueError("length is negative")
    if length == 0:
        return
    if orientation not in ALLOWED_ORIENTATIONS:
        raise ValueError("orientation must be vertical or horizontal")

    # printing the road
    if orientation == "horizontal":
        draw_horizontal_road(length)
    elif orientation == "vertical":
        draw_vertical_road(length)
    else:
        raise ValueError("orientation must be vertical or horizontal")
    return

def draw_horizontal_road(length):
    for _ in range(length):
        print("-", end="")
    print()
    return

def draw_vertical_road(length):
    for _ in range(length):
        print("|")
    return
