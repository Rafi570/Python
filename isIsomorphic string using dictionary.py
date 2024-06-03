class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        hSet = set()

        for i in range (len(s)):
            sChar = s[i]
            tChar = t[i]
            if (sChar not in dict):
                if(tChar in hSet):
                    return False
                
                dict[sChar] = tChar
                hSet.add(tChar)
            
            else:    #check if exists
                if(tChar != dict[sChar]):
                    return False

        return True
ob=Solution()
print(ob.isIsomorphic("badc","baba"))
