class Solution:
    def sortSentence(self, s: str):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        spaces = 1
        for space in s:
            if space == ' ':
                spaces += 1
        words = {}
        word = ''
        index = 0
        for char in s:
            if char == ' ':
                word = ''
                continue
            else:
                if char not in nums:
                    word += char
                else:
                    words[int(char)] = word
        
        myKeys = list(words.keys())
        myKeys.sort()
        words = {i: words[i] for i in myKeys}
        javoblar = []
        for qiymat in words.values():
            javoblar.append(qiymat)
        return ' '.join(javoblar)


solve = Solution()
print(solve.sortSentence("mushuk3 yomon2 boyka1"))