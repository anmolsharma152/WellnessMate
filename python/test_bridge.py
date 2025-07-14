"""
Test script to verify the Rust-Python bridge is working correctly.
"""
import sys

def test_function(name: str) -> str:
    """A simple test function that returns a greeting."""
    return f"Hello from Python, {name}! The Rust-Python bridge is working! 🎉"

if __name__ == "__main__":
    # Get name from command line arguments or use default
    name = sys.argv[1] if len(sys.argv) > 1 else "Tester"
    print(test_function(name))
