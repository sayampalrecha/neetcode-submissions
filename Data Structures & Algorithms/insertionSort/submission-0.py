# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        n = len(pairs)

        if n == 0:
            return res

        for i in range(0,n):
            key = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > key.key:
                pairs[j+1] = pairs[j]
                j = j - 1
            
            pairs[j+1] = key

            res.append(pairs[:])
        return res
        