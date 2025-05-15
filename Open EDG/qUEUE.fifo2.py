class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.list = []

    def put(self, elem):
        self.list.insert(0, elem)

    def get(self):
        if len(self.list) > 0:
            val = self.list[-1]
            del self.list[-1]
            return val
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.list) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
