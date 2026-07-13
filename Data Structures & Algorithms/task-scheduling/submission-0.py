class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        job_freq = [(count, letter) for letter, count in freq.items()]

        heapq.heapify_max(job_freq)
        queue = deque()
        time = 0

        while queue or job_freq:
            time += 1

            if queue and queue[0][0] == time:
                cooled_down = queue.popleft()[1]
                heapq.heappush_max(job_freq, cooled_down)

            if job_freq:
                task = heapq.heappop_max(job_freq)
                remaining = task[0] - 1
                if remaining > 0:
                    queue.append((time+n+1,(remaining,task[1])))

        return time


