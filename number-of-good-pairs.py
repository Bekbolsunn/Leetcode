""" 
Учитывая массив целых чисел nums, верните количество хороших пар .

Пара (i, j)называется хорошей , если nums[i] == nums[j]и i< j.

 

Пример 1:

Ввод: nums = [1,2,3,1,1,3]
 Вывод: 4
 Объяснение: Есть 4 хорошие пары (0,3), (0,4), (3,4), (2,5). 0-индексированный.
Пример 2:

Ввод: nums = [1,1,1,1]
 Вывод: 6
 Объяснение: Каждая пара в массиве хороша .
Пример 3:

Ввод: nums = [1,2,3]
 Вывод: 0
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        unique_elements = set(nums)
        result = []
        for i in unique_elements:
            count = 0
            for num in nums:   
                if num == i:
                    count += 1
            result.append((i, count))
        
        count_unique = 0
        for _, count in result:
            count_unique += (count * (count - 1)) // 2
        
        return count_unique

q = Solution()
print(q.numIdenticalPairs(nums=[1,2,3,1,1,3]))
