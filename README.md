# Linux-Scripting787
Test Scripts for Linux Administration

Prerequisites

Install Required Packages:

Install psutil for memory monitoring:

bash


sudo pip3 install psutil


Install notify2 for popup notifications:

bash


sudo pip3 install notify2


Ensure libnotify-bin is installed (for notifications):

bash


sudo apt install libnotify-bin  # Debian/Ubuntu-based systems
sudo dnf install libnotify      # Fedora-based systems


Permissions:

The script needs write access to /var/log/ram_usage_alerts.log. You can change LOG_FILE to a user-writable location (e.g., ~/ram_usage_alerts.log) if preferred.


Setting Up the Cron Job

Make the Script Executable:
Save the script as ram_monitor.py and make it executable:

bash


chmod +x ram_monitor.py


Edit Crontab:
Open the cron configuration file:

bash


crontab -e


Add Cron Entry:
Run the script every 5 minutes (adjust as needed):

bash


*/5 * * * * /usr/bin/python3 /path/to/ram_monitor.py



Replace /path/to/ram_monitor.py with the full path to your script.



Ensure the shebang (#!/usr/bin/env python3) is at the top of the script.


How It Works

RAM Check: Uses psutil.virtual_memory() to get current RAM usage.



Threshold: Triggers an alert if usage exceeds 80% (configurable via THRESHOLD_PERCENT).



Popup: Displays a desktop notification using notify2.



Logging: Records alerts to /var/log/ram_usage_alerts.log.



Cron: Runs periodically (e.g., every 5 minutes) via cron.


Notes

Desktop Environment: The popup requires a graphical desktop environment with a notification daemon (e.g., GNOME, KDE). It won’t work on a headless server without modification.



Single Execution: The script runs once per cron call. If you want continuous monitoring, you’d need to modify it to loop



