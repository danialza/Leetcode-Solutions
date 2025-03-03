class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(self.perm(nums)) 

    def insertion(self, e,s):
        for i in range(len(s)+1):
            yield s[:i] + [e] + s[i:]

    def perm(self, s):
        if s == []:
            yield []    
        else:
            e, s1 = s[0], s[1:]
            for perms1 in self.perm(s1):
                for p in self.insertion(e,perms1):
                    yield p