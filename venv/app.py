""" Implement a class for fractions that supports
    addition, subtraction, multiplication, division and check if
    equal, not equal, less than, less than or equal to,
    greater thangreater than or equal to

    author: Fatih IZGI
    date: 09-Feb-2020
    version: python 3.6.9
"""

class Fraction:
    """ Support addition, subtraction, multiplication, division
        and checking the equation of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator
        """

        if denom == 0.0:
            raise ZeroDivisionError

        self.num: float = num
        self.denom: float = denom

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{float(self.num)}/{float(self.denom)}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        new_self_num: float = self.num * other.denom
        new_other_num: float = other.num * self.denom

        final_num: float = new_self_num + new_other_num
        final_denom: float = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def __sub__(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        new_self_num: float = self.num * other.denom
        new_other_num: float = other.num * self.denom

        final_num: float = new_self_num - new_other_num
        final_denom: float = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def __mul__(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        final_num: float = self.num * other.num
        final_denom: float = self.denom * other.denom

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        final_num: float = self.num * other.denom
        final_denom: float = self.denom * other.num

        final_fraction: Fraction = Fraction(final_num, final_denom)

        return final_fraction

    def __eq__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """
        if self.num * other.denom == self.denom * other.num:
            return True
        else:
            return False # the fractions are not equal

    def __ne__(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are not equivalent """
        if self.num * other.denom == self.denom * other.num:
            return False
        else:
            return True # the fractions are not equal

    def __lt__(self, other: "Fraction") -> bool:
        """ return True/False if the first fraction is less than the second fraction """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 < f2:
            return True
        else:
            return False

    def __le__(self, other: "Fraction") -> bool:
        """ return True/False if the first fraction is less than or equal to the second fraction """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 <= f2:
            return True
        else:
            return False

    def __gt__(self, other: "Fraction") -> bool:
        """ return True/False if the first fraction is greater than the second fraction """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 > f2:
            return True
        else:
            return False

    def __ge__(self, other: "Fraction") -> bool:
        """ return True/False if the first fraction is greater than or equal to the second fraction """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 >= f2:
            return True
        else:
            return False

    def simplify(self) -> "Fraction":
        """ Simplify fractions by finding the Greatest Common Factor (GCF)
            and then dividing the number and denominator.
        """

        def gcd(a, b): # a function to find the gcd
            while b != 0:
                (a, b) = (b, a%b)
            return a

        gcf: int = gcd(int(self.num), int(self.denom))

        start: int = min(abs(int(self.num)), abs(int(self.denom)))

        for number in range(start, 2, -1):
            if number % gcf:
                return Fraction(float(self.num / gcf), float(self.denom / gcf))

        return Fraction(float(self.num), float(self.denom))


def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction(count: int) -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        num = get_number(f"Enter a numerator for Fraction {count}: ")

        while True:
            denom = get_number(f"Enter a denominator for Fraction {count}: ")
            if denom != 0:
                break
            else:
                print("Denominator cannot be 0. Please enter another number.")

        fraction: Fraction = Fraction(num, denom)

        return fraction


def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    result: Optional[Union[Fraction, bool]]  # just define the type of result, don't set a value
    okay: bool = True # a variable to decide printing the result

    if operator == '+':
        result = f1 + f2
    elif operator == "-":
        result = f1 - f2
    elif operator == "*":
        result = f1 * f2
    elif operator == "/":
        result = f1 / f2
    elif operator == "==":
        result = f1 == f2
    elif operator == "!=":
        result = f1 != f2
    elif operator == "<":
        result = f1 < f2
    elif operator == "<=":
        result = f1 <= f2
    elif operator == ">":
        result = f1 > f2
    elif operator == ">=":
        result = f1 >= f2
    else:
        print(f"Error: '{operator}' is an unrecognized operator")
        okay = False # unrecognized operator --> do not print the result

    if okay:
        print(f"{f1} {operator} {f2} ---> {result}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction(1)
    operator: str = input("Operation (+, -, *, /, ==, !=, <, <=, >, >=): ")
    f2: Fraction = get_fraction(2)

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError:
        print("Zero Division Error!")


if __name__ == '__main__':
    main()
