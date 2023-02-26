class Solution(object):
    
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
        return True
object1= Solution()
a= input()
flag =False;
flag=object1.isPalindrome(a)
if(flag== True):
    print("true")
else:
    print("false")
