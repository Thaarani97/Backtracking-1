#TC - O(N^T/M+1)
#SC - O(T/M)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.candidates = candidates
        self.backtrack(target,0,[])
        return self.result
        
    def backtrack(self,target,i,path):
        if target == 0:
            self.result.append(path)
            return

        if(target<0 or i >= len(self.candidates)):
            return

        #logic- action,recurse,backtrack
        self.backtrack(target,i+1,path[:])

        path.append(self.candidates[i])

        self.backtrack(target-self.candidates[i],i,path[:])

        #backtrack
        #path.pop()
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.candidates = candidates
        self.backtrack(target,0,[])
        return self.result
        
    def backtrack(self,target,pivot,path):
        if target == 0:
            self.result.append(path[:])
            return

        if(target<0):
            return

        #logic- action,recurse,backtrack
        for i in range(pivot,len(self.candidates)):
        
            path.append(self.candidates[i])

            self.backtrack(target-self.candidates[i],i,path)

            #backtrack
            path.pop()