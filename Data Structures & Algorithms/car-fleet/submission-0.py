class Solution:
    def timeToDest(self, d, s):
        return d / s

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = list(zip(position, speed))
        positionSpeed.sort(reverse=True)

        stack = []

        for pos, spd in positionSpeed:
            t = self.timeToDest(target - pos, spd)

            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)