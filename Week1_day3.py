
# Section 1.1 - Variables and Types

score = 85
average = 85.5
passed: bool   = True
print("Values  :", score, average, passed)
print("Types   :", type(score), type(average), type(passed))

# Section 1.2 - Arithmetic and Expressions

result1 = (10 + 3) * 2 - 4
int_div  = 17 // 5
remainder = 17 % 5
power    = 2 ** 5
print("(10 + 3) * 2 - 4   :", result1)
print("17 // 5            :", int_div)
print("17 % 5             :", remainder)
print("2 ** 5             :", power)

# ============================================================
# Section 1.3 - Comparison and Logical Operators
# ============================================================
a, b = 10, 20
print("a < b              :", a < b)
print("a == 10 and b == 20:", a == 10 and b == 20)
print("not (a > b)        :", not (a > b))


# Section 1.4 - Complex Expressions

expr1 = (5 + 3) * 2 - 4 ** 2 // 3
expr2 = 10 % 3 + 2 ** 3 - 1
x, y, z = 5, 3, 2
expr3 = (x + y) * z - x // y
print("(5+3)*2 - 4**2//3  :", expr1)
print("10%3 + 2**3 - 1    :", expr2)
print("(x+y)*z - x//y     :", expr3)

# Section 1.5 - Operator Precedence

no_parens  = 2 + 3 * 4 - 1        
with_parens = (2 + 3) * (4 - 1)   
print("2 + 3 * 4 - 1      :", no_parens,  " (no parentheses)")
print("(2 + 3) * (4 - 1)  :", with_parens, "(with parentheses)")

# Section 1.6 - Type Conversion Practice
print("int(True)          :", int(True))
print("int(False)         :", int(False))
print("float(100)         :", float(100))
print("int(3.14)          :", int(3.14), " (decimal part truncated)")