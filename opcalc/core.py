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
        '''
        计算保存于OpCalc类中的字符串表达式，若无错误则返回值
        '''
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
        '''
        输入原始用户字符串，输出元素分割后的列表
        '''
        def GetNumfromStr(num_str):
            if num_str != "":
                # num_str不为空
                if "." in num_str:
                    # 取出为浮点数
                    num = float(num_str)
                else:
                    # 取出为整数
                    num = int(num_str)
                Raw_list.append(num)

        # 预处理 & 增强容错能力
        if Input_str == "":
            Input_str = self.input_str
        Input_str = Input_str.replace(' ', '')

        if Input_str == "":
            raise Exception("The expression is empty now, Please try again!")

        if not Input_str[0] in "0123456789":
            if Input_str[0] in "(":
                # 首元素为(,添加1*
                Input_str = "1*" + Input_str
            elif Input_str[0] in "*/":
                # 首元素为*/，则添加1
                Input_str = "1" + Input_str
            elif Input_str[0] == ".":
                # 若为".",添加0
                Input_str = "0" + Input_str

        Raw_list = []  # 初始化元素分割数组
        num_str = ""  # 初始化num_str（发挥的是队列的作用,没有另写这一数据结构的class）,主要用以将"1","2",合并输出为"12"

        for element in Input_str:
            if element in "0123456789.":
                # 若元素为数字或小数点，则加入num_str
                num_str += element
            else:
                # 若元素为运算符，取出num_str中保存的数字，并添加到最终输出中
                GetNumfromStr(num_str)
                num_str = ""  # 清空num_str
                Raw_list.append(element)

        # 遍历完成后，取出最后的数字
        GetNumfromStr(num_str)
        return Raw_list

    def Raw2RPN(self, Raw_list):
        '''
        输入元素分割列表，输出后缀表达式
        '''

        def OperationCompare(op1, op2):
            # 该函数用以判定运算符优先级
            # ^ > */ > +-
            # True for push, False for pop
            def GetPiority(op):
                if op == "^":
                    p = 3
                elif op in "*/":
                    p = 2
                elif op in "+-":
                    p = 1
                else:
                    # 此处暂不处理括号，交由其他逻辑判定运算
                    p = 0
                return p

            p1 = GetPiority(op1)
            p2 = GetPiority(op2)

            return p1 >= p2

        def PopandAppend():
            while True:
                if stack.peek() in "()":
                    # 删除栈顶的"(",")"
                    stack.pop()
                RPN_list.append(stack.pop())
                if stack.is_empty():
                    break

        stack = Stack()  # 初始化栈
        RPN_list = []  # 初始化后辍表达式
        for element in Raw_list:  # 遍历输入的元素分割字符串
            if str(element) in "*/+-()^":
                # 判断元素为运算符
                if stack.is_empty():  # 若当前为空栈则压入首个运算符，进入下一次循环
                    stack.push(element)
                    continue
                if element == ")" and stack.peek() == "(":
                    # 判断当前元素与栈顶元素是否构成了(和），若是则忽略该对括号
                    # 如(1),(12)等
                    stack.pop()
                elif OperationCompare(element, stack.peek()) or element == "(" or stack.peek() == "(":
                    # 若当前运算符优先级大于等于栈顶运算符或是"("，压入该运算符
                    # stack.peek() == "(" 表明 "("的优先级最低
                    stack.push(element)
                elif element == ")" and not stack.peek() == "(":
                    # 遇到运算符为右括号且栈顶元素不为"("时
                    # 反例(1)，(12)
                    while True:
                        # 循环写入后辍表达式，直到栈顶元素为"("
                        # 该过程中不写入"(",")"
                        RPN_list.append(stack.pop())
                        if stack.peek() == "(":
                            stack.pop()
                            break
                else:
                    # 均不满足上述条件，则说明当前运算符优先级小于栈顶运算符，取出栈中全部元素并添加至后辍表达式，最后压入当前运算符
                    PopandAppend()
                    stack.push(element)
            else:
                # 判断为数字，直接写入后缀表达式
                RPN_list.append(element)

        # 遍历完成后，取出栈中全部元素并添加至后辍表达式
        PopandAppend()
        return RPN_list

    def RPN2Result(self, RPN_list):
        '''
        计算后缀表达式并给出结果
        '''
        stack = Stack()  # 创建一个栈
        for element in RPN_list:  # 遍历后缀表达式的元素
            if stack.is_empty():
                stack.push(RPN_list[0])  # 当栈为空时，push入第一关元素
            else:
                if str(element) in "*/+-^":  # 遇到计算符号时，pop出顶上的两个元素，并基于操作符给予操作，得出答案
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
                    stack.push(result)  # 将答案压入栈
                else:
                    stack.push(element)  # 遇到数字元素，则压入栈
        # 遍历完成后，取出栈顶（底）保存的唯一结果
        return stack.pop()


if __name__ == "__main__":
    calculator = OperationCalculator()
    # calculator.input_str = "#*60"
    # print(calculator.CalcExpression())
    print("SymCalc demo")
    print("Copyright (c) Quix Fan  @ZQWEI  All right reserved.")
    # # calculator.input_str = "#*60"
    # print(calculator.CalcExpression())
    while True:
        try:
            result = calculator.CalcExpression()
            print(result)
        except:
            print("Invalid Input!")
        # calculator.input_str = "#*60"
        # print(calculator.CalcExpression())
