# diagnostic.py
import sys
print("Running diagnostic check...")
print(f"Using Python executable: {sys.executable}")
print("-" * 20)

try:
    import requests
    print("✔ 'requests' library imported successfully.")
except ImportError as e:
    print(f"✖ Failed to import 'requests': {e}")

try:
    from rich.image import Image
    print("✔ 'rich.image' module imported successfully.")
except ImportError as e:
    print(f"✖ Failed to import 'rich.image': {e}")

print("-" * 20)
print("Diagnostic complete.")