class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        first_element = 0
        output = self.__queue[first_element]
        self.__queue.pop(first_element)
        return output

    def enqueue(self, value):
        self.__queue.append(value)
  
    def front(self):
        return self.__queue[0]


# Testcase:
if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    queue1 . enqueue(2)
    print(queue1 . is_full())
    # False
    print(queue1 . front())
    # 1
    print(queue1 . dequeue())
    # 1
    print(queue1 . front())
    # 2
    print(queue1 . dequeue())
    # 2
    print(queue1 . is_empty())
    # True

    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    assert queue1 . is_full() == False
    queue1 . enqueue(2)
    print(queue1 . is_full())

    queue1 = MyQueue(capacity=5)
    queue1 . enqueue(1)
    assert queue1 . is_full() == False
    queue1 . enqueue(2)
    print(queue1 . front())
