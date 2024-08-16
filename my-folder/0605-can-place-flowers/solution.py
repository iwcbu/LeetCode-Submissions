class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if (n == 0 or flowerbed == [0]):
            return True

        i = 0
        while (i < len(flowerbed) and n > 0):
            if flowerbed[i] == 1:
                i += 1
                continue
            if i == 0:
                if flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) -1:
                if flowerbed[i-1] == 0:
                    n -= 1
            elif (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
            
            i += 1

        return n <= 0

