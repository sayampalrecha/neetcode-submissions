from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
            
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + letter + word[i + 1 :]
                    if (
                        new_word in wordSet
                        and new_word not in visited
                        and new_word != word
                    ):
                        if new_word == endWord:
                            return level + 1
                        queue.append((new_word, level + 1))
                        visited.add(new_word)
                        
        return 0