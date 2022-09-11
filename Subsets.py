#TC - O(N*2^N)
#SC - O(N*2^N)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.result = []
        self.recur(0,[])
        return self.result
    
    def recur(self,i,path):
        if i == len(self.nums):
            self.result.append(path[:])
            return
        
        self.recur(i+1,path) #no choose
        path.append(self.nums[i])
        self.recur(i+1,path) #choose
        path.pop()

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.result = []
        self.recur(0,[])
        return self.result
    
    def recur(self,pivot,path):
        self.result.append(path[:])
            
        for i in range(pivot,len(self.nums)):
            
            path.append(self.nums[i])
            self.recur(i+1,path) #choose
            path.pop()

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.result = []
        self.recur(0,[])
        return self.result
    
    def recur(self,i,path):
        if i == len(self.nums):
            self.result.append(path)
            return
        
        self.recur(i+1,path[:])
        path.append(self.nums[i])
        self.recur(i+1,path[:])
        