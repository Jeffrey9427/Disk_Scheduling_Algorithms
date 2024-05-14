import random

cylinder_min = 0
cylinder_max = 4999
total_requests = 1000

requests = [random.randint(cylinder_min, cylinder_max) for _ in range(total_requests)]

# Write requests to a text file
with open("requests.txt", "w") as file:
    for req in requests:
        file.write(str(req) + "\n")

print("File 'requests.txt' has been created with 1,000 random cylinder requests.")
