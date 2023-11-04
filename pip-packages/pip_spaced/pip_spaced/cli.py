"""Console script for pip_spaced."""
import argparse
import sys


def main():
    """Console script for pip_spaced."""
    parser = argparse.ArgumentParser(description='Add two numbers together.')
    parser.add_argument('numbers', nargs='2', type=int, help="Two numbers to add")
    args = parser.parse_args()

    result = add_numbers(*args.numbers)
    print(f"The result is {result}")


if __name__ == "__main__":
    main()

