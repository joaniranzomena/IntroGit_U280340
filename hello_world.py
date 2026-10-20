# My first file tracked by Git
# Author: Tu Nombre

def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

def farewell(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}! See you next commit."

def show_footer():
    """Print a footer with course information."""
    print("---")
    print("© 2026 - Introduction to Programming, UPF")

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    show_footer()
    