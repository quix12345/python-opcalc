import opcalc.core as opc
from time import time

iteration = 10000
expression = "2^3+(9/2^2)^2^2+1.5^0.3+9"

start_time = time()
calculator = opc.OperationCalculator()
for i in range(iteration):
    calculator.input_str = expression
    calculator.CalcExpression()
print("Opcalc Time:" + str(time() - start_time))

start_time = time()
for i in range(iteration):
    input_str = expression
    input_str = input_str.replace("^", "**")
    eval(input_str)
print("eval Time:" + str(time() - start_time))
