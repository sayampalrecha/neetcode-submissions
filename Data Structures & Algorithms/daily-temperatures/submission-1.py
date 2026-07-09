class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n =len(temperatures)
        stk = []
        result = [0] * n

        for i,t in enumerate(temperatures):
            
            while stk and temperatures[stk[-1]] < t:
                prev_index = stk.pop()
                result[prev_index] = i - prev_index
            stk.append(i)
        return result