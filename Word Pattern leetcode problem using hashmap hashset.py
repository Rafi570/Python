class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        if len(pattern) != len(s):
            return False
        my_dict={}
        a=[]
        hset=set()
        for i in range(len(pattern)):
            if pattern[i] not in my_dict:
                my_dict[pattern[i]]=s[i]
                hset.add(s[i])
                a.append(s[i])
            if pattern[i] in my_dict:
                if my_dict[pattern[i]]!=s[i]:
                    return False
        return len(a)==len(hset)
        
"""
ob=Solution()
print(ob.wordPattern("abba","dog dog dog dog"))"""

"""============================================================================================================="""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        length = len(pattern)
        t = s.split(" ")
        if length != len(t):
            return False
        hashh = {}
        for a in range(length):
            if pattern[a] in hashh:
                if hashh[pattern[a]] != t[a]:
                    return False
                else: 
                    continue
            elif t[a] in hashh.values():
                return False
            hashh[pattern[a]] = t[a]
        return True
        
