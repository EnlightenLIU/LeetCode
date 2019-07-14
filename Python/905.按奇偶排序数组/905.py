class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = len(A)
        if l < 2:
            return A
        j = l - 1
        i = 0
        while (i < j):

            if A[i] % 2 == 0 and A[j] % 2 == 1:
                i += 1
                j -= 1
            elif A[i] % 2 == 0 and A[j] % 2 == 0:
                i += 1
            elif A[i] % 2 == 1 and A[j] % 2 == 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i += 1
                j -= 1
            else:
                j -= 1

        return A
