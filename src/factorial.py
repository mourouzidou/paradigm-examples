# create a class that will calculate the factorial of a number

class Factorial_Calculation:
    def __init__(self):
        pass
    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        elif n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        else:
            return n * self.factorial(n - 1)
        
    def calculate(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return self.factorial(n)

if __name__ == "__main__":
    fc = Factorial_Calculation()
    
    print(fc.calculate(5))  # Output for n = : 120
