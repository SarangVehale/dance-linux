import subprocess
import sys
import os

# Set the path to the bundled Toybox binary
TOYBOX_PATH = os.path.join(os.path.dirname(__file__), 'toybox', 'toybox')

def run_toybox_command(command):
    """Run a Toybox command or fallback to system command."""
    try:
        # Check if the embedded Toybox binary exists
        if os.path.exists(TOYBOX_PATH):
            command = f"{TOYBOX_PATH} {command}"
        else:
            print("Toybox binary not found, falling back to system command.")
        return subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

