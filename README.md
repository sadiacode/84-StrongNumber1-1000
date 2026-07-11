# Strong Number From 1-1000
## Description
This project is a Python program that demonstrates the use of while loop in Python. A while loop repeatedly executes a block of code as long as **a specified condition is True**. It is useful when the number of iterations is not fixed or depends on a condition.
## Syntax
```python
while condition:
   # Code to execute if condition is True
```
## Concepts Used
- Variables
- while Loop
- Comparison Operators
- Increment and Decrement
- Modulus Operator(%)
- Floor Division(//)
- if Condition
## Technologies Used
- Pycharm
- Python 3
## Working of the Code
1. The program starts checking numbers from 1 to 1000.
2. For each number, it stores the original value in original and creates a copy in temp.
3. A variable sum is initialized to 0 to store the sum of the factorials of the digits.
4. A while loop extracts each digit of the number one by one using the modulus (%) operator.
5. For every extracted digit, another while loop calculates its factorial.
6. The factorial of each digit is added to sum.
7. After processing a digit, the last digit is removed from temp using floor division (//).
8. When all digits have been processed, the program compares sum with original.
9. If both values are equal, the number is a Strong Number and is printed.
10. The program repeats the same process for every number from 1 to 1000.
## How to run
1. Clone the repository.
2. Open the project in pycharm.
3. Run the 'main.py' file.
4. View the result.
## Sample Output
```text

1
2
145
```
## Author
- Sadia
- Github: [sadiacode](https://github.com/sadiacode)
