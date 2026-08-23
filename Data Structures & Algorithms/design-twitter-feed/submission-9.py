import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = []
        self.tweet_count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.tweet_count, userId, tweetId))
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for ct, uId, tId in self.tweets:
            if uId == userId or uId in self.following.get(userId, []):
                heapq.heappush(heap, (-ct, tId))
        output = []
        for _ in range(10):
            if not heap:
                break
            _, tId = heapq.heappop(heap)
            output.append(tId)
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = []
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId in self.following
            and followeeId in self.following[followerId]

        ):
            self.following[followerId].remove(followeeId)
