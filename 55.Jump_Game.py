class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = len(nums)
        f = []
        for i in range(m) :
            f.append(False)
        i=0;f[i] = True
        while i<m:
            if f[i] == True :
                if i+nums[i] >= m-1 :
                    return True
                for j in range(1,nums[i]+1) :
                    f[i+j] = True  
            i += 1

        return f[m-1]

    def canJump1(self, nums):
        reach = 0
        i=0
        while i < min(len(nums),reach+1) :
            reach = max(i+nums[i], reach)
            if reach >= len(nums)-1 :
                return True
            i+=1
            
        return False

