# Square a number.
squared = lambda x: x*x
print(squared(2))

# Sum three numbers.
add = lambda a, b, c: a+b+c
print(add(1,2,3))

# Divide two numbers if the denominator is different than 0. 
div = lambda num, den: num / den if (den != 0) else 0
print(div(10,5))
print(div(10,0))

# Create a list of squared numbers.
print([squared(x) for x in range(10)])

# Replace the dashes in a word for a whitespace.
school_dash = ["calculus", "philosophy", "art-history", "computer-science"]
school_space = [(lambda x: x.replace("-"," "))(x) for x in school_dash]
print(school_space)