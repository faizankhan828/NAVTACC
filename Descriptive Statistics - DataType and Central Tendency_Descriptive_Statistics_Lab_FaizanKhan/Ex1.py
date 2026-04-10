'''
Classifying Data Types
'''

#Part A — Fill the Classification Table
#Choices for Specific Type: Continuous | Discrete | Nominal | Ordinal | Binary

'''
1. Variable Quantitative / Qualitative Specific Type (fill in)
Temperature of a room (e.g. 22.5
°C)

Quantitative Continuous

2. Number of books a student owns Quantitative Discrete
3. Favourite programming language
(Python/R/Java) 

Qualitative Nominal

4. Customer satisfaction
(Poor/Fair/Good/Excellent)

Qualitative Ordinal

5. Did the model predict correctly?
(Yes/No)

Qualitative Binary

6. Distance run in a marathon (km) Quantitative Continuous
7. Number of errors in a program Quantitative Discrete
8. Student grade (A/B/C/D/F) Qualitative Ordinal
9. Country of birth Qualitative Nominal
10. Loan approved? (1=Yes, 0=No) Qualitative Binary

'''
# Part B - Assign and Label in Python

# 1. Room temperature — continuous quantitative
temperature = 22.5
temperature_type = "continuous"

# 2. Books owned — discrete quantitative
books = 7
books_type = "discrete"

# 3. Favourite language — nominal qualitative
fav_lang = 'Python'
fav_lang_type = "nominal"

#4. Satisfication rating -ordinal qualitative
satisfaction = 'Good'
satisfaction_type = "ordinal"

#5. Loan approved - binary qualitative
loan_approved = 1 
loan_type = "binary"

variables = [
('Temperature', temperature, temperature_type),
('Books owned', books, books_type),
('Fav language', fav_lang, fav_lang_type),
('Satisfaction', satisfaction, satisfaction_type),
('Loan approved', loan_approved, loan_type),
]

for nam, val, dtype in variables:
    print(f'{nam:<18}: {str (val):<10} -->({dtype})')