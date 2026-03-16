'''
Continuous Variables --Heights Deep Dive
'''

#Part A - Min, Max and Range Without Built-ins
#Find the smallest and largest values using a loop. Do NOT use min() or max().
heights = [158.4, 172.0, 165.5, 180.2, 155.8, 169.3, 174.6, 160.1, 178.9, 163.7, 171.4, 156.2]

smallest = heights[0]
largest = heights[0]

for h in heights:
    if h < smallest:
        smallest = h
    if h > largest:
        largest = h
data_range = largest - smallest

print(f"Smallest height: {smallest} cm")
print(f"Largest height: {largest} cm")
print(f"Range of heights: {data_range} cm")


#Part B — Count Students in a Height Band
#How many students have a height between 160 cm and 175 cm (inclusive)?

count = 0
for h in heights:
    if 160 <= h <= 175:
        count += 1

pct = count / len(heights) * 100
print(f'Students 160-175 cm : {count}')
print(f'Percentage : {pct:.1f}%')


#Part C - Part C — Min-Max Normalisation
#Scale every value to [0, 1] using: n = (x - min) / (max - min)

normalized = []
for h in heights:
    n = (h - smallest) / (largest - smallest)
    normalized.append(round(n, 3))

print('Original :', heights)
print('Normalised:', normalized)

# Verify first value manually
check = round((158.4 - 155.8) / (180.2 - 155.8), 3)
print(f'Check [0] = {check} matches? {check == normalized[0]}')