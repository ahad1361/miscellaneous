class Solution:
    def longestPalindrome(self, s: str) -> str:
      if s == s[::-1]:
          return s
      else:  
        palindromic = ""
        lst =[]
        temp = ""
        ind = 0
        s_len = len(s)

        for i in range(s_len+1):
          for j in (range(i, s_len+1 )):
            
            if s[i:j]==s[i:j][::-1]:
             if s[i:j] not in lst:
                lst.append(s[i:j])
        tul = []
        for i in range(len(lst)):
            tul.append(len(lst[i]))
        if len(s)>1 and len(lst)>0: 
             return(lst[tul.index(max(tul))])
        elif len(s)==1 : return s
        elif len(s)==2 : return s[0]
          
