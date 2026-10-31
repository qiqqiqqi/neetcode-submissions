import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.replace(" ","").lower()
        front_mid_id,back_mid_id=len(s)//2,len(s)//2 if len(s)%2!=0 else len(s)//2-1
        front=s[:front_mid_id]
        back=s[-1:back_mid_id:-1]
        if front==back:
            return True
        else:
            return False