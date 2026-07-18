class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []

        for u in self.followees[userId] | {userId}:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweet_id =  self.tweets[u][idx]
                heap.append((time, tweet_id, u, idx ))

        heapq.heapify_max(heap)
        
        while len(res) < 10 and heap:
            t, tid, u, tidx = heapq.heappop_max(heap)
            res.append(tid)
            if tidx > 0:
                next_tweet_idx = tidx - 1 
                next_tweet_age, next_tweet_id  = self.tweets[u][next_tweet_idx]
                heapq.heappush_max(heap, (next_tweet_age, next_tweet_id, u, next_tweet_idx ))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
