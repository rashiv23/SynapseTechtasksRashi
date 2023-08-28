"""
Create a Python function that takes two numbers, start (inclusive) and end (exclusive), as input.
These numbers represent a range. The function should check if each number in the range is a prime
number or not. If a number is prime, the function should return its binary representation. If a
number is not prime, the function should return an array containing all the divisors of that number.
Finally, the function should return a dictionary with each number in the range as a key and the value
as either the binary representation (if the number is prime) or the array of divisors (if the number is
not prime).
"""

def primeNumber(num):
    if num > 1:  
        for i in range (2, num):  
            if (num % i) == 0:  
                return False
        else:  
            return True  

def findFactors(num):
    factors = []
    for i in range(1, num):
        if (num % i == 0):
            factors.append(i)
    return factors
    
def finalDict(start, end):
    result = {}
    for num in range(start, end):
        if primeNumber(num):
            result[num] = bin(num)[2:]
        else:
            result[num] = findFactors(num)
    return result


num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
dictOut = finalDict(num1, num2)
print(dictOut)

