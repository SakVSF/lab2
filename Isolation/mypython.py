# memory_hog.py

import time

# Define an empty list to hold the memory "hog"
memory_hog = []

while True:
    # Allocate chunks of 10 MB
    memory_hog.append(' ' * 10_000_000)  # 10 million spaces, roughly 10 MB
    print(f"Allocated ~{len(memory_hog) * 10} MB")

    # Wait a bit between allocations
    time.sleep(1)