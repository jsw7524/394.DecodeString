import re
class Solution(object):
    def __init__(self):
        self.strSource=""
        self.index=0
    def decodeString(self, s):
        if s is None:
            return ""
        self.strSource="1["+s+"]"
        self.index = 0
        return self.myParser()

    def myParser(self):
        state='digit'
        repeatTime=""
        contentStr=""
        while self.index < len(self.strSource):
            if self.strSource[self.index].isdigit():
                if state == 'alphabet':
                    contentStr+=self.myParser()
                else:
                    repeatTime += self.strSource[self.index]
            elif self.strSource[self.index]=='[':
                state = 'alphabet'
            elif self.strSource[self.index].isalpha():
                contentStr+=self.strSource[self.index]
            else:
                return ''.join([ contentStr for num in range(int(repeatTime))])
            self.index+=1

sln=Solution()
assert "agagagbbbbbbbb"==(sln.decodeString("3[ag]4[bb]"))
assert "zahhsssssshhsssssshhsssssskkkkkkkkkkrr"==(sln.decodeString("1[za3[hh6[s]]10[k]]2[r]"))