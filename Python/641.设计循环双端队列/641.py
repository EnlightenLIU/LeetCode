class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        from collections import deque
        self.cdeque = deque([])
        self.cur = 0
        self.k = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur + 1 <= self.k:
            self.cdeque.appendleft(value)
            self.cur += 1
            return True
        return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cur + 1 <= self.k:
            self.cdeque.append(value)
            self.cur += 1
            return True
        return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cur >= 1:
            self.cdeque.popleft()
            self.cur -= 1
            return True
        return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cur >= 1:
            self.cdeque.pop()
            self.cur -= 1
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.cur != 0:
            return self.cdeque[0]
        return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.cur != 0:
            return self.cdeque[-1]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.cur == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.cur == self.k