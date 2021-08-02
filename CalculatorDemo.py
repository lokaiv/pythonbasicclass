class Calculator:
    def input_expr(self):
        expr = input('Please enter a formula>>')
        self_expr = expr

        def calculate(self):
            return eval(self.expr)

calc = Calculator
calc.input_expr()
print('The result of the formula is {}'.format(calc.calculate()))