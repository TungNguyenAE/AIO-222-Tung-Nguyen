class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        top_element = len(self.__stack) - 1
        output = self.__stack[top_element]
        self.__stack.pop(top_element)
        return output

    def push(self, value):
        self.__stack.append(value)

    def top(self):
        output = self.__stack[len(self.__stack) - 1]
        return output


# Testcase:
if __name__ == "__main__":
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    # False
    print(stack1.top())
    # 2
    print(stack1.pop())
    # 2
    print(stack1.top())
    # 1
    print(stack1.pop())
    # 1
    print(stack1.is_empty())
    # True

    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.is_full())

    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.top())
