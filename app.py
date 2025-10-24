import sys
import os

# --- This is the key part ---
# We add our 'lib' folder to the Python path
# so we can import modules from it.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
# ---------------------------

# Now we can import from our subtree package
from shared_utils.helpers import greet

def main():
    print("Main app is running...")
    message = greet("Alice")
    print(message)

if __name__ == "__main__":
    main()
