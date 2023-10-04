"""Module for testing test function."""
import pytest

from main import degree

THE_DATA = (
    (5, 12, 7, 3, (9.63)),
    (1, 2, 3, 4, (123.21)),
    (1, 3, 0, 0, (0)),
    (234, 123, 666, 90, (127.29)),
)

THE_DATA_FALIURE = (
    (0, 0, 0, 0, (pytest.raises(ValueError))),
    (-5, 4, 5, 6, (pytest.raises(ValueError))),
)


@pytest.mark.parametrize(
    'test_radius, test_acceleration, test_time, test_velocity, expected',
    THE_DATA,
)
def test_degree(
    test_radius: float,
    test_acceleration: float,
    test_time: float,
    test_velocity: float,
    expected: tuple,
) -> None:
    """Test degree function.

    Args:
        test_radius: [float] - The radius.
        test_acceleration: [float] - The acceleration.
        test_time: [float] - The time.
        test_velocity: [float] - The start velocity.
        expected: [tuple[float]] - expected result of function.

    Asserts:
        True if test_degree returns expected answer.
    """
    assert degree(test_radius, test_acceleration, test_time, test_velocity) == expected


@pytest.mark.parametrize(
    'test_radius, test_acceleration, test_time, test_velocity, expected',
    THE_DATA_FALIURE,
)
def test_degree_failure(
    test_radius: float,
    test_acceleration: float,
    test_time: float,
    test_velocity: float,
    expected: tuple,
) -> None:
    """Test degree function.

    Args:
        test_radius: [float] - The radius.
        test_acceleration: [float] - The acceleration.
        test_time: [float] - The time.
        test_velocity: [float] - The start velocity.
        expected: [tuple[float]] - expected result of function.

    Asserts:
        True if test_degree returns expected answer.
    """
    with expected:
        assert degree(test_radius, test_acceleration, test_time, test_velocity) is not None
