class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        curr_store = self.store[key]
        most_recent = curr_store[-1]

        if most_recent[0] <= timestamp:
            return most_recent[1]
        
        l,r = 0, len(curr_store) - 1

        while l <= r:
            mid = (r-l) // 2 + l

            if curr_store[mid][0] <= timestamp:
                l = mid + 1 

            else:
                r = mid - 1

        return curr_store[r][1] if r >= 0 else ""
        
