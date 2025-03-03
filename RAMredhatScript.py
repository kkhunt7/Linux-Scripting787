#!/usr/bin/env python3

import psutil
import subprocess
import time

# Threshold for RAM usage alert (in percentage)
RAM_THRESHOLD = 80

def get_ram_usage():
    """Get current RAM usage percentage"""
    memory = psutil.virtual_memory()
    return memory.percent

def show_alert(usage):
    """Display popup alert using zenity"""
    message = f"Warning: RAM Usage at {usage:.1f}%\nThreshold exceeded ({RAM_THRESHOLD}%)"
    try:
        subprocess.run([
            'zenity',
            '--warning',
            '--title=RAM Usage Alert',
            '--text=' + message,
            '--width=300',
            '--height=100'
        ], check=True)
    except subprocess.CalledProcessError:
        # If zenity fails, print to console as fallback
        print(message)

def main():
    # Get current RAM usage
    ram_usage = get_ram_usage()
    
    # Check if usage exceeds threshold
    if ram_usage >= RAM_THRESHOLD:
        show_alert(ram_usage)

if __name__ == "__main__":
    main()
