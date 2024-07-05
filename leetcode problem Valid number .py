class Solution(object):
    def isint(self,s):
        if s=="":
            return False
        if s[0]=='+' or s[0]=="-":
            s=s[1:]
        return s.isnumeric()
    def isdec(self,s):
        if s=="":
            return False
        if s[0]=='+' or s[0]=="-":
            s=s[1:]
        parts=s.split('.')
        if len(parts)!=2:
            return  False
        if parts[0]=="":
            return parts[1].isnumeric()
        if parts[1]=="":
            return parts[0].isnumeric()
        return parts[0].isnumeric() and parts[1].isnumeric()
        

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.strip()
        if s=='':
            return False
        s=s.lower()
        e_count=0
        for ch in s:
            if ch=="e":
                e_count+=1
                continue
            if ch not in "0123456789+-.":
                return False
        if e_count>1:
            return False
        parts=s.split("e")
        if len(parts)==1:
            s=parts[0]
            if self.isdec(s) or self.isint(s):
                return True
            return False
        elif len(parts)==2:
            s1=parts[0]
            s2=parts[1]
            if self.isdec(s1) or self.isint(s1):
                if self.isint(s2):
                    return True
                else:
                    return False
                
            else:
                return False
            
        return True

