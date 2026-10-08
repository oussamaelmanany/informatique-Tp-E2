class operation:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def str(self):
        self.num1 = str(self.num1)
        self.num2 = str(self.num2)
    def __add__(self,other):
        return self.num1 + other.num1, self.num2 + other.num2
    def __sub__(self,other):
        return self.num1 - other.num1, self.num2 - other.num2
    def __mul__(self,other):
        return self.num1 * other.num1, self.num2 * other.num2
    def __truediv__(self,other):
        return self.num1 / other.num1, self.num2 / other.num2
    def __gt__(self,other):
        return self.num1 > other.num1, self.num2 > other.num2
    def __lt__(self,other):
        return self.num1 < other.num1, self.num2 < other.num2
    def __le__(self,other):
        return self.num1 <= other.num1, self.num2 <= other.num2
    def __ge__(self,other):
        return self.num1 >= other.num1, self.num2 >= other.num2
    def __eq__(self,other):
        return self.num1 == other.num1, self.num2 == other.num2
    def __ne__(self,other):
        return self.num1 != other.num1, self.num2 != other.num2