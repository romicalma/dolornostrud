from datetime import datetime

# Start date is the beginning of the year 2024
start_date = datetime(2024, 1, 1)

# Current date
current_date = datetime.now()

# Calculate the difference between dates
difference = current_date - start_date

# Get the total number of days elapsed
total_days_elapsed = difference.days

print(f"Total number of days elapsed since the beginning of 2024: {total_days_elapsed}")
