# Python Opcalc 0.0.1

Simple tool for calculate the numerical result from a expression string by python

Based on stack and queue

Opcalc was still under development, sometimes the result may be wrong= =

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
