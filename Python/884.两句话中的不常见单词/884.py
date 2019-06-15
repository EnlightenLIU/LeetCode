class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A + " " + B
        a = dict()
        A = A.split(" ")

        for item in A:
            if a.get(item, 0):
                a[item] += 1
            else:
                a[item] = 1

        res = list()
        for key in a:
            if a[key] == 1:
                res.append(key)
        return res