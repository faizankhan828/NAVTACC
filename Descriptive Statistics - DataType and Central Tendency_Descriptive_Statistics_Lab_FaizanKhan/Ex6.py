'''
Challenge: Full Analysis Pipeline
End-to-End Student Dataset — No Scaffolding

'''


students = [
# (name, age, score, grade, city, passed)
('Alice', 20, 88.5, 'A', 'Lahore', 1),
('Bob', 22, 73.0, 'B', 'Karachi', 1),
('Carol', 21, 55.5, 'C', 'Lahore', 0),
('Dave', 23, 91.0, 'A', 'Islamabad', 1),
('Eva', 20, 62.5, 'C', 'Karachi', 0),
('Frank', 24, 78.0, 'B', 'Lahore', 1),
('Grace', 22, 95.5, 'A', 'Karachi', 1),
('Hasan', 21, 47.0, 'D', 'Peshawar', 0),
('Iman', 20, 83.5, 'B', 'Lahore', 1),
('Jack', 23, 70.0, 'B', 'Islamabad', 1),
]

'''
Task 1 — Data Type for Every Column

For each column write the specific type and a one-sentence justification.
'''

print("\t\t======Task 1=======")
print("Name: str")
print("Age: int")
print("Score: float")
print("Grade: str")
print("City: str")
print("Passed: int (0 or 1)")

'''''''''''
Task 2 — Scores: Mean, Median, Mode
Extract scores into a list, then use your functions from Exercise 5.
'''
print( "\t\t======Task 2=======")
scores = [s[2] for s in students]
print(f'Scores: {scores}')
def my_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)
def my_median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 1: 
        return s[mid] 
    else: 
        return (s[mid - 1] + s[mid]) / 2 
def my_mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return sorted(modes), max_count
print(f'Mean score: {my_mean(scores):.2f}')
print(f'Median score: {my_median(scores):.2f}')
print(f'Mode score: {my_mode(scores)[0][0]:.2f} (appears {my_mode(scores)[1]} times)')

'''
Task 3 — City Frequency Table
Count students per city. Print sorted from most to least common.

'''
print( "\t\t======Task 3=======")
city_freq = {}
for s in students:
    city = s[4]
    city_freq[city] = city_freq.get(city, 0) + 1
ranked = sorted(city_freq.items(), key=lambda x: x[1], reverse=True)
print(f"{'City':<12}| Count")
print('-' * 20)
for city, cnt in ranked: 
 print(f'{city:<12}| {cnt}')


'''
Task 4 — Pass Rate & Conditional Mean Score
Overall pass rate (%). Average score for passed students vs failed students.
'''
print( "\t \t======Task 4=======")
total = len(students)
passed = sum(s[5] for s in students)
failed = total - passed
pass_rate = passed / total * 100
print(f'Total students: {total}')
print(f'Passed: {passed} ({pass_rate:.1f}%)')
passed_scores = [s[2] for s in students if s[5] == 1]
failed_scores = [s[2] for s in students if s[5] == 0]
print(f'Average score (passed): {my_mean(passed_scores):.2f}') 
print(f'Average score (failed): {my_mean(failed_scores):.2f}')

