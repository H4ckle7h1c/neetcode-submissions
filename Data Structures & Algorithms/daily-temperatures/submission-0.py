class Node:
    def __init__(self, day:int, temperature:int):
        self.day = day
        self.temperature = temperature

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for curDay, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1].temperature < temp:
                dayDiff = curDay - stack[-1].day
                res[stack[-1].day] = dayDiff
                stack.pop()
            node = Node(curDay, temp)
            stack.append(node)
        
        return res


