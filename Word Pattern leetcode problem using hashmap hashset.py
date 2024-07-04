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
        for i in range(len(pattern)):
            if pattern[i] not in my_dict:
                if s[i] not in my_dict.values():
                    my_dict[pattern[i]]=s[i]
                else:
                    return False
            if pattern[i] in my_dict:
                if my_dict[pattern[i]]!=s[i]:
                    return False
        return True
ob=Solution()
print(ob.wordPattern("abba","dog dog dog dog"))
        
        
