'''
Discrete Variables — Frequency & Distribution
'''

#Part A — Build a Frequency Dictionary

goals = [2, 0, 1, 3, 2, 1, 4, 2, 0, 1,
3, 2, 1, 0, 2, 3, 1, 2, 4, 1]
freq = {}
for g in goals:
	if g in freq: 
		freq[g] += 1 
	else:
		freq[g] = 1
freq = dict(sorted(freq.items())) 
print(f"{'Goals':>6} | {'Count':>5} | Bar")
print('-' * 32)
for val, cnt in freq.items():
 print(f'{val:>6} | {cnt:>5} | {chr(9608) * cnt}')


#Part B — Relative & Cumulative Frequency 
total = len(goals)
cumulative = 0.0

print(f"{'Goals':>6} | {'Count':>5} | {'Rel.Freq':>9} | {'Cum.Freq':>9}")
print('-' * 42)
for val, cnt in freq.items():
	rel = cnt/total
	cumulative += rel
	print(f'{val:>6} | {cnt:>5} | {rel:>9.3f} | {cumulative:>9.3f}')

#Part C — Summary Statistics

most_common = max(freq, key=lambda k: freq[k])
least_common = min(freq, key=lambda k: freq[k])
print(f'Most common goals : {most_common} ({freq[most_common]} times)')
print(f'Least common goals : {least_common} ({freq[least_common]} times)')
high_scoring = sum(1 for g in goals if g > 2)
print (f'Matches with >2 goals : {high_scoring} ({high_scoring/total*100:.0f}%)')