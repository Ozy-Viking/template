"""
main module

Author: Zack Hankin
Started: 23/02/2023
"""
from __future__ import annotations


def square(x: float) -> float:
    """
    Squares a given number.

    Args:
        x (float): A number to square.

    Returns:
        Squared number.
    """
    return x**2


def main() -> int:
    """
    Main function for module.

    Returns:
        Exit code
    """
    for idx in range(50):
        square(idx)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
