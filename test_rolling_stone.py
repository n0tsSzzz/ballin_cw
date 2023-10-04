"""A module for testing rolling_stone."""

from typing import Any

import pytest

from rolling_stone import rolling_stone_angle

test_cases = (
    (
        5,
        15,
        60,
        0,
        157.21,
    ),
    (
        1,
        5,
        1,
        1,
        200.54,
    ),
    (
        5,
        -5,
        10,
        -5,
        162.25,
    ),
)

test_cases_failure = (
    (
        0,
        5,
        24,
        1,
        pytest.raises(ValueError),
    ),
    (
        5,
        5,
        -5,
        5,
        pytest.raises(ValueError),
    ),
)


@pytest.mark.parametrize('radius, acceleration, time, velocity, expected', test_cases)
def test_rolling_stone_angle(
    radius: float,
    acceleration: float,
    time: float,
    velocity: float,
    expected: float,
) -> None:
    """Test rolling_stone_angle function with test_cases.

    Args:
        radius: float - radius of stone
        acceleration: float - acceleration of stone
        time: float - time stone spent while rolled
        velocity: float - initial velocity of stone, 0 by default
        expected: float - expected result

    Asserts:
        True if rolling_stone_angle returns expected answer.
    """
    assert rolling_stone_angle(radius, acceleration, time, velocity) == expected


@pytest.mark.parametrize('radius, acceleration, time, velocity, expected', test_cases_failure)
def test_rolling_stone_angle_failure(
    radius: float,
    acceleration: float,
    time: float,
    velocity: float,
    expected: Any,
) -> None:
    """Test rolling_stone_angle function with test_cases_failure.

    Args:
        radius: float - radius of stone
        acceleration: float - acceleration of stone
        time: float - time stone spent while rolled
        velocity: float - initial velocity of stone, 0 by default
        expected: ValueError - expected error

    Asserts:
        True if rolling_stone_angles returns expected answer.
    """
    with expected:
        assert rolling_stone_angle(radius, acceleration, time, velocity) is not None
