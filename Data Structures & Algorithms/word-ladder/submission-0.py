from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     "cat"                   "bat"
    # -----------             -------------
    # aat, cat, caa          aat.  aat
    # bat, cbt, cab          dat.  
    # dat, cct, cac
    # ...  .... ....

        word_set = set(wordList)
        n = len(beginWord)
        q = deque()
        q.append((beginWord,1))
        a_ascii = ord('a')
        z_ascii = ord('z')

        while q:
            print(q)
            
            curr_word, step = q.popleft()
            if curr_word == endWord:
                return step
            for pos in range(n):
                for i in range(a_ascii, z_ascii + 1):
                    new_char = chr(i)
                    if new_char == curr_word[pos]:
                        continue
                    new_word = curr_word[:pos] + new_char + curr_word[pos+1:]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append((new_word, step +1))
        return 0



