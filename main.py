"""Classwork for calculating the rotation of a ball."""
from math import pi

CIRCLE_DEGREES = 360


def degree(radius: float, acceleration: float, time: float, velocity: float = 0) -> float:
    """Rotation of the ball.

    Args:
        radius: [float] - The ball radius.
        acceleration: [float] - The ball acceleration.
        time: [float] - The time.
        velocity: [float] - The ball start velocity.

    Returns:
        float - Rotation of the ball.

    Raises:
        ValueError: - if time or radius is inappropriate.
    """
    if radius <= 0 or time < 0:
        raise ValueError('Radius or time has wrong value!')
    circumference = 2 * pi * radius
    distance = velocity * time + (acceleration * (time ** 2)) / 2
    rotation = (distance % circumference) / circumference * CIRCLE_DEGREES
    return round(rotation, 2)
