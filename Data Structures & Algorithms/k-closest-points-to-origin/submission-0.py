class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance_to_origin(p) -> int:
            return math.sqrt(p[0]**2 + p[1]**2)

        
        store = defaultdict(list)

        for point in points:
            d = distance_to_origin(point)
            store[d].append(point)

        
        distances = list(store.keys())
        distances.sort()    
        res = []

        for d in distances: 
            points = store[d]
            for point in points:
                res.append(point)
                if len(res) == k:
                    return res
