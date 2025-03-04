#!/usr/bin/env python3

import psutil
import notify2
import time
import os

# Configuration
THRESHOLD_PERCENT = 80  # Alert if RAM usage exceeds 80%
LOG_FILE = "/var/log/ram_usage_alerts.log"

def log_message(message):
    """Log the alert to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

def check_ram_usage():
    """Check RAM usage and trigger alert if above threshold."""
    # Get RAM usage stats
    memory = psutil.virtual_memory()
    usage_percent = memory.percent
    
    if usage_percent >= THRESHOLD_PERCENT:
        # Initialize notification system
        notify2.init("RAM Monitor")
        
        # Create and show popup notification
        message = f"High RAM Usage Detected!\nCurrent Usage: {usage_percent}%"
        notification = notify2.Notification("RAM Usage Alert", message, "dialog-warning")
        notification.set_urgency(notify2.URGENCY_CRITICAL)
        notification.show()
        
        # Log the event
        log_message(message)
        
        # Small delay to prevent multiple rapid notifications (if running manually)
        time.sleep(5)

if __name__ == "__main__":
    # Ensure log file directory exists and is writable
    log_dir = os.path.dirname(LOG
