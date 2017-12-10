# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x:x.start)
        res = []
        m = len(intervals)
        if m == 0 :
            return res
        i = 1
        L = intervals[0]
        
        while i<m :
            if L.end >= intervals[i].start :
                L.start = min(intervals[i].start,L.start)
                L.end = max(intervals[i].end,L.end)
                i += 1
            else :
                res.append(L)
                L = intervals[i]
                i += 1

        res.append(L)
        return res

'''
x1 = Interval(1,3)
x2 = Interval(2,6)
x3 = Interval(8,10)
x4 = Interval(15,18)
intervals = [x1,x2,x3,x4]
'''

x1 = Interval(2,3)
x2 = Interval(2,2)
x3 = Interval(3,3)
x4 = Interval(1,3)
x5 = Interval(5,7)
x6 = Interval(2,2)
x7 = Interval(4,6)
intervals = [x1,x2,x3,x4,x5,x6,x7]

'''
x1 = Interval(1,4)
x2 = Interval(1,4)
intervals = [x1,x2]
'''

#s = Solution()
#res = s.merge(intervals)
res = Solution().merge(intervals)
for i in range(len(res)):
    print([res[i].start,res[i].end])
    

'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort()
        m=len(intervals)
        i=0
        L=[]
        while i<m-1 :
            if intervals[i][1] >= intervals[i+1][0] :
                L = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                del intervals[i]
                del intervals[i]
                intervals.insert(i,L)
                m -= 1
            else :
                i += 1
        return intervals

# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[1,4]]
s = Solution()
res = s.merge(intervals)
print(res)
'''


            
