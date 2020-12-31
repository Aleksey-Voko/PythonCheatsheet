class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y == 0:
            raise ZeroDivisionError('Zero division error.')
        return x / y


class ExtCalculator(Calculator):
    @staticmethod
    def sqrt(x):
        return x ** 0.5

    @staticmethod
    def pow(x, y):
        return x ** y
