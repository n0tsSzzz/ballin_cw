"""rolling_stone module."""

from math import pi

DEGREES_IN_CIRCLE = 360


def rolling_stone_angle(
    radius: float,
    acceleration: float,
    time: float,
    velocity: float = 0,
) -> float:
    """
    Get the sum of two values.

    Args:
        radius: float - radius of stone
        acceleration: float - acceleration of stone
        time: float - time stone spent while rolled
        velocity: float - initial velocity of stone, 0 by default

    Returns:
        float - an angle of stone's starting point, rounded to 2 digits after point,
            compared to its initial position anticlockwise

    Raises:
        ValueError: - if time or radius is inappropriate
    """
    if radius <= 0 or time < 0:
        raise ValueError('Radius or time has wrong value!')
    full_path = velocity * time + acceleration * time ** 2 / 2
    stone_length = 2 * pi * radius
    coordinate = full_path % stone_length
    return round(coordinate / stone_length * DEGREES_IN_CIRCLE, 2)
