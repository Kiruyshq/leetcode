class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words = s1.split(' ') + s2.split(' ')
        cnt={}

        for word in words:
            if word in cnt:
                cnt[word]+=1
            else:
                cnt[word]=1

        res=[]
        for word in cnt:
            if cnt[word] == 1:
                res.append[word]
        
        return res
