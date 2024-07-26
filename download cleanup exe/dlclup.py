import os
import time
from datetime import datetime, timedelta

# Path to your downloads folder
downloads_folder = "C:\\Users\\meeee\\Downloads"

# Get the current time
now = time.time()

# Set the time threshold for 365 days ago
time_threshold = now - (365 * 24 * 60 * 60)

# Iterate over the files in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)

    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Get the last accessed time of the file
        last_accessed_time = os.path.getatime(file_path)
        
        # If the file has not been accessed in over 365 days, delete it
        if last_accessed_time < time_threshold:
            print(f"Deleting {file_path}...")
            os.remove(file_path)

print("Done!")
