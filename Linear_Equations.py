#  File: LinearEquations.py
#  A program that creates a class, Linear Equations, and creates and perform operations with linear equations.


class LinearEquation():

    def __init__(self, m, b):
        self.m = m
        self.b = b

    def showEq(self):
        if self.m < 0 and self.b < 0:
            return ("- " + str(abs(self.m)) + "x - " + str(abs(self.b)))
        elif self.m > 0 and self.b > 0:
            return (str(self.m) + "x + " + str(self.b))

        elif self.m < 0 and self.b > 0:
            return ("- " + str(abs(self.m)) + "x + " + str(abs(self.b)))
        elif self.m > 0 and self.b < 0:
            return (str(abs(self.m)) + "x - " + str(abs(self.b)))

        elif self.m == 0 and self.b == 0:
            return (0)

        elif self.m == 0 and self.b < 0:
            return ("- " + str(abs(self.b)))
        elif self.m == 0 and self. b > 0:
            return (str(abs(self.b)))

        elif self.m > 0 and self.b == 0:
            return (str(abs(self.m)) + "x")
        elif self.m < 0 and self.b == 0:
            return ("- " + str(abs(self.m)) + "x")


    def evaluate(self, x):
        return (self.m * x + self.b)

    def add(self, other):
        m = self.m + other.m
        b = self.b + other.b
        return LinearEquation(m, b)

    def sub(self, other):
        m = self.m - other.m
        b = self.b - other.b
        return LinearEquation(m, b)

    def compose(self, other):
        m = (self.m * other.m)
        b = (self.m * other.b + self.b)
        return LinearEquation(m, b)

#example equations, values, operations 
def main():

    f = LinearEquation(5, 3)
    print("f(x) =", f.showEq())
    print("f(3) =", f.evaluate(3), "\n")

    g = LinearEquation(-2, -6)
    print("g(x) =", g.showEq())
    print("g(-2) =", g.evaluate(-2), "\n")

    h = f.add(g)
    print("h(x) = f(x) + g(x) =", h.showEq())
    print("h(-4) =", h.evaluate(-4), "\n")

    j = f.sub(g)
    print("j(x) = f(x) - g(x) =", j.showEq())
    print("j(-4) =", j.evaluate(-4), "\n")

    k = f.compose(g)
    print("f(g(x)) =", k.showEq(), "\n")

    m = g.compose(f)
    print("g(f(x)) =", m.showEq(), "\n")

    g = LinearEquation(5, -3)
    print("g(x) =", g.showEq())
    print("g(-2) =", g.evaluate(-2), "\n")

    h = f.add(g)
    print("h(x) = f(x) + g(x) =", h.showEq())
    print("h(-4) =", h.evaluate(-4), "\n")

    j = f.sub(g)
    print("j(x) = f(x) - g(x) =", j.showEq())
    print("j(-4) =", j.evaluate(-4), "\n")

main()