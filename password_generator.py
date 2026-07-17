#!/usr/bin/env python3
"""Generate cryptographically secure random passwords."""

from __future__ import annotations

import argparse
import secrets
import string

CHARSET = string.ascii_letters + string.digits + string.punctuation
MIN_CLI_LENGTH = 8


def generate_password(length: int) -> str:
    """Return a cryptographically secure random password.

    Args:
        length: Number of characters to generate. Must be greater than zero.

    Raises:
        TypeError: If ``length`` is not an integer.
        ValueError: If ``length`` is less than one.
    """
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length < 1:
        raise ValueError("length must be greater than zero")

    return "".join(secrets.choice(CHARSET) for _ in range(length))


def password_length(value: str) -> int:
    """Validate password length supplied through the command line."""
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("length must be an integer") from exc

    if parsed < MIN_CLI_LENGTH:
        raise argparse.ArgumentTypeError(
            f"length must be at least {MIN_CLI_LENGTH} characters"
        )

    return parsed


def build_parser() -> argparse.ArgumentParser:
    """Create and return the command-line parser."""
    parser = argparse.ArgumentParser(
        description="Generate a cryptographically secure random password."
    )
    parser.add_argument(
        "-l",
        "--length",
        type=password_length,
        default=16,
        help=f"password length (minimum: {MIN_CLI_LENGTH}, default: 16)",
    )
    return parser


def main() -> int:
    """Run the command-line interface."""
    args = build_parser().parse_args()
    print(generate_password(args.length))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
