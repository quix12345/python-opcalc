# Python Opcalc 0.0.1

Simple tool for calculate the numerical result from a expression string by python

Based on stack and queue

## Install

Just use pip to install ! :D
```
pip install opcalc
```

## License

MIT License

## Examples

Simple calculator program:

```python
import opcalc.core as opc
calculator = opcalc.OperationCalculator()
calculator.input_str = "#*60"
print(calculator.CalcExpression())
print("SymCalc demo")
print("Copyright (c) Quix Fan  @ZQWEI  All right reserved.")
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