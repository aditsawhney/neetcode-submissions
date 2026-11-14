class Solution:

    def getHours(self, piles: List[int], mid:int) -> int:
        ans = 0
        for pile in piles:
            ans += (pile+mid-1)//mid
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left+right)//2
            if self.getHours(piles, mid) > h:
                left = mid+1
            else:
                k = mid
                right = mid-1
        return k