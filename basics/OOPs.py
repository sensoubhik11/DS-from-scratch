import math

class Complex:
    # class variable
    number_type = "Complex Number Set"
    count = 0

    # Constructor
    def __init__(self, real=0, imag=0):
        # Instance member variables
        self.real = real
        self.imag = imag
        Complex.count += 1
  
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else: 
            return f"{self.real}-{-self.imag}i"

    # Overloading the + operator using the __add__ method    
    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    # This decorator allows you to define methods in a class that can be accessed
    # like attributes, without needing to call them explicitly as methods.
    @property
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imag**2)

class RealNumber(Complex):
    #Class Variable
    number_type = "Real Number Set"

    def __init__(self, real=0):
        # call parent constructor with imag=0
        super().__init__(real,0)

    def __str__(self):
        return f"{self.real}"


if __name__ == "__main__":
    print(Complex.number_type)
    c1 = Complex(3,-4)
    print(f"The magnitude of {c1} is {c1.magnitude}")
    c1 = c1 + Complex(1,1)
    print(f"After addition, the magnitude of {c1} is {c1.magnitude}")

    c2 = Complex(4, -3)
    print(f"c2 is {c2}")
    print(f"c1==c2") if c1 == c2 else print("c1!=c2")
    print(f"Total number of Complex numbers instantiated = {Complex.count}")

    print(RealNumber.number_type)
    r = RealNumber(2)
    print(r)
    print(f"Total number of Complex numbers instantiated = {Complex.count}")