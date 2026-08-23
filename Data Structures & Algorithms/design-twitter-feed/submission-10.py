import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.tweet_count, tweetId))
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Include self + everyone they follow
        users = set(self.following.get(userId, set()))
        users.add(userId)

        # Put each user's most recent tweet into the heap
        for uId in users:
            if uId in self.tweets and self.tweets[uId]:
                index = len(self.tweets[uId]) - 1
                ct, tweetId = self.tweets[uId][index]

                heapq.heappush(
                    heap,
                    (-ct, tweetId, uId, index)
                )

        output = []

        while heap and len(output) < 10:
            neg_ct, tweetId, uId, index = heapq.heappop(heap)
            output.append(tweetId)

            # Get the next older tweet from the same user
            index -= 1

            if index >= 0:
                ct, nextTweetId = self.tweets[uId][index]

                heapq.heappush(
                    heap,
                    (-ct, nextTweetId, uId, index)
                )

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)