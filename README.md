# Python Opcalc 0.0.1

Simple tool for calculate the numerical result from a expression string by python
This code mainly focused on the principle of expression calculation by using stack (one of the basic data structure)
You can use eval() function in python as well!

## Install

Just use pip to install ! :D
```
pip install opcalc
```

## License

MIT License

## Examples

### Simple calculator program:

```python
import opcalc.core as opc
calculator = opc.OperationCalculator()
calculator.input_str = "#*60"
print(calculator.CalcExpression())
print("SymCalc demo")
#print("Copyright (c) Quix Fan  @ZQWEI  All right reserved.")
calculator.input_str = "#*60"
print(calculator.CalcExpression())
while True:
    try:
        result = calculator.CalcExpression()
        print(result)
    except:
        print("Invalid Input!")
    calculator.input_str = "#*60"
    print(calculator.CalcExpression())
```

### Customized string for calculation
```python
import opcalc.core as opc
calculator = opc.OperationCalculator()
calculator.input_str = "2^3+(9/2^2)^2+1.5^0.3+9"
result=calculator.CalcExpression()
print(result)
```

The result should be 23.191846935456855

## Comparisom
test code:

```,python
import opcalc.core as opc
calculator = opc.OperationCalculator()
from time import time
start_time=time()
len=10000

for i in range(len):
    calculator.input_str = "2^3+(9/2^2)^2^2+1.5^0.3+9"
    result=calculator.CalcExpression()
print("Opcalc Time:" +str(time()-start_time))
start_time=time()
for i in range(len):
    input_str = "2^3+(9/2^2)^2^2+1.5^0.3+9"
    input_str=input_str.replace("^","**")
    eval(input_str)
print("eval Time:"+str(time()-start_time))
```

result:
Opcalc Time:0.7659511566162109
eval Time:0.17852163314819336

Although it is slower,but the principle of using stack remain the same, you can rewrite it into other languages easily!

## Releases
Lastest version: opcalc==0.0.1a3
```
pip install opcalc==0.0.1a3
```
1.faster calculation

