import time
import json
from fetch_courses import fetch_course_data

# Load the configuration from the JSON file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Get the interval from the configuration
interval = config.get("interval", 60)  # Default to 60 seconds if 'interval' is not defined

# Infinite loop to call the function at the configured interval
try:
    while True:
        fetch_course_data()
        print("Function executed successfully at:", time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
