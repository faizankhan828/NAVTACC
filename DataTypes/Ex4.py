'''
Nominal · Ordinal · Binary — Pure Python

'''


cities = ['Lahore','Karachi','Islamabad','Lahore','Karachi',
'Karachi','Lahore','Peshawar','Islamabad','Lahore']
city_freq = {}
for city in cities: 
	city_freq[city] = city_freq.get(city, 0) + 1
ranked = sorted(city_freq.items(), key=lambda x: x[1], reverse=True)
print(f"{'City':<12}| Count")
print('-' * 20)
for city, cnt in ranked: 
 print(f'{city:<12}| {cnt}')
print(f'Most popular city: {ranked[0][0]}')


#Part B - Oridnal Sort by Rank

responses = ['Good','Excellent','Poor','Fair','Good',
'Excellent','Poor','Good','Fair','Excellent']

rank = {'Poor': 1, 'Fair': 2, 'Good': 3, 'Excellent': 4}
sorted_r = sorted(responses, key=lambda r: rank[r])
print('Sorted low->high:', sorted_r)
level_freq = {}
for r in responses:
 level_freq[r] = level_freq.get(r, 0) + 1
print(f"\n{'Level':<12}| Count | Rank")
print('-' * 28)
for level in sorted(rank, key=lambda k: rank[k]):
    print(f"{level:<12}| {level_freq.get(level,0):>5} | {rank[level]}")


#Part C -- Binary: Pass / Fail Statistics
results = [1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1] 
total = len(results)
passed = sum(results) 
failed = total - passed
rate = passed / total * 100
print(f'Total : {total}')
print(f'Passed : {passed} ({rate:.1f}%)')
print(f'Failed : {failed} ({100-rate:.1f}%)')
print(f'Pass bar: {chr(9608)*passed}')
print(f'Fail bar: {chr(9617)*failed}')    