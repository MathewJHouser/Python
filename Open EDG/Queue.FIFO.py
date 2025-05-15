class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.insert(0, elem)

    def get(self):
        if len(self.__list) > 0:
            val = self.__list[-1]
            del self.__list[-1]
            return val
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
