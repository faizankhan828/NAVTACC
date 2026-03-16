'''
Mean, Median & Mode from Scratch

'''

#Part A — my_mean()

salaries = [45, 52, 48, 55, 45, 60, 48, 72, 45, 58, 300]

def my_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

print(f'Mean: ${my_mean(salaries):.2f}K')

#Part B — my_median()
def my_median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 1: # odd count
        return s[mid] # single middle index
    else: # even count
        return (s[mid - 1] + s[mid]) / 2 # average of mid-1 and mid

print(f'Sorted : {sorted(salaries)}')
print(f'Median : ${my_median(salaries):.2f}K')

#Part C — my_mode() (handles ties)
def my_mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return sorted(modes), max_count
modes, cnt = my_mode(salaries)
print(f'Mode : {modes} (appears {cnt} times)')


#Part D — Compare All Three & the Outlier Effect

print('=' * 52)
print(f'Dataset : {salaries}')
print('=' * 52)
print(f'Mean : ${my_mean(salaries):.2f}K <- inflated by CEO salary')
print(f'Median : ${my_median(salaries):.2f}K <- resistant to outlier')
print(f'Mode : ${my_mode(salaries)[0][0]:.2f}K <- most common salary')
print('=' * 52)
clean = [s for s in salaries if s < 200]
print(f'Without CEO : {clean}')
print(f'Mean (clean) : ${my_mean(clean):.2f}K')
print(f'Median (clean) : ${my_median(clean):.2f}K')
print(f'Outlier boosted mean by : ${my_mean(salaries)-my_mean(clean):.2f}K')