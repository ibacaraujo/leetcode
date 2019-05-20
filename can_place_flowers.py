class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        consecutive_zero = 0
        flowerbed = [0] + flowerbed + [0]
        for i in flowerbed:
            if i == 1:
                count += 0 if consecutive_zero == 0 else (consecutive_zero-1)//2
                consecutive_zero = 0
            else:
                consecutive_zero += 1
        count += 0 if consecutive_zero == 0 else (consecutive_zero-1)//2
        return count >= n
