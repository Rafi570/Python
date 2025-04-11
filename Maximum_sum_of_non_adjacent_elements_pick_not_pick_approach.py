"""========================================================== pick not pick recursion + memorization  approach =============================================""""
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    n=len(nums)
    dp=[-1] * (n+1)
    def backtarck(index):
        if index == 0 :
            return nums[0]
        
        if index < 0:
            return 0
        if dp[index]!=-1:
            return  dp[index]
        
        pick=nums[index]+backtarck(index -2)
        notpick=0+backtarck(index-1)
        dp[index]=max(pick,notpick)
        return dp[index]
    return backtarck(len(nums) - 1)
# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1


"""========================================================== pick not pick bottom up approach ==============================================================="""" 











from os import *
from sys import *
from collections import *
from math import *

from sys import stdin



def maximumNonAdjacentSum(nums): 
    n=len(nums)
    dp=[-1]*(n+1)
    dp[0]=nums[0]

    for i in range(1,n):
        pick=nums[i]
        if i>1:
            pick+=dp[i-2]
        notpick=0+dp[i-1]
        dp[i]=max(pick,notpick)
    return dp[n-1]



t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1






"""========================================================== pick not pick bottom up approach  with space reduce ========================""""



from os import *
from sys import *
from collections import *
from math import *

from sys import stdin



def maximumNonAdjacentSum(nums): 
    n=len(nums)
    prev1=nums[0]
    prev2=0

    for i in range(1,n):
        pick=nums[i]
        if i>1:
            pick+=prev2
        notpick=0+prev1

        current=max(pick,notpick)
        prev2=prev1
        prev1=current
    return prev1



t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
