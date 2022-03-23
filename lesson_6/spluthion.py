class Solution:

    def two_sum(self, array: list, sum: int) -> list:
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] + array[j] == sum:
                    return [i, j]


print(Solution().two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17))



