class Stack(object):
    def __init__(self, limit=50000):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):  # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('StackError: pop from an empty stack')  # 空栈不能被弹出

    def peek(self):  # 查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]

    def is_empty(self):  # 判断栈是否为空
        return not bool(self.stack)

    def size(self):  # 返回栈的大小
        return len(self.stack)


class OperationCalculator():
    def __init__(self):
        self.input_str = ""
        self.IsResultAvailable = False
        self.RPN = None
        self.result = None

    def CalcExpression(self):
        if self.input_str == "":
            self.GetInput()
        try:
            self.RPN = self.Raw2RPN(self.Input2Raw())
            self.result = self.RPN2Result(self.RPN)
            self.IsResultAvailable = True
            self.input_str = ""
            return self.result
        except:
            self.RPN = None
            self.result = None
            self.input_str = ""
            self.IsResultAvailable = False
            raise Exception("Calculation failed...")

    def GetInput(self):
        self.input_str = input("Please enter the math expression for calculation:")

    def Input2Raw(self, Input_str=""):
        def PopandAppend():
            if not num_stack.is_empty():
                num_str = ''
                while True:
                    if num_stack.is_empty():
                        break
                    num_str = num_str + num_stack.pop()

                    # LIFO 2 FIFO
                l = list(num_str)
                l.reverse()
                num_str = "".join(l)
                if "." in num_str:
                    num = float(num_str)
                else:
                    num = int(num_str)
                Raw_list.append(num)

        if Input_str == "":
            Input_str = self.input_str
        Input_str = Input_str.replace(' ', '')
        if Input_str == "":
            raise Exception("The expression is empty now, Please try again!")
        if not Input_str[0] in "0123456789":
            if Input_str[0] in "()":
                Input_str = "1*" + Input_str
            elif Input_str[0] in "*/":
                Input_str = "1" + Input_str
            else:
                Input_str = "0" + Input_str
        Raw_list = []
        num_stack = Stack()
        for element in Input_str:
            if element in "0123456789.":

                num_stack.push(element)
            else:
                PopandAppend()
                Raw_list.append(element)
        PopandAppend()
        return Raw_list

    def Raw2RPN(self, Raw_list):
        def OperationCompare(op1, op2):
            # True for push,False for pop
            if op1 in "+-" and op2 in "*/":
                return False
            elif op1 in "^" and op2 in "^":
                return True
            elif op1 not in "^" and op2 in "^":
                return False
            elif op1 in "^" and op2 not in "^":
                return True
            elif op1 in "*/" and op2 in "+-":
                return True
            elif op1 in "+-" and op2 in "+-":
                return True
            elif op1 in "*/" and op2 in "*/":
                return True
            else:
                # print("not defined op compare")
                return False

        def PopandAppend():
            while True:
                if stack.peek() in "()":
                    stack.pop()
                RPN_list.append(stack.pop())
                if stack.is_empty():
                    break

        stack = Stack()
        RPN_list = []
        for element in Raw_list:
            if str(element) in "*/+-()^":
                if stack.is_empty():
                    stack.push(element)
                    continue
                if element == ")" and stack.peek() == "(":
                    stack.pop()
                elif OperationCompare(element, stack.peek()) or element == "(" or stack.peek() == "(":
                    # if not (element == "(" and stack.peek() == ")"):
                    stack.push(element)
                elif element == ")" and not stack.peek() == "(":
                    while True:
                        RPN_list.append(stack.pop())
                        if stack.peek() == "(":
                            break
                else:
                    PopandAppend()
                    stack.push(element)
            else:
                RPN_list.append(element)
        PopandAppend()
        return RPN_list

    def RPN2Result(self, RPN_list):
        stack = Stack()
        for element in RPN_list:
            if stack.is_empty():
                stack.push(RPN_list[0])
            else:
                if str(element) in "*/+-^":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    result = 0
                    if element == "+":
                        result = num1 + num2
                    elif element == "-":
                        result = num2 - num1
                    elif element == "/":
                        result = num2 / num1
                    elif element == "*":
                        result = num2 * num1
                    elif element == "^":
                        result = num2 ** num1
                    stack.push(result)
                else:
                    stack.push(element)
        return stack.pop()


if __name__ == "__main__":
    calculator = OperationCalculator()
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
