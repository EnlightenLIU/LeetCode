class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        #超出时间限制
        # result=[0 for i in range(n)]
        # for i in bookings:
        #     for m in range(i[0],i[1]+1):
        #         result[m-1]+=i[2]
        # return result
        res = [0] * n
        for l, r, seat in bookings:
            res[l - 1] += seat
            if r < n:
                res[r] -= seat
        for i in range(1, n):
            res[i] += res[i - 1]
        return res




s=Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
result=s.corpFlightBookings(bookings,n)
print(result)
