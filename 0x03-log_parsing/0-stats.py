#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
import signal


# Initialize metrics
file_sizes = []
status_codes = {}

# Helper function to print statistics
def print_statistics():
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        line = line.strip()
        # Parse the line using a simple split method
        parts = line.split()
        if len(parts) >= 9:
            ip_address = parts[0]
            date = parts[3][1:]  # Remove the leading '[' from the date
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Accumulate file sizes
            file_sizes.append(file_size)

            # Count status codes
            if status_code.isdigit():
                status_codes[int(status_code)] = status_codes.get(int(status_code), 0) + 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)
