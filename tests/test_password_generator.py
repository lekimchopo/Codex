"""Tests for the secure password generator."""

import argparse
import unittest

from password_generator import CHARSET, generate_password, password_length


class GeneratePasswordTests(unittest.TestCase):
    def test_returns_requested_length(self) -> None:
        self.assertEqual(len(generate_password(32)), 32)

    def test_uses_only_supported_characters(self) -> None:
        password = generate_password(256)
        self.assertTrue(set(password).issubset(set(CHARSET)))

    def test_repeated_calls_do_not_return_the_same_value(self) -> None:
        generated = {generate_password(24) for _ in range(20)}
        self.assertEqual(len(generated), 20)

    def test_rejects_zero_and_negative_lengths(self) -> None:
        for invalid_length in (0, -1, -20):
            with self.subTest(invalid_length=invalid_length):
                with self.assertRaises(ValueError):
                    generate_password(invalid_length)

    def test_rejects_non_integer_lengths(self) -> None:
        for invalid_length in (True, 12.5, "16", None):
            with self.subTest(invalid_length=invalid_length):
                with self.assertRaises(TypeError):
                    generate_password(invalid_length)  # type: ignore[arg-type]


class PasswordLengthValidatorTests(unittest.TestCase):
    def test_accepts_valid_cli_length(self) -> None:
        self.assertEqual(password_length("20"), 20)

    def test_rejects_short_cli_length(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            password_length("7")

    def test_rejects_non_numeric_cli_length(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            password_length("twenty")


if __name__ == "__main__":
    unittest.main()
