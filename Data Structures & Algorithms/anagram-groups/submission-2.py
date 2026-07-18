from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = ["act","pots","tops","cat","stop","hat"]
        # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))

            anagram_map[sorted_key].append(s)
        
        return list(anagram_map.values())

        